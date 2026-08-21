# LACUNAS ABERTAS — Frente 1 · CONSULTORIA

> ⚙️ **Arquivo gerado** por `gerar_render.py` a partir de `registro/*.yaml`.
> Não editar à mão (`ESQUEMA_PECA.md` P2). Para mudar algo, mude a peça e regenere.

**60 lacunas abertas** · 🔴 11 critica · 🟠 22 alta · 🟡 21 media · ⚪ 6 baixa

---

## Por natureza do trabalho

A severidade diz o quanto dói. A **natureza** diz quanto custa fechar — e são
coisas diferentes. Um grupo de 19 casos degenerados fecha com **uma** política;
um grupo de 7 fórmulas ausentes é semanas de escrita de método.

| Natureza | Qtd | 🔴 | O que fecha |
|---|---:|---:|---|
| **Fórmula que não existe em fonte nenhuma** | 7 | 2 | escrever a fórmula — trabalho de método, não de catalogação |
| **Documento e código implementado divergem** | 5 | 2 | comparar as duas versões e ratificar uma — decisão pontual |
| **Dois documentos afirmam coisas diferentes** | 7 | 2 | escolher qual vale — decisão pontual, evidência já anexada |
| **A fórmula produz número errado como está escrita** | 9 | 4 | corrigir a expressão — a correção candidata já está registrada |
| **O Gabarito exige um comportamento que a fórmula não tem** | 6 |  | a régua de veracidade já diz a resposta — é implementar |
| **Contradiz um princípio declarado da casa** | 3 | 1 | decisão de método — mexe no que diferencia a Aurora |
| **Higiene de símbolo e fronteira** | 12 |  | renomear e declarar — meia hora, fecha reprovas do validador |
| **A fórmula pede um dado que não existe no modelo** | 6 |  | definir a captura — depende do PDV do cliente, não de nós |
| **Pendência de estrutura comercial, não de fórmula** | 2 |  | decisão de negócio |
| **Não classificada** | 3 |  | — |

---

## As 🔴 críticas, em detalhe

### `LAC-FOR-001` · Vetor de pesos do estágio Construção diverge entre três documentos

Duas variantes vivas para o mesmo estágio. A regra de precedência não resolve (dois satélites contra um Master).

**Evidência**

- F1 (Arsenal, autodeclarado fonte única) §1.2: 0,25 / 0,25 / 0,20 / 0,20 / 0,10
- F2 (ParteF Score_Formula) tabela 2: 0,25 / 0,25 / 0,20 / 0,20 / 0,10
- F6 (Playbook v9 Master, mais recente) tabela 5: 0,30 / 0,25 / 0,20 / 0,15 / 0,10
- Estágios Cego e Cruzeiro: as três fontes concordam.

**Impacto:** Muda todo SEV calculado. Bloqueia implementação.

**Bloqueia:** `FOR-SEV-012` · `PAR-SEV-001`

---

### `LAC-FOR-002` · EMD documentado sem a trava de triagem que a implementação exige

A fórmula Σdesconto ÷ receita não tem teto. Em dado real produziu 337,78% (V-30/L9-Serra) porque o preço de tabela da rede não descreve a prática das lojas. A SPEC_Fase_C existe inteira por causa disso. O Arsenal apresenta a fórmula nua.

**Evidência**

- F1 §6.7: EMD_vend = (Σ Desc_vend ÷ R_vend) × 100
- SPEC_Fase_C §1: 'discount_pct de 337,78% na fórmula do Algoritmo 3'
- Evidência ARP-013: NF R$309,11 · tabela R$838,85 · praticado L9 R$172–248

**Impacto:** Quem implementar a partir do Arsenal reconstrói o bug e acusa vendedor por erro de cadastro.

**Correção candidata:** Anexar à peça a trava da Fase C: dois triggers por linha de venda, triagem antes de atribuir a vendedor.

**Bloqueia:** `FOR-MRG-021`

---

### `LAC-FOR-003` · PV usa o IR normalizado como probabilidade de conversão

O forecast PV = AG × (IR÷100) × TMR trata IR como taxa de conversão. Mas a Blindagem (F3 §2) redefiniu IR como índice NORMALIZADO contra alvo P75 por temperatura. São duas variáveis com o mesmo nome.

**Evidência**

