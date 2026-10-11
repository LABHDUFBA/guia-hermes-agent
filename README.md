# Guia Hermes Agent do LABHDUFBA

**Versão 1.1 — outubro de 2026**

Tutorial passo a passo, em português brasileiro, para pesquisadores e estudantes das Ciências Humanas começarem a usar o [Hermes Agent](https://hermes-agent.nousresearch.com/docs) — o agente de IA autônomo de código aberto desenvolvido pelo [Nous Research](https://nousresearch.com).

> **Aviso.** Este guia é um material educacional do Laboratório de Humanidades Digitais da UFBA (LABHD-UFBA). Ele não substitui a [documentação oficial](https://hermes-agent.nousresearch.com/docs), sempre atualizada. Verifique a versão do seu Hermes com `hermes --version` antes de seguir qualquer instrução.

## Para quem é este guia

Este tutorial foi escrito para pessoas que:

- nunca usaram um agente de IA autônomo;
- pertencem às Ciências Humanas e Sociais;
- precisam compreender conceitos como SSH, servidor, VPS, API, GitHub e modelos de IA antes de usar o Hermes;
- querem usar o Hermes como ferramenta de pesquisa — leitura, análise de dados, escrita, automação.

## O que você vai aprender

Ao final deste guia, você será capaz de:

1. instalar e configurar o Hermes Agent;
2. escolher um provedor e um modelo de IA;
3. usar ferramentas, skills e memória;
4. configurar um bot no Telegram;
5. agendar tarefas com cron;
6. diagnosticar e resolver problemas comuns.

## Onde encontrar tudo

| Recurso | Endereço |
|---|---|
| Documentação oficial | https://hermes-agent.nousresearch.com/docs |
| Repositório do projeto | https://github.com/NousResearch/hermes-agent |
| Repositório deste guia | https://github.com/LABHDUFBA/guia-hermes-agent |
| Laboratório | https://labhdufba.github.io |

## Licença

O texto deste guia está licenciado sob [Creative Commons Atribuição 4.0 Internacional (CC BY 4.0)](https://creativecommons.org/licenses/by/4.0/). Você pode copiar, adaptar e distribuir, desde que atribua a fonte.

O Hermes Agent é software livre sob licença MIT.

## Como contribuir

Este é um guia evolutivo. Para sugerir correções ou acréscimos:

1. Abra uma *issue* no repositório descrevendo o problema ou a sugestão.
2. Envie um *pull request* com a alteração proposta.
3. Indique sempre a versão do Hermes testada (`hermes --version`) e a página oficial de referência.

## Versões

| Versão | Data | Mudanças principais |
|---|---|---|
| 1.0 | out/2026 | rascunho inicial |
| 1.1 | out/2026 | instalação, conceitos, troubleshooting, glossário e PDF |