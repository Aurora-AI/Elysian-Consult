# Arsenal Completo de Fórmulas — Consultoria Aurora

Este documento é a fonte única de todas as fórmulas criadas para a arquitetura de performance da consultoria. Divide-se em 6 blocos:

1. [Motor Determinístico (SEV)](#1-motor-determinístico--score-de-engenharia-de-venda-sev)
2. [Ticket Médio Ideal (TMI)](#2-ticket-médio-ideal-tmi)
3. [Motor Probabilístico (Forecast)](#3-motor-probabilístico-forecast)
4. [Motor Comportamental](#4-motor-analítico-comportamental)
5. [Atingimento de Metas por Categoria](#5-atingimento-de-metas-por-categoria)
6. [Margem de Contribuição (5 Níveis)](#6-margem-de-contribuição-desdobrada-em-5-níveis)

---

## 1. Motor Determinístico — Score de Engenharia de Venda (SEV)

### 1.1 Os 5 Índices Base

**Índice de Captura (IC)** — O vendedor alimenta o motor?
$$IC = \frac{AC}{AT} \times 100$$
- AC = Atendimentos Cadastrados (com CPF/contato)
- AT = Atendimentos Totais (orçamentos + vendas)

**Índice de Anexação (IA)** — Ele expande o ticket ou só tira pedido?
$$IA = \frac{VC}{VG} \times 100$$
- VC = Vendas com item Complementar (solar com grau, lente de contato, 2º par)
- VG = Vendas de óculos de Grau

**Índice de Ticket (IT)** — Ele vende o mix de valor?
$$IT = \frac{TMR}{TMI} \times 100 \quad \text{(teto em 100)}$$
- TMR = Ticket Médio Real do vendedor
- TMI = Ticket Médio Ideal (ver Bloco 2)

**Índice de Resgate (IR)** — Ele converte a fila do motor?
$$IR = \frac{RC}{RT} \times 100$$
- RC = Resgates Convertidos
- RT = Resgates Trabalhados

**Índice de Adesão (IAd)** — Ele segue a prioridade da semana?
$$IAd = \frac{VCa}{VT} \times 100$$
- VCa = Vendas da Campanha vigente
- VT = Vendas Totais do vendedor

### 1.2 A Composição do SEV

$$SEV = (IC \times p_1) + (IA \times p_2) + (IT \times p_3) + (IR \times p_4) + (IAd \times p_5)$$

Pesos padrão (Construção): IC×0,25 + IA×0,25 + IT×0,20 + IR×0,20 + IAd×0,10

| Estágio da Loja | IC | IA | IT | IR | IAd | Prioridade |
|---|---|---|---|---|---|---|
| Cego (Fases 1–2) | 0,45 | 0,15 | 0,10 | 0,20 | 0,10 | Encher a base |
| Construção (padrão) | 0,25 | 0,25 | 0,20 | 0,20 | 0,10 | Equilíbrio motor + receita latente |
| Cruzeiro (Fase 4) | 0,15 | 0,25 | 0,20 | 0,30 | 0,10 | Usar a fila (IR) agressivamente |

### 1.3 Blindagem do SEV (Normalização contra Alvo)

Nenhum índice entra no SEV como taxa crua:
$$IN = \min\left(\frac{\text{Real}}{\text{Alvo}}, 1\right) \times 100$$

| Índice | Alvo | Método |
|---|---|---|
| IC | 100% (fixo) | Todo atendimento deve ser cadastrado |
| IA | P75 do attach por segmento | O que os melhores da loja já anexam |
| IT | TMI operacional (ver Bloco 2) | Ponte entre histórico e planejamento |
| IR | P75 da conversão por temperatura da fila | Quente ≠ fria |
| IAd | Participação-meta da campanha (do plano) | Nunca 100% — não canibalizar o mix |

### 1.4 Bandas do Painel

| Banda | Faixa SEV | Assinatura |
|---|---|---|
| Topo | 90–100 | Captura, anexa, executa fila, puxa mix de valor |
| Forte | 75–90 | Bom em quase tudo, 1 índice fraco identificável |
| Médio | 60–75 | Tira pedido. Maior Receita Latente interna |
| Base | 0–60 | Vaza em vários índices. Coaching ou decisão de saída |

---

## 2. Ticket Médio Ideal (TMI)

### 2.1 TMI Histórico do Segmento (o que a loja consegue)
$$TMI_{hs} = P75(\text{tickets do segmento } s \text{ na loja})$$

### 2.2 TMI Histórico do Vendedor (ponderado pelo mix)
$$TMI_{hv} = \sum (M_i \times TMI_{hs\_i})$$
- $M_i$ = participação (%) das vendas do vendedor no segmento i

### 2.3 TMI de Planejamento (o que o negócio precisa)
$$TMI_p = \frac{MR}{NV_p}$$
- MR = Meta de Receita | NV_p = Nº de Vendas projetado

### 2.4 TMI Operacional — A Ponte (a régua do vendedor)
$$TMI_o = TMI_{hv} + \alpha \times (TMI_p - TMI_{hv})$$
- α = fração da ponte percorrida (0 a 1), calibrada trimestralmente

### 2.5 O Gap (o achado)
$$Gap_{TMI} = TMI_p - TMI_{hv}$$
- Gap fechável por mix/coaching = operacional
- Gap estrutural (mercado não entrega) = decisão do dono

---

## 3. Motor Probabilístico (Forecast)

### 3.1 Previsão de Venda do Vendedor (PV)
$$PV = AG \times \frac{IR}{100} \times TMR$$
- AG = Agendamentos na fila da semana
- IR = Índice de Resgate (%)
- TMR = Ticket Médio Real

### 3.2 Dias até a Ruptura (DR)
$$DR = \frac{EA}{VMD}$$
- EA = Estoque Atual (unidades)
- VMD = Venda Média Diária projetada

---

## 4. Motor Analítico-Comportamental

### 4.1 Nota Comportamental (NC)
$$NC = \frac{E + Pt + Va + Qa}{4}$$
- E = Ética | Pt = Pontualidade | Va = Valores | Qa = Qualidade atendimento (NPS)

### 4.2 Perfil Ideal de Contratação
$$Perfil = \text{assinatura(Banda Topo)} - \text{assinatura(Banda Base + quem saiu)}$$

---

## 5. Atingimento de Metas por Categoria

Categorias: Óculos de Sol (OS), Lentes Grau Simples (LGS), Lentes Multifocais (LMF), Lentes Transition (LTR), Serviços (SRV), Acessórios (ACC). O subscrito `c` = qualquer categoria.

### 5.1 Atingimento Real (AR)
$$AR_c = \frac{V_c}{M_c} \times 100$$
- $V_c$ = Volume realizado na categoria | $M_c$ = Meta mensal da categoria

### 5.2 Projeção de Atingimento (PA)
$$PA_c = \frac{V_c}{DU_e} \times DU_t$$
- $DU_e$ = Dias Úteis transcorridos | $DU_t$ = Dias Úteis totais do mês

Em percentual da meta:
$$PA\%_c = \frac{PA_c}{M_c} \times 100$$

### 5.3 Meta Esperada proporcional ao dia (ME)
$$ME_c = \frac{DU_e}{DU_t} \times 100$$

### 5.4 Descolamento da Meta (Gap)
$$Gap_c = AR_c - ME_c$$
- Positivo = adiantado | Negativo = atrasado

### 5.5 Velocidade Diária (Pace)
$$Pace_c = \frac{V_c}{DU_e}$$

### 5.6 Esforço Diário Necessário (EDN)
$$EDN_c = \frac{M_c - V_c}{DU_t - DU_e}$$

| Situação | Leitura |
|---|---|
| $EDN_c \leq Pace_c$ | Confortável — mantendo ritmo bate a meta |
| $EDN_c \leq 1{,}5 \times Pace_c$ | Recuperável — precisa acelerar até 50% |
| $EDN_c > 1{,}5 \times Pace_c$ | Crítico — intervenção do gestor |

### 5.7 Meta Residual (MR)
$$MR_c = M_c - V_c$$

### 5.8 Índice de Mix (IM)
$$IM_c = \frac{P_c^{real}}{P_c^{meta}}$$

Onde:
$$P_c^{real} = \frac{V_c}{\sum V} \quad ; \quad P_c^{meta} = \frac{M_c}{\sum M}$$

- IM = 1 → mix perfeito | IM > 1 → sobre-representada | IM < 1 → sub-representada

### 5.9 Tendência Semanal (T)
$$T_c = \frac{Pace_c^{S_{atual}}}{Pace_c^{S_{anterior}}}$$
- T > 1,05 → Acelerando | 0,95–1,05 → Estável | T < 0,95 → Desacelerando

### 5.10 Classificação de Risco de Atingimento (CRA)

| Cor | Condição |
|---|---|
| 🟢 Verde | $PA\%_c \geq 100\%$ e $T_c \geq 0{,}95$ |
| 🟡 Amarelo | $PA\%_c \geq 85\%$ e $EDN_c \leq 1{,}5 \times Pace_c$ |
| 🔴 Vermelho | $PA\%_c < 85\%$ ou $EDN_c > 1{,}5 \times Pace_c$ |

### 5.11 Elasticidade de Recuperação (ER)
$$ER_c = \frac{EDN_c}{Pace_c^{max}}$$
- $Pace_c^{max}$ = maior velocidade diária sustentada por 1 semana nos últimos 3 meses
- ER ≤ 1 → Viável | 1–1,3 → Apertada | > 1,3 → Improvável (não queime o vendedor)

### 5.12 Contribuição Marginal por Categoria (CMC)
$$CMC_c = \frac{V_c}{\sum V} \times \frac{Gap_c}{\sum |Gap|}$$

### 5.13 Atingimento Geral do Vendedor (AGV)
$$AGV = \sum (AR_c \times w_c)$$

| Categoria | Peso Sugerido | Racional |
|---|---|---|
| Multifocais (LMF) | 0,25 | Maior margem e ticket |
| Transition (LTR) | 0,20 | Alto valor agregado |
| Grau Simples (LGS) | 0,20 | Volume base |
| Óculos de Sol (OS) | 0,15 | Margem forte, sazonal |
| Serviços (SRV) | 0,10 | Fidelização |
| Acessórios (ACC) | 0,10 | Complemento |

### 5.14 Atingimento Geral da Loja (AGL)
$$AGL = \sum (AR_c^{loja} \times w_c)$$

---

## 6. Margem de Contribuição Desdobrada em 5 Níveis

A fórmula base B5 (já existente na SPEC) calcula a MC por item. Abaixo, o desdobramento completo nos 5 níveis operacionais.

### 6.1 Nível 1 — MC por Item / SKU (Base B5 existente)
$$MC_{item} = PV_{item} - CE_{item} - CV_{item}$$

| Variável | Significado |
|---|---|
| $PV_{item}$ | Preço de Venda praticado (líquido de desconto) |
| $CE_{item}$ | Custo de Entrada (NF de compra) |
| $CV_{item}$ | Custos Variáveis (imposto sobre venda, comissão, taxa de cartão/Pix, frete) |

MC percentual do item:
$$MC\%_{item} = \frac{MC_{item}}{PV_{item}} \times 100$$

### 6.2 Nível 2 — MC por Categoria de Produto
$$MC_{cat} = \sum_{i \in cat} MC_{item_i}$$

MC percentual da categoria:
$$MC\%_{cat} = \frac{MC_{cat}}{R_{cat}} \times 100$$

- $R_{cat}$ = Receita total da categoria (soma dos PV)

**Participação da categoria na MC total:**
$$Part_{cat} = \frac{MC_{cat}}{\sum MC_{cat}} \times 100$$

Isso responde: "Qual categoria mais contribui para pagar o custo fixo?"

### 6.3 Nível 3 — MC por Vendedor
$$MC_{vend} = \sum_{i \in vendas_{vend}} MC_{item_i}$$

MC percentual do vendedor:
$$MC\%_{vend} = \frac{MC_{vend}}{R_{vend}} \times 100$$

- $R_{vend}$ = Receita total gerada pelo vendedor

**MC por Categoria por Vendedor (a matriz completa):**
$$MC_{vend,cat} = \sum_{i \in (vendas_{vend} \cap cat)} MC_{item_i}$$

Isso responde: "O vendedor X vende Multifocal com margem boa ou está dando desconto que corrói?"

**MC por Transação do vendedor:**
$$MC_{tx,vend} = \frac{MC_{vend}}{N_{vend}}$$

- $N_{vend}$ = Número de transações do vendedor

Isso responde: "Qual é a margem média que cada venda dele gera?"

### 6.4 Nível 4 — MC por Gestor (Equipe)
$$MC_{gestor} = \sum_{v \in equipe_{gestor}} MC_{vend_v}$$

MC percentual do gestor:
$$MC\%_{gestor} = \frac{MC_{gestor}}{R_{gestor}} \times 100$$

- $R_{gestor}$ = Receita total da equipe do gestor

**Dispersão de margem na equipe:**
$$Disp_{gestor} = MC\%_{vend}^{max} - MC\%_{vend}^{min}$$

- Se a dispersão for alta, o gestor tem vendedores destruindo margem e vendedores preservando. É sinal de falta de padrão na negociação.

### 6.5 Nível 5 — MC por Loja
$$MC_{loja} = \sum_{v \in loja} MC_{vend_v}$$

MC percentual da loja:
$$MC\%_{loja} = \frac{MC_{loja}}{R_{loja}} \times 100$$

**Ponto de Equilíbrio Operacional (PE) — onde a loja para de dar prejuízo:**
$$PE_{loja} = \frac{CF_{loja}}{MC\%_{loja} / 100}$$

- $CF_{loja}$ = Custo Fixo mensal da loja (aluguel, folha, energia, sistemas)
- Resultado em R$: a receita mínima para cobrir o fixo

**Índice de Cobertura do Custo Fixo (ICCF):**
$$ICCF_{loja} = \frac{MC_{loja}}{CF_{loja}}$$

| Resultado | Leitura |
|---|---|
| ICCF < 1 | A loja não cobre o custo fixo — **prejuízo operacional** |
| ICCF = 1 | Empata (breakeven) |
| ICCF > 1 | Gera lucro operacional. Quanto maior, mais saudável |

### 6.6 Nível 6 — MC da Operação Consolidada
$$MC_{op} = \sum_{l \in lojas} MC_{loja_l}$$

MC percentual da operação:
$$MC\%_{op} = \frac{MC_{op}}{R_{op}} \times 100$$

**Ponto de Equilíbrio da Operação:**
$$PE_{op} = \frac{CF_{op}}{MC\%_{op} / 100}$$

- $CF_{op}$ = Custo Fixo total de todas as lojas + overhead corporativo

### 6.7 Fórmulas Derivadas de Margem (Diagnósticos)

**Alerta de Margem Negativa (por transação):**
$$Alerta_{MC} = \begin{cases} \text{🔴 TRAVA} & \text{se } MC_{item} \leq 0 \\ \text{🟡 RISCO} & \text{se } MC\%_{item} < MC\%_{piso} \\ \text{🟢 OK} & \text{caso contrário} \end{cases}$$

- $MC\%_{piso}$ = Margem mínima aceitável definida pelo dono/consultor (ex: 15%)

**Erosão de Margem por Desconto (EMD):**
$$EMD_{vend} = \frac{\sum Desc_{vend}}{R_{vend}} \times 100$$

- $Desc_{vend}$ = Soma dos descontos concedidos pelo vendedor
- Identifica quem está comprando a venda com a margem da loja

**Ranking de Destruição de Margem:**
$$RDM_{vend} = MC\%_{vend} - MC\%_{loja}$$

- Negativo = vendedor destrói margem comparado à média da loja
- Positivo = vendedor preserva margem acima da média

**MC Projetada para o Fim do Mês:**
$$MC_{proj} = \frac{MC_{acum}}{DU_e} \times DU_t$$

**Gap de MC vs. Meta de MC:**
$$Gap_{MC} = MC_{proj} - MC_{meta}$$

---

## 7. Glossário Completo

| Sigla | Significado |
|---|---|
| AC / AT | Atendimentos Cadastrados / Totais |
| ACC | Acessórios |
| AGL | Atingimento Geral da Loja |
| AGV | Atingimento Geral do Vendedor |
| AR | Atingimento Real (%) |
| CE | Custo de Entrada |
| CF | Custo Fixo |
| CMC | Contribuição Marginal por Categoria |
| CRA | Classificação de Risco de Atingimento |
| CV | Custos Variáveis |
| DR | Dias até a Ruptura |
| DU_e / DU_t | Dias Úteis transcorridos / totais |
| EA / VMD | Estoque Atual / Venda Média Diária |
| EDN | Esforço Diário Necessário |
| EMD | Erosão de Margem por Desconto |
| ER | Elasticidade de Recuperação |
| Gap | Descolamento da Meta |
| IA | Índice de Anexação |
| IAd | Índice de Adesão |
| IC | Índice de Captura |
| ICCF | Índice de Cobertura do Custo Fixo |
| IM | Índice de Mix |
| IR | Índice de Resgate |
| IT | Índice de Ticket |
| LGS | Lentes Grau Simples |
| LMF | Lentes Multifocais |
| LTR | Lentes Transition |
| MC | Margem de Contribuição |
| ME | Meta Esperada proporcional |
| MR | Meta Residual |
| NC | Nota Comportamental |
| OS | Óculos de Sol |
| PA | Projeção de Atingimento |
| Pace | Velocidade Diária de vendas |
| PE | Ponto de Equilíbrio |
| PV (forecast) | Previsão de Venda |
| PV (margem) | Preço de Venda |
| RC / RT | Resgates Convertidos / Trabalhados |
| RDM | Ranking de Destruição de Margem |
| SEV | Score de Engenharia de Venda |
| SRV | Serviços |
| T | Tendência Semanal |
| TMI / TMR | Ticket Médio Ideal / Real |
| VC / VG | Vendas Complementar / Grau |
