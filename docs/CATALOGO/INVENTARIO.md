# INVENTÁRIO DO ACERVO AURORA / ELYSIAN — Fase 0

> **Status:** EXECUTADO em 13/08/2026
> **Escopo varrido:** `ElysianConsult/**` + `AuroraControler/{*.md, *.json, docs/Documentos Gerais, docs/Vault, docs/superpowers, laudo_executivo}`
> **Fora do escopo:** `AuroraControler/{src, tests, libs, aurora-frontend, output, reports, scratch}` — código e artefatos de execução, sem densidade doutrinária
> **Método:** varredura + hash SHA-256 (12 díg.) + **teste de legibilidade por extração real de texto**, não por extensão
> **Anexo:** `INVENTARIO.csv` — os 141 arquivos com classe, tamanho, data, hash e diagnóstico

---

## 1. Sumário

**141 arquivos · ~25,6 MB · 10 classes**

| Classe | Arq. | Tamanho | O que é |
|---|---:|---:|---|
| **S · Spec técnica** | 54 | 994 KB | SPECs do EXRS, planos superpowers, laudo, OS |
| **D · Doutrina/Método** | 21 | 794 KB | Playbooks, PBM, SSOT, framework — **a fonte do método** |
| **E · Evidência** | 18 | 15 KB | Gabaritos, OS-Evidence, logs de gate |
| **I · Infra/Agente** | 17 | 58 KB | Prompts, system-prompts, Doutrina-Sandeep, schema Qdrant |
| **O · Organização** | 9 | 51 KB | Índices, backlog, estado atual, READMEs |
| **C · Comercial** | 6 | 393 KB | Apresentações, docs de sócios, linguagem simples |
| **T · Dado/Fixture** | 6 | 1.437 KB | Consultoria.xlsx, PetShop, baselines |
| **F · Fórmulas** | 5 | 69 KB | ParteF (SEV, TMI, Blindagem), Mapa de Aplicação, Arsenal |
| **X · Intel competitiva** | 3 | 21.629 KB | Método Aurora, 360 Óticas, transcrição OCR |
| **P · Pesquisa externa** | 3 | 164 KB | Metodologias Pós-IA, GTM PMEs, Go Live |

**Leitura:** 84% do volume documental é spec técnica e infra. A doutrina — o ativo real — são **21 arquivos**. O alvo da primeira extração (D + F) são **26 arquivos**, ~860 KB.

---

## 2. Legibilidade

| Estado | Arq. | |
|---|---:|---|
| ✅ OK | 139 | texto extraível integralmente |
| ⚠️ PARCIAL | 1 | `360_Oticas_Apresentacao.pdf` — 34 pág., **10 sem camada de texto** |
| 🔴 ILEGÍVEL | 1 | `Método Aurora_ Estratégia e Fosso Competitivo.pdf` — 13 pág., 79 chars extraíveis |

O acervo estava em estado melhor do que o esperado: só **2 pontos cegos**, ambos em material de inteligência competitiva, nenhum em doutrina.

### 2.1. O ponto cego já tinha sido resolvido — e ninguém sabia

`ElysianConsult/docs/Historico/Metodo_Aurora_Transcricao_OCR.md` (5.739 chars, **10/08/2026**) é a transcrição completa das 13 páginas do PDF ilegível, feita com `pdfimages` + `tesseract`, com ressalva de fidelidade declarada.

Ela existia há três dias, arquivada em `Historico/`, enquanto o `metodologia_consolidada.md` registrava o PDF como não incorporável e o SSOT era construído sem ele. **A transcrição foi verificada contra leitura visual independente das 13 páginas em 13/08 — bate integralmente.**

Isso não é falha de OCR. É ausência de índice: o acervo não sabia o que já tinha resolvido.

> **Ruling do autor (13/08/2026):** o `Método Aurora_ Estratégia e Fosso Competitivo.pdf` é comparativo de mercado sobre consultorias e franquias, **nunca foi usado**. Classificação: `X · Intel competitiva`, canonicidade `NAO_UTILIZADO`. Não é doutrina.

Esse ruling resolveu, numa frase, **três dos quatro conflitos** que a leitura do deck havia aberto (o "+20% de faturamento", o "70% de cadastros incompletos" e o limiar de estoque morto em 180 dias). Nenhum deles é doutrina — são material de pesquisa não utilizado. A regra de precedência funcionou na primeira aplicação.

