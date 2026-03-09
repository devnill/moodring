# Constraints

## Technology Constraints
1. **macOS audio playback via afplay.** Sound playback uses the macOS `afplay` utility. No cross-platform audio abstraction required for v1.
2. **Synth tool for sound generation.** All sounds are generated using the `synth` tool at `~/code/synth`. Sound definitions are Python functions using synth primitives (sine, square, sweep, fm, adsr, seq, silence). Output is WAV files at 44100 Hz.
3. **Claude Code plugin system.** The plugin must conform to the Claude Code plugin directory structure: `.claude-plugin/plugin.json` manifest, `hooks/hooks.json` for hook configuration, `skills/` for any slash commands, `scripts/` for shell scripts.
4. **Python 3.11+ for sound definitions.** The synth tool requires Python 3.11+ with numpy and scipy.
5. **Shell scripts (bash/zsh) for runtime.** Hook handlers and playback scripts run as shell commands on macOS.

## Design Constraints
6. **Prompt-type hooks for mood capture.** Mood checks use `"type": "prompt"` hooks to run in the same Claude session context. This is non-negotiable — the experiment requires the same model instance.
7. **Fixed 16-mood vocabulary.** The mood palette is fixed at 16 labels. The model chooses from this list. No free-form mood expression.
8. **JSONL log format.** Mood log entries are JSON objects with exactly three fields: `timestamp` (ISO 8601), `mood` (string from the 16-mood vocabulary), `session_id` (string). One entry per line.
9. **No secondary inference.** The mood check must not trigger summarization, reflection, or any task that could influence the model's state. Single label response only.

## Process Constraints
10. **Synth as git submodule.** Following beepboop's pattern, synth should be included as a git submodule, not vendored or installed globally.
11. **Build-time sound generation.** A `generate.sh` script runs `synth generate` to produce WAV files. These are committed to the plugin directory so the plugin works without running the build step.

## Scope Constraints
12. **No mood analysis or visualization.** The plugin captures and sonifies moods. It does not analyze trends, generate reports, or provide dashboards. That is a separate tool.
13. **No cross-model comparison.** v1 does not include tooling to compare moods across different models. The JSONL format enables this externally.
14. **No prompt customization in v1.** The mood check prompt is hardcoded. Future revisions may make it configurable.
