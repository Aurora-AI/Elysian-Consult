# FILA DE DECISÃO — o resíduo que só o autor resolve

> **Gerada em:** 13/08/2026 · Passe 2 (diagnóstico) do bloco `FOR`
> **Contrato:** `ESQUEMA_PECA.md` §6 e §10 — o extrator não decide. Nunca.
> **Princípio dimensionador** (herdado da `SPEC_Fase_C`): a fila recebe o resíduo, nunca o
> atacado. **Fila com 200 itens = esquema errado. Fila com 13 itens = governança.**

**Estado:** 120 peças extraídas · 51 lacunas registradas · **13 decisões nesta fila** ·
8 reprovas no validador, todas rastreadas a uma lacuna.

Cada decisão fecha, em média, 3 lacunas e destrava 4 peças. Tempo estimado de leitura: 15 min.

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

# O que acontece depois

| Você decide | O validador libera | Fica pronto para |
|---|---|---|
| D-01 a D-08 | as 8 reprovas | codificar contra o Gabarito |
| D-09 a D-12 | o registro fecha o passe | extrair os blocos BAS, EST, FIN, CNC, AUD |
| D-13 | `FOR-CMP-002`, `FOR-TMI-006` | — |

Com D-08 respondida, a Fase 4 (base de homologação) destrava. Sem ela, não.

E fica valendo o critério de pronto do `ESQUEMA_PECA` §9: **fórmula documentada que não foi
codificada contra o gabarito ainda é hipótese.** Hoje, 52 das 62 estão nesse estado.
