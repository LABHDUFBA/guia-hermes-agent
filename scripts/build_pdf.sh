#!/usr/bin/env bash
set -euo pipefail

ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
cd "$ROOT"
SOURCE="$ROOT/docs/guia-hermes-agent-v1.1.md"
OUTPUT_DIR="$ROOT/releases/v1.1"
OUTPUT="$OUTPUT_DIR/guia-hermes-agent-labhdufba-v1.1.pdf"
CSS="$ROOT/styles/labhd.css"

mkdir -p "$OUTPUT_DIR"

pandoc "$SOURCE" \
  --from markdown+raw_html+link_attributes \
  --to html5 \
  --standalone \
  --metadata title="Guia Hermes Agent do LABHDUFBA" \
  --css "$CSS" \
  --pdf-engine=weasyprint \
  --output "$OUTPUT"

printf 'PDF criado: %s\n' "$OUTPUT"
