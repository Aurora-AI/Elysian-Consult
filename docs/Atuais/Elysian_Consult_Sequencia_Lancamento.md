[INCORPORADO]
# Elysian Consult — Sequência de Lançamento

**Eixo 1 — Framework Elysian (GTM e modelo de entrega)**
**Origem:** extraído de `ORGANIZACAO-DO-TRABALHO-20260802.md` (§2, §5, §6-Trilha A, §7 itens 1–3). O restante daquele documento — Trilha B, §3, §4 — trata do Agente Sandeep e saiu de escopo para o Repo Aurora.
**Fonte-irmã:** `Go Live Elysian Consult.md`
**Atualizado:** 2026-08-10, com a resposta do fundador à pergunta bloqueante da §2.

---

## 0. O que este documento NÃO faz

- Não decide o nicho, o preço nem o formato do contrato. São chamadas do fundador; aqui elas ficam **nomeadas e ordenadas**, não resolvidas.
- Não trata do Agente Sandeep, do corpus Swadia nem do schema Qdrant. Aquela frente vive no Repo Aurora.
- Não avalia se o posicionamento "GTM Engineer" vence no mercado do Sul. Nenhum documento do corpus responde isso — só o campo responde.
- Não é OS.

---

## 1. A pergunta bloqueante — respondida

O documento de origem (§5) condicionava todo o calendário a uma verificação, e a deixava explicitamente **não verificada** (linha 201: *"Vi nomes de diretório em `AuroraControler`, não abri nenhum"*):

> *O motor analítico que produz o Laudo em 7 dias existe e foi rodado contra dados reais de uma empresa que não é a Cooper Card?*

**Resposta do fundador (2026-08-10): não. Nunca rodou contra dados reais de terceiro.**

### Consequência declarada pela própria fonte

O documento de origem antecipou os dois ramos: *"Se sim, o lançamento é executável e a prioridade é comercial. Se não, 'agosto de 2026' é aspiração, e o sequenciamento abaixo muda."*

Logo, e sem suavização:

- **"Agosto de 2026" é aspiração, não plano.** A data do `Go Live` perdeu a base que a sustentava.
- A oferta central — **Laudo de Choque em 7 dias** — é hoje uma **promessa não testada fora de casa**. Prometer prazo a terceiro sobre um motor que nunca viu dado de terceiro é assumir risco de entrega no primeiro cliente, que é exatamente o cliente que não se pode perder.
- **A prioridade deixa de ser comercial e passa a ser de validação.** Não por conservadorismo: porque a decisão de preço (retainer pela receita latente resgatada em 60 dias) precifica um resultado que ainda não foi medido em nenhuma empresa fora da Cooper Card.

### O que muda na prática

O A1 do documento de origem era "confirmar que o Laudo roda ponta a ponta em dados de terceiro". Ele deixa de ser uma **confirmação** e vira uma **construção** — com trabalho, prazo e risco próprios. É o novo caminho crítico.

---

## 2. As quatro decisões que nenhum agente cobre

Achado central do documento de origem (§2), e a razão de ele ter sido preservado.

O system prompt do conselheiro declara literalmente os domínios em que se recusa a opinar:

> *"Continuam sem veto: precificação, aquisição de cliente, distribuição e posicionamento. Nesses domínios eu declaro a ausência em vez de improvisar."*

E o `Go Live` é composto **integralmente** desses quatro domínios:

| Decisão do Go Live | Domínio | Cobertura |
|---|---|---|
| Retainer pago pela receita latente resgatada em 60 dias | precificação | **sem veto** |
| Os 3 primeiros clientes, Laudo de Choque em 7 dias | aquisição | **sem veto** |
| Nicho verticalizado no Sul — varejo regional, óticas, distribuidores B2B | distribuição | **sem veto** |
| "GTM Engineer" contra consultoria clássica; vender governança de receita, não metodologia | posicionamento | **sem veto** |

**O conselheiro disponível não pode aconselhar o lançamento a ser feito.** Isso não é defeito — é o agente funcionando como projetado, declarando ausência em vez de preencher lacuna com plausibilidade. O problema é de **cobertura**, não de qualidade.

