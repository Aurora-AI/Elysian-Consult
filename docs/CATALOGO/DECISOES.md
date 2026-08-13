# DECISÕES — log append-only do Passe 3

> **Regra:** só o autor decide. Cada entrada registra a decisão, a razão, o que ela mata e o
> que ela destrava. **Nada é apagado** — peças superadas mudam de `status_canonico`, não somem.
> **Contrato:** `ESQUEMA_PECA.md` §10, Passe 3.

---

## DEC-001 · Neutralidade da recomendação financeira

**Data:** 2026-08-13 · **Decisor:** Rodrigo · **Fecha:** `LAC-FOR-054` · **Fila:** D-15

### A decisão

> *"Quando eu recomendo um parceiro para financiar as vendas do cliente, eu não recebo
> compensação financeira. Entra no pacote da consultoria."*

### Por que era um conflito

O acervo tinha dois modelos incompatíveis, escritos com um dia de diferença:

| | `Playbook_Operacional_Detalhado` (07/07) | `Camada_Financeira_C2` (08/07) |
|---|---|---|
| Risco de default | ótica provisiona ≈8,5% | parceiro assume 100% |
| Receita financeira | da ótica (MDR/juros) | da Aurora, paga pelo parceiro |

A decisão **não escolheu nenhum dos dois**. Manteve o risco zero do C2 e eliminou a
monetização — que era a parte do C2 que exigia toda a arquitetura de "transparência radical"
para não parecer conflito de interesse.

### O que muda no registro

| Peça | De | Para | Motivo |
|---|---|---|---|
| `FOR-FIN-007` · Provisão de inadimplência na ótica | `CONFLITANTE` | **`SUPERADO`** | A ótica não carrega risco — não há o que provisionar |
| `FOR-FIN-008` · Inadimplência monitorada no parceiro | `CONFLITANTE` | **`CANONICO`** | Modelo de risco zero confirmado |
| `FOR-FIN-009` · Receita financeira | `CONFLITANTE` | **`SUPERADO`** | Nem a Aurora nem a fórmula têm mais objeto |
| `REG-FIN-001` · Neutralidade da recomendação | — | **novo, `CANONICO`** | A decisão vira trava executável |

### O que isso destrava — e fortalece

**Some o conflito de interesse.** O C2 §2 dedicava três parágrafos a defender a neutralidade
("painel e não bandeira única", "transparência radical", "dever de arquiteto"). Todo esse
andaime existia para sustentar uma remuneração que agora não existe. A neutralidade deixa de
ser argumentada e passa a ser **estrutural**.

**Fecha com o posicionamento.** *"Não cobrar pedágio sobre a receita bruta"* e *"taxa fixa,
não percentual"* — a recomendação financeira sem comissão é a mesma tese aplicada à camada C2.

**A condição do dado de volta sobrevive.** O C2 §3 torna o retorno do dado da transação
condição inegociável de seleção do parceiro, e declara que *"o volume que a Aurora leva é a
alavanca para exigi-lo"*. A alavanca sempre foi o **volume**, nunca a comissão — então a
exigência permanece intacta.

### Ponto residual

Resolvido no mesmo dia pela `DEC-002`.

---

## DEC-002 · A remuneração financeira segue o risco

**Data:** 2026-08-13 · **Decisor:** Rodrigo · **Fecha:** `LAC-FIN-078`

### A decisão

> *"Isto vai do fornecedor, mas não é praxe de mercado. O contratante não recebe parte do MDR
> porque não tem participação no risco."*

A ótica **não** tem receita financeira própria na operação de crédito. Pode variar por
fornecedor, mas não é o padrão de mercado e não é o modelo Aurora.

### O princípio que ela explicita

A `DEC-001` e a `DEC-002` são a **mesma regra aplicada a duas partes diferentes**. Juntas,
formam um princípio único que o acervo aplicava por intuição e nunca escreveu:

> **A remuneração financeira segue o risco.**
>
> | Parte | Carrega risco? | Recebe? |
> |---|---|---|
> | Aurora | não | **não** — a recomendação está no pacote da consultoria |
> | Ótica | não | **não** — não participa do MDR |
> | Parceiro | **100% do default** | **sim** — fica com a receita financeira |

Antes disso a doutrina tinha duas exceções mal justificadas — a Aurora recebendo comissão sem
risco (C2 §2) e a ótica com receita financeira própria (Detalhado, Parte A · C2). As duas
caem pelo mesmo motivo, e o motivo agora está escrito.

### O que muda no registro

| Peça | Efeito |
|---|---|
| `FOR-FIN-009` · Receita financeira | **removida do escopo** — não precisa ser reescrita, some. Permanece `SUPERADO` por histórico |
| `REG-FIN-001` | ganha o princípio "a remuneração segue o risco" como fundamento |
| `LAC-FIN-078` | `RESOLVIDA` |

### ⚠️ Correção de escopo — ver DEC-003

O princípio *"a remuneração segue o risco"* foi generalizado demais no registro original desta
decisão. Ele vale para **intermediação de crédito**, não para toda parceria. Corrigido pela
`DEC-003`. A `DEC-002` em si (a ótica não participa do MDR) permanece válida.

### Pendência aberta pela DEC-001 (não pela DEC-002)

Com a `DEC-001`, deixa de existir contrato entre Aurora e parceiro (indicador/seller) — e era
nesse contrato que a **cláusula de retorno do dado da transação** (C2 §3, condição inegociável
de seleção) moraria naturalmente.

A alavanca continua sendo o **volume** que a Aurora leva, não a comissão, então a exigência
permanece legítima. Mas o **instrumento** sumiu. A cláusula precisa migrar para:

- (a) o contrato do **cliente** com o parceiro, com a Aurora redigindo a cláusula; ou
- (b) **critério de curadoria** do painel — a Aurora simplesmente não indica quem não devolve o dado.

Registrado como `LAC-FIN-079`, severidade MÉDIA. Não bloqueia fórmula nenhuma; bloqueia a
operacionalização do C2 §3.

---

## DEC-003 · Dois tipos de parceiro, duas economias

**Data:** 2026-08-13 · **Decisor:** Rodrigo · **Abre:** `LAC-CNC-080` · **Corrige:** escopo da `DEC-002`

### O erro que ela corrige

O registro tratava "parceiro" como categoria única. São **dois**, com economias opostas — e o
extrator confundiu os dois ao aplicar a `REG-FIN-001` sobre ambos.

| | **Parceiro financeiro** (Cooper Card, emissores, BaaS) | **Fornecedor ótico** (concentradora) |
|---|---|---|
| Objeto | crédito ao consumidor final | compra de produto pela ótica |
| O que se negocia | **não** se negocia MDR | preço, tier, acesso a marca |
| Como o mercado remunera o indicador | cartões aprovados, tarifa de anuidade, seguros | rebate/spread por volume |
| Quem carrega risco | o parceiro, 100% | ninguém (drop-ship, zero estoque) |
| **A Aurora recebe?** | **não** (`DEC-001`) — [ver ressalva aberta] | **sim, das duas partes** |

### A decisão sobre a concentradora

> *"Neste cenário nós queremos uma compensação financeira das partes: do meu cliente, que vai
> comprar muito mais barato ou vai ter acesso a marcas que ele não conseguiria, e do fornecedor,
> pelo volume de vendas que eu vou trazer para eles."*

**Remuneração bilateral, explícita:**

- **do cliente** — pelo valor entregue: preço menor e acesso a marcas fora do alcance dele sozinho
- **do fornecedor** — pelo volume de vendas que a Aurora agrega

### Por que o princípio da DEC-002 não se aplica aqui

Na concentradora a Aurora não carrega risco (o modelo recomendado é agregação com drop-ship —
zero estoque, zero capital de giro) e **ainda assim** é remunerada. Isso não contradiz nada:
são bases diferentes.

