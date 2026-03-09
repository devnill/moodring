# Module: Config Skill

## Scope
Defines the `/moodring:config` slash command for managing plugin settings. Allows users to toggle mute, set poll interval, and view current configuration.

NOT responsible for: the settings schema (that is `settings`), or any runtime behavior beyond settings management.

## Provides
- `config.md` — Skill definition at `commands/config.md`
  - Slash command: `/moodring:config`
  - Behavior: Read and modify settings.json

## Requires
- `settings.json` (from: `settings`) — The file to read and modify

## Boundary Rules
- Only exposes the two user-facing settings: `muted` and `poll_interval` (Principle #7)
- Volume and player are available as advanced options but not prominently surfaced
- Must confirm changes after making them
- Must show current settings when invoked with no arguments

## Internal Design Notes

### Skill Definition (commands/config.md)

```markdown
---
description: Configure moodring plugin settings
argument-hint: "[show | mute | unmute | interval <duration> | volume <0.0-1.0>]"
allowed-tools: Read, Edit, Bash
---

Manage the moodring plugin configuration.

Find the settings file:
```bash
find ~/.claude/plugins/cache/moodring -name "settings.json" | sort -V | tail -1
```

Use the path returned above for all read/write operations.

## Actions

**No args or "show":** Read settings.json and display:
- Muted: Yes/No
- Poll interval: value
- Volume: value

**"mute":** Set `muted` to `true`

**"unmute":** Set `muted` to `false`

**"interval <duration>":** Set `poll_interval` to the given value (e.g., "5m", "30s", "1h")

**"volume <value>":** Set `volume` to the given float (0.0-1.0)

After any change, confirm what was updated and show the new value.
```

### Differences from Beepboop Config

- Simpler: fewer settings to manage
- No hook-sound mapping (moods map to sounds, not configurable)
- No notifications toggle
- Mute/unmute instead of enable/disable sounds
