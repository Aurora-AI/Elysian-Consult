[INCORPORADO]
# Metodologia Consolidada — Aurora / Framework Elysian / Óticas

> Consolidação de todo o material de metodologia de consultoria encontrado na pasta `Documentos Gerais`. Especificações técnicas do produto EXRS, prompts de IA e arquivos de infraestrutura foram deixados de fora — ver `indice_fontes.md` para o mapa completo, incluindo esses itens.

---

## Parte 1 — O Framework Elysian: a teoria-mãe

A Aurora vende "arquitetura de receita", não software. A tese central do Framework Elysian é usar IA para eliminar o trabalho braçal das operações comerciais e liberar o humano para a única coisa que não se comoditiza: a confiança (`Analise_Estrategica_Framework_Elysian.docx`).

O núcleo teórico do método está no **Módulo 0 — Fundação** (`PBM_Modulo_0_Fundacao.docx`): não é um manual de passos, é o motor que ensina o consultor a transformar qualquer processo intuitivo em previsível — e a partir daí derivar novas ferramentas sozinho. A ideia central em uma frase: *"Determinismo não é eliminar o humano. É eliminar a variabilidade onde ela é desperdício."* A ordem de construção do método é deliberada e proposital: teoria primeiro, depois as ferramentas, depois testes simulados, e só então testes no cliente real — "construímos o gerador antes das peças."

O primeiro módulo operacional derivado dessa teoria é o **Portão de Dupla Trilha** (`PBM_Modulo_2-1_Portao_Dupla_Trilha.docx`), validado no caso AçoForte Sul: a reengenharia da qualificação de leads na Fase 2. No modelo antigo, cinco fatores decidiam *se* o lead entrava; no modelo correto, os mesmos cinco fatores decidem *para onde* ele vai — Balcão, Desenvolvimento ou Consultiva, cada trilha servida por um perfil humano diferente e triada por uma camada de máquina. O princípio evita dois erros simétricos: rejeitar a base (jogar a empresa no "mar vermelho" da briga por cliente novo) e não segmentar o atendimento por potencial real do lead.

A entrega do método ao cliente segue o **Playbook de Entrega Elysian v1.0** (`Playbook_Entrega_Elysian_v1.docx`), o "documento-mãe" da metodologia de entrega: como conduzir um cliente da assinatura ao sistema instalado, na ordem exata, com a ferramenta certa e o porquê de cada decisão. Cada fase segue a mesma anatomia — Objetivo → Inputs → Passo a passo → Julgamento → Ferramentas → Entregável → **Gate** — e o documento é explícito que pular um Gate é "a causa raiz de quase todo projeto que dá errado". A distinção entre o passo a passo (o *que* fazer) e o julgamento (o *porquê* e *quando* abrir exceção) é central: segundo o próprio documento, um júnior que só executa os passos entrega 70% do resultado; quem entende o porquê entrega 100%.

O caminho de construção desse arsenal está documentado em `Roteiro_Construcao_Playbook_Master.docx`, que analisa três documentos-base pré-existentes como um "triângulo completo em teoria e incompleto em execução" — cada um respondendo uma pergunta diferente (teoria, cronograma, realidade de mercado), faltando a "musculatura" de ferramentas e templates executáveis.

### Configuração por frente de mercado

O motor Elysian se reconfigura para quatro frentes de negócio — B2C, B2B, Indústria e Governo — segundo cinco eixos que as diferenciam: ciclo de venda, grau de toque humano, o que ganha o negócio, onde mora a recorrência/margem, e quem decide a compra (`Modelos_Comerciais_2026.docx`). O documento `PBM_Config_Motor_por_Frente.docx` traduz esses achados em parâmetros concretos de configuração do motor — trilha, ponto de decisão humana, o que vira sinal, e quais travas determinísticas evitam a "autodestruição" do processo — a partir da pesquisa "Estratégia GTM para PMEs Brasileiras". Um padrão comum às quatro frentes: em todas elas alguém "sequestra" o dado do cliente (o marketplace no B2C, o distribuidor no industrial, a falta de dado de intenção no B2B, a dispersão em portais públicos no governo), e a primeira configuração do motor é sempre "onde reconquistar o dado".

