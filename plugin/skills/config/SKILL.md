---
description: Configure moodring plugin settings
argument-hint: "[show | mute | unmute | interval <duration> | volume <0.0-1.0>]"
allowed-tools: Read, Edit, Bash
---

Manage the moodring plugin configuration.

## Locate Settings File

First, resolve the settings file path:
1. If `CLAUDE_PLUGIN_ROOT` is set, use `${CLAUDE_PLUGIN_ROOT}/settings.json`
2. Otherwise, run: `find ~/.claude/plugins -path "*/moodring/settings.json" 2>/dev/null | head -1`
3. If neither works, report that the settings file could not be found and stop.

## Actions

**Before any write action:** Always use the Read tool to read the full contents of settings.json first. The Edit tool requires the exact current text to replace.

**No args or "show":** Read settings.json and display:
- Muted: Yes/No
- Poll interval: value
- Volume: value

**"mute":** Read settings.json, then use the Edit tool to change `"muted": false` to `"muted": true`.

**"unmute":** Read settings.json, then use the Edit tool to change `"muted": true` to `"muted": false`.

**"interval <duration>":** Read settings.json, then use the Edit tool to replace the current `poll_interval` value with the given value (e.g., "5m", "30s", "1h").

**"volume <value>":** Read settings.json, then use the Edit tool to replace the current `volume` value with the given float (0.0-1.0).

After any change, confirm what was updated and show the new value.
