# 004: Playback Script

## Objective
Create `scripts/play-sound.sh` that plays the WAV file corresponding to a given mood label, respecting mute and volume settings.

## Acceptance Criteria
- [ ] File `scripts/play-sound.sh` exists and is executable
- [ ] Given argument "Focus", it plays `sounds/Focus.wav`
- [ ] When `settings.json` has `"muted": true`, no sound plays and script exits 0
- [ ] When `settings.json` has `"volume": 0.5`, afplay is called with `-v 0.5`
- [ ] When the mood argument is empty, script exits 0
- [ ] When the WAV file does not exist, script exits 0
- [ ] Sound plays in background (afplay runs with `&`)
- [ ] Script produces no stdout or stderr output

## File Scope
- `scripts/play-sound.sh` (create)

## Dependencies
- Depends on: 001 (settings.json must exist)
- Blocks: 006

## Implementation Notes

```bash
#!/bin/sh
MOOD="${1:-}"
PLUGIN_ROOT="${CLAUDE_PLUGIN_ROOT:-$(cd "$(dirname "$0")/.." && pwd)}"
SETTINGS="${PLUGIN_ROOT}/settings.json"

[ -z "$MOOD" ] && exit 0
[ -f "$SETTINGS" ] || exit 0

# Check muted
grep -q '"muted": *true' "$SETTINGS" && exit 0

# Find sound file
SOUND="${PLUGIN_ROOT}/sounds/${MOOD}.wav"
[ -f "$SOUND" ] || exit 0

# Read volume
VOLUME=$(grep '"volume":' "$SETTINGS" | sed 's/.*: *\([0-9.]*\).*/\1/')
VOLUME="${VOLUME:-0.2}"

# Play in background, suppress output
/usr/bin/afplay -v "$VOLUME" "$SOUND" > /dev/null 2>&1 &
exit 0
```

### Key Decisions
- Uses `/usr/bin/afplay` directly (macOS only per Constraint #1) — no player detection
- Reads settings on every invocation (no caching) so mute/volume changes take effect immediately
- `grep` for muted/volume is intentionally simple — works for the known settings.json format
- All error paths exit 0 to never block Claude Code hook execution
- Stdout/stderr redirected to /dev/null to prevent polluting hook output

## Complexity
Low