*[Nota de rastreabilidade: `Modelos_Comerciais_2026.docx` e `PBM_Config_Motor_por_Frente.docx` cobrem a mesma matriz de quatro frentes sob ângulos diferentes — briefing comercial vs. parâmetros de motor. Não foi possível, nesta síntese, confirmar se os dois estão de fato alinhados campo a campo; ver observação no índice de fontes.]*

### Base teórica de pesquisa (insumo externo)

Duas pesquisas extensas fundamentam o Framework Elysian, mas são material de pesquisa/insumo, não metodologia proprietária da Aurora:

- **`Metodologias de Vendas Pós-IA.md`** argumenta que o mercado B2B atingiu saturação crítica: a IA generativa democratizou prospecção e conteúdo, inundando o ecossistema de "ruído sintético" e derrubando a taxa mediana de vitórias (win rate) para 19%. O comprador corporativo tornou-se imune ao outbound puramente algorítmico.
- **`Estratégia GTM para PMEs Brasileiras.md`** aplica essa lógica ao contexto de PMEs do Sul do Brasil (Paraná/Santa Catarina), sob condições macro específicas: juros altos, 67% das tentativas de captação de crédito frustradas, e a fase experimental da Reforma Tributária (IBS/CBS).
- **`Go Live Elysian Consult.md`** cita literatura de HBS, Columbia e Stanford somada a dados do SEBRAE para propor quatro teses de GTM/RevOps que devem orientar o lançamento da consultoria em 2026, com destaque para a mudança de "Consultor de Processos" para "Go-to-Market Engineer".

### Ressalva estratégica em aberto

A consultoria externa registrada em `Analise_Estrategica_Framework_Elysian.docx` valida a arquitetura conceitual do Elysian como à frente de 95% das consultorias comerciais brasileiras, mas aponta um risco de fundo: toda a base teórica foi importada do universo SaaS/enterprise americano (Winning by Design, Clari, Gong, modelo bow-tie, NRR de 110–130%, comitês de 6–10 pessoas, deals de US$250 mil) — um contexto muito diferente do cliente real da Aurora, uma PME de varejo ou B2B tradicional em Curitiba ou Joinville, frequentemente sem CRM e sem receita recorrente estabelecida. Esse ponto ainda não aparece respondido explicitamente nos demais documentos do framework lidos nesta síntese — fica registrado como tensão em aberto, não resolvida silenciosamente aqui.

*(Não foi possível incorporar `Método Aurora_ Estratégia e Fosso Competitivo.pdf` a esta síntese — as 13 páginas do PDF não retornaram texto extraível por ferramentas automáticas; provavelmente é um PDF escaneado/de imagem. Ver índice de fontes.)*

---

## Parte 2 — O Playbook Óticas: metodologia aplicada ao Cliente #1

O primeiro cliente de aplicação prática do Framework Elysian é uma rede independente de três óticas, com proprietário único. A referência vigente e mais completa é o **Playbook Operacional v9 Master** (`Oticas_Playbook_v9_Master.docx`), que integra oito partes complementares (A a H) e substitui a versão v6 anterior. A promessa central do documento: "extrai inteligência do dado morto, transforma em roteiro diário, gira o estoque como moda em dois relógios de recompra, blinda o caixa com crédito sem risco, e mapeia a performance individual como radar de desenvolvimento — nunca como vigilância."

### A. Caixa de ferramentas analíticas (diagnóstico)

O ponto de partida é a base de clientes existente — "o dado morto". Quatro ferramentas centrais (detalhadas com fórmula em `Oticas_Playbook_Operacional_Detalhado.docx`):