- F1 §3.1: PV = AG × (IR ÷ 100) × TMR · legenda: 'IR = Índice de Resgate (%)'
- F1 §1.3 e F3 §2: IR = mín(ConvReal ÷ P75(conv por temperatura) ; 1) × 100
- Aritmética: conversão real 30%, alvo P75 40% → IR = 75 → PV usa 0,75 quando o esperado é 0,30. Forecast 2,5× inflado.
- Degrada com a qualidade: vendedor que bate o alvo tem IR = 100 → PV assume conversão de 100%.

**Impacto:** Todo forecast de vendedor, loja e rede sai superestimado. Piora quanto melhor o vendedor.

**Correção candidata:** PV deve consumir ConvReal (FOR-SEV-008), não IR (FOR-SEV-010).

**Bloqueia:** `FOR-FCT-001`

---

### `LAC-FOR-006` · TMI operacional mistura grão de vendedor com grão de loja

TMIo = TMIhv + α(TMIp − TMIhv). O TMIhv é por vendedor (ponderado pelo mix dele); o TMIp é da loja (MR ÷ NVp). Conforme α sobe, todos convergem para o mesmo destino e a ponderação por mix — que é a tese inteira do bloco — se dissolve.

**Evidência**

- F4 §2: 'Erro 2 — TMI = número único para todos: confunde sorte com habilidade'
- F4 §2 Passo 3: TMIhv = Σ(Mi × TMIhs_i) — grão vendedor
- F4 §3: TMIp = MR ÷ NVp — grão loja
- Em α = 1: TMIo = TMIp para todo vendedor da loja. O Erro 2 volta.

**Impacto:** A régua fica injusta progressivamente ao longo dos trimestres, exatamente quando ninguém lembra mais o porquê.

**Correção candidata:** Preservar a razão de mix no destino: TMIp_vendedor = TMIp_loja × (TMIhv_v ÷ TMIhv_loja).

**Bloqueia:** `FOR-TMI-004` · `FOR-SEV-007`

---

### `LAC-FOR-013` · AGV não tem teto por categoria — é gamificável

AGV = Σ(AR_c × w_c) com AR_c ilimitado. Estourar uma categoria de meta pequena levanta a nota inteira. O SEV tem teto em 100 por índice justamente para bloquear isso.

**Evidência**

- F1 §5.1: AR_c = (V_c ÷ M_c) × 100 · sem teto declarado
- F1 §1.1: 'IT = (TMR ÷ TMI) × 100 (teto em 100)' — o Bloco 1 protege, o Bloco 5 não

**Impacto:** Nota de atingimento manipulável por concentração numa categoria de meta frouxa.

**Correção candidata:** Teto por categoria (ex. mín(AR_c ; 150)), coerente com a blindagem do SEV.

**Bloqueia:** `FOR-MET-013` · `FOR-MET-014`

---

### `LAC-FOR-014` · Pesos w_c do AGV são chutados — contradiz a doutrina da casa

A fonte rotula a tabela como 'Peso Sugerido' com coluna 'Racional'. São seis valores fixados por julgamento, não derivados do dado do cliente.

**Evidência**

- F1 §5.13: LMF 0,25 · LTR 0,20 · LGS 0,20 · OS 0,15 · SRV 0,10 · ACC 0,10
- F6 (nota final): 'Todo número ideal do sistema é derivado do dado do próprio cliente e caminha por um glide path — nunca chutado. É a espinha do método.'

**Impacto:** Viola o princípio que diferencia o método. E não se autoatualiza.

**Correção candidata:** w_c = Part_cat (FOR-MRG-005) — a contribuição real da categoria para pagar o custo fixo. Deriva do dado e se atualiza sozinho.

**Bloqueia:** `PAR-MET-001`

---

### `LAC-FOR-015` · Projeção linear ignora a curva intra-mês e produz falso vermelho todo início de mês

PA_c = (V_c ÷ DU_e) × DU_t assume venda uniforme pelos dias úteis. O varejo brasileiro concentra em quinzena e fim de mês. Nos primeiros 10 dias o PA% sai baixo e o EDN alto para todo mundo — e a CRA pinta a rede de vermelho.

**Evidência**

- F1 §5.2 · extrapolação linear
- F1 §5.10 · CRA depende de PA% e EDN
- Fase 3 do plano de massa de dados tem índice sazonal MENSAL, nenhum intra-mês

