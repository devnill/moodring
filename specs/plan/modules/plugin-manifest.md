# Module: Plugin Manifest

## Scope
Defines the plugin identity for Claude Code's plugin system. This is the `.claude-plugin/plugin.json` file that registers Moodring as a plugin.

NOT responsible for: hook configuration, settings, or any runtime behavior.

## Provides
- `plugin.json` — Plugin manifest file at `.claude-plugin/plugin.json`

## Requires
Nothing. This module has no dependencies on other modules.

## Boundary Rules
- Must conform to Claude Code's plugin manifest schema
- Contains only static metadata: name, version, description, author, license
- No runtime logic

## Internal Design Notes

```json
{
  "name": "moodring",
  "version": "1.0.0",
  "description": "Sonifies an AI model's self-reported internal state by playing mood-mapped synthesized sounds",
  "author": { "name": "dan" },
  "license": "MIT"
}
```

Follows the exact structure of beepboop's `plugin.json`.
