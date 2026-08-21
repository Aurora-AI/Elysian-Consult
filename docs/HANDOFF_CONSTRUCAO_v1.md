# HANDOFF — Construção do Sistema Aurora / Elysian

> **Para:** o modelo/agente que vai implementar
> **De:** sessão de catalogação de 13/08/2026
> **Uso:** cole o bloco `PROMPT INICIAL` abaixo como primeira mensagem, com acesso a
> `C:\Projetos\Aurora\ElysianConsult` e `C:\Projetos\Aurora\AuroraControler`.

---

# PROMPT INICIAL

Você vai implementar parte de um sistema de consultoria comercial para varejo ótico. Antes de
escrever qualquer linha de código, leia esta mensagem inteira e depois os arquivos na ordem
indicada. **Não pule a ordem de leitura** — ela existe porque cada documento depende do anterior.

## 1. O que é isto

A **Elysian Consult** é uma consultoria comercial que opera sobre um motor determinístico
(**EXRS**, em `C:\Projetos\Aurora\AuroraControler`). O motor lê planilhas de operação de varejo,
calcula métricas comerciais e produz um relatório de auditoria congelado. Sobre esse relatório
são construídos artefatos: um laudo executivo, um painel do dono, filas operacionais.

O método (fórmulas, regras, artefatos) foi extraído de ~145 documentos e vive num **registro
estruturado** em `ElysianConsult/docs/CATALOGO/registro/*.yaml`. **Esse registro é a fonte da
verdade.** Documentos em prosa são a origem histórica; o registro é o que vale.

## 2. Ordem de leitura obrigatória

| # | Arquivo | Por quê |
|---|---|---|
| 1 | `ElysianConsult/docs/CATALOGO/ESQUEMA_PECA.md` | o contrato: como o conhecimento está estruturado, o que cada campo significa |
| 2 | `ElysianConsult/docs/CATALOGO/DECISOES.md` | 9 decisões do autor que governam tudo. **Leia todas.** |
| 3 | `ElysianConsult/docs/CATALOGO/registro/regras.yaml` | 14 regras, várias `INEGOCIAVEL` |
| 4 | `ElysianConsult/docs/CATALOGO/registro/artefatos.yaml` | 6 artefatos — o contrato entre fórmula e tela |
| 5 | `ElysianConsult/docs/CATALOGO/render/DICIONARIO_DASHBOARD.md` | gerado: o que renderizar, onde, com que profundidade |
| 6 | `ElysianConsult/docs/CATALOGO/registro/formulas.yaml` + `formulas_p2.yaml` | 99 fórmulas |
| 7 | `ElysianConsult/docs/CATALOGO/render/LACUNAS_CONSULTORIA.md` | gerado: 60 problemas conhecidos e abertos |
| 8 | `AuroraControler/laudo_executivo/EXRS_Spec_Laudo_Executivo_v4.md` | a **LEI** de apresentação do laudo |
| 9 | `AuroraControler/SPEC_Fase_B/C/D2/E_*.md` | o que o motor já implementa |

## 3. O que já existe e funciona

- **Motor EXRS** (`AuroraControler/src/`) — pipeline A0→A4, 461 testes passando.
  `commercial_auditor.py` já implementa GMROI, attach rate, corrosão de desconto, curva ABC,
  follow-on, churn, RFM, completude, estoque morto, margem de contribuição.
- **`build_laudo.py`** — gera o laudo executivo a partir do relatório congelado, com validador
  de zero contradição.
- **Duas fixtures** em `ElysianConsult/docs/FONTES/dados/`:
  `Consultoria.xlsx` (rede ótica, 10 lojas, 41 meses) e `Rede_PetShop.xlsx`.
  Ambas têm aba **`Gabarito`** com **37 anomalias plantadas e resultado esperado** — é a régua
  de veracidade. Use-a para verificar qualquer cálculo que você implementar.
- **Registro** com 210 peças: 99 fórmulas, 14 regras, 6 artefatos, 91 lacunas, 9 decisões.
- **Validador** (`CATALOGO/validar.py`) e **gerador** (`CATALOGO/gerar_render.py`).

## 4. As travas inegociáveis

Estas não são preferências. Violar qualquer uma reprova a entrega.

**T1 · A apresentação não recalcula.**
O motor produz `audit_report_<rodada>.json` **congelado**. Toda camada acima lê esse JSON e
**nunca** recalcula, nunca acessa a planilha, nunca chama LLM. Se um número precisa existir na
tela e não está no relatório, a correção é **exportá-lo do motor** — jamais calculá-lo na
apresentação. *(SPEC_Fase_D2 §0)*