**Permanece extraível como intel, com canonicidade baixa:** Berry / royalty até 24%, o mecanismo "Judô Corporativo", e a comparação de modelo de receita (% sobre bruto × taxa fixa/SaaS). São as únicas peças de inteligência competitiva nomeada do acervo inteiro.

---

## 3. Achados

### A-01 · Arquivo órfão: a "fonte única das fórmulas" estava fora do repositório 🔴

`Formulas_Consultoria_Aurora.md` — que se autodeclara *"a fonte única de todas as fórmulas criadas para a arquitetura de performance"* — **não estava em nenhuma das duas pastas.** Chegou por upload manual em 13/08/2026.

É o documento mais denso do acervo em fórmulas (Blocos 5 · Metas e 6 · Margem em 5 níveis **não existem em nenhum outro arquivo**), e estava fora do controle de versão.

> **Ação executada:** copiado para `ElysianConsult/docs/Atuais/Formulas_Consultoria_Aurora.md`. Deixa de ser órfão. (Cópia, não edição — o conteúdo não foi tocado.)

### A-02 · Três pares de arquivo com mesmo nome e conteúdo divergente 🔴

| Arquivo | Vault | laudo_executivo | Delta |
|---|---:|---:|---|
| `EXRS_Spec_Laudo_Executivo_v4.md` | 12,2 KB · 19/07 | **26,1 KB · 21/07** | 2,1× |
| `EXRS_Template_Laudo_Executivo_v4.html` | 22,3 KB · 19/07 | **38,6 KB · 21/07** | 1,7× |
| `build_laudo.py` | 7,9 KB · 19/07 | **34,8 KB · 10/08** | 4,4× |

Os dois primeiros são o documento que se declara **"LEI · o System Prompt mestre do agente gerador de laudos"**, com precedência sobre qualquer instrução de formatação. Existem duas leis com o mesmo nome e versão `v4`.

Pela regra de precedência (§ Esquema), a de `laudo_executivo/` vence: mais recente, maior, e é a que o `build_laudo.py` ativo consome. A do Vault deve ser marcada `SUPERADO` — não apagada, o Vault é append-only.

**Item #1 da fila de decisão.**

### A-03 · O documento do moat mora no repositório errado 🟡

`Oticas_Motor_Dois_Relogios.docx` está em `AuroraControler/docs/Documentos Gerais/`. O `metodologia_consolidada.md` o trata como o **núcleo conceitual** do método ("óticas é moda disfarçada de saúde" — a Parte B do Playbook, onde mora o moat).

O documento que define a vantagem competitiva está fora da pasta de metodologia.

### A-04 · O "documento-mãe" está arquivado como histórico 🟡

`Playbook_Entrega_Elysian_v1.docx` (170 parágrafos, 9 tabelas, 16.038 chars) está em `docs/Historico/`. O `metodologia_consolidada.md` o chama de *"o documento-mãe da metodologia de entrega"* e fonte da anatomia de fase (Objetivo → Inputs → Passo a passo → Julgamento → Ferramentas → Entregável → **Gate**).

Ou ele foi superado por algo e isso não está registrado, ou a pasta está errada. **Item #2 da fila.**

### A-05 · Duplicata exata 🟢

`PBM_Config_Motor_por_Frente.docx` — hash idêntico em `ElysianConsult/docs/Atuais/` e `AuroraControler/docs/Documentos Gerais/`. Existe ainda uma versão `.md` (9,3 KB, 11/08) que é **derivada, não idêntica**. Manter a `.md` como canônica e as `.docx` como origem.

### A-06 · Um corpo doutrinário inteiro fora do radar 🟡

`AuroraControler/docs/Vault/Doutrina-Sandeep/` — 8 arquivos: `filtro-de-decisao`, `vantagem-assimetrica`, `posicionamento-atual`, `capacidade-e-limites`, e quatro ferramentas (`DART`, `EDGE`, `3C`, `ASC`). Mais `system-prompt-agente-sandeep-final.md` e uma auditoria de v8.

É doutrina de decisão estratégica do fundador, não citada em nenhum documento do acervo Elysian. Classificada como `I · Infra/Agente` por ora — **pode ser reclassificada como `D`** dependendo do que a extração encontrar.

### A-07 · Assimetria de datas 🟢

