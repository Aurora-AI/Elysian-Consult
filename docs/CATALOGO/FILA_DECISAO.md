# FILA DE DECISÃO — o resíduo que só o autor resolve

> **Gerada em:** 13/08/2026 · Passe 2 (diagnóstico) do bloco `FOR`
> **Contrato:** `ESQUEMA_PECA.md` §6 e §10 — o extrator não decide. Nunca.
> **Princípio dimensionador** (herdado da `SPEC_Fase_C`): a fila recebe o resíduo, nunca o
> atacado. **Fila com 200 itens = esquema errado. Fila com 13 itens = governança.**

**Estado (após os dois passes):** 183 peças · 99 fórmulas · 77 lacunas · 7 regras ·
**19 decisões nesta fila** · 6 reprovas e 23 itens de fila no validador, todos rastreados.

Cada decisão fecha, em média, 3 lacunas e destrava 4 peças. Tempo estimado de leitura: 20 min.

---

## Como usar

Responda cada item com uma linha. A resposta vira entrada no Vault com data e razão, o
`status_canonico` da peça muda de `CONFLITANTE` para `CANONICO`, e o validador libera.

Onde há **recomendação**, ela é minha leitura — não é decisão tomada.

---

# 🔴 Bloqueiam implementação

## D-01 · Qual é o vetor de pesos do estágio Construção?

**Lacuna:** `LAC-FOR-001` · **Destrava:** `FOR-SEV-012`, `PAR-SEV-001`

| Fonte | Vetor | Data |
|---|---|---|
| `Formulas_Consultoria_Aurora.md` (autodeclarada "fonte única") | 0,25 / 0,25 / 0,20 / 0,20 / 0,10 | — |
| `Oticas_ParteF_Score_Formula.docx` | 0,25 / 0,25 / 0,20 / 0,20 / 0,10 | 08/07 |
| `Oticas_Playbook_v9_Master.docx` (Master, mais recente) | **0,30** / 0,25 / 0,20 / **0,15** / 0,10 | 08/07 |

Os estágios **Cego** e **Cruzeiro** têm as três fontes concordando — só Construção diverge.
A regra de precedência não resolve: dois satélites contra um Master é inversão de nível.

**A pergunta por trás:** no estágio Construção, Captura vale mais que Resgate (0,30/0,15) ou
os dois pesam igual (0,25/0,20)?

☐ Variante A (0,25/0,25/0,20/0,20/0,10) ☐ Variante B (0,30/0,25/0,20/0,15/0,10) ☐ Outro

---

## D-02 · O PV deve usar a conversão crua ou o índice normalizado?

**Lacuna:** `LAC-FOR-003` · **Destrava:** `FOR-FCT-001` · **Severidade: a mais alta da fila**

```
PV = AG × ( IR ÷ 100 ) × TMR
```

O `IR` foi redefinido pela Blindagem como `mín(ConvReal ÷ P75 ; 1) × 100`. Usá-lo como
probabilidade de conversão infla o forecast: conversão real de 30% com alvo de 40% entra
como 0,75 quando deveria entrar como 0,30 — **2,5× de superestimação, que piora quanto
melhor o vendedor** (quem bate o alvo tem IR = 100 → o forecast assume conversão de 100%).

**Recomendação:** o `PV` consome `ConvReal` (`FOR-SEV-008`). O `IR` normalizado serve ao SEV,
não ao forecast. São duas variáveis com o mesmo nome.

☐ PV usa ConvReal ☐ PV usa IR normalizado (e a fórmula está certa) ☐ Rever

---

## D-03 · Resolver as duas colisões de sigla

**Lacunas:** `LAC-FOR-004`, `LAC-FOR-005` · **Destrava:** 4 peças · **Reprova V1 no validador**

| Sigla | Uso 1 | Uso 2 | Glossário da fonte |
|---|---|---|---|
| **MR** | Meta de Receita (§2.3) | Meta Residual (§5.7) | lista só "Meta Residual" |
| **PV** | Previsão de Venda (§3.1) | Preço de Venda (§6.1) | admite os dois, não resolve |

Numa planilha isso passa. Num sistema, alguém referencia o campo errado e o erro é silencioso.

