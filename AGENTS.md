# AGENTS.md — Doutrina ElysianConsult

> **Domínio Soberano:** Consultoria e Estratégia (ElysianConsult)
> Este repositório é um domínio vertical isolado da Fábrica Aurora.

## 1. Regras de Domínio (Domain Sovereignty)
- **NÃO** importar arquivos físicos da Fábrica (`C:\Projetos\Aurora\docs`, etc) nem do motor EXRS (`AuroraControler`) por caminho relativo (`../`).
- Todo consumo de inteligência, LLM ou ferramenta externa deve ser feito via **API Tipada** ou pacote npm/uv publicado pela Fábrica.
- O material contido neste repositório representa a propriedade intelectual, laudos, estratégias e diagnósticos dos clientes da consultoria. PII (dados de clientes) não devem vazar para logs em plaintext.

## 2. Herança da Fábrica
Os agentes executando neste repositório operam sob as leis da Constituição Aurora v9.0.
A doutrina global é importada e deve ser respeitada em sua totalidade (ver `C:\Projetos\Aurora\AGENTS.md`).

## 3. Sandboxing de Skills
Qualquer nova skill desenhada especificamente para fluxos de consultoria deve nascer na pasta `Sandbox/` deste repositório. Só será promovida para o eixo cognitivo global (`aurora-agents/`) após auditoria e OS do Comandante.
