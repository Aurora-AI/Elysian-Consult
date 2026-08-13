# ESQUEMA DA PEÇA — o contrato de extração do conhecimento Aurora

> **Status:** PROPOSTA v1.0 — 13/08/2026
> **Derivado de:** `AuroraControler/CATALOGO_METODOS_VENDAS_v0.1.md` §1 (princípios P1–P8) e o esquema do pedaço (12 campos), **generalizado** de "métodos de venda" para todo o conhecimento do acervo
> **Governa:** a Fase 2 (extração) e tudo que vier depois

---

## 0. Os três princípios que geram o resto

**P1 · A unidade é a peça, não o documento.**
Herdado direto do Catálogo. O trabalho não é organizar arquivos — é extrair peças de conhecimento de dentro deles. Um `.docx` pode conter 14 peças de 5 tipos diferentes; um `.pptx` inteiro pode conter uma.

**P2 · O registro é dado; o documento é renderização.**
Cada peça vira um registro estruturado. O `Elysian_SSOT.md`, o manual do método, o dicionário de dados e o gabarito passam a ser **gerados** a partir do registro — nunca escritos à mão. É o §0 da `SPEC_Fase_D2` aplicado à documentação: *dois lugares produzindo verdade é o bug arquitetural que esta casa não comete.* Hoje a documentação comete — três arquivos com três vetores de peso são o sintoma.

**P3 · Extração é fiel; correção é decisão do autor.**
Quem extrai **não conserta**. Extrai como está, sinaliza o problema como lacuna, e a correção entra por decisão registrada. Extrator que melhora em silêncio transforma o registro na opinião dele e mata a procedência.

---

## 1. Os nove tipos de peça

| Prefixo | Tipo | O que é | Teste de pertencimento |
|---|---|---|---|
| `AXI` | **Axioma** | Tese fundadora, crença que sustenta o método | "Se isto fosse falso, o que ruiria?" |
| `MEC` | **Mecanismo** | Movimento tático nomeado (o "pedaço") | "Alguém executa isto numa reunião ou numa loja?" |
| `FOR` | **Fórmula** | Expressão calculável | "Uma máquina calcula isto a partir de dados?" |
| `REG` | **Regra / Trava** | Condição → ação obrigatória | "Existe um SE que dispara um DEVE?" |
| `APA` | **Anti-padrão** | O que reprova | "Isto é uma proibição com sintoma observável?" |
| `GAT` | **Gate** | Condição de avanço de fase | "Isto bloqueia a próxima etapa?" |
| `ART` | **Artefato** | Entregável (laudo, fila, playbook, painel) | "Isto é entregue a alguém?" |
| `EVI` | **Evidência** | Fato observado em dado real, com número e fonte | "Isto aconteceu, num arquivo, numa data?" |
| `LAC` | **Lacuna** | Pendência declarada, tensão não resolvida | "Isto está em aberto e alguém precisa decidir?" |

**Regra de desambiguação:** na dúvida entre `AXI` e `MEC`, pergunte se é executável. Entre `FOR` e `REG`, se produz **número** é fórmula, se produz **decisão binária** é regra. Uma peça nunca tem dois tipos — se parecer ter, são duas peças ligadas por `ver_tambem`.

---

## 2. Campos comuns — obrigatórios em toda peça

```yaml
id: FOR-SEV-003              # <TIPO>-<BLOCO>-<NNN>, imutável
tipo: FOR
nome: "Índice de Ticket (IT)"
bloco: SEV                   # agrupador temático
resumo: "..."                # uma frase, sem jargão

procedencia:                 # [OBRIGATÓRIO] no mínimo uma
  - arquivo: "ElysianConsult/docs/Atuais/Oticas_ParteF_Score_Formula.docx"
    sha: "a3f9c21b0e44"
    local: "§1.1"
    data_doc: 2026-07-08

status_canonico: CANONICO    # ver §3
confianca: ALTA              # ALTA | MEDIA | BAIXA — quão literal foi a extração
natureza_conhecimento: EMPIRICO_AUTOR   # ver §4

extraido_em: 2026-08-13
extrator: "..."
ver_tambem: [FOR-TMI-005, REG-SEV-002]
lacunas: [LAC-FOR-011]       # problemas detectados, NUNCA corrigidos aqui
```

