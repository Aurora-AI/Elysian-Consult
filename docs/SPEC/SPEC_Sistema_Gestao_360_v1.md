# SPEC — Sistema de Gestão 360º · Consultoria Comercial Elysian

> **Codinome:** CHRONOS (o Cockpit do dono + o painel do consultor)
> **Versão:** v1.0 — Módulo 1: KPIs Comerciais
> **Status:** PROPOSTA (redigida 12/08/2026, não executada)
> **Autor da spec:** Estrategista de Documentação Aurora
> **Subordinada a:** `docs/SSOT/Elysian_SSOT.md` (a Lei metodológica) e
> `AuroraControler/laudo_executivo/EXRS_Spec_Laudo_Executivo_v4.md` (a Lei de apresentação)
> **Consome o motor de:** `AuroraControler` — pipeline EXRS A0→A4 + `commercial_auditor.py`

---

## 0. Princípio arquitetural (governa tudo)

**O sistema não recalcula. Ele exibe o que o motor congelou.**

A separação já vigente no EXRS é lei aqui: o `commercial_auditor.py` produz o
`audit_report_<rodada>.json` congelado; a camada de apresentação é um formatador burro.
Dois lugares produzindo "verdade" é o bug arquitetural que esta casa não comete
(`SPEC_Fase_D2` §0). A diferença do CHRONOS para o Laudo é apenas a **cadência**: o laudo é
uma foto de diagnóstico; o CHRONOS é o filme da operação.

Quatro travas herdadas, inegociáveis:

1. **Nenhum indicador infere o que não está no dado.** Falta de coluna → `[LACUNA]` visível
   no painel, nunca estimativa silenciosa (`SPEC_Fase_E` §0.1).
2. **Todo número tem procedência.** Cada card é clicável até as linhas de origem
   (`source_rows`). Um KPI sem drill-down até a transação não entra em produção.
3. **Todo "número ideal" é derivado do dado do próprio cliente** e caminha por glide path —
   nunca benchmark externo, nunca chute (Playbook v9, Nota final).
4. **Radar, não vigilância.** Todo indicador individual respeita a escada de 3 modos e o
   painel por bandas (Playbook v9, Parte F, regras 1–5). Isso é requisito de **software**,
   não de conduta: o modo é uma configuração do sistema, não uma promessa do consultor.

---

## 1. Escopo

### 1.1. No escopo (v1)

- Modelo de dados canônico multi-cliente / multi-loja / multi-vendedor.
- Camada semântica: catálogo formal de **65 KPIs comerciais** derivados dos documentos.
- Motor de cálculo incremental (near-real-time) sobre o núcleo EXRS existente.
- 7 telas de dashboard com drill-down até a linha de venda.
- Sistema de alvos derivados (P75 + planejamento + α) e de alertas.
- Governança de exibição por modo (a/b/c) e por perfil de usuário.

### 1.2. Fora do escopo (v1, endereçado em specs irmãs)

| Item | Spec futura |
|---|---|
| Motor de Recompra — disparo de fila e cadência WhatsApp | `SPEC_Modulo_2_Motor_Recompra` |
| Camada Financeira C2 — esteira de crédito | `SPEC_Modulo_3_Credito` |
| Concentradora de Compras — sell-in × sell-through | `SPEC_Modulo_4_Concentradora` |
| Auditor de Sequência de vendas (Catálogo de Métodos) | `SPEC_Modulo_5_Auditor_Sequencia` |
| Frentes B2B / Indústria / Governo | `SPEC_Modulo_6_Config_por_Frente` |