- **Completude de cadastro**: % preenchido por campo (telefone/CPF/exame); se insuficiente, o diagnóstico pivota para o lado de estoque.
- **RFM**: pontuação 1–5 por Recência, Frequência e Valor, segmentando a base em quintis (Campeões, Fiéis, Em risco, Perdidos), alimentando o "Mapa da Mina".
- **Churn Invisível**: em vez de usar benchmark de mercado, deriva o ciclo de recompra da própria base (mediana dos "vitais" do cliente) — um cliente está em churn quando (hoje − última compra) supera 1,5× esse ciclo.
- **Receita Latente**: calcula o "attach rate" por categoria (% de clientes de uma categoria que também têm outra) e converte a base sem aquele produto em fila de cross-sell.

Esse diagnóstico gera o "choque do Dia 5" — o momento em que o dono da ótica vê, pela primeira vez, o tamanho da receita que está deixando na mesa.

### B. O motor de recompra de dois relógios (o moat)

O núcleo conceitual do método (`Oticas_Motor_Dois_Relogios.docx`) parte de uma inversão de categoria: "óticas é moda disfarçada de saúde". Um único relógio (o ciclo de troca por necessidade médica, hoje acima de 15 meses) não comprime o intervalo de recompra — a graduação muda quando muda, não antes. A alavanca é ligar um segundo relógio, o da moda: o óculos deixa de ser só necessidade médica e passa a ser acessório de guarda-roupa, trocado por estação/coleção (o modelo "Chilli Beans", nova coleção a cada 40 dias).

O motor cobre duas populações, não apenas quem já comprou:
- **Base (comprou)**: entra nos dois relógios de recompra.
- **Pendentes (deu dados, não comprou)**: entra num track específico de conversão da primeira venda, tratando o "não compre antes de me ligar" como pipeline em vez de venda perdida.

### C. Adoção e cultura (a adesão da equipe)

`Oticas_Adocao_e_Cultura.docx` resolve um ponto explicitamente identificado como fraqueza em versões anteriores do playbook (o "vago mapeamento cultural/shadowing"): a tropa de vendedores tem dois eixos de avaliação, não um. O documento detalha como medir a qualidade do vendedor, como identificar e conquistar o líder informal da equipe, e — o ponto central — como fazer o vendedor *querer* cadastrar o cliente, em vez de tratar o cadastro como tarefa imposta. O método foi adaptado de treinamento de crédito próprio já usado pela Aurora.

### D–E. Cronograma e cockpit

O playbook estrutura a execução em uma linha do tempo do Dia 1 ao Dia 30+ (Parte D), com um "Cockpit" de KPIs para o painel do dono, referido internamente como "Chronos" (Parte E). O detalhamento de "como fazer" cada etapa da linha do tempo — método, fórmula e ferramenta associados — está em `Oticas_Playbook_Operacional_Detalhado.docx`.

### F. Arquitetura de performance individual (o Score de Engenharia de Venda)

A Parte F organiza a avaliação de performance do vendedor em uma "arquitetura de três camadas com governança", detalhada em três documentos satélite que se complementam:

1. **`Oticas_ParteF_Score_Formula.docx`** define cinco índices normalizados por vendedor (camada 1, motor determinístico).
2. **`Oticas_ParteF_TMI.docx`** detalha como derivar o Ticket Médio Ideal (TMI), componente central do Índice de Ticket (IT = TMR ÷ TMI × 100). O documento é explícito sobre dois erros a evitar ao calcular o TMI: usar a média simples da própria loja (o que "premia a mediocridade" ao tomar o histórico como teto) ou ignorar o gap entre o que a loja historicamente consegue e o que o negócio efetivamente precisa.
3. **`Oticas_ParteF_Blindagem_SEV.docx`** generaliza, para os demais índices (IC, IA, IR, IAd), a correção estrutural testada primeiro no TMI: normalizar cada índice contra um alvo derivado do próprio dado, não contra a taxa crua — porque um attach rate de 30%, por exemplo, pode ser excelente numa loja e ruim em outra dependendo do mix de produto.