Peça sem `procedencia` não entra no registro. Peça sem `sha` do arquivo de origem não é auditável.

---

## 3. Estados de canonicidade

| Estado | Significado | Uso permitido |
|---|---|---|
| `CANONICO` | É a verdade vigente | Livre |
| `CANDIDATO` | Existe, é coerente, mas não foi ratificado | Uso interno, marcado |
| `SUPERADO` | Foi substituído; preservado por histórico | Só no Vault, nunca em código |
| `CONFLITANTE` | Duas versões vivas; **na fila de decisão** | 🔴 Bloqueia implementação |
| `NAO_UTILIZADO` | Existe no acervo, nunca foi aplicado | Nunca como doutrina |
| `IMPORTADO` | Literatura externa, não é ativo proprietário | Sempre com a fonte |

> Exemplo real: o deck `Método Aurora — Estratégia e Fosso Competitivo` é `NAO_UTILIZADO` por ruling do autor (13/08). Suas peças entram no registro como intel competitiva, e o "+20% de faturamento" **nunca** pode ser citado como método.

---

## 4. Natureza do conhecimento

Herdado do Catálogo de Métodos §0, e é o campo que protege o ativo:

- `LITERATURA_PUBLICA` — commodity, replicável (SPIN, MEDDIC, GMROI, RFM)
- `DERIVADO_DE_DADO` — nasce do dado do cliente (P75, ciclo mediano, TMIhv)
- `EMPIRICO_AUTOR` — conhecimento de campo do Rodrigo, **o produto**
- `IMPORTADO_EXTERNO` — pesquisa de terceiros (bow-tie, NRR, win rate 19%)

Misturar isso é como o acervo perdeu a fronteira entre o que é vantagem e o que é manual de mercado.

---

## 5. Campos por tipo

### 5.1. `FOR` · Fórmula — o tipo mais exigente

```yaml
simbolo: IT
expressao: "IT = mín( TMR ÷ TMIo ; 1 ) × 100"
variaveis:
  - simbolo: TMR
    nome: "Ticket Médio Real do vendedor"
    unidade: BRL
    origem: fato_venda
    natureza: CRUA
  - simbolo: TMIo
    nome: "Ticket Médio Ideal operacional"
    unidade: BRL
    origem: FOR-TMI-004
    natureza: DERIVADA

grao: vendedor               # item | venda | vendedor | equipe | loja | rede | sku | cliente | mes
janela: mensal               # tempo real | diaria | semanal | mensal | trimestral | acumulado
natureza: NORMALIZADA        # CRUA | NORMALIZADA | DERIVADA  ← [CRÍTICO]
alvo: FOR-TMI-004
teto: 100
piso: 0

# Mapa de Aplicação (Playbook v9, Parte H) — obrigatório
onde: "Painel de performance, Fase 3+"
quando: "Mensal, recalibra trimestral"
quem: "Máquina"
entra: "Vendas do vendedor por segmento"
sai: "Parcela do SEV"

casos_degenerados:           # [OBRIGATÓRIO — mínimo um]
  - condicao: "TMIo = 0"
    comportamento: "[LACUNA] não definido na fonte"
  - condicao: "vendedor com < N vendas no período"
    comportamento: "[LACUNA] não definido na fonte"

implementado_em: "src/product_b/oracle/commercial_auditor.py"   # ou null
verificado_contra: "Consultoria.xlsx › Gabarito linha 14"        # ou null
```

**Os três campos que existem por causa de bugs reais:**