> **Crédito:** a remuneração segue o **risco**. Receita financeira é o preço de carregar default.
> **Compra:** a remuneração segue o **valor entregue**. Acesso, preço e a inteligência de
> sell-in × sell-through — que é o que separa a central inteligente da central commodity.

O princípio da `DEC-002` fica restrito à camada financeira. `REG-FIN-001` estreitada,
`REG-CNC-001` criada.

### Nota de extração

O `Oticas_Concentradora_Compras.docx` §3 **já documentava** as linhas de receita — rebate/spread
de volume, marca própria, financiamento do pedido via C2, fee de adesão opcional. O passe 2
extraiu as métricas (`FOR-CNC-001` a `004`) e não extraiu o modelo de receita. Corrigido aqui.

### Consequência que precisa de atenção

O mesmo documento recomenda *"rebate transparente (a ótica vê preço de fábrica + fee) — preserva
a confiança, **igual à C2**"*. Esse paralelo **quebrou**: a C2 deixou de ter monetização
(`DEC-001`) e a concentradora manteve. A transparência do rebate agora se sustenta sozinha,
não por analogia. Registrado em `LAC-CNC-080`.

---

## DEC-004 · A DEC-001 é absoluta · e crédito remunera por originação, não por transação

**Data:** 2026-08-13 · **Decisor:** Rodrigo · **Fecha:** `LAC-FIN-081` · **Ratifica:** `DEC-001`

### Resposta à ressalva da Cooper Card

**Leitura (a) — descritiva.** É assim que o mercado remunera indicador; a Aurora *poderia*
receber e **não recebe**. A `DEC-001` fica **absoluta** e a neutralidade permanece estrutural.

### O fato de mercado que veio junto — e é mais importante

> *"Falando especificamente em cartões, sim, é a regra do mercado. Mas em geral, no mercado
> financeiro você não ganha pelo volume transacionado, e sim pela venda do produto: não ganho
> pelo R$ transacionado, mas pela venda do cartão, do crediário, etc."*

**A base de remuneração no crédito é ORIGINAÇÃO, não TRANSAÇÃO.**

Isso reclassifica o erro do C2 §2. A "Rota 1 — share de MDR" não era apenas eticamente
desconfortável: era **factualmente errada sobre o mercado**. MDR é transacional, e o mercado
financeiro não paga indicador por transação — paga por produto vendido (cartão aprovado,
crediário aberto, seguro contratado, tarifa de anuidade).

### O eixo que isso revela — refina a DEC-003

A `DEC-003` separou os dois parceiros pela presença de risco. O eixo real é **a base de
remuneração**:

| Camada | Base | Unidade | Métrica correspondente |
|---|---|---|---|
| **Crédito** | **originação** | produto financeiro vendido | `FOR-FIN-006` · taxa de aprovação |
| **Compra** | **volume** | R$ ou unidades transacionadas | `FOR-CNC-002` · volume agregado |

### Achado colateral

A `FOR-FIN-006` — *aprovação = limites aprovados ÷ propostas enviadas* — **já é uma métrica de
originação**. Conta aprovações, não reais. A camada de métricas estava alinhada ao mercado
desde a extração; era o documento de monetização (C2 §2) que estava fora de eixo.

Isso é uma evidência a favor do método: a métrica derivada do que a operação realmente faz
sobreviveu à revisão do modelo de negócio que a acompanhava.

### O que muda no registro

| Peça | Efeito |
|---|---|
| `DEC-001` | **ratificada como absoluta** |
| `REG-FIN-001` | `base_de_remuneracao: ORIGINACAO` corrigido e generalizado |
| `REG-CNC-001` | `base_de_remuneracao: VOLUME` explicitado |
| `LAC-FIN-081` | `RESOLVIDA` |

---
## ~~❓ EM ABERTO · A ressalva da Cooper Card~~ ✅ RESOLVIDA pela DEC-004

**Levantada em:** 2026-08-13 · **Bloqueia:** confirmação da `DEC-001`