**Recomendação:** `MRec` / `MRes` e `PVF` (forecast) / `PVU` (preço unitário).

☐ Aceito a recomendação ☐ Outros nomes: ______

---

## D-04 · O TMI operacional deve preservar a ponderação por mix?

**Lacuna:** `LAC-FOR-006` · **Destrava:** `FOR-TMI-004`, `FOR-SEV-007`

```
TMIo = TMIhv + α × ( TMIp − TMIhv )
       ↑ grão VENDEDOR      ↑ grão LOJA
```

O bloco inteiro existe para eliminar o "Erro 2 — TMI único para todos". Mas conforme α sobe,
todo vendedor converge para o mesmo `TMIp` de loja e o Erro 2 volta — três trimestres depois,
quando ninguém lembra mais por que a régua estava certa.

**Recomendação:** preservar a razão de mix no destino —
`TMIp_vendedor = TMIp_loja × (TMIhv_v ÷ TMIhv_loja)`.

☐ Preservar o mix no destino ☐ Manter como está (destino único é intencional)

---

## D-05 · A projeção de meta deve ter curva intra-mês?

**Lacuna:** `LAC-FOR-015` · **Destrava:** 4 peças

`PA_c = (V_c ÷ DU_e) × DU_t` assume venda uniforme pelos dias úteis. O varejo brasileiro
concentra em quinzena e fim de mês. Nos primeiros dias o PA% sai baixo e o EDN alto para
todo mundo — e a **CRA pinta a rede de vermelho todo começo de mês, todo mês**.

O risco não é matemático, é de adoção: falso alarme previsível ensina o gestor a ignorar o
painel — inclusive quando o vermelho é verdadeiro.

**Recomendação:** peso por dia útil derivado do histórico da própria loja. Coerente com a
doutrina (derivado do dado, nunca chutado) e barato de implementar.

☐ Curva de peso por dia útil ☐ Manter linear ☐ Linear + faixa de tolerância nos 10 primeiros dias

---

## D-06 · O AGV precisa de teto por categoria?

**Lacunas:** `LAC-FOR-013`, `LAC-FOR-014` · **Destrava:** `FOR-MET-013`, `FOR-MET-014`, `PAR-MET-001`

Duas coisas no mesmo lugar:

**(a) Sem teto.** `AGV = Σ(AR_c × w_c)` com `AR_c` ilimitado. Estourar uma categoria de meta
pequena levanta a nota inteira. O SEV tem teto em 100 por índice justamente para bloquear isso.

**(b) Pesos chutados.** A fonte rotula a tabela como *"Peso Sugerido"* com coluna *"Racional"*.
Isso contradiz frontalmente a linha final do Playbook v9: *"todo número ideal é derivado do
dado do próprio cliente e caminha por um glide path — nunca chutado. É a espinha do método."*

**Recomendação:** teto por categoria, e `w_c = Part_cat` (`FOR-MRG-005`) — a contribuição real
de cada categoria para pagar o custo fixo. O arsenal já calcula. Os pesos passam a derivar do
dado e se atualizam sozinhos.

☐ Teto + pesos derivados ☐ Só teto ☐ Manter (os pesos são decisão estratégica, não medição)

---

## D-07 · Política única para denominador zero

**Lacunas:** `LAC-FOR-010` (23 fórmulas), `LAC-FOR-032` · **Destrava:** ~25 peças

Nenhuma fonte declara comportamento para denominador nulo. Dois casos são **certos e datados**:

- `EDN` divide por `(DU_t − DU_e)` → zero no **último dia útil de todo mês**
- `PA`, `Pace` e `MC_proj` dividem por `DU_e` → zero no **dia 1 de todo mês**

**Recomendação:** uma política só, no Bloco 0 de contratos: denominador zero → índice **nulo**
com selo "sem base". Nunca 0 (parece ruim), nunca 100 (parece bom).

☐ Nulo + selo ☐ Outra política: ______

---

## D-08 · Escrever os blocos Fiscal e Financeiro

**Lacunas:** `LAC-FOR-019`, `LAC-FOR-049` · **Bloqueia:** a base de homologação inteira