- **`natureza`** — o `PV = AG × (IR÷100) × TMR` usa `IR` como taxa de conversão, mas a Blindagem redefiniu `IR` como índice normalizado contra alvo. Duas variáveis, um nome. Declarar a natureza torna a colisão visível na extração, não em produção.
- **`grao` + `janela`** — o `TMIo` mistura `TMIhv` (vendedor) com `TMIp` (loja). Sem grão declarado, a mistura é invisível.
- **`casos_degenerados`** — `EDN = (M−V)÷(DU_t−DU_e)` divide por zero no último dia útil de todo mês. Campo obrigatório força o extrator a perguntar.

### 5.2. `REG` · Regra / Trava

```yaml
gatilho: "completude(telefone ∪ CPF) < 30%"
acao: "Pivotar o diagnóstico 100% para estoque (B4/B5)"
obrigatoriedade: INEGOCIAVEL     # INEGOCIAVEL | PADRAO | SUGERIDA
quem_executa: "Consultor"
o_que_reprova: "Diagnóstico de base entregue sobre cadastro inutilizável"
```

### 5.3. `MEC` · Mecanismo

```yaml
funcao: "Roteamento de lead por potencial, não por valor atual"
fase: "2 — Blindagem do Portão (D8–D15)"
pre_condicao: "Triagem ativa em 100% dos leads"
executor: "Máquina tria · Gestor desenvolve · Vendedor conduz consultiva"
anti_padroes: [APA-POR-001, APA-POR-002]
gate: GAT-02
validado_em: "Caso AçoForte Sul"
```

### 5.4. `AXI` · Axioma

```yaml
enunciado: "Mudar o sistema é fácil; mudar o hábito do vendedor requer respeito e a prova de que o cadastro é a sua carteira de comissões futura."
sustentacao: [EVI-CUL-003]
o_que_falsificaria: "Loja que adota cadastro sem incentivo imediato e sustenta o hábito por 6 meses"
```

O campo `o_que_falsificaria` não é filosofia: é o que separa axioma operante de slogan. Axioma que nada falsifica é `CANDIDATO`, não `CANONICO`.

### 5.4-bis. `ART` · Artefato — o contrato entre a teoria e a tela

Criado por `DEC-009`. É a peça que liga fórmula a entregável — sem ela, o dashboard volta a
ser desenhado à mão e a teoria diverge da tela.

**Os dois princípios que governam todo `ART`:**

> **Superfície mínima, profundidade total.**
> A complexidade não é eliminada, é **latente**. Nada sai do sistema; tudo sai da entrega ativa.
>
> **O drill-down é diagnóstico, não navegação.**
> Erro mínimo explica problema complexo — o `ARP-013` (erro de cadastro num SKU) explicou o
> "vendedor que corrói 337% de margem". Sem descer até a NF, o laudo acusa a pessoa errada.

```yaml
id: ART-COC-001
tipo: ART
nome: "Cockpit do dono"
consumidor: dono              # dono | gestor | vendedor | consultor | cliente_final
gatilho: "abre quando quer saber como a rede está"
cadencia: semanal

# ─── SUPERFÍCIE: o que aparece SEM pedido ───
superficie:
  teto_elementos: 7           # [OBRIGATÓRIO] limite duro. Estourou, não é superfície.
  numero_ancora: FOR-BAS-003  # o UM número que justifica abrir
  elementos: [FOR-BAS-003, FOR-BAS-004, ...]
  o_que_NAO_aparece:          # [OBRIGATÓRIO] tão importante quanto o que aparece
    - "nome de vendedor (REG-SEV-004)"
    - "qualquer métrica que não vire R$ ou decisão"

# ─── PROFUNDIDADE: o que existe SOB DEMANDA ───
profundidade:
  eixo_vertical:              # desagregar por grão — termina SEMPRE em source_rows
    - rede
    - loja
    - equipe
    - vendedor
    - venda
    - item
    - linha_de_origem         # [OBRIGATÓRIO] o piso. SPEC_Fase_D2 Pilar 2.
  eixo_horizontal:            # fatiar por outra dimensão NO MESMO grão
    - {grao: vendedor, dimensoes: [categoria, segmento, temperatura_fila, periodo]}
    - {grao: loja, dimensoes: [categoria, natureza_item, forma_pagamento, periodo]}
  completude: TOTAL           # TOTAL | PARCIAL — se PARCIAL, declarar onde corta e por quê

lei_de_linguagem: LAUDO       # LAUDO (R$ e consequência) | TECNICA (símbolo e taxa)
modo_minimo: a                # a | b | c — governança de exibição (REG-SEV-004)
regras_aplicaveis: [REG-SEV-004, REG-NUM-001]
```

