#!/usr/bin/env python3
"""Validação determinística do Guia Hermes Agent do LABHDUFBA."""
from __future__ import annotations

import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
VERSION = "1.2"
GUIDE = ROOT / "docs" / f"guia-hermes-agent-v{VERSION}.md"
README = ROOT / "README.md"
REQUIRED = [
    "# Como usar este guia",
    "# 1. O que acontece quando você fala com o Hermes no Telegram?",
    "# 2. Configuração inicial: a única etapa necessariamente administrativa",
    "# 3. Primeiros passos inteiramente pelo Telegram",
    "# 4. Mapa dos comandos mais úteis no Telegram",
    "# 5. O que não é comando do Telegram",
    "# 7. Conceitos do Hermes vistos pelo Telegram",
    "# 8. Automações e cron inteiramente pelo Telegram",
    "# 9. Uso em grupos e tópicos do Telegram",
    "# 11. Recuperação de problemas pelo Telegram",
    "# 12. Quando o Telegram não consegue consertar o Telegram",
    "# 13. Mensagens de erro: como interpretar e reagir",
    "# 16. Glossário essencial",
    "# Referências oficiais",
]
REQUIRED_COMMANDS = [
    "/help", "/commands", "/whoami", "/status", "/context",
    "/new", "/resume", "/model", "/agents", "/stop",
    "/reload-skills", "/reload-mcp", "/restart", "/approve", "/deny",
]
FORBIDDEN = [
    r"sk-[A-Za-z0-9_-]{20,}",
    r"ghp_[A-Za-z0-9]{20,}",
    r"AIza[A-Za-z0-9_-]{20,}",
    r"-----BEGIN (?:RSA |OPENSSH )?PRIVATE KEY-----",
]


def fail(message: str) -> None:
    print(f"FAIL: {message}")
    raise SystemExit(1)


def main() -> None:
    if not GUIDE.exists():
        fail(f"guia ausente: {GUIDE}")
    if not README.exists():
        fail("README.md ausente")
    text = GUIDE.read_text(encoding="utf-8")
    normalized = re.sub(r"\s+", " ", text)
    readme = README.read_text(encoding="utf-8")

    for heading in REQUIRED:
        if re.sub(r"\s+", " ", heading) not in normalized:
            fail(f"seção obrigatória ausente: {heading}")

    for command in REQUIRED_COMMANDS:
        if command not in text:
            fail(f"comando Telegram obrigatório ausente: {command}")

    for pattern in FORBIDDEN:
        if re.search(pattern, text, re.IGNORECASE):
            fail(f"padrão de segredo encontrado: {pattern}")

    urls = re.findall(r"https?://[^\s)>]+", text)
    if len(urls) < 15:
        fail(f"referências insuficientes: {len(urls)} URLs encontradas")
    if f"Versão {VERSION}" not in readme:
        fail(f"README não declara a versão {VERSION}")
    if "CC BY 4.0" not in readme:
        fail("README não declara licença CC BY 4.0")
    if len(text.split()) < 5000:
        fail(f"guia curto demais para a versão {VERSION}")
    if "Telegram-first não significa Telegram-only" not in text:
        fail("o limite estrutural Telegram-first/Telegram-only não está explícito")

    print("PASS: estrutura, seções, referências mínimas e padrões de segredo verificados")
    print(f"INFO: palavras={len(text.split())}; urls={len(urls)}")


if __name__ == "__main__":
    main()
