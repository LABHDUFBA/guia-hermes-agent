---
title: "Guia Hermes Agent do LABHDUFBA"
subtitle: "Instalação, conceitos fundamentais, práticas de pesquisa e resolução de problemas"
author: "Laboratório de Humanidades Digitais da UFBA — LABHD-UFBA"
date: "Versão 1.1 · outubro de 2026"
lang: pt-BR
---

<div class="title-block">
  <img src="assets/labhdufba_logo_oficial.png" alt="Marca do LABHDUFBA" />
  <div class="kicker">LABORATÓRIO DE HUMANIDADES DIGITAIS DA UFBA</div>
  <h1>Guia Hermes Agent</h1>
  <p class="subtitle">Instalação, conceitos fundamentais, práticas de pesquisa e resolução de problemas</p>
  <p class="version">Versão 1.1 · outubro de 2026</p>
  <p class="license">Material aberto sob licença CC BY 4.0</p>
</div>

# Como usar este guia

Este é um guia progressivo. Não é preciso dominar todos os conceitos antes de conversar com o Hermes. O percurso recomendado é:

1. entender onde o Hermes vai rodar;
2. instalar e configurar um provedor;
3. fazer uma primeira tarefa verificável;
4. aprender a usar ferramentas e skills;
5. só depois configurar automações, MCP, servidores e múltiplos agentes.

> **Princípio de segurança:** antes de aceitar uma ação do agente, pergunte: *em qual máquina isso ocorrerá, quais dados serão enviados, o que será alterado e como posso verificar o resultado?*

## Convenções deste manual

- Blocos com `>` são comandos para o **terminal** (shell), não mensagens para o chat.
- Comandos que começam com `/` são digitados **dentro de uma conversa Hermes**.
- Campos entre `< >` devem ser substituídos por valores seus; não copie os sinais de menor/maior.
- Nunca publique chaves de API, senhas, tokens de bot ou chaves SSH.

---

# 1. Antes de instalar: onde o Hermes vai rodar?

O Hermes pode rodar no seu computador ou em uma máquina remota. A decisão altera custo, privacidade, disponibilidade e dificuldade de manutenção.

## 1.1 Computador local

É o caminho mais simples para começar. Você instala o Hermes no notebook ou desktop e o usa no terminal ou no aplicativo Desktop.

**Vantagens:** controle direto, menos infraestrutura, bom para aprender.

**Limites:** o agente para quando a máquina está desligada; tarefas agendadas e bots não ficam disponíveis continuamente.

## 1.2 Servidor e VPS

Um **servidor** é um programa que atende solicitações ou, no uso cotidiano, a máquina que executa programas continuamente. Uma **VPS** (*Virtual Private Server*) é uma máquina virtual alugada em um data center.

Pense numa VPS como uma sala alugada em um prédio: ela é sua área de trabalho virtual, mas precisa de configuração, atualizações e cuidados de segurança.

Uma VPS é útil quando você quer:

- manter um bot do Telegram ativo 24 horas;
- executar cron jobs mesmo com o notebook desligado;
- trabalhar remotamente a partir de qualquer computador.

> **Não confunda:** colocar o Hermes numa VPS não torna o modelo de IA automaticamente local. O Hermes pode estar numa VPS e ainda enviar pedidos para um provedor remoto de modelos.

## 1.3 SSH: a porta segura para a máquina remota

**SSH** (*Secure Shell*) é um protocolo que permite acessar outra máquina por uma conexão criptografada, geralmente pelo terminal.

Exemplo:

```bash
ssh <usuario>@<ip-ou-dominio>
```

Se você recebeu um servidor, o provedor costuma informar:

- endereço IP ou domínio;
- nome de usuário;
- senha temporária ou chave SSH;
- porta, se não for a padrão.

**Boa prática:** prefira chaves SSH a senhas. A chave privada fica no seu computador e nunca deve ser enviada por e-mail, WhatsApp, GitHub ou chat.

## 1.4 URL, domínio e caminho local