**T2 · Sem base → NULO com selo. Nunca 0, nunca 100, nunca a média.**
Denominador zero ou insumo ausente não produzem número; produzem a **ausência declarada** de
número. O nulo é **excluído** de agregações e rankings, não tratado como zero.
*(REG-NUM-001, INEGOCIÁVEL)*

**T3 · Todo número desce até a linha de origem.**
Todo eixo vertical de todo artefato termina em `linha_de_origem` (`source_rows`). O drill-down
é **mecanismo de diagnóstico**, não navegação — um erro de cadastro num SKU já explicou um
falso "vendedor que corrói 337% de margem". *(DEC-009, SPEC_Fase_D2 Pilar 2)*

**T4 · Superfície mínima, profundidade total.**
Cada artefato declara `teto_elementos`. Estourou o teto, não é superfície. A complexidade é
**latente**, não ausente: nada sai do sistema, tudo sai da entrega ativa. *(DEC-009)*

**T5 · Nomes de vendedor nunca aparecem em painel.**
Só distribuição por bandas. Score sai **sempre** com caminho de desenvolvimento, nunca ranking
cru. Nomes vivem só no coaching privado, e o modo nominal exige aceite de RH/jurídico
registrado. Isso é controle de acesso no software, não convenção. *(REG-SEV-004, LGPD +
trabalhista)*

**T6 · Item pendente nunca vira fato.**
Achado na fila de auditoria não entra em nenhum total, não gera acusação, não aparece em painel
de negócio até ter veredito humano. *(SPEC_Fase_C)*

**T7 · Nada é inferido do que não está no dado.**
Coluna ausente → `[LACUNA]` visível. Zero estimativa silenciosa. *(SPEC_Fase_E §0.1)*

## 5. O que NÃO fazer

**Esta seção é mais importante que a anterior.** Você vai encontrar coisas que parecem erradas.
Muitas **são** erradas. Elas estão erradas de propósito e já estão registradas.

❌ **Não corrija fórmula nenhuma.**
Existem 60 lacunas abertas, 12 delas críticas — inclusive um forecast inflado em 2,5× e um TMI
que dissolve a própria tese. **Todas já estão documentadas** em `LACUNAS_CONSULTORIA.md` com
evidência e correção candidata, aguardando decisão do autor. Se você "consertar", quebra a
procedência e o autor perde a rastreabilidade. **Implemente como está, ou pare e reporte.**

❌ **Não invente fórmula que não existe.**
Os blocos **Fiscal** (DAS, faixa, RBT12) e **Financeiro consolidado** (fluxo de caixa, DRE) não
existem em nenhum dos 145 arquivos. Se precisar deles, **pare e declare a lacuna**. Não deduza,
não use "padrão de mercado", não copie de outro sistema.

❌ **Não edite nada em `CATALOGO/render/`.**
É saída de build. Para mudar, mude a peça no registro e rode `gerar_render.py`.

❌ **Não use `docs/SPEC/SPEC_Sistema_Gestao_360_v1.md` §5 nem o `prototipo_chronos_v1.html`.**
O conceito de interface está **SUPERADO** (`DEC-009`). O catálogo de KPIs e o modelo de dados
daquele documento sobrevivem — as 8 telas densas, não. O contrato de tela é o bloco `ART`.

❌ **Não trate as fixtures como amostra de volume.**
`Consultoria.xlsx` tem 7,4 linhas/loja/mês e R$ 3.497 de receita/loja/mês. É fixture
**funcional** — construída para carregar as anomalias do Gabarito, não para representar
densidade operacional. Serve para validar **corretude**, nunca para calibrar limiar estatístico.

❌ **Não acuse vendedor com base em desconto.**
A fórmula de erosão de margem não tem teto e já produziu 337% em dado real — a causa era erro de
cadastro, não conduta. Toda discrepância passa pela triagem da Fase C antes de virar afirmação
sobre uma pessoa.

❌ **Não peça permissão para cada passo, mas não avance sobre bloqueio.**
Trabalhe até o ponto onde falta uma decisão do autor. Aí pare, nomeie o bloqueio pelo ID
(`LAC-FOR-003`, etc.) e reporte.

## 6. Estado real: nenhum artefato está 100% desbloqueado

Verificado no registro em 13/08/2026:

| Artefato | Fórmulas | `CONFLITANTE` | Lacuna crítica | Estado |
|---|---:|---:|---:|---|
| `ART-ANX-001` Anexo Vivo | 0 | 0 | 0 | ✅ construível |
| `ART-FIL-001` Fila de resgate | 8 | 1 | 1 | ⚠️ quase |
| `ART-FIL-002` Fila de auditoria | 10 | 5 | 2 | ⛔ |
| `ART-COC-001` Cockpit | 27 | 4 | 2 | ⛔ |
| `ART-LAU-001` Laudo | 31 | 7 | 3 | ⛔ |
| `ART-PER-001` Painel de bandas | 30 | 3 | 10 | ⛔ |

**Consequência:** você **não** vai construir o sistema inteiro. Construa o que está limpo, pare
no bloqueio, reporte com o ID da lacuna.

## 7. Sua primeira tarefa

Implementar o **`ART-FIL-001` — Fila de resgate diária**, em versão v1 reduzida.

**Por que este:** superfície de 1 elemento, 8 fórmulas, domínio `CLIENTE` (o único 100%
coberto pelo registro), maior frequência de uso (diária), maior valor operacional, e há dado
real na fixture para testar — **146 clientes em churn, R$ 68.785 de perda medida**.

**Escopo v1 — implemente:**
- Lista de clientes a resgatar, **ordenada por recuperabilidade** (`FOR-BAS-006`), não por valor.
  Um cliente de R$ 1.640 sumido há 2,8 ciclos vale menos hoje que um de R$ 894 sumido há 1,7.
- Para cada: identificação, última compra, silêncio ÷ ciclo, ticket histórico, segmento RFM.
- Drill-down até `linha_de_origem` (T3).
- Superfície de **1 elemento** (T4): a lista. Nada de dashboard em volta.

**Fora do escopo v1 — e declare o porquê na saída:**
- Coluna "o que oferecer" (cross-sell). Depende de `FOR-BAS-007` (`CONFLITANTE` — denominador
  diverge entre documento e código, `LAC-FOR-060`) e de `FOR-BAS-008` (lacuna crítica
  `LAC-FOR-061` — a "conversão esperada" não tem origem declarada em fonte nenhuma).

**Cuidado obrigatório:** `FOR-BAS-004` (churn) tem falso positivo sazonal conhecido. O Gabarito
exige que `SEAS-001..005` **não** sejam marcados como churn — compram solar só no verão, ciclo
anual. Sua implementação tem que passar nesse teste. *(LAC-FOR-057)*

## 8. Como verificar seu próprio trabalho

1. **Contra o Gabarito.** `Consultoria.xlsx` › aba `Gabarito` tem o resultado esperado.
   Para esta tarefa: `Churn Invisível (A3) — C-017..C-021, 5 clientes, perda ≈ 5 × R$ 694,85` e
   o falso positivo `SEAS-001..005`.
2. **Contra o validador.** `python CATALOGO/validar.py` deve continuar em 4 reprovas ou menos.
   Se subiu, você quebrou alguma coisa.
3. **Contra as travas.** Releia §4 e confirme cada uma explicitamente na sua entrega.

## 9. Formato da sua primeira resposta

Antes de codar, responda:

1. **O que você entendeu** que o sistema faz — em 5 linhas, sem repetir este texto.
2. **Três coisas que você acha que estão erradas** no registro. (Estão. Quero ver se você as
   encontra sem que eu aponte — e você **não** vai corrigi-las.)
3. **Qual trava você acha mais fácil de violar sem perceber** e como pretende se proteger.
4. **O plano de implementação** da fila de resgate, em passos, com o ponto exato onde você
   espera esbarrar num bloqueio.

Não escreva código nesta primeira resposta.

---

# Notas para o Rodrigo (não colar no prompt)

**Por que a pergunta 2 está lá.** É um teste de leitura, não de esperteza. Se o modelo não achar
o `PVS` inflado, o `TMIo` misturando grão, ou o `AGV` sem teto, ele não leu o registro — leu o
sumário. Melhor descobrir isso na primeira resposta que depois de 400 linhas de código.

**Por que não mandei construir o Cockpit.** É o que o cliente vê, mas tem 4 fórmulas
`CONFLITANTE` e 2 lacunas críticas. Um modelo novo vai "resolver" os conflitos sozinho — e aí
você tem um painel que não bate com o registro, e ninguém sabe qual dos dois está certo.

**O que este prompt não resolve.** Ele passa contexto, não julgamento. As decisões `D-01` a
`D-19` da `FILA_DECISAO.md` continuam sendo suas. Nenhum modelo deveria tomá-las — e este prompt
diz isso explicitamente três vezes, porque um modelo novo vai querer ajudar.

**Se ele responder bem às 4 perguntas**, o contexto passou. Se ele começar a propor melhorias no
método logo de cara, o contexto não passou — reforce a §5 antes de deixar codar.
