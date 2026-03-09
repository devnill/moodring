# Module: Mood Handler

## Scope
The central dispatch script (`scripts/mood-handler.sh`) that receives a mood label and triggers both sound playback and log writing. This is the command hook's entry point.

NOT responsible for: mood detection (that is the prompt hook's job), sound playback mechanics (delegated to `playback`), log format details (delegated to `mood-log`), or settings management.

## Provides
- `mood-handler.sh` — Shell script at `scripts/mood-handler.sh`
  - Invocation: `mood-handler.sh <EventName>`
  - Stdin: Hook context JSON (includes prompt hook response with mood label)
  - Behavior: Extracts mood label, calls play-sound.sh and write-log.sh

## Requires
- `play-sound.sh` (from: `playback`) — Called with mood label to play sound
- `write-log.sh` (from: `mood-log`) — Called with mood label and session ID to write log
- `settings.json` (from: `settings`) — Read to check `muted` state

## Boundary Rules
- Must parse the mood label from stdin JSON reliably
- Must validate the mood label against the 16-label vocabulary
- Must exit cleanly (exit 0) on any error — hook scripts must never block Claude Code
- Must not perform any inference or model interaction
- Must handle missing or malformed input gracefully
- Sound playback runs in background (non-blocking)
- Log writing is synchronous (must complete before exit to avoid data loss)

## Internal Design Notes

### Input Parsing

The script receives hook context on stdin as JSON. The mood label is extracted from the prompt hook's response within that context. The exact JSON path depends on Claude Code's hook data format.

Expected extraction approach using Python one-liner or jq:

```bash
MOOD=$(echo "$STDIN_DATA" | python3 -c "
import sys, json
data = json.load(sys.stdin)
# Extract mood from prompt hook response
# Exact path TBD based on hook system's data format
response = data.get('prompt_response', data.get('response', ''))
if isinstance(response, str):
    parsed = json.loads(response)
else:
    parsed = response
print(parsed.get('mood', ''))
")
```

### Validation

```bash
VALID_MOODS="Eureka Flow Excitement Satisfaction Calm Contentment Frustration Anxiety Urgency Confusion Tedium Doubt Focus Curiosity Determination Contemplation"
echo "$VALID_MOODS" | grep -qw "$MOOD" || exit 0
```

### Dispatch

```bash
# Play sound (background, non-blocking)
"$PLUGIN_ROOT/scripts/play-sound.sh" "$MOOD" &

# Write log (foreground, must complete)
"$PLUGIN_ROOT/scripts/write-log.sh" "$MOOD" "$SESSION_ID"
```

### Session ID

Extracted from stdin JSON context or `CLAUDE_SESSION_ID` environment variable. Falls back to `unknown` if neither is available.

### Error Handling

Every failure path exits with code 0. A hook script that exits non-zero could disrupt Claude Code's operation. Errors are silently swallowed — this aligns with the non-interference principle.
