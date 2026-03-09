---
description: Configure moodring plugin settings
argument-hint: "[show | mute | unmute | interval <duration> | volume <0.0-1.0>]"
allowed-tools: Read, Edit, Bash
---

Manage the moodring plugin configuration.

Settings file location: `${CLAUDE_PLUGIN_ROOT}/settings.json`

## Actions

**No args or "show":** Read settings.json and display:
- Muted: Yes/No
- Poll interval: value
- Volume: value

**"mute":** Set `muted` to `true` in settings.json using the Edit tool.

**"unmute":** Set `muted` to `false` in settings.json using the Edit tool.

**"interval <duration>":** Set `poll_interval` to the given value (e.g., "5m", "30s", "1h") using the Edit tool.

**"volume <value>":** Set `volume` to the given float (0.0-1.0) using the Edit tool.

After any change, confirm what was updated and show the new value.
