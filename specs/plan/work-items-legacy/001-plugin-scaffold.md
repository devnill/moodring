# 001: Plugin Scaffold

## Objective
Create the plugin directory structure, manifest, and default settings file so the plugin is recognized by Claude Code.

## Acceptance Criteria
- [ ] File `.claude-plugin/plugin.json` exists with `name` = `"moodring"`, `version` = `"1.0.0"`
- [ ] File `settings.json` exists with keys: `muted` (false), `poll_interval` ("5m"), `volume` (0.2), `player` ("")
- [ ] Directory `hooks/` exists
- [ ] Directory `scripts/` exists
- [ ] Directory `skills/` exists
- [ ] Directory `sounds/` exists
- [ ] `plugin.json` contains `"hooks": "./hooks/hooks.json"`

## File Scope
- `.claude-plugin/plugin.json` (create)
- `settings.json` (create)
- `hooks/` (create directory)
- `scripts/` (create directory)
- `skills/` (create directory)
- `sounds/` (create directory)

## Dependencies
- Depends on: none
- Blocks: 004, 007, 009

## Implementation Notes

### plugin.json
```json
{
  "name": "moodring",
  "description": "Sonifies an AI model's self-reported internal state by playing mood-mapped synthesized sounds",
  "version": "1.0.0",
  "author": { "name": "dan" },
  "license": "MIT",
  "hooks": "./hooks/hooks.json"
}
```

### settings.json
```json
{
  "muted": false,
  "poll_interval": "5m",
  "volume": 0.2,
  "player": ""
}
```

The plugin root is the directory containing `.claude-plugin/`. All paths in hooks and scripts use `${CLAUDE_PLUGIN_ROOT}` to reference files relative to this root.

## Complexity
Low