**Nota de honestidade:** o v1 é B2C-varejo-first porque é onde existe dado real testado
(Óticas Cliente #1 e Rede PetShop). A generalização para as outras três frentes está mapeada
em `PBM_Config_Motor_por_Frente` mas **não foi validada em dado** — ver §11.

---

## 2. Modelo de dados canônico

Derivado por evidência direta de `Consultoria.xlsx` (3.046 vendas / 508 clientes / 35
vendedores / 1.189 SKUs / 1.012 compras / 268 meses-loja) e `Rede_PetShop.xlsx` (3.543 vendas).
São as **7 tabelas universais** que o `column_mapper.py` já sabe ler.

### 2.1. Tabelas de fato

| Tabela | Grão | Colunas canônicas |
|---|---|---|
| **Vendas** | 1 linha = 1 item vendido | `venda_id, data, loja, cliente_id, vendedor_id, sku, categoria, tipo_venda, qtd, preco_unit, custo_entrada, forma_pagto` |
| **Compras** | 1 linha = 1 item de NF de entrada | `compra_id, data, loja, sku, qtd, custo_unit` |
| **Financeiro** | 1 linha = 1 mês × loja | `mes, loja, receita_vendas, receita_servicos, despesa_fixa, despesa_variavel, saldo` |

### 2.2. Tabelas de dimensão

| Tabela | Grão | Colunas canônicas |
|---|---|---|
| **Clientes** | 1 linha = 1 cliente | `cliente_id, loja, nome, telefone, cpf, data_cadastro, data_ultimo_exame\|data_ultimo_atendimento` |
| **Vendedores** | 1 linha = 1 vendedor | `vendedor_id, loja, nome` |
| **Estoque** | 1 linha = 1 SKU × loja | `sku, loja, categoria, descricao, custo_unit, qtd_atual, preco_venda, data_ultimo_mov` |

### 2.3. Tabelas novas exigidas por esta spec

| Tabela | Grão | Por que | Nível |
|---|---|---|---|
| **Atendimentos** | 1 linha = 1 atendimento (comprou ou não) | Sem ela o denominador `AT` do IC não existe e o índice vira métrica de vaidade | 🔴 Bloqueante para IC pleno |
| **Fila** | 1 linha = 1 contato atribuído | Denominador `RT` do IR + temperatura da fila | 🔴 Bloqueante para IR |
| **Campanhas** | 1 linha = 1 campanha × período | Denominador `VTC` do IAd + participação-meta | 🟡 Bloqueante para IAd |
| **Escalas** | 1 linha = vendedor × dia × horas | Física do tempo (Fase E, pilar E4) | 🟢 Opcional v2 |
| **Orçamentos** | 1 linha = cotação | Conversão real (Fase E, pilar E3 v2) | 🟢 Opcional v2 |

**A Escada do AT (implementação obrigatória, `Oticas_ParteF_Score_Formula` Tabela 1):**

| Nível | Como o sistema mede AT | Efeito no painel |
|---|---|---|
| 0 — sem registro | Proxy: orçamentos no PDV + vendas (clientes únicos). Ponte: `Cadastros Novos ÷ Vendas Totais` | IC exibido com selo **"razão, não taxa"**; não entra em comparação entre lojas |
| 1 — em construção | Ficha de Atendimento obrigatória (trava de PDV antes de mostrar produto) | IC vira taxa real; entra no SEV com peso pleno |
| 2 — maduro | Orçamentos + vendas cruzados com contador de fluxo na porta | IC comparável entre lojas |

**Anti-gaming [INEGOCIÁVEL]:** o AT é sempre contado pelo sistema, nunca por autorreporte do
vendedor. Se o campo vier de entrada manual livre, o sistema marca o IC daquela loja como
`confidence: low` e o exclui de qualquer ranking.

### 2.4. Chaves de rastreabilidade

Todo registro derivado carrega `source_rows` (Pilar 2 da Fase D), respeitando o teto
`provenance_sample_cap`. Um KPI sem `source_rows` é bug de build, não feature incompleta.

---

## 3. Arquitetura do sistema

```
┌─────────────────────────────────────────────────────────────────────┐
│  CAMADA 0 · INGESTÃO                                                │
│  Planilha (.xlsx) ──► EXRS pipeline A0→A4 ──► tabelas canônicas      │
│  ERP/PDV via API   ──► conector ────────────►  (mesmo schema §2)     │
│  Retorno C2 (crédito) ──► webhook ──────────►                        │
├─────────────────────────────────────────────────────────────────────┤
│  CAMADA 1 · MOTOR DETERMINÍSTICO  (commercial_auditor.py estendido)  │
│  · Detectores A1–A4, B1–B5, C1–C2                                    │
│  · 5 índices normalizados + SEV + bandas                             │
│  · Derivação de alvos (P75 por segmento) + glide path α              │
│  · Triagem de discrepâncias (Fase C) → fila de auditoria             │
│  SAÍDA: audit_report_<rodada>.json  ── CONGELADO ──                  │
├─────────────────────────────────────────────────────────────────────┤
│  CAMADA 2 · MOTOR PROBABILÍSTICO                                     │
│  · Forecast PV por vendedor · DR por SKU · risco de evasão (E1)      │
├─────────────────────────────────────────────────────────────────────┤
│  CAMADA 3 · CAMADA SEMÂNTICA (o "modelo" do BI)                      │
│  · 62 KPIs com definição, fórmula, grão, fonte, alvo, dono           │
│  · Governança de modo (a/b/c) + mascaramento LGPD                    │
├─────────────────────────────────────────────────────────────────────┤
│  CAMADA 4 · APRESENTAÇÃO (CHRONOS)                                   │
│  · 7 telas · drill-down até source_rows · alertas · export           │
│  · Formatador burro: zero recálculo                                  │
└─────────────────────────────────────────────────────────────────────┘
```

### 3.1. Cadência de atualização ("tempo real" com honestidade)

"Tempo real" no varejo PME é uma promessa perigosa. O sistema declara a latência de cada
camada no próprio painel:

| Camada | Cadência | Justificativa |
|---|---|---|
| Vendas, fila, estoque | **Streaming / ≤5 min** | É onde a decisão do dia acontece |
| Índices IC/IA/IT/IR/IAd | **Diária (D-1)** | Estabilidade estatística; evita ruído diário |
| SEV e bandas | **Mensal** | `Mapa_Aplicacao_Formulas`, Tabela 3 |
| Alvos (P75, α, pesos) | **Trimestral** | Recalibração é decisão de consultor, não job |
| Forecast PV | **Semanal** | Idem |
| GMROI / ABC / estoque morto | **Mensal** | Idem |

**Trava:** todo card exibe `atualizado_em` + a cadência declarada. Um card sem carimbo de
frescor é card que mente.

---

## 4. Camada semântica — Catálogo de KPIs

Notação: **G** = grão · **F** = fonte · **A** = alvo · **C** = cadência.
Todo KPI carrega ainda os quatro campos do Mapa de Aplicação: **Onde · Quando · Quem ·
Entra→Sai**.

### 4.1. Bloco A — Base de clientes (o dado morto)

| # | KPI | Fórmula | G / F / A / C |
|---|---|---|---|
| A1 | **Completude de Cadastro** | `registros com o campo ÷ total × 100`, por campo (telefone, CPF, data de exame) | Loja / Clientes / 100% / Diária |
| A1b | **Gatilho de Contingência** | `SE completude(telefone∪CPF) < 30% ENTÃO pivotar diagnóstico 100% p/ estoque (B4/B5)` | Loja / Clientes / — / Evento |
| A2 | **RFM** | Quintis 1–5 em Recência, Frequência, Valor → segmentos Campeões (555), Fiéis, Em Risco, Hibernando, Perdidos | Cliente / Vendas / — / Mensal |
| A2b | **Distribuição RFM** | `nº clientes por segmento ÷ base × 100` | Loja / Vendas / — / Mensal |
| A2c | **Receita por segmento RFM** | `Σ receita do segmento` | Loja / Vendas / — / Mensal |
| A3 | **Ciclo de Recompra (mediana)** | `mediana(intervalo entre compras dos clientes fiéis)` — nunca 12 meses genéricos | Loja / Vendas / ↓ (15+→<12 m) / Mensal |
| A3b | **Churn Invisível (flag)** | `(hoje − última compra) > ciclo × 1,5` | Cliente / Vendas / — / Semanal |
| A3c | **Clientes em Churn** | `count(flag A3b)` | Loja / Vendas / ↓ / Semanal |
| A3d | **Perda R$ por Churn** | `nº em churn × ticket médio` | Loja / Vendas / ↓ / Semanal |
| A3e | **Índice de Recuperabilidade** | `silence_to_cycle_ratio` (Fase D, Pilar 3) — quanto mais perto de 1,5 mais recuperável | Cliente / Vendas / — / Semanal |
| A4 | **Attach Rate por categoria** | `clientes com categoria X ÷ clientes de grau × 100` | Loja×Cat / Vendas / P75 / Semanal |
| A4b | **Receita Latente (R$)** | `(base sem X) × conversão esperada × ticket de X` | Loja×Cat / Vendas / ↓ / Semanal |
| A4c | **Gap Kit Clínico** | `ticket do kit ideal engenheirado − P75 do segmento` | Segmento / Estoque+Vendas / — / Trimestral |
| A5 | **Conversão de Pendentes** | `pendentes que compraram ÷ pendentes` — o lado esquerdo do funil | Loja / Atendimentos / ↑ / Semanal |
| A6 | **Taxa de Recompra** | `voltaram ÷ elegíveis no período` | Loja / Vendas / ↑ / Mensal |
| A7 | **Base Ativa** | `clientes com ≥1 compra dentro do ciclo × 1,5` | Loja / Vendas / ↑ / Diária |

### 4.2. Bloco B — Estoque e margem (a salvação do caixa)

| # | KPI | Fórmula | G / F / A / C |
|---|---|---|---|
| B1 | **Giro** | `CMV ÷ estoque médio a custo` | SKU/Cat/Loja / Vendas+Estoque / — / Mensal |
| B1b | **Cobertura (dias)** | `365 ÷ giro` | idem | idem |
| B2 | **GMROI** | `margem bruta (R$) ÷ estoque médio a custo` | SKU/Cat/Loja / Vendas+Estoque / **> 1** / Mensal |
| B3 | **Curva ABC × Giro** | A = 80% da receita/margem; matriz A×baixo giro (capital preso) e C×alto giro (risco de ruptura) | SKU / Vendas / — / Mensal |
| B4 | **Estoque Morto** | SKUs sem saída há 6–9 meses | SKU / Estoque / ↓ / Mensal |
| B4b | **Capital Preso (R$)** | `Σ (qtd × custo)` dos SKUs de B4 | Loja / Estoque / ↓ / Mensal |
| B5 | **Margem de Contribuição** | `preço − custo de entrada − variáveis (imposto, comissão, taxa de cartão)` | Item/SKU/Loja / Vendas / > 0 / Diária |
| B5b | **Alerta MC < 0** | flag por SKU e por loja | SKU / Vendas / zero ocorrências / Diária |
| B5c | **Markup Defasado** | `preco_venda(Estoque) vs. P50(preco_unit praticado)` — divergência = catálogo desalinhado | SKU / Estoque+Vendas / — / Mensal |
| B6 | **Dias até a Ruptura (DR)** | `EA ÷ VMD` (estoque atual ÷ venda média diária projetada) | SKU / Estoque+Vendas / > lead time / Semanal |
| B7 | **Divergência de Custo** | `custo_entrada(Vendas) vs. custo_unit(Compras NF)` | SKU / Vendas+Compras / zero / Mensal |

> **Evidência de por que B5c e B7 existem:** SKU `ARP-013` em `Consultoria.xlsx` — NF de entrada
> a R$ 309,11, tabela única de rede a R$ 838,85, praticado em L9 a R$ 172–248 e em L2/L3 a
> R$ 1.344–2.031 com `custo_entrada` divergente da NF. Duas assinaturas independentes de erro
> cadastral que o laudo **nunca** pode apresentar como "vendedor descontista"
> (`SPEC_Fase_C` §1).

### 4.3. Bloco F — Performance individual (SEV, Camada 1)

**Regra de normalização universal [INEGOCIÁVEL]** (`Oticas_ParteF_Blindagem_SEV` §1):

```
IN = mín( Real ÷ Alvo ; 1 ) × 100
```

Nenhum índice entra no SEV como taxa crua. Um attach de 30% pode ser excelente no segmento —
somar 30/100 faz o bom vendedor parecer medíocre.

| # | Índice | Real | Alvo derivado | Fórmula final |
|---|---|---|---|---|
| F1 | **IC · Captura** | `AC ÷ AT` | **100%** (a exceção — o ideal é identificar todo atendimento) | `mín(AC÷AT;1)×100` |
| F2 | **IA · Anexação** | `VC ÷ VG` | `P75(attach por vendedor, por segmento)` | `mín(AttachReal÷AttachAlvo;1)×100` |
| F3 | **IT · Ticket** | `TMR` | `TMIo` (ver §4.4) | `mín(TMR÷TMIo;1)×100` |
| F4 | **IR · Resgate** | `RC ÷ RT` | `P75(conversão da fila, **por temperatura**)` | `mín(ConvReal÷ConvAlvo;1)×100` |
| F5 | **IAd · Adesão** | `VCa ÷ VTC` | participação-meta da campanha — **não é 100%** | `mín(AdesãoReal÷AdesãoAlvo;1)×100` |

**Composição:**

```
SEV = (IC×p1) + (IA×p2) + (IT×p3) + (IR×p4) + (IAd×p5)     Σp = 1,00
```

**Régua de Pesos por Maturidade** (configurável por loja — lojas da mesma rede estão em
estágios diferentes):

| Estágio | IC | IA | IT | IR | IAd | Prioridade |
|---|---|---|---|---|---|---|
| **Cego** (dado ruim · Fases 1–2) | 0,45 | 0,15 | 0,10 | 0,20 | 0,10 | Encher a base — a loja está cega |
| **Construção** (padrão) | 0,30 | 0,25 | 0,20 | 0,15 | 0,10 | Equilíbrio |
| **Cruzeiro** (Fase 4) | 0,15 | 0,25 | 0,20 | 0,30 | 0,10 | Usar a fila (IR) agressivamente |

> **Divergência documental detectada [LACUNA-01].** `Oticas_ParteF_Score_Formula` fixa o vetor
> Construção em `0,25/0,25/0,20/0,20/0,10`; o `Playbook_v9_Master` (posterior, Master) usa
> `0,30/0,25/0,20/0,15/0,10`. **A spec adota o v9** por recência e por status Master. Registrar
> a decisão no Vault e corrigir o documento satélite.

**Requisito de software — saturação de índice:** quando o desvio-padrão de um índice entre
vendedores da loja cai abaixo de um limiar configurável, o sistema **sugere** rebaixar o peso
dele e subir o do índice que ainda discrimina. Sugere; não aplica. A recalibração é ato do
consultor, trimestral.

**Requisito de software — comparabilidade:** lojas com vetores de peso diferentes têm SEV
**não comparável**. O sistema bloqueia qualquer visual que ranqueie SEV entre lojas de vetores
distintos e oferece, no lugar, a comparação de **tendência intra-loja**.

**Bandas do painel** (nunca nomes):

| Banda | Faixa SEV | Assinatura de comportamento |
|---|---|---|
| Topo | 90–100 | Captura quase todo atendimento, anexa 1 em cada 3 graus, executa a fila, puxa o mix de valor. É o template |
| Forte | 75–90 | Bom em quase tudo, com um índice fraco identificável |
| Médio | 60–75 | Tira pedido: converte na frente, mas não captura, não anexa, ignora a fila. **Maior Receita Latente interna** |
| Base | 0–60 | Vaza em vários índices. Coaching direcionado — ou decisão de saída com o gestor |

### 4.4. Bloco G — Engenharia do TMI (o denominador do IT)

O IT só vale o quanto o TMI vale. Dois erros proibidos no sistema: TMI = média da loja
(premia a mediocridade) e TMI = número único para todos (confunde sorte com habilidade).

| # | KPI | Fórmula | Quem / Quando |
|---|---|---|---|
| G1 | **TMI histórico do segmento** | `TMIhs = P75(tickets do segmento s, na própria loja)` | Máquina / Trimestral |
| G2 | **TMI histórico do vendedor** | `TMIhv = Σ (Mi × TMIhs_i)` — `Mi` = participação % do vendedor no segmento i | Máquina / Trimestral |
| G3 | **TMI de planejamento** | `TMIp = MR ÷ NVp` (meta de receita ÷ nº de vendas projetado) | Consultor + Dono / Trimestral |
| G4 | **Gap** | `Gap = TMIp − TMIhv` — classificar em *operacional* (fechável por mix/coaching), *estrutural* (decisão do dono) ou *Hopium* (orçamento irreal) | Consultor / Trimestral |
| G5 | **TMI operacional (a régua)** | `TMIo = TMIhv + α × (TMIp − TMIhv)`, `α ∈ [0,1]` sobe por trimestre | Consultor / Trimestral |
| G6 | **TMR** | ticket médio real do vendedor no período | Máquina / Diária |

**Segmentos canônicos (Óticas):** grau simples · multifocal · solar com grau · lente de contato.
Sem a venda etiquetada por tipo, o sistema usa **P75 geral** provisoriamente e marca a
segmentação como pendência da fase de higiene — com selo visível no card, nunca em silêncio.

**Requisito de UI:** a tela do TMI mostra as **três réguas simultâneas** (TMIhv, TMIo, TMIp)
com o α como slider. É a única forma de o dono ver que a régua caminha, e não que foi imposta.

### 4.5. Bloco H — Forecast e risco (Camada 2)

| # | KPI | Fórmula | Cadência |
|---|---|---|---|
| H1 | **Previsão de Venda (PV)** | `PV = AG × (IR ÷ 100) × TMR` | Semanal |
| H2 | **Forecast da loja** | `Σ PV de todos os vendedores` | Semanal |
| H3 | **Acurácia do Forecast** | `1 − |previsto − realizado| ÷ realizado` | Semanal (retro) |
| H4 | **Dias até a Ruptura (DR)** | `EA ÷ VMD` | Semanal |
| H5 | **Risco de Evasão de Talento** | série temporal de receita/vendedor + desvio σ (Fase E, pilar E1) | Mensal |
| H6 | **Risco de Concentração** | `% da receita VIP (top 20% clientes = 80% receita) atrelada a 1 vendedor` — **alerta se > 40%** | Mensal |

> **Maturação declarada:** a Camada 2 amadurece em 60–90 dias conforme o dado acumula
> (Playbook v9, Parte F). O sistema exibe o PV com `confidence` explícito e **não** o usa em
> decisão de meta antes de H3 estabilizar.

### 4.6. Bloco N — Nota humana (Camada 3)

| # | KPI | Fórmula | Cadência |
|---|---|---|---|
| N1 | **Nota Comportamental** | `NC = (E + Pt + Va + Qa) ÷ 4`, cada critério 0–100 | Trimestral (ou mensal) |
| N2 | **Matriz SEV × NC** | quadrantes: Âncora tóxico (SEV↑ NC↓) · Desenvolver (SEV↓ NC↑) · Template · Base | Trimestral |
| N3 | **Régua de Perfil Ideal** | `RPI = assinatura(Banda Topo) − assinatura(Banda Base + quem saiu)` | Ao contratar |
| N4 | **Matriz Desempenho × Influência** | Artesão · Âncora · Base · **O Portão** (sociometria) | Fase 2 e semestral |

**[INEGOCIÁVEL]** N1–N3 só ficam visíveis no **modo (c)** e apenas para o perfil Gestor. O
sistema exige um aceite registrado de RH/jurídico antes de habilitar o modo (c) — a régua toca
decisão trabalhista e LGPD de colaborador.

### 4.7. Bloco C — Camadas de negócio

| # | KPI | Fórmula |
|---|---|---|
| C1 | **Mensalidade mínima do Clube** | `custo mensal de servir ÷ (1 − margem-alvo)` |
| C1b | **Break-even do Clube** | `fixos ÷ margem por assinante` |
| C1c | **MRR do Clube** | `Σ mensalidades ativas` |
| C2a | **Uplift de Ticket (crédito)** | `(ticket médio com crédito ÷ ticket médio à vista − 1) × 100` |
| C2b | **Taxa de Aprovação** | `limites aprovados ÷ propostas enviadas × 100` — baixa = parceiro apertado, acionar outro do painel |
| C2c | **Inadimplência do parceiro** | monitorada **no parceiro**, nunca no caixa da ótica (risco zero) |
| C3a | **Economia por unidade (concentradora)** | `(preço antigo − preço concentrado) ÷ preço antigo × 100` |
| C3b | **Volume agregado da rede** | `Σ pedidos consolidados` |
| C3c | **Taxa de adesão** | `óticas ativas ÷ óticas da rede` |
| C3d | **Estoque morto pós-concentração** | delta de B4 — a prova do "comprar inteligente" |

### 4.8. Bloco P — Portão de Dupla Trilha (roteamento)

| # | KPI | Fórmula |
|---|---|---|
| P1 | **Cobertura de Triagem** | `leads triados ÷ leads totais × 100` — **Gate 2 exige 100%** |
| P2 | **Distribuição por trilha** | % em Balcão / Desenvolvimento / Consultiva |
| P3 | **Gap de Share (Receita Latente B2B)** | `mix possível pelo ramo − mix comprado`, por cliente |
| P4 | **Taxa de Graduação** | clientes-base promovidos à Consultiva ÷ base com potencial |
| P5 | **Taxa de Rebaixamento** | leads de topo que esfriaram ÷ topo — evita pipeline com fantasma |
| P6 | **Taxa de Auto-Close** | vendas fechadas pela máquina ÷ vendas de balcão (só whitelist) |
| P7 | **Aderência às 4 condições** | auditoria: nenhum auto-close fora da whitelist / quantidade / intenção simples |

### 4.9. Bloco X — Cockpit do dono (a tela que ele abre)

Sete cards, e o indicador-mãe é um só. Sem métrica de vaidade.

| Ordem | KPI | Meta declarada |
|---|---|---|
| 1 ★ | **Ciclo médio de recompra** (north-star) | 15+ → **< 12 meses** |
| 2 | Taxa de cadastro por vendedor | fim do anonimato |
| 3 | Taxa de recompra | sobe se o recall funciona |
| 4 | Attach rate / UPT | captura de Receita Latente |
| 5 | GMROI | **> 1** |
| 6 | Conversão de pendentes | o lado esquerdo do funil |
| 7 | MRR do Clube | recorrência nova |

---

## 5. As telas

### Tela 0 · Cockpit (perfil: Dono)
Os 7 KPIs de §4.9, o ciclo de recompra em destaque tipográfico, e **um único número em R$**
no topo: a receita em risco consolidada da semana. Segue a Lei da Linguagem do laudo (§3):
todo bloco responde "quanto custa" ou "quanto rende", nunca "quanto mede". Vocabulário
proibido nesta tela: SKU, churn, attach, GMROI, dataset, outlier — traduzidos conforme a
tabela do `EXRS_Spec_Laudo_Executivo_v4` §3.4.

### Tela 1 · Base de Clientes (Mapa da Mina)
Matriz RFM 5×5 clicável, cada célula com nº de clientes e R$; sobreposição do churn invisível;
fila de resgate ordenada por recuperabilidade (A3e); receita latente por categoria em funil de
2 degraus com o vão rotulado em R$.

### Tela 2 · Estoque e Margem
Treemap de capital preso proporcional ao R$; scatter GMROI × giro com a linha de corte em 1;
matriz ABC × giro; lista de alertas MC < 0. **Visual obrigatório para margem mascarada:
waterfall** (produto desce ao vermelho, serviço sobe, total "verde de mentira") — nunca tabela
de margens.

### Tela 3 · Performance da Equipe
**Modo (a):** distribuição por bandas, sem nomes, com a assinatura de comportamento de cada
banda e o **gap em R$ entre a média e o topo**. KPI da tela: mover a curva para a direita, não
cortar a cauda.
**Modo (b):** arquétipos e amostragem anônima.
**Modo (c):** nominal, restrito ao perfil Gestor, com aceite de RH/jurídico registrado.
Em todos os modos, o score sai **sempre acompanhado do caminho de desenvolvimento** — ranking
cru é proibido pelo sistema, não pela política (`Playbook v9`, regra 2).

### Tela 4 · Engenharia do Ticket (TMI)
As três réguas (TMIhv / TMIo / TMIp) com slider de α; decomposição do gap em operacional ×
estrutural × Hopium; comparação P75 vs. kit clínico por segmento.

### Tela 5 · Forecast e Ruptura
PV por vendedor somando ao forecast da loja, com faixa de confiança; acurácia histórica (H3);
lista de SKUs da Curva A por DR crescente; risco de evasão (H5) e de concentração (H6).

### Tela 6 · Fila de Auditoria (perfil: Consultor)
O resíduo da triagem da Fase C — **nunca o atacado**. Cada item com todas as evidências
anexadas para veredito em ~30 segundos. Princípio dimensionador: uma fila com 300 itens é
backlog morto; uma com 5 itens especificamente inexplicáveis é governança. Item pendente
**nunca** vira fato no Cockpit.

### Tela 7 · Anexo Vivo (procedência)
Toda tabela que soma exatamente o número exibido no card. O corpo afirma; o anexo **é** a
soma. Divergência de 1 centavo entre card e Σ(anexo) = build quebrado, nada é renderizado
(`SPEC_Fase_D2` §0).

---

## 6. Governança de exibição

| Perfil | Telas | Modo SEV máximo | Nomes visíveis |
|---|---|---|---|
| **Dono** | 0, 1, 2, 4, 5 | (a) por padrão; (c) só após aceite | Não, exceto no modo (c) |
| **Gestor de loja** | 0, 1, 2, 3, 5 | conforme escada | Só no coaching privado |
| **Vendedor** | painel próprio | próprio score + caminho | Só o dele |
| **Consultor Aurora** | todas | todas | Sim, com log de acesso |

**Onde os nomes vivem:** no coaching privado, com o caminho de melhora anexado. Nunca no
painel. O sistema implementa isso como controle de acesso, não como convenção.

**LGPD:** dado de cliente e dado de colaborador têm bases legais distintas. O modo anônimo por
bandas protege **e** garante dado honesto — sistema que pune, a equipe gambiarra; sistema que
desenvolve, o dado fica limpo.

---

## 7. Sistema de alertas

| Alerta | Gatilho | Destino |
|---|---|---|
| Margem negativa | `MC < 0` em qualquer SKU vendido | Dono + Consultor, imediato |
| Ruptura iminente | `DR < lead time` em SKU da Curva A | Gestor de compras, diário |
| Churn entrando | cliente cruza `ciclo × 1,5` | Fila do vendedor, diário |
| Concentração de VIP | 1 vendedor > 40% da receita VIP | Dono, mensal |
| Aprovação de crédito caindo | `C2b` abaixo do piso do contrato | Consultor, semanal |
| Índice saturado | σ do índice < limiar | Consultor, trimestral (sugestão de recalibragem) |
| Divergência de custo | `custo_entrada ≠ custo NF` | Fila de auditoria, contínuo |
| Gate não cumprido | P1 < 100% na Fase 2 | Consultor — **bloqueia avanço de fase** |

---

## 8. Critérios de aceite

1. Todo KPI de §4 tem drill-down até `source_rows` na Tela 7.
2. Card e Σ(anexo) batem ao centavo, senão o build reprova.
3. Nenhum índice do SEV é somado como taxa crua (auditar por teste).
4. IC de loja em Nível 0 aparece com selo "razão, não taxa" e fora de ranking entre lojas.
5. SEV entre lojas de vetores de peso distintos é bloqueado para comparação direta.
6. Modo (c) exige aceite registrado antes de expor nome.
7. Todo card exibe `atualizado_em` + cadência declarada.
8. Coluna ausente na origem → `[LACUNA]` visível; zero estimativa silenciosa.
9. Item pendente na fila de auditoria não aparece como fato em nenhuma tela de negócio.
10. Vocabulário proibido (§3.4 da Lei do Laudo) não aparece nas telas de perfil Dono.

---

## 9. Roadmap de implementação

| Fase | Entrega | Depende de |
|---|---|---|
| **1** | Camada semântica + Blocos A e B sobre o motor atual | Nada novo — o `commercial_auditor.py` já calcula |
| **2** | Telas 0, 1, 2, 7 (Cockpit + Base + Estoque + Anexo) | Fase 1 |
| **3** | Bloco G (TMI) + Tela 4 | Venda etiquetada por segmento |
| **4** | Bloco F (SEV) + Tela 3 modo (a) | **Tabelas Atendimentos, Fila, Campanhas** |
| **5** | Bloco H + Tela 5 | 60–90 dias de dado acumulado |
| **6** | Tela 6 (fila de auditoria) com UI | `SPEC_Fase_C` já executada no motor; falta só a UI |
| **7** | Modos (b) e (c) + Bloco N | Aceite de RH/jurídico |
| **8** | Blocos C e P | Specs irmãs dos Módulos 2–4 |

---

## 10. Anti-padrões (o que reprova o sistema)

1. Recalcular na apresentação.
2. Somar taxa crua no SEV.
3. Ranking nominal cru em qualquer tela.
4. Estimar valor de coluna ausente.
5. Exibir item pendente de auditoria como fato.
6. Comparar SEV entre lojas de vetores distintos.
7. Usar benchmark de mercado onde o método exige alvo derivado do dado do cliente.
8. TMI congelado no histórico ou fixado na fantasia do planejamento no dia 1.
9. Card sem carimbo de frescor.
10. Apresentar erro cadastral (B5c/B7) como culpa de vendedor.

---

## 11. Lacunas e tensões em aberto

| # | Lacuna | Impacto | Quem resolve |
|---|---|---|---|
| **L-01** | Vetor de pesos Construção diverge entre `Score_Formula` (0,25/0,25/0,20/0,20/0,10) e `Playbook_v9` (0,30/0,25/0,20/0,15/0,10) | Baixo — spec adota o v9 | Rodrigo, corrigir o satélite |
| **L-02** | Tabelas Atendimentos, Fila e Campanhas não existem em nenhuma planilha real | 🔴 **Bloqueia IC, IR e IAd** — 55% do peso do SEV | Definir captura no PDV do Cliente #1 |
| **L-03** | "Motor de 7 dias" (Laudo de Choque) nunca cronometrado em cliente externo | Bloqueia o escalonamento da oferta de entrada (SSOT §8) | Piloto V1 |
| **L-04** | Base teórica importada do universo SaaS/enterprise americano (bow-tie, NRR 110–130%, comitês de 6–10) vs. PME de varejo em Curitiba/Joinville sem CRM | Risco de fundo, registrado e **não resolvido** | Decisão estratégica |
| **L-05** | Frentes B2B / Indústria / Governo mapeadas em `PBM_Config_Motor_por_Frente` mas sem dado validado | v1 é B2C-first por consequência | Módulo 6 |
| **L-06** | `Modelos_Comerciais_2026` e `PBM_Config_Motor_por_Frente` cobrem a mesma matriz sem alinhamento campo a campo confirmado | Médio | Auditoria documental |
| **L-07** | `Método Aurora_Estratégia e Fosso Competitivo.pdf` (13 pág.) é imagem escaneada — conteúdo não incorporado | Desconhecido | OCR |
| **L-08** | Segmentação de venda por tipo (multifocal, simples, solar, LC) ausente no dado bruto | Degrada G1–G2 para P75 geral | Higiene de dado, Fase 1 |
| **L-09** | Teto de ticket do Contrato de Reunião vs. C3/Rackham (Catálogo v0.2) | Fora do escopo v1 | Módulo 5 |

---

## 12. Rastreabilidade documental

| Origem | O que esta spec extraiu |
|---|---|
| `ElysianConsult/docs/SSOT/Elysian_SSOT.md` | Axiomas, frameworks, tensões L-03/L-04 |
| `Oticas_Playbook_v9_Master.docx` | Blocos A, B, F, G, N; Cockpit (§4.9); governança (§6) |
| `Oticas_ParteF_Score_Formula.docx` | Cinco índices, escada do AT, bandas, glossário |
| `Oticas_ParteF_Blindagem_SEV.docx` | Regra de normalização universal (§4.3) |
| `Oticas_ParteF_TMI.docx` | Bloco G completo |
| `Oticas_Mapa_Aplicacao_Formulas.docx` | Campos Onde·Quando·Quem·Entra→Sai; cadências (§3.1) |
| `Oticas_Camada_Financeira_C2.docx` | C2a–C2c |
| `Oticas_Concentradora_Compras.docx` | C3a–C3d |
| `PBM_Modulo_2-1_Portao_Dupla_Trilha.docx` | Bloco P |
| `metodologia_consolidada.md` | Mapa geral, L-04, L-06, L-07 |
| `AuroraControler/SPEC_Fase_B_*.md` | GMROI, attach, corrosão, concentração (H6), follow-on |
| `AuroraControler/SPEC_Fase_C_*.md` | Tela 6, B5c, B7, princípio dimensionador |
| `AuroraControler/SPEC_Fase_D2_*.md` | Tela 7, zero contradição, procedência |
| `AuroraControler/SPEC_Fase_E_*.md` | H5, tabelas Escalas/Orçamentos, princípio §0.1 |
| `AuroraControler/laudo_executivo/EXRS_Spec_Laudo_Executivo_v4.md` | Lei da linguagem, lei visual, arquitetura narrativa |
| `Consultoria.xlsx` / `Rede_PetShop.xlsx` | Modelo de dados canônico (§2) |

---

**Fim da SPEC v1.0.** Próximo artefato: protótipo HTML navegável das Telas 0–5.

---

# ⚠️ STATUS: SUPERADO PARCIALMENTE — DEC-009 (13/08/2026)

**A camada de apresentação deste documento está superada.** O conceito CHRONOS — 8 telas
densas, muitos cards, tudo visível — partia de uma premissa de dashboard corporativo que o
autor descartou:

> *"Pessoalmente eu não utilizaria o CHRONOS. As pessoas estão querendo ler menos, não mais —
> no máximo por demanda. As interfaces precisam ser limpas, simples. A complexidade vem da
> demanda, não na entrega ativa."*

| Camada | Destino |
|---|---|
| Catálogo de 65 KPIs (§4) | ✅ **absorvido** — virou 99 fórmulas no `CATALOGO/registro/formulas*.yaml` |
| Modelo de dados canônico (§2) | ✅ **vigente** |
| Governança de modo a/b/c (§6) | ✅ **virou** `REG-SEV-004` |
| Sistema de alertas (§7) | ⚠️ a revisar sob o novo princípio |
| **As 8 telas (§5) e o protótipo HTML** | ❌ **`SUPERADO`** |

**O que substitui:** o bloco `ART` do registro (`CATALOGO/registro/artefatos.yaml`), governado
por dois princípios da `DEC-009` — **superfície mínima, profundidade total** e **o drill-down
é diagnóstico, não navegação**.

Este documento permanece como registro histórico. Não usar a §5 como spec de implementação.
