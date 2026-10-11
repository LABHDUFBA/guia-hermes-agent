# Como contribuir

Obrigado por ajudar a manter este guia útil e verificável.

## Antes de abrir uma contribuição

1. Consulte a [documentação oficial do Hermes](https://hermes-agent.nousresearch.com/docs).
2. Informe a versão testada com `hermes --version`.
3. Não inclua chaves, tokens, senhas, IDs privados ou informações pessoais de terceiros.
4. Não apresente recursos experimentais como se fossem garantidos.

## Correções

Para corrigir um comando ou uma explicação:

- indique a seção afetada;
- informe o sistema operacional e a versão do Hermes;
- inclua URL da documentação oficial ou saída de comando não sensível;
- explique como verificar a correção.

## Checklist antes do pull request

```bash
python3 scripts/validate.py
bash scripts/build_pdf.sh
pdfinfo releases/v1.2/guia-hermes-agent-labhdufba-v1.2.pdf
```

Toda alteração no texto deve preservar a distinção entre:

- comandos de terminal;
- comandos internos do chat;
- prompts em linguagem natural;
- ações que apenas consultam;
- ações que alteram estado ou têm efeitos externos.
