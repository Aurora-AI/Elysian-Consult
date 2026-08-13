# DICIONÁRIO DO DASHBOARD — o que renderizar, onde, com que profundidade

> ⚙️ **Arquivo gerado** por `gerar_render.py` a partir de `registro/*.yaml`.
> Não editar à mão. É o documento que o desenvolvedor do painel consome —
> se ele diverge da tela, a tela está errada, não o dicionário.

> **Dois princípios (`DEC-009`):** superfície mínima, profundidade total ·
> o drill-down é diagnóstico, não navegação.

**6 artefatos** · 24 na superfície · 39 no drill-down ·
0 por dependência · **36 sem artefato declarado**

---

## Onde cada fórmula reside

O **domínio** é propriedade da fórmula — não muda com a tela. O artefato é
circunstância: hoje consome, amanhã pode não consumir. Esta é a leitura estável.

| Domínio | Fórmulas | Na superfície | No drill-down | **Sem artefato** |
|---|---:|---:|---:|---:|
| **COMERCIAL** | 35 | 6 | 13 | **16** |
| **FINANCEIRO** | 28 | 5 | 13 | **10** |
| **CLIENTE** | 12 | 9 | 3 |  |
| **ESTOQUE** | 8 | 2 | 5 | **1** |
| **CREDITO** 🔴 | 5 |  |  | **5** |
| **AUDITORIA** | 5 | 1 | 4 |  |
| **SUPRIMENTOS** 🔴 | 4 |  |  | **4** |
| **PESSOAS** | 2 | 1 | 1 |  |

### COMERCIAL · 35

