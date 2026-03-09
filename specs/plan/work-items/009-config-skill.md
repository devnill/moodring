# 009: Config Skill

## Objective
Create the `/moodring:config` skill that allows users to view and modify plugin settings (mute, poll interval, volume).

## Acceptance Criteria
- [ ] File `skills/config/SKILL.md` exists
- [ ] Skill has `description` and `allowed-tools` frontmatter fields
- [ ] `allowed-tools` includes `Read`, `Edit`, `Bash`
- [ ] Skill has `argument-hint` field showing available subcommands
- [ ] With no args or "show": displays current muted state, poll interval, and volume
- [ ] With "mute": sets `muted` to `true` in settings.json
- [ ] With "unmute": sets `muted` to `false` in settings.json
- [ ] With "interval <duration>": sets `poll_interval` to the given value
- [ ] With "volume <value>": sets `volume` to the given float
- [ ] After any change, confirms what was updated

## File Scope
- `skills/config/SKILL.md` (create)

## Dependencies
- Depends on: 001 (settings.json must exist)
- Blocks: none

## Implementation Notes

### SKILL.md Content
```markdown
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
```

### Key Design Decisions
- Uses Edit tool for settings changes (preserves rest of JSON, shows diff to user)
- Exposes `volume` as an advanced option even though Principle #7 says minimal config — volume control is natural for audio
- Does not expose `player` setting — that remains internal/advanced
- `${CLAUDE_PLUGIN_ROOT}` resolves to the installed plugin path, not the source repo

## Complexity
Low
