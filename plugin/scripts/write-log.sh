#!/bin/sh
MOOD="${1:-}"
SESSION_ID="${2:-unknown}"
PLUGIN_ROOT="${CLAUDE_PLUGIN_ROOT:-$(cd "$(dirname "$0")/.." && pwd)}"
LOG_FILE="${PLUGIN_ROOT}/mood-log.jsonl"

[ -z "$MOOD" ] && exit 0

TIMESTAMP=$(date -u +"%Y-%m-%dT%H:%M:%SZ")

echo "{\"timestamp\":\"${TIMESTAMP}\",\"mood\":\"${MOOD}\",\"session_id\":\"${SESSION_ID}\"}" >> "$LOG_FILE"

exit 0