**Impacto:** Falso alarme previsível e recorrente. O gestor aprende a ignorar o painel — inclusive quando o vermelho é verdadeiro.

**Correção candidata:** Peso por dia útil derivado do histórico da loja: PA = V ÷ Σpeso(dias transcorridos) × Σpeso(dias totais).

**Bloqueia:** `FOR-MET-002` · `FOR-MET-003` · `FOR-MET-005` · `FOR-MRG-023`

---

### `LAC-FOR-019` · 'Imposto sobre venda' em CV não está definido para o Simples Nacional

MC_item subtrai CV, que inclui 'imposto sobre venda'. Sob o Simples, o DAS incide sobre a receita bruta do mês pela faixa (RBT12), não por item — e não há crédito de ICMS/PIS/COFINS na compra. A regra de alocação por item não existe em nenhum documento.

**Evidência**

- F1 §6.1: CV_item = 'imposto sobre venda, comissão, taxa de cartão/Pix, frete'
- Nenhum arquivo do acervo contém fórmula fiscal (INVENTARIO §4)

**Impacto:** Toda MC, MC%, PE, ICCF e GMROI nascem com base fiscal indefinida.

**Correção candidata:** Escrever o Bloco Fiscal antes de gerar qualquer base. Declarar a alíquota efetiva do mês e o método de alocação.

**Bloqueia:** `FOR-MRG-001` · `FOR-MRG-002` · `FOR-MRG-015` · `FOR-MRG-019`

---

### `LAC-FOR-052` · GMROI tem dois denominadores diferentes — documento × código

O método documentado divide a margem bruta pelo ESTOQUE MÉDIO a custo. O motor implementado divide pelo CAPITAL PRESO (qtd_atual × custo_unit) — o estoque ATUAL. São métricas diferentes com o mesmo nome, e a métrica é declarada "a rainha do estoque".

**Evidência**

- F7/F6 (B2): 'GMROI = Margem bruta (R$) ÷ Estoque médio (a custo)'
- F10 (SPEC_Fase_B, EXECUTADA) Algoritmo 1: '(Receita Total − Custo Total) / Capital Preso' com 'Capital Preso = qtd_atual * custo_unit'
- Nenhuma fonte define como calcular 'estoque médio' (janela? método?)

**Impacto:** Numa loja que girou bem no período mas está com estoque baixo agora, as duas versões dão resultados opostos. O GMROI aparece no Cockpit do dono como KPI.

**Correção candidata:** Pela precedência (§6), o código executado vence. Mas a divergência não é de valor — é de definição. Precisa de decisão, não de desempate.

**Bloqueia:** `FOR-EST-003` · `FOR-AUD-001`

---

### `LAC-FOR-053` · Estoque morto tem três limiares em circulação

O N de 'SKU sem venda há N meses' nunca foi fixado.

**Evidência**

- F7/F6 (B4): '6–9 meses, calibrado pela sazonalidade da moda de armação'
- F11 (Gabarito): DEAD-001..012 marcados com '~250 dias' (≈8,2 meses)
- Deck NAO_UTILIZADO: '180 dias' — não é doutrina, mas circulou em material comercial

**Impacto:** Entre 180 e 270 dias, o mesmo SKU é ou não é estoque morto. Define o número que vai para o Ato 3 do laudo.

**Correção candidata:** Fixar N, ou declarar o método de calibração pela sazonalidade (que a fonte menciona e não descreve).

**Bloqueia:** `FOR-EST-005` · `FOR-EST-006`

---

### `LAC-FOR-061` · A 'conversão esperada' da Receita Latente não tem origem declarada

R_latente = (base sem X) × conversão esperada × ticket de X. É o número que abre o Executive Audit Report e produz o choque do Dia 5. O único fator não derivado do dado é justamente o multiplicador.

**Evidência**

- F6 e F7 (A4): a expressão aparece nos dois, sem definir a origem de 'conversão esperada'
- Contraste: todo outro parâmetro do método (P75, ciclo, TMI) tem derivação declarada

**Impacto:** O número mais persuasivo do laudo depende de um parâmetro chutado.

**Correção candidata:** Derivar da conversão histórica de cross-sell da própria loja, ou do P75 do attach por segmento (que já existe em FOR-SEV-005).