**Os quatro campos que existem por causa de uma decisão, não de gosto:**

- **`teto_elementos`** — sem limite duro, toda superfície vira o CHRONOS de novo. O teto é a
  trava; a profundidade é a válvula de escape.
- **`o_que_NAO_aparece`** — declarar a omissão força a decisão. Omissão não declarada é
  esquecimento; declarada é design.
- **`eixo_horizontal`** — a maioria dos painéis só desagrega. Sem o horizontal não se responde
  *"ele vende mal, ou vende mal só multifocal?"* — que é a pergunta que muda a intervenção.
- **`completude: TOTAL`** — o padrão é descer até a linha de origem. `PARCIAL` exige
  justificativa escrita, porque quebra o princípio de que nenhum detalhe é básico demais.

### 5.5. `EVI` · Evidência

```yaml
fato: "SKU ARP-013: NF de entrada R$ 309,11 · tabela única de rede R$ 838,85 · praticado em L9 a R$ 172–248"
fonte_dado: "tests/fixtures/consultoria_real_test.xlsx"
data_observacao: 2026-07-20
o_que_prova: "Preço de tabela único não descreve a prática de nenhuma loja — assinatura de erro cadastral, não de vendedor descontista"
usado_por: [REG-TRI-001, FOR-MRG-009]
```

### 5.6. `LAC` · Lacuna

```yaml
descricao: "Vetor de pesos do estágio Construção diverge entre três documentos"
evidencia:
  - "Oticas_ParteF_Score_Formula.docx: 0,25/0,25/0,20/0,20/0,10"
  - "Formulas_Consultoria_Aurora.md: 0,25/0,25/0,20/0,20/0,10"
  - "Oticas_Playbook_v9_Master.docx: 0,30/0,25/0,20/0,15/0,10"
impacto: "Altera todo SEV calculado"
quem_decide: "Rodrigo"
bloqueia: [FOR-SEV-006]
status: ABERTA
```

`GAT`, `ART` e `APA` seguem o mesmo padrão — campos em `ESQUEMA_PECA.tipos.yaml` quando o registro for criado.

---

## 6. Regra de precedência

Quando duas peças afirmam coisas diferentes sobre o mesmo assunto:

```
1. Código executado e testado, com evidência de gate
2. SPEC com status EXECUTADA
3. Documento Master mais recente
4. Documento satélite
5. Apresentação comercial
6. Pesquisa externa importada
7. Material NAO_UTILIZADO
```

**Empate ou inversão de nível → não decide o extrator.** A peça vai para `CONFLITANTE`, gera uma `LAC` e entra na fila de decisão com as evidências anexadas.

> **Dimensionamento (herdado da `SPEC_Fase_C`):** a fila recebe o resíduo, nunca o atacado. Fila com 200 itens = esquema errado. Fila com 8 itens = governança.

O caso do vetor de pesos é exatamente uma inversão: dois satélites (nível 4) contradizem um Master (nível 3). A regra não resolve — e é correto que não resolva.

---

## 7. Validador — o que roda sem julgamento humano

