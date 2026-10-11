#!/usr/bin/env python3
"""Validação determinística do Guia Hermes Agent do LABHDUFBA."""
from __future__ import annotations

import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
GUIDE = ROOT / "docs" / "guia-hermes-agent-v1.1.md"
README = ROOT / "README.md"
REQUIRED = [
    "# Como usar este guia",
    "# 1. Antes de instalar: onde o Hermes vai rodar?",
    "# 2. Instalação do Hermes Agent",
    "# 4. Modelo, provedor, API, contexto e tokens",
    "# 6. Skills: procedimentos reutilizáveis",
    "# 7. SOUL.md, arquivos de contexto e personalidade",
    "# 8. Memória, histórico e MemPalace",
    "# 10. MCP: conectando ferramentas externas",
    "# 11. Agentes, subagentes e orquestração",
    "# 12. Gateway: Hermes no Telegram, Discord e outras plataformas",
    "# 13. Cron: automatizando tarefas",
    "# 15. Troubleshooting: problemas comuns",
    "# 16. Glossário essencial",
    "# Referências oficiais",
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

    for pattern in FORBIDDEN:
        if re.search(pattern, text, re.IGNORECASE):
            fail(f"padrão de segredo encontrado: {pattern}")

    urls = re.findall(r"https?://[^\s)>]+", text)
    if len(urls) < 18:
        fail(f"referências insuficientes: {len(urls)} URLs encontradas")
    if "Versão 1.1" not in readme:
        fail("README não declara a versão 1.1")
    if "CC BY 4.0" not in readme:
        fail("README não declara licença CC BY 4.0")
    if len(text.split()) < 3000:
        fail("guia curto demais para a versão 1.1")

    print("PASS: estrutura, seções, referências mínimas e padrões de segredo verificados")
    print(f"INFO: palavras={len(text.split())}; urls={len(urls)}")


if __name__ == "__main__":
    main()