O documento reforça, em mais de um ponto do material, que essa arquitetura de performance deve funcionar como radar de desenvolvimento do vendedor, nunca como ferramenta de vigilância ou punição — a governança do "painel por bandas" e "escada de 3 modos" evita que o score vire arma disciplinar.

### G–H. SEV/TMI em detalhe e mapa de aplicação

A Parte G aprofunda as fórmulas de comportamento e a engenharia do ticket ideal (coberta pelos três documentos da Parte F acima). A Parte H — `Oticas_Mapa_Aplicacao_Formulas.docx` — é a camada de instrução final: para cada fórmula do sistema, define onde (fase/momento do processo), quando (gatilho e cadência), por quem, e a que outra parte do sistema ela se liga. O objetivo declarado é tornar o material autossuficiente, a ponto de um consultor novo — ou um agente de IA — conseguir aplicar cada fórmula sem precisar do contexto da conversa original em que foi criada.

### Camadas de negócio complementares

Duas frentes de negócio adjacentes ao motor de recompra, com arquitetura própria:

- **Camada Financeira / Crédito Risco Zero (C2)** (`Oticas_Camada_Financeira_C2.docx`): a Aurora viabiliza parcelamento/crediário para a ótica sem que ela precise assumir risco de crédito ("virar banco"), atuando como arquiteta financeira que negocia e conecta parceiros (emissores de cartão, plataformas de crediário), monetizando diretamente com esse painel de fornecedores financeiros — com o dado da transação retornando ao motor.
- **Concentradora de Compras** (`Oticas_Concentradora_Compras.docx` e, em versão de pitch, `Oticas_A_Vantagem_Injusta.docx`): parceria com "Marcos" para agregar pedidos de várias óticas independentes e romper a barreira de acesso/preço das marcas premium. O ponto estratégico central, repetido nos dois documentos sob ângulos diferentes, é a separação clara entre o que a concentradora de compras entrega (acesso e preço — a "isca" de impacto imediato) e o que só a Aurora entrega sozinha, sem depender do parceiro (o motor de venda e recorrência sobre a base já existente do cliente) — essa segunda parte é o que sustenta a posição da Aurora como sócio, e não acessório de uma central de compras.

### Comunicação do método

O mesmo conteúdo do playbook técnico existe em duas outras camadas de comunicação, sem adicionar substância nova:

- `Oticas_Metodo_Linguagem_Simples.docx` reescreve a metodologia inteira para público leigo, removendo as fórmulas e mantendo o raciocínio.
- `Oticas_Apresentacao_Texto.docx` e `Oticas_Apresentacao_Consultoria.pptx` (o segundo é a versão em slides, com notas do apresentador, do primeiro) apresentam a proposta de experiência do cliente na ótica sob o título "A ótica que o cliente não esquece" — material de posicionamento comercial voltado à venda da consultoria, não ao detalhamento operacional.

---

## Resumo da relação entre as duas partes

O Playbook Óticas (Parte 2 deste documento) é a primeira aplicação prática, documentada e testada em campo, do Framework Elysian (Parte 1). O Módulo 0 (Fundação) do Elysian é a teoria que justifica por que o motor de Óticas é construído como é — determinístico, derivável, com Gates de fase — e o Portão de Dupla Trilha (módulo genérico do Elysian) é o mesmo princípio de roteamento por potencial que aparece, em versão especializada para o nicho, na segmentação Base/Pendentes do Motor de Dois Relógios. A relação inversa também vale: os achados táticos do caso Óticas (ex. a lógica de normalizar índices contra alvo derivado do dado, não taxa crua) são candidatos naturais a subirem de volta para o Módulo 0 como princípio geral do framework — mas essa generalização não está documentada explicitamente em nenhum arquivo lido nesta síntese, e não deve ser presumida.

---

*Fontes: ver `indice_fontes.md` para a lista completa dos 57 arquivos da pasta, incluindo os itens de infraestrutura do produto EXRS, prompts de IA, gabaritos de teste e planilhas de dados que foram deliberadamente deixados fora desta síntese de metodologia.*