**Bloqueia:** `FOR-BAS-008`

---

## Todas as abertas

### Fórmula que não existe em fonte nenhuma · 7

| | ID | Bloqueia | Lacuna |
|---|---|---:|---|
| 🔴 | `LAC-FOR-019` | 4 | 'Imposto sobre venda' em CV não está definido para o Simples Nacional |
| 🔴 | `LAC-FOR-061` | 1 | A 'conversão esperada' da Receita Latente não tem origem declarada |
| 🟠 | `LAC-FOR-049` | 1 | Blocos Fiscal e Financeiro não existem em nenhum arquivo do acervo |
| 🟡 | `LAC-FOR-025` | 1 | Expressão do TMR nunca foi escrita |
| 🟡 | `LAC-FOR-028` | 1 | VMD 'projetada' sem método de projeção |
| 🟡 | `LAC-FOR-059` | 1 | Índice de recuperabilidade existe no motor e em nenhum documento de método |
| ⚪ | `LAC-FOR-077` |  | Dados sujos que o Gabarito exige tratar não têm fórmula em lugar nenhum |

### Documento e código implementado divergem · 5

| | ID | Bloqueia | Lacuna |
|---|---|---:|---|
| 🔴 | `LAC-FOR-002` | 1 | EMD documentado sem a trava de triagem que a implementação exige |
| 🔴 | `LAC-FOR-052` | 2 | GMROI tem dois denominadores diferentes — documento × código |
| 🟠 | `LAC-FOR-060` | 2 | Attach rate: denominador fixo no documento, parametrizado no código |
| 🟠 | `LAC-FOR-074` | 2 | Flag de corrosão a 2σ existe no código e não no documento |
| 🟡 | `LAC-FOR-039` | 2 | Exclusão de pseudo-entidade existe no motor e não na documentação |

### Dois documentos afirmam coisas diferentes · 7

| | ID | Bloqueia | Lacuna |
|---|---|---:|---|
| 🔴 | `LAC-FOR-001` | 2 | Vetor de pesos do estágio Construção diverge entre três documentos |
| 🔴 | `LAC-FOR-053` | 2 | Estoque morto tem três limiares em circulação |
| 🟠 | `LAC-FOR-017` | 1 | Denominador do IAd divergente entre fontes (VT × VTC) |
| 🟠 | `LAC-FOR-055` | 1 | Completude tem dois limiares sem hierarquia |
| 🟠 | `LAC-FOR-062` | 2 | Taxa de identificação e IC medem o mesmo com denominadores diferentes |
| 🟡 | `LAC-FOR-064` | 1 | 'Attach rate / UPT' é um KPI do Cockpit com duas fórmulas distintas |
| 🟡 | `LAC-FOR-066` | 1 | Curva ABC: ordenar por receita ou por margem? |

### A fórmula produz número errado como está escrita · 9

| | ID | Bloqueia | Lacuna |
|---|---|---:|---|
| 🔴 | `LAC-FOR-003` | 1 | PV usa o IR normalizado como probabilidade de conversão |
| 🔴 | `LAC-FOR-006` | 2 | TMI operacional mistura grão de vendedor com grão de loja |
| 🔴 | `LAC-FOR-013` | 2 | AGV não tem teto por categoria — é gamificável |
| 🔴 | `LAC-FOR-015` | 4 | Projeção linear ignora a curva intra-mês e produz falso vermelho todo início de mês |
| 🟠 | `LAC-FOR-008` | 1 | Σ PV é apresentado como forecast da loja, mas só cobre o canal de resgate |
| 🟠 | `LAC-FOR-041` | 1 | MC da loja soma vendedores, não itens — perde venda sem vendedor |
| 🟠 | `LAC-FOR-047` | 1 | RDM compara o vendedor contra uma média que o contém |
| 🟠 | `LAC-FOR-069` | 1 | Uplift de ticket pelo crédito tem viés de seleção não tratado |
| 🟡 | `LAC-FOR-035` | 1 | CMC sem propósito declarado e com mistura de sinal |

### O Gabarito exige um comportamento que a fórmula não tem · 6