Não existe, em nenhum dos 145 arquivos inventariados, fórmula de DAS, faixa, RBT12, tributo
embutido, fluxo de caixa, DRE ou resultado operacional.

E isso já contamina o que existe: `MC_item` subtrai "imposto sobre venda" dentro de `CV`, mas
sob o Simples o DAS incide sobre a receita bruta do mês pela faixa — não por item. A regra de
alocação não está escrita em lugar nenhum. Toda MC, MC%, PE, ICCF e GMROI herdam essa base
indefinida.

**Não se gera massa de dados contra fórmula que não existe.** Um terço do escopo da Fase 4
seria gerado às cegas.

☐ Escrevo os dois blocos ☐ Você escreve a partir de entrevista comigo ☐ Adiar (e a Fase 4 espera)

---

# 🟡 Bloqueiam o registro, não o código

## D-09 · Qual `EXRS_Spec_Laudo_Executivo_v4.md` é a Lei?

**Achado:** `INVENTARIO` A-02

| Caminho | Tamanho | Data |
|---|---|---|
| `AuroraControler/docs/Vault/` | 12,2 KB | 19/07 |
| `AuroraControler/laudo_executivo/` | **26,1 KB** | 21/07 |

Duas "Leis" com a mesma versão `v4`, 2,1× de diferença. O `build_laudo.py` tem a mesma
divergência (7,9 KB × 34,8 KB) e o template também.

**Recomendação:** a de `laudo_executivo/` — mais recente, maior, e é a que o `build_laudo.py`
ativo consome. A do Vault vira `SUPERADO` **no registro**, sem sair do disco (append-only).

☐ laudo_executivo/ é a Lei ☐ Vault é a Lei ☐ Preciso comparar antes

---

## D-10 · `Playbook_Entrega_Elysian_v1.docx` é vigente?

**Achado:** `INVENTARIO` A-04

Estava em `Historico/` e a `metodologia_consolidada` o chama de *"documento-mãe da metodologia
de entrega"* — define a anatomia de fase (Objetivo → Inputs → Passo a passo → Julgamento →
Ferramentas → Entregável → **Gate**) e afirma que pular um Gate é *"a causa raiz de quase todo
projeto que dá errado"*.

Já foi movido para `FONTES/metodo/` (a pasta não decide mais vigência). Falta o campo.

☐ `CANONICO` ☐ `SUPERADO` por: ______ ☐ `CANDIDATO`

---

## D-11 · `Doutrina-Sandeep` é doutrina (D) ou infra de agente (I)?

**Achado:** `INVENTARIO` A-06

8 arquivos em `AuroraControler/docs/Vault/Doutrina-Sandeep/` — `filtro-de-decisao`,
`vantagem-assimetrica`, `posicionamento-atual`, `capacidade-e-limites` e quatro ferramentas
(`DART`, `EDGE`, `3C`, `ASC`), mais dois system-prompts e uma auditoria de v8.

Nenhum documento do acervo Elysian os cita. Se for doutrina de decisão do fundador, entra na
extração como `AXI`/`MEC`. Se for configuração de agente, fica fora.

☐ Doutrina — extrair ☐ Infra de agente — fora do escopo ☐ Misto (eu separo e te mostro)

---

## D-12 · `Oticas_Motor_Dois_Relogios.docx` migra de repositório?

**Achado:** `INVENTARIO` A-03 · **Fila #6**

O documento do moat — *"óticas é moda disfarçada de saúde"*, a Parte B do Playbook — está em
`AuroraControler/docs/Documentos Gerais/`, não em `ElysianConsult/docs/FONTES/metodo/`.

É o único arquivo de doutrina comprovadamente na pasta errada. Mover entre repositórios é
decisão sua.

☐ Mover ☐ Manter e referenciar de lá

---

## D-13 · Duas fórmulas ficam `CANDIDATO` até você decidir

**Lacunas:** `LAC-FOR-009`, `LAC-FOR-025` · **Reprovas V4 no validador**

**(a) `RPI = assinatura(Topo) − assinatura(Base + saíram)`** — a própria fonte diz que *"a
subtração é conceitual"*. Não produz número. Ou define a operação vetorial, ou vira `MEC`.