| Fórmula | Símbolo | Grão | Janela | Onde aparece |
|---|---|---|---|---|
| `FOR-FCT-001` Previsão de Venda Semanal do vendedor (PVS) | `PVS` | vendedor | semanal | **— sem artefato —** |
| `FOR-MET-001` Atingimento Real (AR) | `AR_c` | vendedor_categoria | mensal_acumulado | **— sem artefato —** |
| `FOR-MET-002` Projeção de Atingimento (PA) | `PA_c` | vendedor_categoria | mensal_projetado | **— sem artefato —** |
| `FOR-MET-003` Projeção de Atingimento em % da meta | `PA%_c` | vendedor_categoria | mensal_projetado | **— sem artefato —** |
| `FOR-MET-004` Meta Esperada proporcional ao dia (ME) | `ME_c` | mes | diaria | **— sem artefato —** |
| `FOR-MET-005` Descolamento da Meta (Gap) | `Gap_c` | vendedor_categoria | diaria | **— sem artefato —** |
| `FOR-MET-006` Velocidade Diária (Pace) | `Pace_c` | vendedor_categoria | diaria | **— sem artefato —** |
| `FOR-MET-007` Esforço Diário Necessário (EDN) | `EDN_c` | vendedor_categoria | diaria | **— sem artefato —** |
| `FOR-MET-008` Meta Residual | `MRes_c` | vendedor_categoria | mensal_acumulado | **— sem artefato —** |
| `FOR-MET-009` Índice de Mix (IM) | `IM_c` | vendedor_categoria | mensal_acumulado | **— sem artefato —** |
| `FOR-MET-010` Tendência Semanal (T) | `T_c` | vendedor_categoria | semanal | **— sem artefato —** |
| `FOR-MET-011` Elasticidade de Recuperação (ER) | `ER_c` | vendedor_categoria | mensal | **— sem artefato —** |
| `FOR-MET-012` Contribuição Marginal por Categoria (CMC) | `CMC_c` | vendedor_categoria | mensal | **— sem artefato —** |
| `FOR-MET-013` Atingimento Geral do Vendedor (AGV) | `AGV` | vendedor | mensal | **— sem artefato —** |
| `FOR-MET-014` Atingimento Geral da Loja (AGL) | `AGL` | loja | mensal | **— sem artefato —** |
| `FOR-SEV-001` Normalização universal de índice | `IN` | vendedor | mensal | `ART-PER-001` |
| `FOR-SEV-002` Índice de Captura — taxa crua | `IC_cru` | vendedor | mensal | `ART-PER-001` |
| `FOR-SEV-003` Índice de Captura (IC) — normalizado | `IC` | vendedor | mensal | `ART-PER-001` |
| `FOR-SEV-004` Attach do vendedor — taxa crua | `attach` | vendedor | mensal | `ART-PER-001` |
| `FOR-SEV-005` Attach-alvo (P75 por segmento) | `AttachAlvo` | loja_segmento | trimestral | `ART-PER-001` |
| `FOR-SEV-006` Índice de Anexação (IA) — normalizado | `IA` | vendedor | mensal | `ART-PER-001` |
| `FOR-SEV-007` Índice de Ticket (IT) | `IT` | vendedor | mensal | `ART-PER-001` |
| `FOR-SEV-008` Conversão de fila — taxa crua | `ConvReal` | vendedor_temperatura | mensal | `ART-PER-001` |
| `FOR-SEV-009` Conversão-alvo por temperatura de fila | `ConvAlvo` | loja_temperatura | trimestral | `ART-PER-001` |
| `FOR-SEV-010` Índice de Resgate (IR) — normalizado | `IR` | vendedor | mensal | `ART-PER-001` |
| `FOR-SEV-011` Índice de Adesão (IAd) — normalizado | `IAd` | vendedor | mensal | `ART-PER-001` |
| `FOR-SEV-012` Score de Engenharia de Venda (SEV) | `SEV` | vendedor | mensal | `ART-PER-001` |
| `FOR-TMI-001` TMI histórico do segmento | `TMIhs` | loja_segmento | trimestral | `ART-PER-001` |
| `FOR-TMI-002` TMI histórico do vendedor (ponderado pelo mi | `TMIhv` | vendedor | trimestral | `ART-PER-001` |
| `FOR-TMI-003` TMI de planejamento | `TMIp` | loja | trimestral | `ART-PER-001` |
| `FOR-TMI-004` TMI operacional — a ponte (a régua do vended | `TMIo` | vendedor | trimestral | `ART-PER-001` |
| `FOR-TMI-005` Gap do TMI (o achado) | `Gap_TMI` | vendedor | trimestral | `ART-PER-001` |
| `FOR-TMI-006` Ticket Médio Real | `TMR` | vendedor | mensal | `ART-LAU-001` · `ART-COC-001` · `ART-PER-001` · `ART-FIL-001` |
| `PAR-MET-001` Pesos por categoria (w_c) — AGV/AGL | `w_c` | rede | fixa | **— sem artefato —** |
| `PAR-SEV-001` Régua de Pesos por Maturidade — vetor p1..p5 | `p⃗` | loja | trimestral | `ART-PER-001` |

### FINANCEIRO · 28

| Fórmula | Símbolo | Grão | Janela | Onde aparece |
|---|---|---|---|---|
| `FOR-FIN-001` Mensalidade mínima do Clube (C1) | `mensalidade_min` | clube | anual | **— sem artefato —** |
| `FOR-FIN-002` LTV do assinante do Clube | `LTV_clube` | clube | anual | **— sem artefato —** |
| `FOR-FIN-003` Break-even do Clube | `BE_clube` | clube | anual | **— sem artefato —** |
| `FOR-FIN-004` MRR do Clube | `MRR` | loja | mensal | `ART-COC-001` |
| `FOR-MRG-001` MC por item / SKU — Nível 1 | `MC_item` | item | tempo_real | `ART-LAU-001` · `ART-COC-001` · `ART-FIL-002` |
| `FOR-MRG-002` MC percentual do item | `MC%_item` | item | tempo_real | `ART-LAU-001` · `ART-FIL-002` |
| `FOR-MRG-003` MC por categoria — Nível 2 | `MC_cat` | categoria_loja | mensal | `ART-LAU-001` · `ART-COC-001` |
| `FOR-MRG-004` MC percentual da categoria | `MC%_cat` | categoria_loja | mensal | `ART-LAU-001` · `ART-COC-001` |
| `FOR-MRG-005` Participação da categoria na MC total | `Part_cat` | categoria_loja | mensal | `ART-LAU-001` · `ART-COC-001` |
| `FOR-MRG-006` MC por vendedor — Nível 3 | `MC_vend` | vendedor | mensal | `ART-PER-001` |
| `FOR-MRG-007` MC percentual do vendedor | `MC%_vend` | vendedor | mensal | `ART-PER-001` |
| `FOR-MRG-008` MC por categoria por vendedor (a matriz) | `MC_vend,cat` | vendedor_categoria | mensal | `ART-PER-001` |
| `FOR-MRG-009` MC por transação do vendedor | `MC_tx,vend` | vendedor | mensal | `ART-PER-001` |
| `FOR-MRG-010` MC por gestor (equipe) — Nível 4 | `MC_gestor` | gestor | mensal | `ART-PER-001` |
| `FOR-MRG-011` MC percentual do gestor | `MC%_gestor` | gestor | mensal | `ART-PER-001` |
| `FOR-MRG-012` Dispersão de margem na equipe | `Disp_gestor` | gestor | mensal | `ART-PER-001` |
| `FOR-MRG-013` MC por loja — Nível 5 | `MC_loja` | loja | mensal | `ART-LAU-001` · `ART-COC-001` |
| `FOR-MRG-014` MC percentual da loja | `MC%_loja` | loja | mensal | `ART-LAU-001` · `ART-COC-001` |
| `FOR-MRG-015` Ponto de Equilíbrio Operacional da loja | `PE_loja` | loja | mensal | **— sem artefato —** |
| `FOR-MRG-016` Índice de Cobertura do Custo Fixo (ICCF) | `ICCF_loja` | loja | mensal | **— sem artefato —** |
| `FOR-MRG-017` MC da operação consolidada — Nível 6 | `MC_op` | rede | mensal | **— sem artefato —** |
| `FOR-MRG-018` MC percentual da operação | `MC%_op` | rede | mensal | **— sem artefato —** |
| `FOR-MRG-019` Ponto de Equilíbrio da operação | `PE_op` | rede | mensal | **— sem artefato —** |
| `FOR-MRG-020` Alerta de Margem Negativa | `Alerta_MC` | item | tempo_real | `ART-LAU-001` · `ART-FIL-002` |
| `FOR-MRG-021` Erosão de Margem por Desconto (EMD) | `EMD_vend` | vendedor | mensal | `ART-LAU-001` · `ART-PER-001` · `ART-FIL-002` |
| `FOR-MRG-022` Ranking de Destruição de Margem (RDM) | `RDM_vend` | vendedor | mensal | `ART-PER-001` |
| `FOR-MRG-023` MC projetada para o fim do mês | `MC_proj` | loja | mensal_projetado | **— sem artefato —** |
| `FOR-MRG-024` Gap de MC vs. meta de MC | `Gap_MC` | loja | mensal_projetado | **— sem artefato —** |

### CLIENTE · 12

| Fórmula | Símbolo | Grão | Janela | Onde aparece |
|---|---|---|---|---|
| `FOR-BAS-001` Completude de Cadastro (A1) | `Compl` | loja_campo | diaria | `ART-LAU-001` · `ART-COC-001` |
| `FOR-BAS-002` Segmentação RFM (A2) | `RFM` | cliente | mensal | `ART-LAU-001` · `ART-COC-001` · `ART-FIL-001` |
| `FOR-BAS-003` Ciclo de recompra da própria base (A3) | `ciclo` | loja | mensal | `ART-LAU-001` · `ART-COC-001` · `ART-FIL-001` |
| `FOR-BAS-004` Churn Invisível — flag (A3) | `churn` | cliente | semanal | `ART-LAU-001` · `ART-COC-001` · `ART-FIL-001` |
| `FOR-BAS-005` Perda em R$ por churn | `perda_churn` | loja | semanal | `ART-LAU-001` · `ART-COC-001` |
| `FOR-BAS-006` Índice de recuperabilidade do churn | `silence_to_cycle_ratio` | cliente | semanal | `ART-LAU-001` · `ART-COC-001` · `ART-FIL-001` |
| `FOR-BAS-007` Attach rate por categoria (A4) | `attach_cat` | loja_categoria | semanal | `ART-LAU-001` · `ART-COC-001` · `ART-FIL-001` |
| `FOR-BAS-008` Receita Latente em R$ (A4) | `R_latente` | loja_categoria | semanal | `ART-LAU-001` · `ART-COC-001` · `ART-FIL-001` |
| `FOR-BAS-009` Taxa de recompra | `tx_recompra` | loja | mensal | `ART-LAU-001` · `ART-COC-001` |
| `FOR-BAS-010` Taxa de identificação | `tx_ident` | loja | diaria | `ART-COC-001` |
| `FOR-BAS-011` Conversão de pendentes | `conv_pendentes` | loja | semanal | `ART-COC-001` |
| `FOR-BAS-012` UPT — itens por venda | `UPT` | loja | mensal | `ART-COC-001` · `ART-FIL-001` |

### ESTOQUE · 8

| Fórmula | Símbolo | Grão | Janela | Onde aparece |
|---|---|---|---|---|
| `FOR-EST-001` Giro de estoque (B1) | `giro` | sku_categoria_loja | mensal | `ART-LAU-001` · `ART-COC-001` |
| `FOR-EST-002` Cobertura de estoque em dias (B1) | `cobertura` | sku_categoria_loja | mensal | `ART-LAU-001` · `ART-COC-001` |
| `FOR-EST-003` GMROI — versão documentada (B2) | `GMROI_doc` | sku_categoria_loja | mensal | `ART-LAU-001` · `ART-COC-001` |
| `FOR-EST-004` Curva ABC cruzada com giro (B3) | `ABC` | sku | mensal | `ART-LAU-001` · `ART-COC-001` |
| `FOR-EST-005` Estoque morto — critério (B4) | `morto` | sku_loja | mensal | `ART-LAU-001` · `ART-COC-001` · `ART-FIL-002` |
| `FOR-EST-006` Capital preso em estoque morto (B4) | `capital_preso` | loja | mensal | `ART-LAU-001` · `ART-COC-001` |
| `FOR-EST-007` Índice de estoque morto | `idx_morto` | loja | mensal | `ART-LAU-001` · `ART-COC-001` |
| `FOR-FCT-002` Dias até a Ruptura (DR) | `DR` | sku_loja | semanal | **— sem artefato —** |

### CREDITO · 5

| Fórmula | Símbolo | Grão | Janela | Onde aparece |
|---|---|---|---|---|
| `FOR-FIN-005` Uplift de Ticket pelo crédito (C2) | `uplift` | loja | mensal | **— sem artefato —** |
| `FOR-FIN-006` Taxa de Aprovação do parceiro (C2) | `aprovacao` | loja_parceiro | semanal | **— sem artefato —** |
| `FOR-FIN-007` Provisão de inadimplência — versão de risco  | `provisao_inad` | loja | mensal | **— sem artefato —** |
| `FOR-FIN-008` Inadimplência — versão risco zero (C2) | `inad_parceiro` | parceiro | mensal | **— sem artefato —** |
| `FOR-FIN-009` Receita financeira da operação | `rec_financeira` | loja | mensal | **— sem artefato —** |

### AUDITORIA · 5

| Fórmula | Símbolo | Grão | Janela | Onde aparece |
|---|---|---|---|---|
| `FOR-AUD-001` GMROI — versão implementada | `GMROI_impl` | sku | mensal | `ART-LAU-001` · `ART-FIL-002` |
| `FOR-AUD-002` Attach Rate — versão implementada | `attach_impl` | loja_par_categoria | mensal | `ART-LAU-001` · `ART-FIL-002` |
| `FOR-AUD-003` Corrosão de Ticket Médio por Vendedor — vers | `corrosao` | vendedor | mensal | `ART-LAU-001` · `ART-FIL-002` |
| `FOR-AUD-004` Risco de Concentração de receita VIP | `concentracao_vip` | vendedor | mensal | `ART-LAU-001` · `ART-FIL-002` |
| `FOR-AUD-005` Conversão Follow-on (serviço → produto) | `follow_on` | loja | trimestral | `ART-LAU-001` · `ART-FIL-002` |

### SUPRIMENTOS · 4

| Fórmula | Símbolo | Grão | Janela | Onde aparece |
|---|---|---|---|---|
| `FOR-CNC-001` Economia gerada por ótica | `economia` | otica_sku | mensal | **— sem artefato —** |
| `FOR-CNC-002` Volume agregado da rede | `volume_agregado` | rede_fornecedor | mensal | **— sem artefato —** |
| `FOR-CNC-003` Taxa de adesão da rede | `adesao_rede` | rede | mensal | **— sem artefato —** |
| `FOR-CNC-004` Efeito do comprar inteligente (sell-in × sel | `efeito_concentracao` | otica | trimestral | **— sem artefato —** |

### PESSOAS · 2

| Fórmula | Símbolo | Grão | Janela | Onde aparece |
|---|---|---|---|---|
| `FOR-CMP-001` Nota Comportamental (NC) | `NC` | vendedor | trimestral | `ART-PER-001` |
| `FOR-CMP-002` Régua de Perfil Ideal (RPI) | `RPI` | loja | anual | `ART-PER-001` |

---

## `ART-ANX-001` · Anexo Vivo — a procedência

> O corpo afirma; o anexo É a soma. É o piso de todo drill-down do sistema.

**Quem abre:** dono · **Quando:** clique em qualquer número do laudo · **Cadência:** sob_demanda · **Modo mínimo:** (a) · **Linguagem:** TECNICA

### Superfície — teto de 0 elemento(s)

- nada — o anexo não tem superfície, ele É profundidade

**Não aparece ativamente:**

- nada é omitido; é o único artefato sem omissão declarada

### Profundidade

**Vertical** (desagregar) — `agregado` → `componente` → `linha_de_origem`

**Completude:** `TOTAL`

**Piso:** source_rows com teto em provenance_sample_cap (F14 Pilar 2)

---

## `ART-COC-001` · Cockpit do dono

> O painel que o dono abre. Indicador-mãe é um só: o ciclo de recompra caindo.

**Quem abre:** dono · **Quando:** acompanhamento da operação · **Cadência:** mensal · **Modo mínimo:** (a) · **Linguagem:** LAUDO

### Superfície — teto de 7 elemento(s)

**Âncora:** `FOR-BAS-003` — o número que justifica abrir.

| # | Fórmula | Símbolo | Grão | Janela | Teto | Sem base → |
|---|---|---|---|---|---|---|
| 1 | `FOR-BAS-003` Ciclo de recompra da própria base (A3) | `ciclo` | loja | mensal | — | NULO+selo |
| 2 | `FOR-BAS-010` Taxa de identificação | `tx_ident` | loja | diaria | — | NULO+selo |
| 3 | `FOR-BAS-009` Taxa de recompra | `tx_recompra` | loja | mensal | — | NULO+selo |
| 4 | `FOR-BAS-007` Attach rate por categoria (A4) | `attach_cat` | loja_categoria | semanal | — | NULO+selo |
| 5 | `FOR-EST-003` GMROI — versão documentada (B2) | `GMROI_doc` | sku_categoria_loja | mensal | — | NULO+selo |
| 6 | `FOR-BAS-011` Conversão de pendentes | `conv_pendentes` | loja | semanal | — | NULO+selo |
| 7 | `FOR-FIN-004` MRR do Clube | `MRR` | loja | mensal | — | NULO+selo |

**Não aparece ativamente:**

- métrica de vaidade — a fonte proíbe explicitamente
- nome de vendedor (REG-SEV-004)
- índice sem base: aparece NULO com selo, nunca 0 nem 100 (REG-NUM-001)

### Profundidade

**Vertical** (desagregar) — `rede` → `loja` → `equipe` → `vendedor` → `venda` → `item` → `linha_de_origem`

**Horizontal** (fatiar no mesmo grão)

| Grão | Dimensões |
|---|---|
| `loja` | categoria · natureza_item · periodo · forma_pagamento |
| `cliente` | segmento_rfm · recuperabilidade · temperatura_fila |
| `sku` | categoria · curva_abc · giro |

**Completude:** `TOTAL`

### Regras que o render deve obedecer

- `REG-NUM-001` — Sem base → resultado NULO com selo, nunca zero nem cem · **INEGOCIAVEL**
- `REG-NUM-005` — Composição parcial → renormaliza sobre o disponível e declara · **INEGOCIAVEL**
- `REG-SEV-004` — Empacotamento do score (a trava-mãe) · **INEGOCIAVEL**

### 🔴 Bloqueios ativos

- `FOR-BAS-007` — CONFLITANTE
- `FOR-BAS-010` — CONFLITANTE
- `FOR-EST-003` — CONFLITANTE

---

## `ART-FIL-001` · Fila de resgate diária

> A ponte entre a inteligência da máquina e a venda de verdade. Ordenada por recuperabilidade, não por cifrão.

**Quem abre:** vendedor · **Quando:** abertura da loja · **Cadência:** diaria · **Modo mínimo:** (a) · **Linguagem:** LAUDO

### Superfície — teto de 1 elemento(s)

**Âncora:** `a lista de contatos do dia` — o número que justifica abrir.

- cliente · o que oferecer · por que agora

**Não aparece ativamente:**

- score do próprio vendedor (isso é ART-PER-001, e no coaching privado)
- métrica de loja ou de rede — o vendedor não precisa
- o cálculo por trás da ordenação

### Profundidade

**Vertical** (desagregar) — `fila` → `cliente` → `historico_de_compra` → `venda` → `item` → `linha_de_origem`

**Horizontal** (fatiar no mesmo grão)

| Grão | Dimensões |
|---|---|
| `cliente` | temperatura_fila · segmento_rfm · categoria_faltante · ciclo |

**Completude:** `TOTAL`

### Regras que o render deve obedecer

- `REG-NUM-001` — Sem base → resultado NULO com selo, nunca zero nem cem · **INEGOCIAVEL**

---

## `ART-FIL-002` · Fila de auditoria manual

> O resíduo não classificável — nunca o atacado. Veredito em ~30 segundos por item.

**Quem abre:** consultor · **Quando:** rodada de auditoria concluída · **Cadência:** por_rodada · **Modo mínimo:** (a) · **Linguagem:** TECNICA

### Superfície — teto de 1 elemento(s)

**Âncora:** `quantos itens aguardam veredito` — o número que justifica abrir.

- item + todas as evidências já cruzadas, para decisão em ~30s

**Não aparece ativamente:**

- o atacado — só o resíduo que o motor não conseguiu classificar sozinho
- acusação a vendedor antes do veredito

### Profundidade

**Vertical** (desagregar) — `fila` → `item` → `transacao` → `sku` → `nota_fiscal` → `linha_de_origem`

**Horizontal** (fatiar no mesmo grão)

| Grão | Dimensões |
|---|---|
| `item` | custo_nf · preco_tabela · preco_praticado · flag_promocao · estoque_morto |

**Completude:** `TOTAL`

---

## `ART-LAU-001` · Executive Audit Report — o Laudo

> Prova ao dono que o relatório que ele olha hoje mente. Uma vez, no D5–D7.

**Quem abre:** dono · **Quando:** diagnóstico concluído — o choque do Dia 5 · **Cadência:** uma_vez_por_rodada · **Modo mínimo:** (a) · **Linguagem:** LAUDO

### Superfície — teto de 1 elemento(s)

**Âncora:** `R$ total em risco, consolidado` — o número que justifica abrir.

- um único número em R$, tipografia gigante, zero tabela, zero lista

**Não aparece ativamente:**

- SKU, churn, attach, GMROI, margem de contribuição, LTV, dataset, outlier — vocabulário PROIBIDO (F12 §3.4)
- qualquer métrica que responda 'quanto mede' em vez de 'quanto custa'
- item pendente na fila de auditoria (F13) — pendente nunca vira fato
- 4º capítulo no Ato 3 — são exatamente 3, o resto vira sub-item ou anexo

### Profundidade

**Vertical** (desagregar) — `rede` → `loja` → `categoria` → `sku` → `venda` → `item` → `linha_de_origem`

**Horizontal** (fatiar no mesmo grão)

| Grão | Dimensões |
|---|---|
| `loja` | natureza_item · categoria · periodo |
| `cliente` | segmento_rfm · recuperabilidade |

**Completude:** `TOTAL`

**Piso:** ART-ANX-001 — o anexo É a soma; divergência de 1 centavo quebra o build

### Regras que o render deve obedecer

- `REG-NUM-001` — Sem base → resultado NULO com selo, nunca zero nem cem · **INEGOCIAVEL**
- `REG-NUM-004` — Valor fora do domínio → vira leitura, não número · **INEGOCIAVEL**

---

## `ART-PER-001` · Painel de performance por bandas

> Distribuição, nunca nomes. O KPI da tela é mover a curva para a direita, não cortar a cauda.

**Quem abre:** gestor · **Quando:** ciclo de desenvolvimento da equipe · **Cadência:** mensal · **Modo mínimo:** (a) · **Linguagem:** TECNICA

### Superfície — teto de 4 elemento(s)

**Âncora:** `gap em R$ entre a média e o topo` — o número que justifica abrir.

- distribuição por banda (Topo/Forte/Médio/Base)
- assinatura de comportamento de cada banda
- gap em R$
- tendência intra-loja

**Não aparece ativamente:**

- 🔴 NOMES — vivem só no coaching privado (REG-SEV-004)
- 🔴 ranking cru — o score sai SEMPRE com caminho de desenvolvimento
- 🔴 comparação de SEV entre lojas de vetores de peso distintos (REG-SEV-003)
- SEV abaixo do piso de 60% de peso disponível (REG-NUM-005)
- vendedor abaixo do mínimo de amostra em ranking ou banda (REG-NUM-002)

### Profundidade

**Vertical** (desagregar) — `rede` → `loja` → `equipe` → `banda` → `vendedor` → `venda` → `item` → `linha_de_origem`

**Horizontal** (fatiar no mesmo grão)

| Grão | Dimensões |
|---|---|
| `vendedor` | indice · categoria · segmento · temperatura_fila · periodo |
| `banda` | assinatura_comportamento · gap_em_reais |

**Completude:** `PARCIAL`
 — corta em: o nível VENDEDOR nominal só abre no modo (c), com aceite de RH/jurídico registrado
  · razão: REG-SEV-004 — o painel é radar de desenvolvimento, nunca vigilância. LGPD e trabalhista.

### Regras que o render deve obedecer

- `REG-SEV-002` — Anti-gaming do denominador · **INEGOCIAVEL**
- `REG-SEV-003` — Comparabilidade do SEV entre lojas · **INEGOCIAVEL**
- `REG-SEV-004` — Empacotamento do score (a trava-mãe) · **INEGOCIAVEL**
- `REG-NUM-002` — Amostra insuficiente → calcula, marca, e fica fora de comparação · **INEGOCIAVEL**
- `REG-NUM-005` — Composição parcial → renormaliza sobre o disponível e declara · **INEGOCIAVEL**

---

## Índice reverso — onde cada fórmula aparece

| Fórmula | Aparece em | Papel |
|---|---|---|
| `FOR-AUD-001` GMROI — versão implementada | `ART-LAU-001` (profundidade) · `ART-FIL-002` (profundidade) | direta |
| `FOR-AUD-002` Attach Rate — versão implementada | `ART-LAU-001` (profundidade) · `ART-FIL-002` (profundidade) | direta |
| `FOR-AUD-003` Corrosão de Ticket Médio por Vendedor —  | `ART-LAU-001` (profundidade) · `ART-FIL-002` (superfície) | direta |
| `FOR-AUD-004` Risco de Concentração de receita VIP | `ART-LAU-001` (profundidade) · `ART-FIL-002` (profundidade) | direta |
| `FOR-AUD-005` Conversão Follow-on (serviço → produto) | `ART-LAU-001` (profundidade) · `ART-FIL-002` (profundidade) | direta |
| `FOR-BAS-001` Completude de Cadastro (A1) | `ART-LAU-001` (profundidade) · `ART-COC-001` (profundidade) | direta |
| `FOR-BAS-002` Segmentação RFM (A2) | `ART-LAU-001` (profundidade) · `ART-COC-001` (profundidade) · `ART-FIL-001` (profundidade) | direta |
| `FOR-BAS-003` Ciclo de recompra da própria base (A3) | `ART-LAU-001` (profundidade) · `ART-COC-001` (superfície) · `ART-FIL-001` (profundidade) | direta |
| `FOR-BAS-004` Churn Invisível — flag (A3) | `ART-LAU-001` (superfície) · `ART-COC-001` (profundidade) · `ART-FIL-001` (superfície) | direta |
| `FOR-BAS-005` Perda em R$ por churn | `ART-LAU-001` (superfície) · `ART-COC-001` (profundidade) | direta |
| `FOR-BAS-006` Índice de recuperabilidade do churn | `ART-LAU-001` (profundidade) · `ART-COC-001` (profundidade) · `ART-FIL-001` (superfície) | direta |
| `FOR-BAS-007` Attach rate por categoria (A4) | `ART-LAU-001` (profundidade) · `ART-COC-001` (superfície) · `ART-FIL-001` (superfície) | direta |
| `FOR-BAS-008` Receita Latente em R$ (A4) | `ART-LAU-001` (superfície) · `ART-COC-001` (profundidade) · `ART-FIL-001` (superfície) | direta |
| `FOR-BAS-009` Taxa de recompra | `ART-LAU-001` (profundidade) · `ART-COC-001` (superfície) | direta |
| `FOR-BAS-010` Taxa de identificação | `ART-COC-001` (superfície) | direta |
| `FOR-BAS-011` Conversão de pendentes | `ART-COC-001` (superfície) | direta |
| `FOR-BAS-012` UPT — itens por venda | `ART-COC-001` (profundidade) · `ART-FIL-001` (profundidade) | direta |
| `FOR-CMP-001` Nota Comportamental (NC) | `ART-PER-001` (superfície) | direta |
| `FOR-CMP-002` Régua de Perfil Ideal (RPI) | `ART-PER-001` (profundidade) | direta |
| `FOR-EST-001` Giro de estoque (B1) | `ART-LAU-001` (profundidade) · `ART-COC-001` (profundidade) | direta |
| `FOR-EST-002` Cobertura de estoque em dias (B1) | `ART-LAU-001` (profundidade) · `ART-COC-001` (profundidade) | direta |
| `FOR-EST-003` GMROI — versão documentada (B2) | `ART-LAU-001` (profundidade) · `ART-COC-001` (superfície) | direta |
| `FOR-EST-004` Curva ABC cruzada com giro (B3) | `ART-LAU-001` (profundidade) · `ART-COC-001` (profundidade) | direta |
| `FOR-EST-005` Estoque morto — critério (B4) | `ART-LAU-001` (profundidade) · `ART-COC-001` (profundidade) · `ART-FIL-002` (profundidade) | direta |
| `FOR-EST-006` Capital preso em estoque morto (B4) | `ART-LAU-001` (superfície) · `ART-COC-001` (profundidade) | direta |
| `FOR-EST-007` Índice de estoque morto | `ART-LAU-001` (profundidade) · `ART-COC-001` (profundidade) | direta |
| `FOR-FIN-004` MRR do Clube | `ART-COC-001` (superfície) | direta |
| `FOR-MRG-001` MC por item / SKU — Nível 1 | `ART-LAU-001` (superfície) · `ART-COC-001` (profundidade) · `ART-FIL-002` (profundidade) | direta |
| `FOR-MRG-002` MC percentual do item | `ART-LAU-001` (profundidade) · `ART-FIL-002` (profundidade) | direta |
| `FOR-MRG-003` MC por categoria — Nível 2 | `ART-LAU-001` (profundidade) · `ART-COC-001` (profundidade) | direta |
| `FOR-MRG-004` MC percentual da categoria | `ART-LAU-001` (profundidade) · `ART-COC-001` (profundidade) | direta |
| `FOR-MRG-005` Participação da categoria na MC total | `ART-LAU-001` (profundidade) · `ART-COC-001` (profundidade) | direta |
| `FOR-MRG-006` MC por vendedor — Nível 3 | `ART-PER-001` (profundidade) | direta |
| `FOR-MRG-007` MC percentual do vendedor | `ART-PER-001` (profundidade) | direta |
| `FOR-MRG-008` MC por categoria por vendedor (a matriz) | `ART-PER-001` (profundidade) | direta |
| `FOR-MRG-009` MC por transação do vendedor | `ART-PER-001` (profundidade) | direta |
| `FOR-MRG-010` MC por gestor (equipe) — Nível 4 | `ART-PER-001` (profundidade) | direta |
| `FOR-MRG-011` MC percentual do gestor | `ART-PER-001` (profundidade) | direta |
| `FOR-MRG-012` Dispersão de margem na equipe | `ART-PER-001` (profundidade) | direta |
| `FOR-MRG-013` MC por loja — Nível 5 | `ART-LAU-001` (superfície) · `ART-COC-001` (profundidade) | direta |
| `FOR-MRG-014` MC percentual da loja | `ART-LAU-001` (profundidade) · `ART-COC-001` (profundidade) | direta |
| `FOR-MRG-020` Alerta de Margem Negativa | `ART-LAU-001` (superfície) · `ART-FIL-002` (superfície) | direta |
| `FOR-MRG-021` Erosão de Margem por Desconto (EMD) | `ART-LAU-001` (profundidade) · `ART-PER-001` (profundidade) · `ART-FIL-002` (superfície) | direta |
| `FOR-MRG-022` Ranking de Destruição de Margem (RDM) | `ART-PER-001` (profundidade) | direta |
| `FOR-SEV-001` Normalização universal de índice | `ART-PER-001` (profundidade) | direta |
| `FOR-SEV-002` Índice de Captura — taxa crua | `ART-PER-001` (profundidade) | direta |
| `FOR-SEV-003` Índice de Captura (IC) — normalizado | `ART-PER-001` (superfície) | direta |
| `FOR-SEV-004` Attach do vendedor — taxa crua | `ART-PER-001` (profundidade) | direta |
| `FOR-SEV-005` Attach-alvo (P75 por segmento) | `ART-PER-001` (profundidade) | direta |
| `FOR-SEV-006` Índice de Anexação (IA) — normalizado | `ART-PER-001` (superfície) | direta |
| `FOR-SEV-007` Índice de Ticket (IT) | `ART-PER-001` (superfície) | direta |
| `FOR-SEV-008` Conversão de fila — taxa crua | `ART-PER-001` (profundidade) | direta |
| `FOR-SEV-009` Conversão-alvo por temperatura de fila | `ART-PER-001` (profundidade) | direta |
| `FOR-SEV-010` Índice de Resgate (IR) — normalizado | `ART-PER-001` (superfície) | direta |
| `FOR-SEV-011` Índice de Adesão (IAd) — normalizado | `ART-PER-001` (superfície) | direta |
| `FOR-SEV-012` Score de Engenharia de Venda (SEV) | `ART-PER-001` (superfície) | direta |
| `FOR-TMI-001` TMI histórico do segmento | `ART-PER-001` (profundidade) | direta |
| `FOR-TMI-002` TMI histórico do vendedor (ponderado pel | `ART-PER-001` (profundidade) | direta |
| `FOR-TMI-003` TMI de planejamento | `ART-PER-001` (profundidade) | direta |
| `FOR-TMI-004` TMI operacional — a ponte (a régua do ve | `ART-PER-001` (profundidade) | direta |
| `FOR-TMI-005` Gap do TMI (o achado) | `ART-PER-001` (profundidade) | direta |
| `FOR-TMI-006` Ticket Médio Real | `ART-LAU-001` (profundidade) · `ART-COC-001` (profundidade) · `ART-PER-001` (profundidade) · `ART-FIL-001` (profundidade) | direta |
| `PAR-SEV-001` Régua de Pesos por Maturidade — vetor p1 | `ART-PER-001` (profundidade) | direta |

## Fórmulas sem artefato declarado — 36

Existem, têm domínio, e nenhum artefato as consome. Não é defeito da fórmula —
é ausência do entregável que a mostraria.

| Domínio | Qtd | Fórmulas |
|---|---:|---|
| **COMERCIAL** | 16 | `FOR-FCT-001` · `FOR-MET-001` · `FOR-MET-002` · `FOR-MET-003` · `FOR-MET-004` · `FOR-MET-005` · `FOR-MET-006` · `FOR-MET-007` · `FOR-MET-008` · `FOR-MET-009` · `FOR-MET-010` · `FOR-MET-011` · `FOR-MET-012` · `FOR-MET-013` · `FOR-MET-014` · `PAR-MET-001` |
| **FINANCEIRO** | 10 | `FOR-FIN-001` · `FOR-FIN-002` · `FOR-FIN-003` · `FOR-MRG-015` · `FOR-MRG-016` · `FOR-MRG-017` · `FOR-MRG-018` · `FOR-MRG-019` · `FOR-MRG-023` · `FOR-MRG-024` |
| **CREDITO** | 5 | `FOR-FIN-005` · `FOR-FIN-006` · `FOR-FIN-007` · `FOR-FIN-008` · `FOR-FIN-009` |
| **SUPRIMENTOS** | 4 | `FOR-CNC-001` · `FOR-CNC-002` · `FOR-CNC-003` · `FOR-CNC-004` |
| **ESTOQUE** | 1 | `FOR-FCT-002` |

## Fórmulas que alimentam por dependência — 0

Não aparecem em tela, mas são consumidas por quem aparece. São intermediárias legítimas.


