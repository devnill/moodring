# Module: Playback

## Scope
Shell script (`scripts/play-sound.sh`) that plays a mood's WAV file using the system audio player. Adapted from beepboop's play-sound.sh but keyed on mood labels instead of hook event names.

NOT responsible for: deciding which mood to play (that comes from `mood-handler`), generating sounds (that is `build`), or logging.

## Provides
- `play-sound.sh` — Shell script at `scripts/play-sound.sh`
  - Invocation: `play-sound.sh <MoodLabel>`
  - Behavior: Plays `sounds/<MoodLabel>.wav` if not muted

## Requires
- `settings.json` (from: `settings`) — Read for `muted`, `volume`, and `player` fields
- WAV files (from: `build`) — Pre-rendered sound files at `sounds/<MoodLabel>.wav`

## Boundary Rules
- Must exit 0 on any error (non-blocking)
- Must check `muted` setting before playback
- Must play sound in background (& suffix) so the script returns immediately
- macOS only for v1 (afplay) per Constraint #1
- Must handle missing WAV files gracefully (skip, exit 0)
- Must not produce any stdout/stderr that could pollute hook output

## Internal Design Notes

### Script Structure (adapted from beepboop)

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

# Play
/usr/bin/afplay -v "$VOLUME" "$SOUND" &
exit 0
```

### Simplifications vs. Beepboop

- No cross-platform player detection needed (macOS only, Constraint #1)
- No fallback sound paths (only mood-keyed WAV files)
- No player caching in settings (hardcoded to afplay)
- Simpler: mood label maps directly to filename

### Volume

Default 0.2 (matching beepboop). Read from `settings.json` on each invocation. No caching — settings could change between calls.