**(b) `TMR`** — o Ticket Médio Real aparece em 4 fórmulas e **nunca teve a expressão escrita**,
só a legenda. Eu reconstruí (`receita ÷ nº de vendas`) e marquei `CANDIDATO`. E o Gabarito
exige robustez a outlier (*"L9: preço R$33.900 e qtd=99 · usar P75, não média"*), o que a
reconstrução não faz.

☐ RPI vira MEC ☐ RPI ganha fórmula: ______
☐ TMR = média simples ☐ TMR = mediana/P75 ☐ TMR = média winsorizada

---

---

# 🔴 Passe 2 — divergências entre documento e código

Classe nova. No passe 1 todas as fontes eram documentais; aqui entram as **versões
implementadas** (`SPEC_Fase_B`, status EXECUTADA), que pela regra de precedência têm o nível
mais alto. Em cinco casos elas **não descrevem a mesma coisa** que o documento.

## D-14 · GMROI tem dois denominadores diferentes

**Lacuna:** `LAC-FOR-052` · **Destrava:** `FOR-EST-003`, `FOR-AUD-001`

| Versão | Fórmula | Denominador |
|---|---|---|
| Documentada (Playbook B2) | margem bruta ÷ estoque médio a custo | **estoque MÉDIO** |
| Implementada (Algoritmo 1) | (receita − custo) ÷ capital preso | **estoque ATUAL** (`qtd_atual × custo_unit`) |

Numa loja que girou bem no período mas está com estoque baixo hoje, as duas dão resultados
opostos. E nenhuma fonte define como calcular "estoque médio" — janela? método?

O GMROI é declarado *"a métrica-rainha do estoque"* e aparece no Cockpit do dono.

**Nota:** a precedência diz que o código vence. Mas isso não é desempate de valor, é escolha
de definição — por isso está aqui.

☐ Estoque médio (e definir o método) ☐ Capital preso atual ☐ As duas, com nomes distintos

---

## D-15 · Quem carrega o risco de crédito?

**Lacuna:** `LAC-FOR-054` · **Destrava:** `FOR-FIN-007`, `FOR-FIN-008`, `FOR-FIN-009`

Dois modelos incompatíveis convivendo, com um dia de diferença entre os documentos:

| | `Playbook_Operacional_Detalhado` (07/07) | `Camada_Financeira_C2` (08/07) |
|---|---|---|
| Risco | a ótica provisiona ≈**8,5%** de inadimplência | parceiro assume **100%** — ótica tem risco zero |
| Receita financeira | **da ótica** (MDR/juros) | **da Aurora**, paga pelo parceiro |
| Inadimplência | linha do P&L da loja | monitorada no parceiro, avalia o parceiro |

Muda quem tem o P&L, quem provisiona e quem recebe. E o 8,5% é benchmark de mercado, o que
contraria a doutrina de derivar do dado.

**Recomendação:** o C2 é mais recente e é o documento dedicado ao tema — provavelmente supera.
Mas o Detalhado continua listado como método vigente, então precisa do seu martelo.

☐ C2 supera (risco zero) ☐ Os dois modelos coexistem por contexto ☐ Rever

---

## D-16 · Qual é o limiar do estoque morto?

**Lacuna:** `LAC-FOR-053` · **Destrava:** `FOR-EST-005`, `FOR-EST-006`

Três valores em circulação: **6–9 meses** (Playbook), **~250 dias** (Gabarito), **180 dias**
(deck não-canônico). Entre 180 e 270 dias o mesmo SKU é ou não é morto — e isso define o
número que vai para o Ato 3 do laudo.

O Playbook diz que N é *"calibrado pela sazonalidade da moda de armação"* mas não dá o método.
E o Gabarito exige que solar parado desde fevereiro **não** seja marcado (gira no verão).

☐ Fixar N = ___ dias ☐ Comparar contra o mesmo período do ano anterior ☐ Ambos

---

## D-17 · De onde sai a "conversão esperada" da Receita Latente?

**Lacuna:** `LAC-FOR-061` · **Destrava:** `FOR-BAS-008`

```
R_latente = (base sem X) × conversão esperada × ticket de X
```

É o número que abre o Executive Audit Report e produz o choque do Dia 5. **O único fator que
não é derivado do dado é justamente o multiplicador** — nenhuma fonte diz de onde ele vem.

