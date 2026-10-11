---
title: "Guia Hermes Agent no Telegram — LABHDUFBA"
subtitle: "Uso cotidiano, comandos, automações e recuperação de problemas em uma abordagem Telegram-first"
author: "Laboratório de Humanidades Digitais da UFBA — LABHD-UFBA"
date: "Versão 1.2 · outubro de 2026"
lang: pt-BR
---

<div class="title-block">
  <img src="assets/labhdufba_logo_oficial.png" alt="Marca do LABHDUFBA" />
  <div class="kicker">LABORATÓRIO DE HUMANIDADES DIGITAIS DA UFBA</div>
  <h1>Guia Hermes Agent no Telegram</h1>
  <p class="subtitle">Uso cotidiano, comandos, automações e recuperação de problemas em uma abordagem Telegram-first</p>
  <p class="version">Versão 1.2 · outubro de 2026</p>
  <p class="license">Material aberto sob licença CC BY 4.0</p>
</div>

# Como usar este guia

Este tutorial parte de uma situação comum: o Hermes foi instalado em um computador ou servidor, mas a maior parte das pessoas o utiliza pelo **Telegram**, sem abrir um terminal.

A regra editorial desta versão é simples:

1. toda operação cotidiana começa no Telegram;
2. comandos próprios do chat aparecem como comandos `/...`;
3. tarefas sem comando próprio são solicitadas em linguagem natural;
4. o terminal ou SSH aparece apenas quando o bot está inacessível, faltam credenciais ou é necessária uma configuração administrativa.

> **Telegram-first não significa Telegram-only.** Se o gateway, a máquina ou a conexão estiverem fora do ar, o próprio bot não poderá consertar o canal pelo qual deveria receber a ordem. Nesses casos, alguém com acesso administrativo precisará usar o Desktop, o painel web, o terminal local ou SSH.

## As quatro etiquetas operacionais

Cada procedimento distingue quatro elementos:

- **NO TELEGRAM — COMANDO:** digite exatamente o comando iniciado por `/`.
- **NO TELEGRAM — MENSAGEM:** envie o pedido em linguagem natural ao bot.
- **RESULTADO ESPERADO:** o que deve acontecer se a operação funcionar.
- **ADMINISTRAÇÃO — FORA DO TELEGRAM:** ação excepcional, feita no computador ou servidor.

## Antes de executar qualquer ação

Pergunte:

- em qual máquina a operação ocorrerá;
- quais dados serão lidos ou enviados;
- se haverá escrita, publicação, exclusão ou custo;
- como o resultado será verificado;
- como interromper ou desfazer a ação.

Nunca envie pelo Telegram senhas, chaves de API, token do BotFather, chave SSH privada ou dados pessoais desnecessários.

---

# 1. O que acontece quando você fala com o Hermes no Telegram?

O Telegram é a interface de conversa, mas o agente roda em outra máquina. O fluxo básico é:

```text
Você no Telegram
        ↓
Bot do Telegram e Bot API
        ↓
Gateway do Hermes no computador ou servidor
        ↓
Agente Hermes + modelo de IA + ferramentas
        ↓
Arquivos, web, bancos, APIs e outros serviços autorizados
```

Essa arquitetura explica uma diferença central: **o Telegram transporta mensagens; ele não é o servidor do Hermes**.

## 1.1 Conceitos mínimos

- **Bot:** conta automatizada criada no Telegram por meio do BotFather.
- **BotFather:** bot oficial do Telegram que cria e administra outros bots.
- **Token do bot:** credencial secreta que permite controlar o bot.
- **Gateway:** processo do Hermes que recebe mensagens, administra sessões, executa cron jobs e entrega respostas.
- **Servidor:** máquina ou programa que permanece disponível para atender solicitações.
- **VPS:** servidor virtual alugado, frequentemente usado para manter o Hermes ligado 24 horas.
- **SSH:** protocolo seguro para administrar uma máquina remota quando o Telegram não basta.
- **Perfil:** área separada de configuração, memória, skills, sessões e cron do Hermes.
- **Modelo:** sistema de IA que interpreta pedidos e produz respostas.
- **Provedor:** serviço que disponibiliza o modelo, normalmente por API.
- **Ferramenta:** função que permite ao agente pesquisar, ler arquivos, usar o terminal ou operar serviços.

## 1.2 Três formas de interação

### A. Conversa normal

Você escreve um pedido como escreveria para uma pessoa:

> **NO TELEGRAM — MENSAGEM**
> Leia o PDF anexado. Produza uma síntese de 300 palavras, indique as páginas das citações e separe o que o texto afirma do que você está inferindo.

### B. Comando de chat

Você envia uma instrução curta iniciada por `/`:

```text
/status
```

O gateway interpreta o comando diretamente, sem depender de uma resposta inventada pelo modelo.

### C. Ação administrativa solicitada ao agente

Você pode pedir que o Hermes diagnostique a própria máquina usando suas ferramentas:

> **NO TELEGRAM — MENSAGEM**
> Faça um diagnóstico somente de leitura do gateway e do provedor. Não altere configurações. Informe os comandos executados, a saída relevante e a conclusão.

Isso só funciona se o perfil do Telegram tiver as ferramentas e permissões necessárias. Digitar `hermes doctor` como mensagem comum **não transforma automaticamente o texto em comando de terminal**.

