# Changelog

## [1.2] — 2026-10-11

### Alterado
- Guia reestruturado para uma abordagem Telegram-first.
- Comandos e correções cotidianas apresentados a partir do chat do Telegram.
- Separação explícita entre comandos `/...`, pedidos em linguagem natural e administração fora do Telegram.

### Adicionado
- Mapa dos comandos efetivamente disponíveis no gateway de mensagens.
- Fluxos copiáveis para pesquisa, arquivos, repositórios, cron e diagnóstico.
- Recuperação em duas camadas: bot responsivo e bot inacessível.
- Matriz de erros com primeira ação no Telegram e escalonamento administrativo.

### Precisão operacional
- `/cron`, `/tools`, `/config` e pesquisa/instalação de skills identificados como superfícies CLI; no Telegram, operações equivalentes são solicitadas em linguagem natural quando a ferramenta está habilitada.
- Telegram-first não é apresentado como Telegram-only: falhas do gateway, servidor, rede ou token exigem canal administrativo externo.

## [1.1] — 2026-10-11

### Adicionado
- Tutorial passo a passo em português brasileiro.
- Conceitos de SSH, servidor, VPS, URL, Git, GitHub, API, modelos, provedores e contexto.
- Capítulos sobre tools, skills, SOUL.md, memória, MemPalace, perfis, MCP, delegação, gateway e cron.
- Matriz de troubleshooting baseada na documentação oficial.
- PDF reproduzível, validador determinístico e CI.

### Precisão conceitual
- MemPalace identificado como extensão específica, não como recurso nativo oficial do Hermes.
- Diferenciação entre modelo, provedor, ferramenta, skill, perfil, MCP e gateway.