> *"o que eu posso ver é com a Cooper Card uma compensação financeira sobre as indicações"*

Duas leituras possíveis, com efeitos opostos sobre a `DEC-001`:

**(a) Descritivo** — é assim que o mercado financeiro remunera indicadores (cartões aprovados,
anuidade, seguros). A Aurora *poderia* receber, mas não recebe. `DEC-001` fica **absoluta**.

**(b) Exceção** — com a Cooper Card especificamente, a Aurora recebe por indicação. `DEC-001`
ganha ressalva, e volta a valer a questão de conflito de interesse que ela tinha eliminado —
com o agravante de que aí a neutralidade volta a ser **argumentada**, não estrutural.

Registrado como `LAC-FIN-081`, severidade ALTA. Até a resposta, a `DEC-001` permanece como
está e a `FOR-FIN-009` segue `SUPERADO`.

---

## DEC-005 · A concentradora é canal de aquisição · e existe uma terceira frente: a franqueadora

**Data:** 2026-08-13 · **Decisor:** Rodrigo · **Corrige:** `REG-CNC-001` · **Abre:** bloco FRQ

### 1. A concentradora tem duas funções, e a primeira não é receita

> *"A concentradora, inicialmente, é a maior ferramenta de captação de clientes para a consultoria."*

Isso **reposiciona** a frente. O `Oticas_Concentradora_Compras.docx` a trata como negócio
próprio, com moat próprio (cruzar sell-in × sell-through). A decisão a coloca antes disso:
é o **canal de aquisição** da consultoria. A economia dela deve ser lida como **CAC**, não
só como margem.

Consequência de medição: faltam duas métricas que nenhum documento tem —
**taxa de conversão concentradora → consultoria** e **CAC por cliente adquirido pela frente**.
Registrado em `LAC-CNC-083`.

### 2. A remuneração — correção da REG-CNC-001

A `DEC-003` registrou "remuneração bilateral" como fato. **Estava errado.** O correto:

| Origem | Status | Base |
|---|---|---|
| **Cliente (ótica)** | ✅ **REGRA** | **% sobre o valor do produto** |
| **Fábrica / fornecedor** | ⚠️ **POSSIBILIDADE** | não vista hoje; anotada, não adotada |

> *"A princípio não vejo como cobrar uma comissão das fábricas, mas é uma possibilidade — e
> possibilidade é importante ser notada, não é regra."*

`REG-CNC-001` corrigida: a linha do fornecedor passa de `CANONICO` para `CANDIDATO`.
A distinção entre **o que é regra** e **o que é possibilidade anotada** é exatamente o que os
estados de canonicidade do `ESQUEMA_PECA` §3 existem para carregar.

### 3. A escada de três degraus

> *"Dar inicialmente força para os clientes comprarem melhor através da concentradora, depois
> vender melhor com uma marca mais forte, a franquia, e com tudo isso mantemos a consultoria
> para garantir a qualidade da marca e a saúde financeira das lojas."*

| Degrau | Frente | O que entrega | Efeito |
|---|---|---|---|
| 1 | **Concentradora** | comprar melhor | aquisição · prova de valor no dia 1 |
| 2 | **Franqueadora** | vender melhor | marca · ticket · pertencimento |
| 3 | **Consultoria** | operar melhor | qualidade da marca + saúde financeira |

Não são três produtos: é **uma escada de custo de troca crescente**. E a consultoria muda de
papel no degrau 3 — deixa de ser o produto vendido e vira o **mecanismo de controle de
qualidade da franquia**. É o que impede a franquia de virar "fast-food".

### 4. A franqueadora

- Modelo de franquia de **marca ótica**
- **Clientes já na base são isentos da taxa de franquia** e têm vantagens
- A **consultoria está dentro** da franquia — acesso para todos
- É declarada como **o diferencial competitivo** e a fonte de ferramentas de aumento de receita

**Nenhuma linha sobre a franqueadora existe nos 145 arquivos inventariados.** Frente inteira
sem documentação — bloco `FRQ` aberto, `LAC-FRQ-084` a `087`.