**Decisão registrada:** aceitar a lacuna. As quatro decisões são tomadas pelo fundador, sem conselheiro, e **registradas como casos** (ver §4). Construir um segundo conselheiro antes de lançar atrasaria o único movimento que gera dado real — e agora, com a §1 respondida, há trabalho de validação mais urgente do que trabalho de conselheiro.

---

## 3. Sequência revisada

A Trilha A original assumia motor validado. Com a resposta da §1, ela ganha uma fase anterior.

```
FASE 0 — VALIDAÇÃO DO MOTOR   (novo caminho crítico)
  V1  Escolher uma empresa-piloto que não seja a Cooper Card
  V2  Rodar o Laudo ponta a ponta com os dados dela
  V3  Cronometrar o ciclo real — "7 dias" é hipótese até virar medição
  V4  Registrar onde o motor quebrou, o que exigiu intervenção manual
      e o que precisou de dado que o cliente não tinha
  V5  Só então decidir se a promessa pública é 7 dias, ou outro número

FASE A — LANÇAMENTO   (destravada por V5)
  A2  Fechar o subsegmento único do Sul
  A3  Escrever a oferta dos 3 primeiros — o que promete,
      em quantos dias, a que custo
  A4  Rodar. As quatro decisões da §2 são tomadas sem conselheiro
  A5  Registrar cada uma das quatro como caso

DEPOIS DO LANÇAMENTO
  C1  Decidir se o 2º conselheiro é necessário — com os casos
      de A5 na mão, não por antecipação
```

**Nota sobre V1.** O piloto pode ser um cliente pagante com expectativa calibrada ("estamos rodando isto pela primeira vez fora de casa, o preço reflete isso") em vez de um teste gratuito. A diferença é que um piloto pago já é evidência comercial; um teste gratuito é só evidência técnica. Chamada do fundador.

**Por que A5 importa mais do que parece.** As quatro decisões da §2 serão tomadas de qualquer forma. Registradas no formato situação → veredito → mecanismo, viram o começo da coleção empírica — o único corpus que ninguém pode copiar. É a diferença entre tomar quatro decisões e acumular quatro casos.

---

## 4. Decisões pendentes

| # | Decisão | Estado | Por que é do fundador |
|---|---|---|---|
| 1 | O Laudo roda em dados de terceiro? | **RESPONDIDA — não.** Ver §1 | reordenou toda a sequência |
| 2 | Qual empresa-piloto para o V1 | **aberta, agora é a mais urgente** | depende de acesso e de confiança, não de análise |
| 3 | Subsegmento único do Sul | aberta (`Go Live` §3.1) | nenhum agente tem base; depende de onde já se domina a linguagem |
| 4 | Piloto pago ou teste gratuito | aberta | ver nota do V1 |
| 5 | Aceitar a lacuna dos 4 domínios e lançar sem 2º conselheiro | **DECIDIDA — aceitar.** Ver §2 | — |

---

## 5. Julgamento declarado

- **Evidência:** o texto de `ORGANIZACAO-DO-TRABALHO-20260802` e do `Go Live Elysian Consult`. O conflito da §2 está literal nos dois documentos — é leitura, não inferência. A resposta da §1 é declaração direta do fundador em 2026-08-10.
- **Julgamento:** a Fase 0 e sua precedência sobre a Fase A. O documento de origem previu que o "não" reordenaria o sequenciamento, mas não escreveu o sequenciamento alternativo — a Fase 0 acima é construção minha a partir dessa instrução.
- **Não verificado:** o estado dos artefatos `retail_hostile_test_v1_diagnostico`, `retail_hostile_test_v1_auditoria` e `laudo_executivo` em `AuroraControler`. Continuam sem leitura, aqui como no documento de origem. Eles podem reduzir o escopo do V2 — ou revelar que o motor está mais distante do que a resposta da §1 sugere.
- **Fora do campo:** se "GTM Engineer" vence no mercado específico do Sul. Nenhum agente tem veto para o domínio. Só o campo responde — que é, aliás, o argumento para lançar assim que o V5 permitir.