| | ID | Bloqueia | Lacuna |
|---|---|---:|---|
| 🟠 | `LAC-FOR-042` | 3 | MC não decompõe serviço × produto — e o Gabarito exige |
| 🟠 | `LAC-FOR-057` | 1 | Churn não trata sazonalidade — e o Gabarito exige |
| 🟠 | `LAC-FOR-065` | 3 | Serviço não pode entrar nas métricas de estoque — regra não documentada |
| 🟠 | `LAC-FOR-067` | 1 | Estoque morto não trata sazonalidade — e o Gabarito exige |
| 🟡 | `LAC-FOR-024` | 2 | TMR usa média, e o Gabarito exige robustez a outlier |
| 🟡 | `LAC-FOR-046` | 1 | Alerta de margem sem regra de exceção para promoção sinalizada |

### Contradiz um princípio declarado da casa · 3

| | ID | Bloqueia | Lacuna |
|---|---|---:|---|
| 🔴 | `LAC-FOR-014` | 1 | Pesos w_c do AGV são chutados — contradiz a doutrina da casa |
| 🟡 | `LAC-FOR-023` | 1 | Classificação do Gap do TMI não tem critério numérico |
| 🟡 | `LAC-FOR-026` | 1 | Maturação da Camada 2 declarada sem regra de confiança |

### Higiene de símbolo e fronteira · 12

| | ID | Bloqueia | Lacuna |
|---|---|---:|---|
| 🟠 | `LAC-FOR-009` | 1 | Régua de Perfil Ideal não é computável como escrita |
| 🟠 | `LAC-FOR-050` | 1 | Bandas do SEV com fronteira ambígua |
| 🟠 | `LAC-FOR-051` | 3 | CRA não é mutuamente exclusiva nem tem precedência declarada |
| 🟠 | `LAC-FOR-056` | 3 | 'Clientes vitais/fiéis' não tem definição operacional |
| 🟡 | `LAC-FOR-016` | 1 | Banda-alvo do IAd sugerida mas não definida |
| 🟡 | `LAC-FOR-031` | 5 | Unidade de V_c e M_c ambígua (valor ou quantidade?) |
| 🟡 | `LAC-FOR-058` | 1 | 'Ticket médio' da perda por churn não é qualificado |
| 🟡 | `LAC-FOR-071` | 1 | Volume agregado sem unidade declarada |
| 🟡 | `LAC-FOR-076` | 1 | Follow-on sem janela temporal |
| ⚪ | `LAC-FOR-044` |  | Bloco 6 titulado '5 Níveis' mas apresenta 6 |
| ⚪ | `LAC-FOR-072` | 1 | 'Ótica ativa' sem janela de atividade declarada |
| ⚪ | `LAC-FOR-073` | 1 | Efeito da concentração sem janela de comparação |

### A fórmula pede um dado que não existe no modelo · 6

| | ID | Bloqueia | Lacuna |
|---|---|---:|---|
| 🟠 | `LAC-FOR-020` | 3 | Risco de dupla contagem: comissão em CV e folha em CF |
| 🟠 | `LAC-FOR-063` | 2 | Três tabelas de fato citadas por fórmulas do Cockpit não existem |
| 🟡 | `LAC-FOR-040` | 1 | Atribuição de vendedor a gestor ao longo do tempo não declarada |
| 🟡 | `LAC-FOR-048` | 1 | Meta de MC não existe no modelo de dados |
| ⚪ | `LAC-FOR-037` | 1 | CE_item divergente da NF de compra não tem tratamento na fórmula |
| ⚪ | `LAC-FOR-045` | 1 | Overhead corporativo não cabe no modelo de custo fixo proposto |

### Pendência de estrutura comercial, não de fórmula · 2

| | ID | Bloqueia | Lacuna |
|---|---|---:|---|
| 🟡 | `LAC-CNC-080` |  | A transparência do rebate perdeu a analogia que a justificava |
| 🟡 | `LAC-FIN-079` |  | Onde passa a viver a cláusula de retorno do dado da transação? |

### Não classificada · 3

| | ID | Bloqueia | Lacuna |
|---|---|---:|---|
| 🟠 | `LAC-NUM-090` |  | As fórmulas estatísticas nunca foram observadas em regime |
| 🟠 | `LAC-NUM-091` |  | A fila de auditoria foi dimensionada contra fixture pequena — em escala vira backlog |
| 🟡 | `LAC-NUM-089` |  | A Consultoria.xlsx é fixture FUNCIONAL, não volumétrica — não calibra mínimo de amostra |