### 5. Efeito colateral estratégico da isenção

A isenção converte a base de consultoria em semente da franquia sem custo de aquisição. Isso
torna os **clientes iniciais da consultoria estrategicamente mais valiosos do que a receita
deles indica** — cada um é um ponto de franquia futuro já validado, já operando o método, já
com dado no motor.

Implicação prática: a régua de decisão de "aceitar ou não um cliente de consultoria hoje"
deveria considerar a adequação dele como franqueado amanhã. Hoje não considera.

---

## DEC-006 · A Aurora é parte da transação na compra · e a ordem de execução

**Data:** 2026-08-13 · **Decisor:** Rodrigo · **Corrige:** enquadramento da `DEC-001` e da
`LAC-FRQ-086` · **Governa:** ordem de trabalho

### 1. O eixo real não é "sobre ganho × sobre faturamento" — é quem fatura

> *"O cliente não tem acesso hoje. O faturamento vem da concentradora, não do fornecedor —
> então para o cliente é transparente. Isso é diferente da discussão sobre produtos
> financeiros: não é antiético cobrar por um serviço. O que existe é uma prática de mercado
> de não pagar sobre o MDR."*

A distinção que resolve a `LAC-FRQ-086` é **posicional**, não moral:

| | Papel da Aurora | Faturamento | Natureza do que ela cobra |
|---|---|---|---|
| **Concentradora** | **parte da transação** | a concentradora fatura para a ótica | **preço de um serviço prestado** |
| **Crédito** | **fora da transação** (indica) | o parceiro fatura o consumidor | seria fatia de transação alheia |
| **Royalty de franquia (Berry)** | fora da transação | o franqueado fatura o consumidor | extração sobre faturamento alheio |

Cobrar margem sobre uma venda que **você faz** é vender. Cobrar percentual sobre uma
transação da qual você **não é parte** é pedágio. A forma é parecida; a posição é oposta.

E o cliente **não tinha acesso ao fornecedor**: o ganho é criado pela central, não capturado
de um fluxo que já existia.

### 2. Correção do enquadramento da DEC-001

O registro da `DEC-001` atribuiu a decisão, em parte, a **conflito de interesse**. Segundo o
autor, isso é enquadramento errado do extrator:

> *"Não é antiético cobrar por um serviço. O que existe é uma prática de mercado de não pagar
> sobre o MDR."*

A `DEC-001` continua válida, mas a **razão** muda: a recomendação de parceiro financeiro entra
no pacote da consultoria por **decisão de empacotamento comercial** — e a não-remuneração sobre
MDR é **prática de mercado**, não imperativo ético. `REG-FIN-001` ajustada.

Isso é mais forte, não mais fraco: uma regra apoiada em prática de mercado e em decisão de
pacote é verificável. Uma apoiada em "seria antiético" é opinião.

### 3. Modelo associativo para a base — anotado, não adotado

> *"Podemos pensar inclusive em um modelo associativo para este cliente, mas isto não é foco agora."*

Registrado como `CANDIDATO` em `LAC-FRQ-088`. Não usar em projeção nem em material comercial.

### 4. A ordem de execução

> *"Primeiro vamos fechar a consultoria, depois a concentradora, depois a franqueadora."*

| Ordem | Frente | Estado do registro |
|---|---|---|
| **1** | **Consultoria** | 99 fórmulas · 18 decisões abertas · blocos Fiscal e Financeiro ausentes |
| 2 | Concentradora | 4 métricas · nenhuma fórmula de receita (`LAC-CNC-082`) |
| 3 | Franqueadora | **vazio** (`LAC-FRQ-084` a `088`) |

**Efeito no trabalho:** as lacunas `FRQ` ficam **estacionadas** — registradas para não se
perderem, fora da fila ativa. A fila de decisão passa a ordenar por frente, não só por
severidade. O foco volta para a `D-08` (Fiscal e Financeiro), que é o que trava a consultoria.

---
