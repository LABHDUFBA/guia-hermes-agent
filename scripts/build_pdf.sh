#!/usr/bin/env bash
set -euo pipefail

ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
cd "$ROOT"
VERSION="${1:-1.2}"
SOURCE="$ROOT/docs/guia-hermes-agent-v${VERSION}.md"
OUTPUT_DIR="$ROOT/releases/v${VERSION}"
OUTPUT="$OUTPUT_DIR/guia-hermes-agent-labhdufba-v${VERSION}.pdf"
CSS="$ROOT/styles/labhd.css"

mkdir -p "$OUTPUT_DIR"

pandoc "$SOURCE" \
  --from markdown+raw_html+link_attributes \
  --to html5 \
  --standalone \
  --metadata title="Guia Hermes Agent no Telegram — LABHDUFBA" \
  --css "$CSS" \
  --pdf-engine=weasyprint \
  --output "$OUTPUT"

printf 'PDF criado: %s\n' "$OUTPUT"