Doutrina Óticas: **06–09/07/2026**, congelada. Specs EXRS: **19–30/07**. Consolidação e SSOT: **11–12/08**. Doutrina-Sandeep e organização: **02–03/08**.

O método parou de ser escrito em julho; desde então o movimento é de consolidação e de produto. Coerente com a fase — mas significa que **a doutrina não foi revisada depois que as SPECs de execução (Fases B/C/D/E) descobriram problemas reais no dado**. O aprendizado do motor não subiu de volta para o método. É a mesma observação que o `metodologia_consolidada.md` já registra no fecho, ainda em aberto.

---

## 4. Alvo da Fase 2 — extração de Fórmulas

Ordem de precedência aplicada. **5 arquivos primários, 6 secundários.**

| # | Arquivo | Papel | Peso |
|---|---|---|---|
| 1 | `Formulas_Consultoria_Aurora.md` | Arsenal — autodeclarado fonte única. **Único com Blocos 5 e 6** | Primário |
| 2 | `Oticas_ParteF_Score_Formula.docx` | Os 5 índices, escada do AT, bandas | Primário |
| 3 | `Oticas_ParteF_Blindagem_SEV.docx` | Regra de normalização universal | Primário |
| 4 | `Oticas_ParteF_TMI.docx` | Engenharia do TMI | Primário |
| 5 | `Oticas_Mapa_Aplicacao_Formulas.docx` | Onde · Quando · Quem · Entra→Sai | Primário |
| 6 | `Oticas_Playbook_v9_Master.docx` | A1–A4, B1–B5, C1–C2, Cockpit, pesos | Secundário |
| 7 | `Oticas_Playbook_Operacional_Detalhado.docx` | Detalhe de A1–A4 com fórmula | Secundário |
| 8 | `Oticas_Camada_Financeira_C2.docx` | Uplift, aprovação | Secundário |
| 9 | `Oticas_Concentradora_Compras.docx` | Economia, adesão, volume | Secundário |
| 10 | `SPEC_Fase_B_Formulas_Avancadas.md` | GMROI, attach, corrosão, ABC, follow-on **implementados** | Secundário |
| 11 | `Consultoria.xlsx` › aba `Gabarito` | 37 anomalias com resultado esperado — **a régua de veracidade** | Verificação |

### Lacunas conhecidas antes de começar

| Bloco | Situação |
|---|---|
| Comercial (SEV, TMI, índices) | ✅ Coberto |
| Metas / Pace / EDN / Elasticidade | ✅ Coberto (só no Arsenal) |
| Margem em 5 níveis | ✅ Coberto (só no Arsenal) |
| Base de clientes (A1–A4) | ⚠️ Disperso no Playbook, sem bloco próprio |
| Estoque (giro, GMROI, ABC, morto) | ⚠️ Disperso entre Playbook v9 e SPEC Fase B |
| **Fiscal (DAS, faixa, RBT12, tributo)** | 🔴 **Não existe em nenhum arquivo** |
| **Financeiro (fluxo, DRE, resultado)** | 🔴 **Não existe em nenhum arquivo** |

As duas linhas vermelhas confirmam o diagnóstico anterior: **a base de homologação não pode ser gerada contra fórmulas que ainda não foram escritas.**

---

## 5. Fila de decisão — abertos

| # | Item | Evidência | Impacto |
|---|---|---|---|
| **1** | Qual `EXRS_Spec_Laudo_Executivo_v4.md` é a lei? | Vault 12,2 KB (19/07) × laudo_executivo 26,1 KB (21/07) | Duas "leis" com a mesma versão |
| **2** | `Playbook_Entrega_Elysian_v1.docx` é histórico ou vigente? | Está em `Historico/`, tratado como documento-mãe | Define a anatomia de fase e os Gates |
| **3** | Vetor de pesos do estágio **Construção** | `Score_Formula` e `Arsenal` = 0,25/0,25/0,20/0,20/0,10 · `Playbook_v9` = 0,30/0,25/0,20/0,15/0,10 | Muda todo SEV calculado |
| **4** | `Doutrina-Sandeep` é doutrina (D) ou infra de agente (I)? | 8 arquivos + 2 system-prompts, sem citação cruzada | Define se entra na extração |
| **5** | Escrever os blocos **Fiscal** e **Financeiro** | Não existem | Bloqueia 1/3 da base de homologação |

---

*Fase 0 encerrada. Próximo artefato: `ESQUEMA_PECA.md` — o contrato de extração.*