| # | Checagem | Severidade |
|---|---|---|
| V1 | Sigla com dois significados no registro (`MR`, `PV`) | 🔴 Reprova |
| V2 | `FOR` sem `grao` ou sem `janela` | 🔴 Reprova |
| V3 | `FOR` sem `casos_degenerados` | 🔴 Reprova |
| V4 | Variável usada em `expressao` e ausente de `variaveis` | 🔴 Reprova |
| V5 | `natureza` ausente em variável que aparece em outra fórmula | 🔴 Reprova |
| V6 | `procedencia` ausente ou `sha` inexistente no inventário | 🔴 Reprova |
| V7 | Referência em `ver_tambem` apontando para `id` inexistente | 🔴 Reprova |
| V8 | Mesmo número com valores diferentes em duas peças | 🟡 Fila |
| V9 | Peça `CONFLITANTE` sem `LAC` associada | 🟡 Fila |
| V10 | `AXI` sem `o_que_falsificaria` | 🟡 Rebaixa a `CANDIDATO` |
| V11 | `FOR` sem `implementado_em` **e** sem `verificado_contra` | 🟡 Marca `HIPOTESE` |
| V12 | `FOR` com expressão em prosa, não simbólica | 🟡 Fila — não implementável sem tradução |

Os oito problemas encontrados na leitura do `Formulas_Consultoria_Aurora.md` — colisão de `MR` e `PV`, `EDN` dividindo por zero, bandas do SEV com fronteira ambígua, `PV` usando índice normalizado como probabilidade, `ER` indefinido nos três primeiros meses — **todos caem em V1–V5**. Nenhum exigiu inteligência. Exigiu contrato.

---

## 8. Layout do registro

```
ElysianConsult/docs/CATALOGO/
├── INVENTARIO.md            # Fase 0 — o mapa do acervo
├── INVENTARIO.csv           # 141 arquivos com hash e legibilidade
├── ESQUEMA_PECA.md          # este documento — o contrato
├── registro/
│   ├── formulas.yaml        # Fase 2 — bloco FOR
│   ├── regras.yaml
│   ├── mecanismos.yaml
│   ├── axiomas.yaml
│   ├── evidencias.yaml
│   └── lacunas.yaml
├── FILA_DECISAO.md          # o resíduo que só o autor resolve
├── validar.py               # V1–V11
└── render/                  # gerados — nunca editados à mão
    ├── SSOT.md
    ├── DICIONARIO_DADOS.md
    └── MANUAL_METODO.md
```

**`render/` é build.** Editar arquivo em `render/` é o mesmo erro que recalcular na camada de apresentação.

---

## 9. Critério de pronto

Não é "ficou bem escrito". É o critério que o próprio `Oticas_Mapa_Aplicacao_Formulas` já declara:

> *"Um consultor novo — ou um agente de IA — sabe aplicar cada fórmula sem o contexto desta conversa."*

Com um corolário duro: **fórmula documentada que não foi codificada e conferida contra o gabarito ainda é hipótese.** O campo `verificado_contra` existe para isso, e o `Gabarito` do `Consultoria.xlsx` (37 anomalias com resultado esperado) é a régua.

Uma peça está pronta quando: passa em V1–V11 · tem procedência com hash · tem caso degenerado · e, se for `FOR`, aponta para implementação ou para gabarito.

---

## 10. Protocolo de extração — dois passes

**Passe 1 · Fiel.** Transcrever a peça como está. Símbolos, pesos e limiares exatamente como no documento de origem. Divergência entre fontes → duas peças, ambas `CONFLITANTE`, nunca uma média.

**Passe 2 · Diagnóstico.** Rodar o validador. Todo achado vira `LAC` com evidência. **Zero correção.**

**Passe 3 · Decisão (autor).** Rodrigo resolve a fila. Cada decisão vira entrada no Vault com data e razão. Só então a peça muda de `CONFLITANTE` para `CANONICO`.

Passe 3 nunca é executado pelo extrator. Essa é a trava.

---

*Fim do esquema v1.0. Próximo: extração do bloco `FOR` sobre os 11 arquivos-alvo listados no `INVENTARIO.md` §4.*