---

# 2. Configuração inicial: a única etapa necessariamente administrativa

Quem apenas usa um bot já configurado pode avançar para o capítulo 3. Esta seção é destinada à pessoa responsável pela instalação.

## 2.1 Pré-requisitos

Antes de conectar o Telegram, confirme que:

- o Hermes está instalado;
- um modelo e provedor estão configurados;
- o Hermes responde localmente;
- o perfil correto foi escolhido;
- a máquina ficará ligada quando o bot precisar funcionar.

## 2.2 Caminho rápido: Dashboard ou Hermes Desktop

No Dashboard ou aplicativo Desktop, abra **Messaging → Telegram** e use **Create with QR**. Ao escanear o QR ou abrir o link, o Hermes pode criar o bot, detectar o ID do usuário, gravar as credenciais no perfil e reiniciar o gateway.

Esse é o caminho mais simples para iniciantes.

## 2.3 Caminho manual: BotFather

No Telegram:

1. abra [@BotFather](https://t.me/BotFather);
2. envie `/newbot`;
3. escolha o nome de exibição;
4. escolha um username único terminado em `bot`;
5. guarde o token recebido em local seguro.

> **Não envie o token para o seu bot Hermes.** As mensagens passam pelo próprio serviço que você está configurando e podem ficar registradas. Insira a credencial apenas no assistente administrativo, no Desktop/Dashboard ou no arquivo `.env` protegido.

Para personalização, os comandos `/setdescription`, `/setabouttext`, `/setuserpic`, `/setcommands` e `/setprivacy` são enviados ao **BotFather**, não ao Hermes.

## 2.4 Configurar e iniciar o gateway

> **ADMINISTRAÇÃO — FORA DO TELEGRAM**
> No terminal da máquina onde o Hermes está instalado:

```bash
hermes gateway setup
hermes gateway install
hermes gateway start
hermes gateway status
```

No assistente, selecione Telegram, informe o token em campo protegido e autorize somente os IDs de usuário necessários.

**Resultado esperado:** o status indica que o gateway está ativo e o bot passa a receber mensagens.

## 2.5 Primeiro teste pelo Telegram

Abra o bot e envie:

```text
/whoami
```

**Resultado esperado:** o Hermes informa seu nível de acesso — administrador, usuário regular ou modo irrestrito legado.

Depois envie:

```text
/status
```

**Resultado esperado:** aparecem o modelo, provedor, perfil, sessão, uso de contexto e um resumo da conversa.

Por fim, defina este chat como destino principal:

```text
/sethome
```

**Resultado esperado:** o chat passa a ser o canal residencial para entregas que usam o destino padrão do Telegram.

> `/start` é um comando de protocolo do Telegram e pode ser reconhecido silenciosamente. Para um teste visível, prefira `/whoami`, `/help` ou `/status`.

---

# 3. Primeiros passos inteiramente pelo Telegram

## 3.1 Descobrir os comandos disponíveis

```text
/help
```

Mostra a ajuda principal. Para navegar pela lista ampliada:

```text
/commands
/commands 2
```

O menu `/` do Telegram é limitado e pode não exibir todas as skills e comandos instalados. `/commands` é a referência prática dentro do chat.

## 3.2 Iniciar uma sessão limpa

```text
/new pesquisa-bibliografica
```

Ou:

```text
/reset
```

**Resultado esperado:** uma nova sessão, sem a conversa anterior no contexto ativo.

**Risco:** a sessão anterior não é apagada do histórico, mas deixa de ser a sessão corrente. Use `/sessions` e `/resume` para recuperá-la.

## 3.3 Dar um título à conversa

```text
/title Revisão sobre esfera pública digital
```

Títulos facilitam o retorno posterior:

```text
/sessions
/resume Revisão sobre esfera pública digital
```

## 3.4 Fazer um primeiro pedido verificável

> **NO TELEGRAM — MENSAGEM**
> Explique em até 150 palavras a diferença entre modelo, provedor e API. Ao final, indique o que é definição técnica e o que é analogia explicativa. Não use ferramentas externas.

O exercício ensina a distinguir explicação, evidência e inferência.

## 3.5 Interromper uma tarefa

Se o Hermes estiver executando uma tarefa longa:

```text
/agents
```

Mostra agentes e trabalhos ativos. Para interromper o agente atual e processos em segundo plano:

```text
/stop
```

> `/stop` interrompe tarefas e processos; não equivale a desligar permanentemente o gateway.

---

# 4. Mapa dos comandos mais úteis no Telegram

## 4.1 Ajuda, identidade e diagnóstico

| Comando | Função | Efeito |
|---|---|---|
| `/help` | Mostra ajuda de uso | Somente leitura |
| `/commands [página]` | Navega por comandos e skills | Somente leitura |
| `/whoami` | Informa seu nível de acesso | Somente leitura |
| `/version` | Mostra versão e ambiente | Somente leitura |
| `/status` | Mostra sessão, modelo, perfil, contexto e atividade | Somente leitura |
| `/context` | Mostra ocupação da janela de contexto | Somente leitura |
| `/context all` | Acrescenta custos de skills e ferramentas no contexto | Somente leitura |
| `/usage` | Mostra tokens, custos estimados e limites disponíveis | Somente leitura |

## 4.2 Sessões e continuidade

| Comando | Função | Atenção |
|---|---|---|
| `/new [nome]` | Abre sessão limpa | Muda a sessão corrente |
| `/title [nome]` | Nomeia a sessão | Facilita `/resume` |
| `/sessions` | Lista sessões do chat | Somente leitura |
| `/sessions search termo` | Filtra sessões pelo título ou ID | Somente leitura |
| `/resume [nome]` | Retoma sessão anterior | Troca o contexto ativo |
| `/retry` | Repete a última mensagem | Pode repetir ações; confira antes |
| `/undo` | Remove a última troca da sessão | Altera o histórico ativo |
| `/compress` | Resume o histórico para liberar contexto | Perde detalhes finos |
| `/compress here 2` | Mantém as duas trocas mais recentes literalmente | Opção mais controlada |

## 4.3 Modelo, raciocínio e custo

| Comando | Função | Atenção |
|---|---|---|
| `/model` | Abre seletor de provedores/modelos já configurados | Não cadastra nova API |
| `/model nome` | Troca o modelo nesta sessão | Pode alterar custo e comportamento |
| `/model nome --global` | Persiste a troca no perfil | Ação administrativa |
| `/reasoning low` | Ajusta esforço de raciocínio | Disponibilidade depende do modelo |
| `/fast status` | Mostra o modo rápido | Pode envolver cobrança diferenciada |
| `/usage` | Confere consumo e estimativa de custo | Leia antes de automatizar |

Trocar de modelo no meio de uma conversa reinicia o cache de prompt. Em sessões longas, a próxima mensagem pode custar mais porque o contexto será relido.

## 4.4 Tarefas em andamento

| Comando | Função |
|---|---|
| `/agents` | Mostra agentes e tarefas ativos |
| `/bg <pedido>` | Executa um pedido em sessão separada e devolve o resultado ao chat |
| `/queue <pedido>` | Enfileira um pedido para o próximo turno |
| `/steer <nota>` | Redireciona a tarefa após a próxima ferramenta, sem interromper |
| `/stop` | Interrompe o agente e processos em segundo plano |
| `/review` | Solicita revisão independente do trabalho recente |

Exemplo:

```text
/bg pesquise as páginas institucionais das três organizações citadas e devolva uma lista com URLs e datas de acesso
```

## 4.5 Manutenção acessível pelo chat

| Comando | Função | Risco |
|---|---|---|
| `/reload-skills` | Recarrega skills já instaladas | Baixo |
| `/reload-mcp` | Recarrega servidores MCP configurados | Pode alterar ferramentas disponíveis |
| `/platform list` | Mostra adaptadores do gateway | Somente leitura |
| `/platform pause telegram` | Pausa entrada de novas mensagens do Telegram | Pode cortar o próprio canal |
| `/platform resume telegram` | Retoma o adaptador | Requer que o comando alcance outro canal se Telegram estiver pausado |
| `/restart` | Reinicia o gateway de modo controlado | Interrompe brevemente as plataformas |
| `/update` | Atualiza o Hermes | Pode introduzir mudanças; use somente com autorização |
| `/debug` | Envia relatório de diagnóstico e gera links | Pode expor metadados e logs |

> **Não use `/platform pause telegram` no único canal administrativo disponível.** Você poderá não conseguir enviar `/platform resume telegram` pelo mesmo Telegram.

## 4.6 Aprovações de comandos perigosos

Quando uma ação for considerada perigosa, o Hermes poderá mostrar botões ou pedir confirmação.

```text
/approve
/deny
```

Use `/approve session` para autorizar dentro da sessão e `/approve always` apenas quando compreender a regra que será adicionada à lista permanente.

**Padrão seguro:** se o comando contiver exclusão recursiva, sobrescrita, envio externo ou mudança de credencial e você não entender cada parte, use `/deny`.

---

# 5. O que não é comando do Telegram

Alguns comandos pertencem ao terminal interativo e não funcionam como comandos do gateway. Entre eles estão, conforme a versão atual:

- `/cron`;
- `/tools` e `/toolsets`;
- `/skills` para pesquisar, navegar ou instalar;
- `/config`;
- `/platforms`;
- `/browser`;
- `/plugins`;
- `/handoff`;
- `/quit`.

Isso não impede o uso desses recursos pelo Telegram. A forma correta é pedir a operação em linguagem natural para o agente, desde que a ferramenta correspondente esteja habilitada.

## 5.1 Exemplo: cron sem `/cron`

Não envie:

```text
/cron add every day 9am ...
```

Prefira:

> **NO TELEGRAM — MENSAGEM**
> Crie uma tarefa recorrente chamada “Editais de pesquisa”. Toda segunda-feira às 9h, no fuso America/Bahia, pesquise apenas fontes oficiais e envie o resultado para este mesmo chat. Antes de criar, mostre a configuração proposta e aguarde minha confirmação.

## 5.2 Exemplo: diagnóstico de tools

> **NO TELEGRAM — MENSAGEM**
> Liste as ferramentas efetivamente disponíveis nesta sessão e explique quais delas podem ler arquivos, acessar a web, executar comandos ou escrever em serviços externos. Não altere a configuração.

A resposta do agente é útil para operação. Para auditoria administrativa definitiva, a pessoa responsável ainda pode consultar `hermes tools` fora do Telegram.

## 5.3 Exemplo: skill ainda não instalada

> **NO TELEGRAM — MENSAGEM**
> Verifique se existe uma skill instalada para trabalhar com Zotero. Não instale nada. Informe o nome exato, a origem, as dependências e os riscos.

Se a instalação exigir ação administrativa, o Hermes deve informar isso. Depois de uma instalação concluída por pessoa autorizada, use:

```text
/reload-skills
```

---

# 6. Pedidos bem formulados pelo Telegram

Uma solicitação operacional deve conter cinco partes:

1. **Objetivo:** o que deve ser produzido.
2. **Escopo:** quais fontes, arquivos ou sistemas podem ser usados.
3. **Permissões:** pode apenas ler ou também escrever/publicar?
4. **Verificação:** como demonstrar que a tarefa foi concluída.
5. **Parada:** quando interromper e pedir ajuda.

## 6.1 Modelo copiável

> **NO TELEGRAM — MENSAGEM**
> Objetivo: [resultado].
> Fontes permitidas: [arquivos/sites/sistemas].
> Permissões: [somente leitura / pode escrever em...].
> Verificação: [citações, contagem, link, leitura de volta].
> Pare e me pergunte se: [condição].

## 6.2 Leitura de PDF

Anexe o PDF e envie:

> Leia o documento anexado. Apresente tese, argumentos, conceitos e limites. Toda citação literal deve indicar página. Não pesquise na web. Se o PDF não tiver texto extraível, avise antes de usar OCR.

## 6.3 Pesquisa na web

> Pesquise o tema apenas em fontes oficiais e artigos acadêmicos. Para cada afirmação factual, forneça URL, título da fonte e data de acesso. Separe fatos encontrados de sua interpretação. Não publique nada.

## 6.4 Produção de arquivo

> Produza um arquivo DOCX com o texto aprovado nesta conversa. Preserve o original, use um nome versionado, valide a abertura do arquivo e me envie o documento no Telegram.

## 6.5 Alteração de repositório

> Trabalhe somente no repositório informado. Antes de editar, mostre `git status` e crie uma branch. Não faça push nem abra pull request sem autorização explícita. Ao final, execute os testes e apresente o diff.

## 6.6 Mensagem de voz

Você pode enviar áudio ao bot. O gateway tentará transcrevê-lo se houver um provedor de STT configurado. Para reduzir ambiguidades:

- diga o objetivo primeiro;
- soletre nomes próprios incomuns;
- peça que o Hermes repita os pontos entendidos antes de executar uma ação externa;
- revise datas, números e endereços transcritos.

---

# 7. Conceitos do Hermes vistos pelo Telegram

## 7.1 Modelo, provedor, API e token

- **Modelo:** sistema que produz a resposta.
- **Provedor:** serviço que hospeda ou disponibiliza o modelo.
- **API:** interface usada por programas para se comunicarem.
- **Token de texto:** unidade usada para medir contexto e custo.
- **Token de acesso:** credencial secreta; não deve ser enviada pelo chat.

No Telegram, consulte:

```text
/status
/model
/usage
```

`/model` alterna apenas entre provedores já configurados. Nova credencial deve ser cadastrada em superfície administrativa protegida.

## 7.2 Contexto

Contexto é o material disponível ao modelo no turno atual: instruções, mensagens, documentos e resultados de ferramentas.

```text
/context
```

Se a conversa estiver grande:

```text
/compress here 2
```

Se o assunto mudou completamente:

```text
/new novo-assunto
```

## 7.3 Ferramenta, toolset e skill

- **Ferramenta:** executa uma função concreta.
- **Toolset:** conjunto de ferramentas habilitadas para uma superfície, como Telegram ou cron.
- **Skill:** procedimento reutilizável que orienta o agente a executar uma classe de tarefa.

Uma skill não cria credenciais, não instala automaticamente dependências e não concede permissão por si só.

Skills instaladas podem aparecer como comandos dinâmicos:

```text
/<nome-da-skill>
```

Se uma skill recém-instalada não aparecer:

```text
/reload-skills
```

## 7.4 SOUL.md e personalidade

`SOUL.md` define identidade e estilo persistentes do perfil. Pelo Telegram, uma personalidade temporária pode ser aplicada:

```text
/personality teacher
/personality none
```

A personalidade modifica a forma de responder, não os fatos do sistema nem as permissões.

## 7.5 Memória e MemPalace

A memória nativa do Hermes guarda uma seleção pequena de fatos estáveis entre sessões. Ela não é a transcrição integral de todas as conversas.

**MemPalace não é um componente nativo oficial do Hermes.** É uma extensão ou configuração específica de determinados perfis. Não suponha que estará disponível em toda instalação.

Pelo Telegram, você pode pedir:

> Diga quais fatos estáveis sobre mim estão sendo usados nesta conversa. Não mostre segredos, credenciais nem dados de terceiros.

Se houver aprovação de escrita de memória habilitada:

```text
/memory pending
/memory approve <id>
/memory reject <id>
```

## 7.6 MCP

MCP é um padrão para conectar o Hermes a servidores externos de ferramentas e recursos.

Após uma mudança administrativa no MCP:

```text
/reload-mcp
```

Para um diagnóstico pelo chat:

> Faça um teste somente de leitura do servidor MCP chamado `<nome>`. Informe se ele está configurado, se responde e quais ferramentas expõe. Não altere credenciais nem instale componentes.

## 7.7 Agentes, subagentes e orquestração

Um agente combina modelo, instruções, ferramentas e ciclo de execução. Subagentes recebem tarefas separadas e não conhecem automaticamente todo o histórico do agente principal.

Orquestração é a coordenação dessas tarefas e dependências.

Pelo Telegram:

```text
/agents
```

Para trabalho independente:

```text
/bg compare as duas abordagens metodológicas e devolva uma matriz de diferenças
```

Mais agentes não garantem melhor resposta. Eles aumentam custo, necessidade de coordenação e superfície de erro.

---

# 8. Automações e cron inteiramente pelo Telegram

Cron agenda tarefas futuras ou recorrentes. Na superfície Telegram, o método recomendado é conversar com o agente em linguagem natural; a gestão é feita pela ferramenta de cron, não pelo comando CLI `/cron`.

## 8.1 Criar uma tarefa

> **NO TELEGRAM — MENSAGEM**
> Crie uma tarefa chamada “Monitor acadêmico”. Toda sexta-feira às 8h, no fuso America/Bahia, procure publicações da última semana sobre agentes de IA nas Ciências Sociais. Use somente fontes acadêmicas verificáveis. Entregue neste chat. Antes de criar, repita a agenda, o destino, as fontes e o modelo de execução para minha confirmação.

**Resultado esperado:** o Hermes devolve identificador ou nome da tarefa, agenda normalizada, próxima execução e destino.

## 8.2 Listar tarefas

> Liste todas as tarefas agendadas deste perfil. Para cada uma, mostre nome, ID, status, próxima execução, último resultado e destino. Não altere nada.

## 8.3 Testar manualmente

> Execute agora, uma única vez, a tarefa “Monitor acadêmico”. Não altere a agenda. Informe quando a execução terminar e onde o resultado foi entregue.

## 8.4 Pausar, retomar e remover

> Pause a tarefa “Monitor acadêmico” e leia de volta o estado final.

> Retome a tarefa “Monitor acadêmico” e informe a próxima execução.

> Remova a tarefa “Monitor acadêmico”. Antes de remover, mostre o ID e aguarde minha confirmação.

## 8.5 Checklist de uma automação segura

Antes de confirmar a criação, verifique:

- nome inequívoco;
- fuso horário;
- frequência;
- fontes permitidas;
- modelo/provedor e custo;
- destino `origin` ou chat específico;
- critério de silêncio quando não houver novidade;
- forma de pausar e remover;
- execução de teste.

## 8.6 Quando o cron não entrega

> **NO TELEGRAM — MENSAGEM**
> Faça um diagnóstico somente de leitura da tarefa `<nome>`. Mostre agenda, fuso, última execução, `last_status`, `last_fire_error`, falha de entrega e próxima execução. Não altere a tarefa.

Se a execução funciona manualmente, mas não ocorre no horário, o problema tende a estar no scheduler/gateway. Se a execução conclui, mas não chega ao Telegram, examine o destino e as credenciais de entrega.

---

# 9. Uso em grupos e tópicos do Telegram

## 9.1 Por que o bot funciona na DM e não no grupo?

O Telegram ativa **Privacy Mode** por padrão. Com ele, o bot normalmente vê comandos, respostas dirigidas ao bot, menções e mensagens de serviço — não toda a conversa.

Teste no grupo:

```text
@username_do_bot /status
```

Ou responda diretamente a uma mensagem do bot.

Se for necessário que o bot receba mensagens comuns, a pessoa administradora deve desativar a privacidade no BotFather ou tornar o bot administrador do grupo.

> Depois de mudar a privacidade no BotFather, remova e adicione novamente o bot ao grupo. O Telegram pode conservar a configuração anterior enquanto a associação antiga existir.

## 9.2 Autorizações de grupo

O usuário, o grupo ou ambos podem precisar estar nas listas de autorização. IDs negativos de chat são normais em grupos e supergrupos.

Se aparecer “unauthorized”:

```text
/whoami
```

Depois envie à pessoa administradora apenas seu **ID numérico de usuário** e o ID do grupo, nunca o token do bot.

## 9.3 Exigir menção

Em grupos, uma configuração segura é responder somente quando houver:

- `@menção` ao bot;
- resposta a uma mensagem do bot;
- comando `/...@username_do_bot`;
- padrão de chamada explicitamente configurado.

Isso evita que toda conversa do grupo dispare chamadas ao modelo.

## 9.4 Vários bots no mesmo grupo

Cada perfil Hermes deve ter seu próprio bot e token. O mesmo token não deve ser usado simultaneamente por dois gateways: o Telegram rejeitará o polling concorrente.

Mencione explicitamente o bot desejado para impedir respostas cruzadas.

## 9.5 Tópicos em conversa privada

Quando o modo de tópicos está habilitado pelo administrador e pelo BotFather, cada tópico pode manter sessão e contexto próprios.

```text
/topic
/topic help
```

Para separar projetos, use um tópico por linha de trabalho — por exemplo: Pesquisa, Administração e Produção de conteúdo.

---

# 10. Segurança e níveis de acesso

## 10.1 Usuário comum e administrador

Em uma instalação configurada com separação de acesso:

- administradores executam todos os comandos registrados;
- usuários regulares executam somente comandos permitidos;
- `/help` e `/whoami` permanecem disponíveis como piso de diagnóstico.

Se um comando estiver bloqueado, não tente contornar a política em linguagem natural. Peça à pessoa administradora que avalie a necessidade.

## 10.2 Dados que não devem entrar no chat

Não envie:

- token do BotFather;
- chave de API de modelo;
- senha de servidor;
- chave SSH privada;
- arquivo `.env`;
- cookies de navegador;
- base de dados com informações pessoais sem autorização e minimização.

## 10.3 Efeitos externos

Antes de autorizar, identifique se o Hermes pretende:

- excluir ou sobrescrever arquivos;
- enviar e-mail ou mensagem;
- publicar em rede social;
- fazer push no GitHub;
- alterar agenda cron;
- instalar pacote ou skill;
- reiniciar serviço;
- consumir uma API paga.

Use `/deny` quando a ação não estiver suficientemente explicada.

## 10.4 Relatório de debug

`/debug` pode enviar informações de sistema e logs para gerar links compartilháveis. Use somente quando necessário e em ambiente autorizado. Para diagnóstico inicial, prefira:

```text
/status
/context
/platform list
```

Ou peça um diagnóstico de leitura com redação de segredos.

---

# 11. Recuperação de problemas pelo Telegram

A estratégia de recuperação tem dois níveis:

1. **o bot ainda responde:** diagnostique e corrija pelo Telegram;
2. **o bot não responde:** use o canal administrativo mínimo, pois o Telegram não consegue entregar a ordem.

## 11.1 O bot responde, mas a tarefa parece travada

```text
/agents
/status
```

Se houver processo preso:

```text
/stop
```

Depois abra sessão limpa:

```text
/new recuperacao
```

E peça:

> Explique a falha anterior com base nos registros disponíveis. Não repita a ação que falhou. Proponha um teste menor e somente de leitura.

## 11.2 O contexto está cheio ou a resposta perdeu o foco

```text
/context
/compress here 2
```

Se o tema mudou:

```text
/new novo-tema
```

Não use memória como substituto do contexto documental: reanexe fontes necessárias.

## 11.3 O modelo está errado ou indisponível

```text
/model
```

Escolha um modelo já configurado. Se nenhum provedor estiver disponível:

> Faça um diagnóstico somente de leitura do provedor e das credenciais configuradas. Não mostre valores secretos; mostre apenas presença/ausência, validade aparente e mensagem de erro.

Nova chave ou autenticação deve ser configurada fora do chat, em superfície protegida.

## 11.4 Uma skill não aparece

```text
/reload-skills
/commands
```

Depois:

> Verifique se a skill `<nome>` está instalada, habilitada para Telegram e com dependências satisfeitas. Não instale nem altere nada.

## 11.5 Um MCP desapareceu ou não responde

```text
/reload-mcp
```

Depois:

> Teste somente a conexão do MCP `<nome>`. Informe URL ou transporte sem expor credenciais, ferramentas descobertas e erro exato. Não faça operações de escrita.

## 11.6 Uma tarefa agendada não chegou

> Liste a tarefa `<nome>` e suas últimas execuções. Separe: falha de agendamento, falha do agente e falha de entrega. Não altere a tarefa.

Se necessário:

> Execute a tarefa uma vez agora para teste, sem alterar a agenda.

## 11.7 O bot ignora mensagens no grupo

1. envie uma `@menção` explícita;
2. responda a uma mensagem do bot;
3. envie `/whoami`;
4. peça conferência da autorização do grupo;
5. confira Privacy Mode no BotFather;
6. após a mudança, remova e adicione novamente o bot.

## 11.8 Mensagens de voz não são transcritas

> Diagnostique o recurso de transcrição de voz deste perfil. Não instale componentes. Informe se STT está habilitado, qual provedor foi selecionado e qual dependência ou credencial está ausente.

Se faltar um provedor de STT ou `ffmpeg`, a correção exigirá administração fora do Telegram.

## 11.9 O comando exige aprovação

Leia o comando apresentado. Para recusar:

```text
/deny
```

Para autorizar uma vez ou na sessão, use o botão correspondente ou:

```text
/approve
/approve session
```

Evite `/approve always` para comandos amplos, curingas ou ações destrutivas.

## 11.10 Uma atualização mudou o comportamento

Primeiro:

```text
/version
/status
```

Depois peça:

> Compare o comportamento atual com a documentação oficial correspondente à versão instalada. Não altere arquivos. Liste mudanças de configuração ou migrações pendentes.

Se uma reinicialização for recomendada e nenhuma tarefa crítica estiver ativa:

```text
/agents
/restart
```

Use `/update` apenas com autorização e depois de preservar configurações e trabalhos em andamento.

---

# 12. Quando o Telegram não consegue consertar o Telegram

Se o bot não responde a `/help`, `/whoami` ou `/status`, há quatro hipóteses principais:

1. gateway parado;
2. servidor desligado ou sem rede;
3. token inválido ou conflito de polling;
4. usuário/chat bloqueado antes do despacho.

Nesse estado, uma mensagem enviada ao bot não chega ao agente. A pessoa administradora deve usar Desktop/Dashboard, terminal local ou SSH.

## 12.1 Escada administrativa mínima

> **ADMINISTRAÇÃO — FORA DO TELEGRAM**

```bash
hermes gateway status
hermes status --all
hermes logs errors --since 1h
hermes doctor
```

Se o diagnóstico indicar que o gateway precisa reiniciar:

```bash
hermes gateway restart
```

Depois, retorne ao Telegram e teste:

```text
/whoami
/status
```

## 12.2 O gateway para quando a sessão SSH fecha

Um processo aberto manualmente no SSH pode morrer quando a conexão termina. Instale o gateway como serviço:

```bash
hermes gateway install
hermes gateway start
```

Em servidores Linux que usam serviço de usuário, pode ser necessário habilitar persistência após logout:

```bash
sudo loginctl enable-linger "$USER"
```

## 12.3 Token revogado ou inválido

No BotFather, gere ou recupere um token válido. Atualize-o somente na configuração protegida do perfil e reinicie o gateway.

Nunca publique o token num issue do GitHub ou envie-o ao chat Hermes.

## 12.4 Dois gateways usam o mesmo token

O Telegram permite apenas uma sessão de polling por token. Se dois processos usam o mesmo bot, um deles será desconectado ou aparecerão conflitos nos logs.

Interrompa a instância duplicada ou atribua um bot/token diferente a cada perfil.

---

# 13. Mensagens de erro: como interpretar e reagir

| Mensagem ou sintoma | Significado provável | Primeira ação no Telegram | Escalonamento |
|---|---|---|---|
| `unauthorized` | Seu ID/chat não está autorizado | `/whoami` | Administrador corrige allowlist |
| `command not allowed` | Seu nível não permite o comando | `/whoami` e `/help` | Administrador avalia permissão |
| pedido de aprovação | Ação foi classificada como perigosa | `/deny` ou `/approve` após leitura | Nunca autorize sem compreender |
| contexto próximo do limite | Conversa ocupou a janela do modelo | `/context` e `/compress here 2` | `/new` e reanexar fontes |
| modelo não encontrado | Nome inválido ou provedor não configurado | `/model` | Configuração administrativa |
| rate limit / quota | Limite do provedor foi atingido | `/usage`; aguarde ou troque modelo autorizado | Rever plano/provedor fora do chat |
| skill não encontrada | Skill ausente, desabilitada ou não recarregada | `/reload-skills` | Inspeção/instalação administrativa |
| MCP unavailable / connection failed | Servidor MCP não respondeu | `/reload-mcp` e teste de leitura | Conferir daemon, URL e credenciais |
| cron `blocked_config` | A tarefa falhou na validação de provedor, skill ou destino | pedir diagnóstico da tarefa | Corrigir dependência/credencial |
| model drift / provider changed | A tarefa não herdou silenciosamente uma troca de modelo | listar detalhes da tarefa | Fixar modelo autorizado ou recriar tarefa |
| bot responde na DM, não no grupo | Privacy Mode, allowlist ou menção | `@bot /status` e `/whoami` | BotFather/configuração do grupo |
| bot totalmente silencioso | Gateway, rede, token ou processo parados | teste `/help` e `/status` | Escada administrativa do capítulo 12 |
| conflito de polling | O mesmo token está ativo em mais de um gateway | nenhuma correção confiável pelo mesmo bot | Encerrar duplicata fora do Telegram |
| voz não transcrita | STT ausente/desativado ou arquivo incompatível | pedir diagnóstico de STT | Configurar dependência/provedor |
| arquivo produzido não chegou | Caminho não visível ao gateway ou upload excedeu limite | pedir verificação do arquivo e entrega | Corrigir volume/caminho no servidor |

> **Não reinstale por reflexo.** Primeiro identifique em qual camada ocorreu a falha: Telegram, gateway, autorização, agente, modelo, ferramenta ou destino externo.

---

# 14. Fluxos prontos para copiar e colar

## 14.1 Diagnóstico geral sem alterações

> Faça um diagnóstico somente de leitura desta sessão e do gateway. Verifique versão, perfil, modelo, provedor, contexto, tarefas ativas e estado do Telegram. Não mostre segredos, não reinicie serviços e não altere configurações. Organize o resultado em: situação, evidência, hipótese e próximo teste seguro.

## 14.2 Verificar antes de executar

> Antes de agir, apresente: (1) plano; (2) arquivos e serviços afetados; (3) comandos previstos; (4) riscos e custos; (5) forma de desfazer; (6) critérios de sucesso. Aguarde minha confirmação.

## 14.3 Recuperar uma tarefa que falhou

> Não repita automaticamente a ação anterior. Leia o erro e identifique a camada da falha. Proponha um teste mínimo e somente de leitura. Se a correção exigir credencial, reinicialização, instalação ou escrita externa, pare e peça autorização.

## 14.4 Criar automação verificável

> Proponha uma tarefa agendada para [objetivo]. Use o fuso [fuso], execute [frequência] e entregue neste chat. Informe fontes, modelo, custo provável e critério de silêncio. Mostre a configuração final e espere confirmação antes de criar. Depois, execute um teste único e leia de volta o estado salvo.

## 14.5 Trabalhar com dados sensíveis

> Antes de abrir os arquivos, identifique os tipos de dados e proponha minimização. Não envie conteúdo a serviços externos além do provedor já autorizado. Não grave dados pessoais em memória ou skills. Pare se a tarefa exigir exposição adicional.

---

# 15. Checklist do usuário de Telegram

Antes de começar:

- [ ] Estou falando com o bot correto.
- [ ] Usei `/whoami` para conferir meu nível de acesso.
- [ ] Usei `/status` para conferir perfil, modelo e sessão.
- [ ] Não enviei tokens, senhas ou chaves.
- [ ] Separei leitura de escrita/publicação.
- [ ] Pedi verificação do resultado.

Antes de autorizar uma ação:

- [ ] Sei em qual máquina ela ocorrerá.
- [ ] Sei quais arquivos ou serviços serão alterados.
- [ ] Sei se haverá custo externo.
- [ ] Sei como parar, desfazer ou recuperar.
- [ ] A ação não depende de uma credencial enviada pelo chat.

Antes de criar cron:

- [ ] Informei fuso horário e frequência.
- [ ] Defini o destino da entrega.
- [ ] Defini fontes e limites.
- [ ] Confirmei modelo/provedor e custo.
- [ ] Testei uma execução.
- [ ] Sei como pausar e remover.

---

# 16. Glossário essencial

| Termo | Definição curta |
|---|---|
| Administrador | Usuário autorizado a executar comandos e mudanças de maior alcance. |
| Agente | Sistema que combina modelo, instruções, ferramentas e ciclo de execução. |
| Allowlist | Lista explícita de usuários ou chats autorizados. |
| API | Interface padronizada para comunicação entre programas. |
| Bot | Conta automatizada que interage pelo Telegram. |
| BotFather | Bot oficial do Telegram usado para criar e administrar bots. |
| Contexto | Material disponível ao modelo numa chamada. |
| Cron | Sistema de agendamento de tarefas. |
| Ferramenta | Função que permite ao agente realizar uma ação. |
| Gateway | Processo que conecta o Telegram ao Hermes e executa o scheduler. |
| Git | Sistema de controle de versões. |
| GitHub | Plataforma de hospedagem e colaboração com repositórios Git. |
| MCP | Padrão para conectar agentes a servidores de ferramentas e recursos. |
| Memória | Seleção persistente de fatos entre sessões. |
| MemPalace | Extensão específica; não é componente nativo oficial do Hermes. |
| Modelo | Sistema de IA que processa entradas e produz saídas. |
| Orquestração | Coordenação de agentes, tarefas, ferramentas e dependências. |
| Perfil | Área separada de configuração, memória, skills, sessões e cron. |
| Provedor | Serviço que oferece acesso a modelos. |
| Sessão | Conversa com histórico e contexto próprios. |
| Skill | Procedimento reutilizável que orienta o agente. |
| SOUL.md | Arquivo que define identidade e estilo persistente do perfil. |
| SSH | Protocolo seguro para administração remota. |
| Token de acesso | Credencial secreta usada para autenticação. |
| Token de texto | Unidade de processamento e medição dos modelos. |
| Toolset | Conjunto de ferramentas habilitadas para uma superfície. |
| URL | Endereço de um recurso na web. |
| VPS | Servidor virtual privado. |

---

# Referências oficiais

1. Hermes Agent Documentation. https://hermes-agent.nousresearch.com/docs
2. Telegram Setup. https://hermes-agent.nousresearch.com/docs/user-guide/messaging/telegram
3. Messaging Gateway. https://hermes-agent.nousresearch.com/docs/user-guide/messaging/
4. Slash Commands Reference. https://hermes-agent.nousresearch.com/docs/reference/slash-commands
5. Scheduled Tasks (Cron). https://hermes-agent.nousresearch.com/docs/user-guide/features/cron
6. Skills System. https://hermes-agent.nousresearch.com/docs/user-guide/features/skills
7. Persistent Memory. https://hermes-agent.nousresearch.com/docs/user-guide/features/memory
8. MCP. https://hermes-agent.nousresearch.com/docs/user-guide/features/mcp
9. Subagent Delegation. https://hermes-agent.nousresearch.com/docs/user-guide/features/delegation
10. Profiles. https://hermes-agent.nousresearch.com/docs/user-guide/profiles
11. Personality & SOUL.md. https://hermes-agent.nousresearch.com/docs/user-guide/features/personality
12. Toolsets Reference. https://hermes-agent.nousresearch.com/docs/reference/toolsets-reference
13. FAQ & Troubleshooting. https://hermes-agent.nousresearch.com/docs/reference/faq
14. CLI Commands Reference. https://hermes-agent.nousresearch.com/docs/reference/cli-commands
15. Security. https://hermes-agent.nousresearch.com/docs/user-guide/security

---

## Créditos

**Autoria e curadoria:** Laboratório de Humanidades Digitais da UFBA (LABHD-UFBA).

**Fonte técnica:** documentação e repositório oficiais do Hermes Agent, Nous Research.

**Orientação desta versão:** uso cotidiano e recuperação de problemas a partir do Telegram, com administração externa apenas quando o canal está indisponível ou faltam credenciais protegidas.

**Versão:** 1.2 · outubro de 2026.
