# Module: Settings

## Scope
Defines the `settings.json` file that controls runtime configuration. Contains mute toggle, polling interval, volume, and player path.

NOT responsible for: reading or writing settings at runtime (consumers read it directly), or providing a UI for settings changes (that is `config-skill`).

## Provides
- `settings.json` — Configuration file at plugin root with default values

## Requires
Nothing. This module has no dependencies on other modules.

## Boundary Rules
- Only two user-facing settings in v1: `muted` and `poll_interval` (Principle #7)
- `volume` and `player` are internal/advanced settings (carried over from beepboop pattern)
- File is JSON, human-readable and hand-editable
- Must ship with sensible defaults that work out of the box

## Internal Design Notes

### Default settings.json

```json
{
  "muted": false,
  "poll_interval": "5m",
  "volume": 0.2,
  "player": ""
}
```

### Field Definitions

| Field | Type | Default | Description |
|-------|------|---------|-------------|
| `muted` | boolean | `false` | When true, `play-sound.sh` skips playback. Logging still occurs. |
| `poll_interval` | string | `"5m"` | Duration string for the `/moodring:loop` polling interval. Parsed by the loop skill. Supports `s`, `m`, `h` suffixes. |
| `volume` | number | `0.2` | Playback volume passed to afplay (0.0-1.0). |
| `player` | string | `""` | Audio player path. Empty string means use default (`/usr/bin/afplay` on macOS). |

### Differences from Beepboop

- `sounds_enabled` renamed to `muted` (inverted semantics, simpler naming)
- `poll_interval` is new (beepboop has no polling)
- No `notifications_enabled` (moodring has no notification system)
- No `hook_sounds` map (moodring keys sounds by mood, not by hook event)