Todo outro parâmetro do método (P75, ciclo mediano, TMI) tem derivação declarada.

**Recomendação:** derivar da conversão histórica de cross-sell da própria loja, ou reusar o
P75 do attach por segmento que já existe em `FOR-SEV-005`.

☐ P75 do attach ☐ Conversão histórica de cross-sell ☐ Parâmetro do consultor (e declarar)

---

## D-18 · Taxa de Identificação ou IC?

**Lacuna:** `LAC-FOR-062` · **Destrava:** `FOR-BAS-010`, `FOR-SEV-003`

Duas métricas respondendo "o cliente foi identificado?", com denominadores diferentes,
coexistindo no mesmo painel:

- **IC** = cadastrados ÷ **atendimentos**
- **Taxa de Identificação** = vendas identificadas ÷ **vendas totais**

Pior: o Playbook v9 chama a métrica do Cockpit de *"taxa de cadastro"* e usa o denominador do
IC; o Detalhado chama de *"taxa de identificação"* e usa vendas.

**Recomendação:** Taxa de Identificação é a métrica de **Nível 0** (quando o AT não é
observável); o IC é a de **Nível 1+**. A escada do AT já existe em `REG-SEV-001` — é só
amarrar as duas nela.

☐ Aceito ☐ Uma só métrica: ______

---

## D-19 · 16 fórmulas estão escritas em prosa, não em símbolos

**Checagem:** `V12` (nova) · **Afeta:** blocos BAS, EST, FIN, CNC, AUD

O validador ganhou uma checagem que eu não tinha previsto no esquema, porque o problema só
apareceu no passe 2: várias fórmulas das fontes secundárias são frases, não expressões.

> `giro = CMV do período ÷ estoque médio a custo`
> `morto = SKU sem venda há mais de N meses`
> `follow_on = clientes que fizeram follow-on ÷ total que iniciaram em serviço`

São perfeitamente compreensíveis para um humano e **não implementáveis sem tradução**. Cada
uma exige uma decisão escondida (o que é "estoque médio"? qual a janela de "posterior"?).

Não é erro de extração — é como as fontes escrevem. Mas o critério de pronto do
`ESQUEMA_PECA` §9 exige que um agente aplique a fórmula sem contexto, e prosa não passa nesse
teste.

☐ Traduzo as 16 para notação simbólica e você revisa ☐ Deixo em prosa e traduzo só na
implementação ☐ Prioridade só nas que bloqueiam a base de homologação

---

# O que acontece depois

| Você decide | O validador libera | Fica pronto para |
|---|---|---|
| D-01 a D-08 | as reprovas críticas do passe 1 | codificar contra o Gabarito |
| D-09 a D-12 | o registro fecha os dois passes | extrair AXI, MEC, GAT, APA, ART |
| D-13, D-19 | as 16 peças em prosa e as 2 candidatas | implementação direta |
| D-14 a D-18 | as 16 peças `CONFLITANTE` | o motor e a documentação convergirem |

Com **D-08** respondida (blocos Fiscal e Financeiro), a Fase 4 — base de homologação —
destrava. Sem ela, não.

E fica valendo o critério de pronto do `ESQUEMA_PECA` §9: **fórmula documentada que não foi
codificada contra o gabarito ainda é hipótese.** Hoje, **72 das 99** estão nesse estado.

---

## Estado do registro

| | Passe 1 | Passe 2 | Total |
|---|---:|---:|---:|
| Fórmulas (`FOR`) | 62 | 37 | **99** |
| Lacunas (`LAC`) | 51 | 26 | **77** |
| Regras (`REG`) | 7 | — | **7** |
| Peças `CONFLITANTE` | 6 | 10 | **16** |
| Peças com gabarito | 10 | 17 | **27** |

**Blocos cobertos:** SEV · TMI · FCT · CMP · MET · MRG · BAS · EST · FIN · CNC · AUD
**Blocos que não existem em nenhuma fonte:** 🔴 **Fiscal** · 🔴 **Financeiro (fluxo/DRE)**
**Tipos ainda não extraídos:** `AXI` · `MEC` · `GAT` · `APA` · `ART` · `EVI`
