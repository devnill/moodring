#!/bin/sh
MOOD="${1:-}"
PLUGIN_ROOT="${CLAUDE_PLUGIN_ROOT:-$(cd "$(dirname "$0")/.." && pwd)}"
SETTINGS="${PLUGIN_ROOT}/settings.json"

[ -z "$MOOD" ] && exit 0

# Read settings with defaults
VOLUME=0.2
if [ -f "$SETTINGS" ]; then
    grep -q '"muted" *: *true' "$SETTINGS" && exit 0
    _v=$(grep '"volume":' "$SETTINGS" | sed 's/.*: *\([0-9.]*\).*/\1/')
    VOLUME="${_v:-0.2}"
fi

# Find sound file
SOUND="${PLUGIN_ROOT}/sounds/${MOOD}.wav"
[ -f "$SOUND" ] || exit 0

# Play in background, suppress output
/usr/bin/afplay -v "$VOLUME" "$SOUND" > /dev/null 2>&1 &
exit 0