- **URL:** endereço de um recurso na web, como `https://hermes-agent.nousresearch.com/docs`.
- **Domínio:** parte identificadora de um endereço, como `hermes-agent.nousresearch.com`.
- **Caminho local:** endereço de um arquivo na máquina, como `/home/ana/projeto/README.md`.

Uma URL indica onde procurar um recurso na internet. Ela não garante que o conteúdo esteja disponível, seja verdadeiro, esteja atualizado ou possa ser acessado sem login.

**Checkpoint 1.** Antes de avançar, você deve conseguir responder: *vou instalar no meu computador ou em uma VPS? Se for uma VPS, sei usar SSH ou tenho alguém responsável pela infraestrutura?*

---

# 2. Instalação do Hermes Agent

A documentação oficial oferece instaladores diferentes conforme o sistema operacional. Consulte sempre a página [Installation](https://hermes-agent.nousresearch.com/docs/getting-started/installation).

## 2.1 Linux, macOS ou WSL2

No terminal, execute:

```bash
curl -fsSL https://hermes-agent.nousresearch.com/install.sh | bash
```

Ao terminar, recarregue o shell:

```bash
source ~/.bashrc
```

Em computadores com zsh, use:

```bash
source ~/.zshrc
```

Depois confira:

```bash
hermes --version
```

## 2.2 Windows nativo

Abra o PowerShell e execute:

```powershell
iex (irm https://hermes-agent.nousresearch.com/install.ps1)
```

No macOS e Windows, o aplicativo Hermes Desktop também é uma opção recomendada pela documentação oficial. Baixe apenas a partir do site oficial.

## 2.3 O que o instalador faz?

O instalador prepara o ambiente do Hermes, incluindo o runtime necessário e ferramentas usuais. Isso não significa que todos os serviços externos — modelos, bots, APIs ou MCPs — já estarão configurados.

A instalação é apenas o primeiro passo.

## 2.4 Primeiro diagnóstico

Rode:

```bash
hermes doctor
```

O comando verifica configuração e dependências. Leia o diagnóstico antes de usar `--fix`: corrigir automaticamente altera o ambiente.

> **Ação com efeito:** `hermes doctor --fix` tenta corrigir problemas. Use apenas depois de entender a recomendação.

---

# 3. Primeiro uso: um chat verificável

Abra o Hermes:

```bash
hermes
```

Ou use uma pergunta única em um script:

```bash
hermes -z "Explique, em três frases, o que é Sociologia Digital."
```

A primeira conversa deve ser simples. Não configure Telegram, cron ou MCP antes de confirmar que o agente consegue responder normalmente.

## 3.1 Uma atividade inicial de pesquisa

Cole um trecho curto de texto público e solicite:

> Faça uma síntese em até 120 palavras. Separe: (1) uma citação literal; (2) uma interpretação; (3) algo que o trecho não permite concluir. Não use fontes externas.

Depois, confira a citação no texto original.

Esse exercício ensina uma regra decisiva: uma resposta fluente não é, por si só, uma resposta verificável.

**Checkpoint 2.** Você avançou se consegue distinguir citação, síntese, inferência e informação não confirmada.

---

# 4. Modelo, provedor, API, contexto e tokens

## 4.1 Modelo não é provedor

Um **modelo** é o sistema de IA que processa entradas e produz saídas. Um **provedor** é o serviço que oferece acesso a um ou mais modelos.

Exemplos de provedores incluem Nous Portal, OpenAI, Anthropic, Google, OpenRouter, serviços especializados e endpoints locais compatíveis com OpenAI.

O Hermes não é um modelo. Ele combina modelo, instruções, ferramentas, memória e um ciclo de execução.

## 4.2 Configurando um provedor

No terminal, fora do chat, execute:

```bash
hermes model
```

Esse assistente configura provedores, autenticação, modelos e endpoints. Para uma instalação nova, a documentação oficial indica como caminho simples:

```bash
hermes setup --portal
```

Dentro de uma conversa, `/model` serve para alternar entre provedores e modelos **já configurados**. Ele não substitui a configuração inicial de credenciais.

> **Segurança:** chaves de API devem ficar no arquivo `.env` do Hermes, nunca em um repositório, print de tela ou mensagem de chat.

## 4.3 API: uma interface entre programas

Uma **API** é uma interface com regras para um programa solicitar operações a outro. Uma chave de API é uma credencial de acesso — não é a API, nem é uma senha para compartilhar.

Em uma configuração típica:

```text
Você → Hermes → API do provedor → modelo → resposta
```

## 4.4 Contexto

O **contexto** é o material que o modelo recebe em uma chamada: instruções, mensagens anteriores, documentos enviados e resultados de ferramentas.

Uma analogia útil é uma mesa de trabalho com espaço limitado. O contexto não contém automaticamente toda a internet, todos os seus arquivos ou todas as conversas anteriores.

## 4.5 Tokens

**Tokens** são unidades usadas pelos modelos para representar texto. Podem corresponder a uma palavra inteira, parte de uma palavra ou pontuação. Servem para medir limites de contexto e, frequentemente, custos.

Não confunda:

- **token de texto:** unidade de processamento do modelo;
- **token de acesso:** credencial de API, bot ou serviço.

## 4.6 Tipos de modelos: três eixos

Não existe uma única classificação. Separe três perguntas:

1. **Capacidade:** trabalha com texto, imagens, áudio, vídeo, código ou várias modalidades?
2. **Local de execução:** roda no seu hardware ou em um serviço remoto?
3. **Disponibilidade:** os pesos são acessíveis, fechados, ou disponibilizados sob licença específica?

“Local”, “multimodal” e “aberto” não são categorias rivais: um modelo pode ser local e multimodal; outro, remoto e fechado.

## 4.7 Custos

O Hermes Agent é software livre. O uso de modelos e ferramentas externas pode gerar custos do provedor, de uma assinatura, de infraestrutura ou de APIs adicionais.

Antes de automatizar tarefas, verifique:

- qual provedor está ativo;
- como ele cobra;
- qual modelo está selecionado;
- que ferramentas externas têm custo próprio;
- se há limites de uso ou rate limits.

---

# 5. Ferramentas e toolsets

## 5.1 O que são ferramentas?

Ferramentas (*tools*) são funções que o agente pode executar: ler arquivos, pesquisar na web, usar o terminal, criar documentos ou chamar serviços externos.

Uma ferramenta pode produzir efeitos reais. “O agente sabe como fazer” é diferente de “o agente executou e verificou”.

## 5.2 O que são toolsets?

**Toolsets** são conjuntos de ferramentas. Eles controlam o que fica disponível em uma sessão, plataforma ou tarefa.

Exemplo de sessão com ferramentas delimitadas:

```bash
hermes chat --toolsets web,file,terminal
```

Para configurar ferramentas por plataforma, use:

```bash
hermes tools
```

Dentro do chat, quando disponível:

```text
/tools list
```

Habilitar um toolset não instala dependências, não cria credenciais e não garante que uma ferramenta específica possa funcionar. Algumas dependem de chaves, plugins, navegador, serviço externo ou permissões.

## 5.3 Uma regra para tarefas sensíveis

Ao pedir uma ação ao Hermes, explicite:

- objetivo;
- dados permitidos;
- destino do resultado;
- se pode apenas ler ou também alterar;
- como você quer verificar a entrega.

Exemplo:

> Leia apenas estes três PDFs locais. Produza um resumo com citações de página. Não envie arquivos nem escreva em serviços externos. Salve o resultado em `resumo.md` e me mostre o caminho final.

---

# 6. Skills: procedimentos reutilizáveis

Uma **skill** é um procedimento reutilizável, normalmente descrito em um arquivo `SKILL.md` e, às vezes, acompanhado de referências, scripts ou modelos.

Pense numa skill como um protocolo de laboratório: ela ensina o agente a executar uma classe de tarefa com método, verificações e cuidados próprios.

## 6.1 Skills não são ferramentas

- Uma **ferramenta** executa uma ação.
- Uma **skill** orienta como usar ferramentas para uma tarefa.
- Uma skill não treina novamente o modelo.
- Uma skill não concede, por si só, permissões ou credenciais.

## 6.2 Comandos úteis

```bash
hermes skills list
hermes skills search <tema>
hermes skills inspect <identificador>
```

Para instalar uma skill, use fontes confiáveis e leia o conteúdo antes de permitir que ela execute comandos ou use credenciais.

Depois de adicionar ou remover skills durante uma conversa, use:

```text
/reload-skills
```

## 6.3 Skill de projeto versus skill geral

Uma skill geral serve a muitos projetos. Instruções específicas de um repositório devem ficar em `AGENTS.md` ou em outro arquivo de contexto do projeto.

Não transforme regras temporárias, segredos ou caminhos pessoais em skills públicas.

---

# 7. SOUL.md, arquivos de contexto e personalidade

## 7.1 SOUL.md

`SOUL.md` define a identidade persistente do Hermes: tom, estilo, grau de detalhe e postura diante da incerteza.

No perfil padrão, o arquivo fica em:

```text
~/.hermes/SOUL.md
```

Em um perfil específico, ele fica dentro do `HERMES_HOME` daquele perfil.

Use `SOUL.md` para orientações estáveis, por exemplo:

```markdown
# Estilo
- Responda em português brasileiro.
- Priorize precisão e indique incertezas.
- Prefira respostas estruturadas e concisas.
```

Não use `SOUL.md` para regras de um único projeto, portas de servidor, convenções de código ou segredos.

## 7.2 AGENTS.md

Use `AGENTS.md` para regras do projeto: como testar, onde salvar resultados, padrões de escrita, convenções de dados e limitações de escopo.

Regra prática:

- se deve acompanhar o agente em qualquer conversa, use `SOUL.md`;
- se pertence a um projeto, use `AGENTS.md`.

## 7.3 Personalidades temporárias

Dentro do chat, `/personality` aplica um modo de conversa. Exemplo:

```text
/personality teacher
```

Para retornar à identidade de base:

```text
/personality none
```

---

# 8. Memória, histórico e MemPalace

## 8.1 Memória nativa do Hermes

O Hermes possui memória embutida, pequena e curada, em arquivos como:

```text
~/.hermes/memories/MEMORY.md
~/.hermes/memories/USER.md
```

- `MEMORY.md`: fatos sobre ambiente, convenções e aprendizados.
- `USER.md`: preferências e informações estáveis da pessoa usuária.

Memória não é transcrição completa de conversas, nem arquivo ilimitado, nem treinamento do modelo.

Para verificar a configuração de provedores externos de memória:

```bash
hermes memory status
```

## 8.2 Histórico de sessões

Conversas passadas pertencem ao histórico de sessões. Elas não entram automaticamente no contexto do modelo a cada nova conversa.

```bash
hermes sessions list
```

## 8.3 MemPalace

**MemPalace não é um componente nativo documentado do Hermes Agent.** Neste guia, o termo designa uma extensão ou configuração específica de um perfil, que pode ter seu próprio banco, interface ou integração por MCP.

Portanto:

- não suponha que toda instalação Hermes possui MemPalace;
- não confunda MemPalace com `MEMORY.md`/`USER.md`;
- documente separadamente a configuração, armazenamento e política de privacidade dessa extensão.

## 8.4 O que deve — e não deve — ir para a memória

Guarde fatos estáveis e úteis em várias sessões: preferência de idioma, convenções de projeto, ambiente recorrente.

Não guarde: senhas, chaves de API, tokens, dados pessoais de terceiros sem necessidade ou tarefas temporárias.

---

# 9. Perfis: agentes separados, não sandboxes

Um **perfil** é uma área de estado separada do Hermes. Cada perfil pode ter seu próprio `config.yaml`, `.env`, `SOUL.md`, memória, skills, sessões, cron e banco de estado.

Criar um perfil:

```bash
hermes profile create pesquisa
```

Usar esse perfil em uma execução:

```bash
hermes -p pesquisa chat
```

Listar perfis:

```bash
hermes profile list
```

> **Atenção:** perfil não é sandbox. Ele separa o estado do Hermes, mas não impede automaticamente que o agente acesse os mesmos arquivos do sistema. A pasta de trabalho é definida separadamente por `terminal.cwd`; o isolamento depende do backend e das permissões.

Use perfis quando quiser evitar mistura de contextos, por exemplo:

- perfil pessoal;
- perfil de pesquisa;
- perfil de laboratório;
- perfil de bot público;
- perfil de desenvolvimento.

---

# 10. MCP: conectando ferramentas externas

**MCP** significa *Model Context Protocol*. É um padrão para conectar agentes de IA a servidores que oferecem ferramentas, recursos e instruções.

MCP não é uma ferramenta específica; é o padrão de conexão entre o Hermes e um serviço externo.

## 10.1 Casos de uso

Um servidor MCP pode fornecer acesso a:

- banco de dados;
- documentos institucionais;
- repositórios de código;
- serviços de busca;
- sistemas de laboratório;
- ferramentas especializadas.

## 10.2 Comandos básicos

```bash
hermes mcp list
hermes mcp catalog
hermes mcp install <nome>
hermes mcp test <nome>
```

`hermes mcp test <nome>` pode iniciar ou contatar um servidor. Teste apenas integrações confiáveis e compreendidas.

## 10.3 Segurança em MCP

Antes de adicionar um MCP, pergunte:

1. Quem mantém esse servidor?
2. Que dados ele recebe?
3. Quais variáveis de ambiente ou credenciais ele precisa?
4. Que ações ele pode executar?
5. Posso limitar ferramentas específicas?

Para servidores MCP executados localmente por `stdio`, o Hermes filtra o ambiente: não repassa automaticamente todo o seu shell. Ainda assim, configure explicitamente apenas as credenciais necessárias.

---

# 11. Agentes, subagentes e orquestração

## 11.1 O que é um agente?

Um agente combina modelo, instruções, ferramentas e um ciclo de execução. Ele pode planejar uma tarefa, usar recursos, verificar resultados e retornar uma resposta.

Isso não torna o agente infalível. Quanto maior a autonomia, maior deve ser a verificação humana.

## 11.2 Subagentes

O Hermes pode delegar tarefas a subagentes por meio da ferramenta `delegate_task`.

Um subagente:

- inicia uma conversa nova;
- não conhece automaticamente o histórico do agente principal;
- recebe apenas o objetivo e o contexto que foram enviados;
- devolve um resumo final ao agente principal.

Boa delegação inclui objetivo, fontes permitidas, formato de saída e critério de verificação.

Exemplo conceitual:

```text
Objetivo: localizar três fontes primárias sobre X.
Contexto: use somente sites institucionais; registre URL e data; não faça escrita externa.
Entrega: lista com título, URL, trecho de evidência e limite de cada fonte.
```

## 11.3 Orquestração

**Orquestração** é a coordenação de tarefas, agentes, ferramentas e dependências. Pode ser sequencial ou paralela.

Mais agentes não significam automaticamente melhor resultado. A multiplicação de agentes pode ampliar custo, ruído e erro. O agente principal continua responsável por conferir e integrar as entregas.

Para colaboração durável entre perfis, o Hermes oferece Kanban:

```bash
hermes kanban init
hermes kanban list
```

Delegação transitória e Kanban não são a mesma coisa:

- `delegate_task`: trabalho temporário, voltado a uma conversa;
- Kanban: tarefas persistentes, dependências e coordenação entre perfis/processos.

---

# 12. Gateway: Hermes no Telegram, Discord e outras plataformas

O **gateway de mensagens** conecta o Hermes a plataformas como Telegram, Discord, Slack e WhatsApp. Ele também hospeda o scheduler de cron jobs.

Configure de forma interativa:

```bash
hermes gateway setup
```

Para testar em primeiro plano:

```bash
hermes gateway
```

Para verificar o serviço:

```bash
hermes gateway status
```

## 12.1 Segurança de bots

Um bot Hermes pode executar ferramentas. Portanto, não o libere para qualquer pessoa sem pensar em autorização.

Use:

- allowlists de pessoas ou chats;
- pareamento de mensagens diretas;
- permissões mínimas;
- logs e revisão periódica;
- perfis separados para bots com objetivos distintos.

Não confunda o **Messaging Gateway** com o **Nous Tool Gateway**. O primeiro conecta aplicativos de mensagem ao Hermes; o segundo é um conjunto de ferramentas de serviços oferecido pelo Nous Portal.

---

# 13. Cron: automatizando tarefas

**Cron** é um agendador de tarefas. Ele permite executar algo em horários ou intervalos definidos.

Exemplos de uso:

- resumo diário de notícias;
- monitoramento semanal de editais;
- atualização de dados;
- lembrete de revisão;
- geração periódica de relatório.

## 13.1 Verificar o scheduler

```bash
hermes cron status
hermes cron list
hermes cron doctor
```

Os jobs ficam no diretório de cron do perfil ativo e cada execução gera seu próprio resultado.

> **Importante:** criar um job não prova que ele executará. O gateway/scheduler precisa estar ativo, a máquina deve estar ligada e o destino de entrega deve estar configurado.

## 13.2 Antes de automatizar

Automatize somente uma tarefa que já foi executada e validada manualmente.

Defina:

- frequência e fuso horário;
- fontes permitidas;
- limite de custo;
- destino de entrega;
- política para erros;
- forma de interromper ou pausar.

Para pausar e retomar:

```bash
hermes cron pause <id-do-job>
hermes cron resume <id-do-job>
```

Para consultar execuções:

```bash
hermes cron runs
```

## 13.3 Encadeamento

Jobs podem formar cadeias: coleta → triagem → redação. Isso é útil, mas cada etapa precisa produzir um artefato verificável e ter limites claros.

---

# 14. Git e GitHub para quem usa agentes

## 14.1 Git

**Git** registra versões de arquivos. Ele funciona no seu computador mesmo sem internet.

Pense no Git como um arquivo organizado de versões: permite comparar estados, saber o que mudou e voltar a uma versão anterior quando necessário.

Comandos básicos:

```bash
git status
git add <arquivo>
git commit -m "docs: atualiza guia"
```

## 14.2 GitHub

**GitHub** é uma plataforma que hospeda repositórios Git e oferece colaboração, issues, pull requests e automações.

Git e GitHub não são sinônimos:

- `git commit` registra uma versão local;
- `git push` envia versões para um repositório remoto, como GitHub.

## 14.3 Por que isso importa com agentes?

Agentes podem editar muitos arquivos. Um repositório Git permite:

- inspecionar mudanças antes de publicar;
- manter histórico e autoria;
- revisar contribuições;
- separar trabalho experimental de versões estáveis;
- recuperar versões anteriores.

> **Segurança:** remover uma chave de API de um arquivo não a remove automaticamente do histórico Git. Nunca faça commit de segredos.

---

# 15. Troubleshooting: problemas comuns

Comece por diagnóstico, não por reinstalação. Registre o comando, o perfil, a hora, a mensagem de erro e o que mudou antes do problema.

## 15.1 `hermes: command not found`

**Causa provável:** o shell ainda não recarregou o PATH após a instalação.

```bash
source ~/.bashrc
# ou
source ~/.zshrc
```

Em seguida:

```bash
command -v hermes
ls ~/.local/bin/hermes
```

Se o launcher não existir, a instalação pode estar incompleta. Consulte a [FAQ oficial](https://hermes-agent.nousresearch.com/docs/reference/faq).

## 15.2 O Hermes abre, mas não responde

Verifique configuração de modelo e provedor:

```bash
hermes status
hermes doctor
hermes model
```

Possibilidades: chave ausente, OAuth expirado, modelo inválido, endpoint local desligado, limite de uso atingido.

Não copie chaves de API para chats ao tentar depurar.

## 15.3 Uma ferramenta não aparece

Verifique tools e toolsets:

```bash
hermes tools
hermes doctor
```

Confira se a ferramenta exige credencial, plugin, navegador ou serviço adicional. Depois de mudar ferramentas numa conversa, inicie uma sessão nova ou siga o procedimento indicado pela interface.

## 15.4 Uma skill não aparece

```bash
hermes skills list
```

Verifique se:

- você está no perfil correto;
- a skill tem `SKILL.md`;
- a skill está habilitada para a plataforma;
- ela tem requisitos pendentes;
- existe duplicidade ou quarentena.

Dentro da conversa, use:

```text
/reload-skills
```

## 15.5 Um MCP não conecta

```bash
hermes mcp list
hermes mcp test <nome>
```

Confira URL, transporte, runtime, autenticação, ferramentas filtradas e logs. O teste pode executar código do servidor MCP; faça isso apenas se você confia na integração.

## 15.6 O bot está silencioso

```bash
hermes gateway status
hermes logs gateway
hermes pairing list
```

Faça o diagnóstico em sequência:

1. o gateway está rodando?
2. a plataforma está conectada?
3. a mensagem chegou?
4. o usuário ou chat está autorizado?
5. o bot tem permissões e eventos necessários?
6. a resposta foi entregue?

Para Telegram em grupos, considere privacy mode, autorização do grupo e filtros de menção. Para Discord, confira intents e permissões. Para Slack, confira eventos, escopos e se o app foi reinstalado após alterar a configuração.

## 15.7 O cron não executa

```bash
hermes cron status
hermes cron list
hermes cron doctor
hermes cron runs
```

Cheque scheduler/gateway, fuso horário, job pausado, credenciais, script, diretório de trabalho e saída de entrega.

Execução e entrega são etapas diferentes: um job pode concluir localmente e falhar ao enviar uma mensagem.

## 15.8 O Hermes numa VPS morre ao fechar SSH

Um processo iniciado numa sessão SSH pode morrer quando ela fecha. Em Linux com systemd, instale o gateway como serviço e ative persistência de usuário quando apropriado:

```bash
hermes gateway install
hermes gateway start
sudo loginctl enable-linger "$USER"
```

Para servidores, a documentação também prevê serviço de sistema. Não instale simultaneamente serviços de usuário e de sistema sem entender qual deles deve controlar o gateway.

## 15.9 Depois de atualizar, algo mudou

O método correto de atualização depende da instalação.

- source checkout gerenciado: `hermes update`;
- Desktop: mecanismo do aplicativo ou da loja;
- Docker: atualizar imagem e recriar contêiner;
- Nix: atualizar flake/perfil;
- Termux: atualizar pelo gerenciador APT.

Depois de atualizar:

```bash
hermes --version
hermes config check
hermes config migrate
hermes doctor
```

`hermes pm` administra dependências e ferramentas, mas não substitui o atualizador do aplicativo.

## 15.10 Onde procurar logs?

```bash
hermes logs
hermes logs errors
hermes logs --since 1h
```

Para um resumo de suporte:

```bash
hermes dump
```

Revise qualquer relatório antes de compartilhá-lo: logs podem conter nomes de arquivos, caminhos e dados de trabalho. Não use modos que desativem redação de segredos em um tutorial para iniciantes.

---

# 16. Glossário essencial

| Termo | Definição curta |
|---|---|
| Agente | Sistema que combina modelo, instruções, ferramentas e ciclo de execução. |
| API | Interface padronizada para programas solicitarem operações a outros programas. |
| Contexto | Material disponível para o modelo em uma chamada. |
| Cron | Agendamento automático de tarefas. |
| Ferramenta | Função executável que realiza uma ação. |
| Gateway | Processo que conecta plataformas de mensagem ao Hermes e hospeda o scheduler. |
| Git | Sistema local de controle de versões. |
| GitHub | Plataforma remota de hospedagem e colaboração com Git. |
| MCP | Padrão para conectar agentes a servidores de ferramentas e recursos. |
| Memória | Notas persistentes e selecionadas entre sessões. |
| MemPalace | Extensão específica; não é componente nativo oficial do Hermes. |
| Modelo | Sistema de IA que processa entradas e produz saídas. |
| Perfil | Área de estado separada do Hermes: config, memória, skills e sessões. |
| Provedor | Serviço que disponibiliza acesso a modelos. |
| Servidor | Programa ou máquina que atende solicitações. |
| Skill | Procedimento reutilizável que orienta o agente. |
| SOUL.md | Arquivo de identidade e estilo persistente do Hermes. |
| SSH | Protocolo seguro de acesso remoto a uma máquina. |
| Subagente | Agente filho que recebe uma tarefa com contexto próprio. |
| Token | Unidade de texto do modelo; também pode significar credencial, em outro contexto. |
| Toolset | Conjunto de ferramentas disponíveis a uma sessão/plataforma. |
| URL | Endereço de um recurso na web. |
| VPS | Servidor virtual privado, geralmente alugado. |
| Orquestração | Coordenação de agentes, ferramentas, tarefas e dependências. |

---

# 17. Checklist final de uso responsável

Antes de usar o Hermes em uma tarefa relevante, confirme:

- [ ] Sei qual perfil está ativo.
- [ ] Sei em qual máquina os comandos serão executados.
- [ ] Sei qual provedor e modelo estão configurados.
- [ ] Não incluí chaves, senhas ou dados pessoais desnecessários no pedido.
- [ ] Delimitei se o agente pode ler, escrever, publicar ou enviar mensagens.
- [ ] Pedi fontes e critérios de verificação quando a tarefa exige evidência.
- [ ] Revisei as mudanças antes de publicar, executar ou enviar.
- [ ] Para automações, configurei fuso, destino, limite de custo e forma de pausa.
- [ ] Para bots, configurei autorização de usuários e chats.

> **Regra de ouro:** a IA pode acelerar operações; ela não transfere para a máquina a responsabilidade intelectual, metodológica, institucional ou ética pelo resultado.

---

# Referências oficiais

1. Hermes Agent Documentation. https://hermes-agent.nousresearch.com/docs
2. Installation. https://hermes-agent.nousresearch.com/docs/getting-started/installation
3. Quickstart. https://hermes-agent.nousresearch.com/docs/getting-started/quickstart
4. Learning Path. https://hermes-agent.nousresearch.com/docs/getting-started/learning-path
5. Configuration. https://hermes-agent.nousresearch.com/docs/user-guide/configuration
6. AI Providers. https://hermes-agent.nousresearch.com/docs/integrations/providers
7. Toolsets Reference. https://hermes-agent.nousresearch.com/docs/reference/toolsets-reference
8. Skills System. https://hermes-agent.nousresearch.com/docs/user-guide/features/skills
9. Personality & SOUL.md. https://hermes-agent.nousresearch.com/docs/user-guide/features/personality
10. MCP. https://hermes-agent.nousresearch.com/docs/user-guide/features/mcp
11. Scheduled Tasks (Cron). https://hermes-agent.nousresearch.com/docs/user-guide/features/cron
12. Persistent Memory. https://hermes-agent.nousresearch.com/docs/user-guide/features/memory
13. Profiles. https://hermes-agent.nousresearch.com/docs/user-guide/profiles
14. Subagent Delegation. https://hermes-agent.nousresearch.com/docs/user-guide/features/delegation
15. Messaging Gateway. https://hermes-agent.nousresearch.com/docs/user-guide/messaging/
16. FAQ & Troubleshooting. https://hermes-agent.nousresearch.com/docs/reference/faq
17. CLI Commands Reference. https://hermes-agent.nousresearch.com/docs/reference/cli-commands
18. Updating & Uninstalling. https://hermes-agent.nousresearch.com/docs/getting-started/updating

---

## Créditos

**Autoria e curadoria:** Laboratório de Humanidades Digitais da UFBA (LABHD-UFBA).

**Fonte técnica:** documentação e repositório oficiais do Hermes Agent, Nous Research.

**Versão:** 1.1 · outubro de 2026.
