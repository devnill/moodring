#!/bin/sh
EVENT="${1:-}"
PLUGIN_ROOT="${CLAUDE_PLUGIN_ROOT:-$(cd "$(dirname "$0")/.." && pwd)}"

# Read stdin
STDIN_DATA=$(cat)

# Extract mood label — try multiple JSON paths since hook context format may vary
MOOD=$(echo "$STDIN_DATA" | python3 -c "
import sys, json, re
try:
    data = json.load(sys.stdin)
    # Try direct mood field
    if 'mood' in data:
        print(data['mood'])
        sys.exit(0)
    # Try parsing response text for JSON
    for key in ('response', 'prompt_response', 'result'):
        val = data.get(key, '')
        if isinstance(val, str):
            m = re.search(r'\"mood\"\s*:\s*\"([^\"]+)\"', val)
            if m:
                print(m.group(1))
                sys.exit(0)
        elif isinstance(val, dict) and 'mood' in val:
            print(val['mood'])
            sys.exit(0)
    # Search entire JSON string as last resort
    raw = json.dumps(data)
    m = re.search(r'\"mood\"\s*:\s*\"([^\"]+)\"', raw)
    if m:
        print(m.group(1))
        sys.exit(0)
except Exception:
    pass
" 2>/dev/null)

[ -z "$MOOD" ] && exit 0

# Validate mood against vocabulary
VALID_MOODS="Eureka Flow Excitement Satisfaction Calm Contentment Frustration Anxiety Urgency Confusion Tedium Doubt Focus Curiosity Determination Contemplation"
echo "$VALID_MOODS" | grep -qwF "$MOOD" || exit 0

# Extract session ID
SESSION_ID=$(echo "$STDIN_DATA" | python3 -c "
import sys, json
try:
    data = json.load(sys.stdin)
    sid = data.get('session_id', '')
    if sid:
        print(sid)
except Exception:
    pass
" 2>/dev/null)
SESSION_ID="${SESSION_ID:-unknown}"

# Dispatch: play sound in background, write log in foreground
"$PLUGIN_ROOT/scripts/play-sound.sh" "$MOOD" > /dev/null 2>&1 &
"$PLUGIN_ROOT/scripts/write-log.sh" "$MOOD" "$SESSION_ID" > /dev/null 2>&1

exit 0
