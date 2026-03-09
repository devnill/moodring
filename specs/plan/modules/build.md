# Module: Build

## Scope
Build-time pipeline that generates WAV files from sound definitions. Includes `generate.sh` (build script) and `synth.toml` (synth configuration). Also manages the synth git submodule.

NOT responsible for: sound design (that is `sound-definitions`), playback, or plugin runtime behavior.

## Provides
- `generate.sh` — Build script at project root
- `synth.toml` — Synth configuration at project root
- `sounds/*.wav` — 16 generated WAV files (build output, committed to repo)
- `synth/` — Git submodule reference

## Requires
- `moods.py` (from: `sound-definitions`) — Python module with SOUNDS dict
- synth tool (from: git submodule at `~/code/synth`) — Sound generation engine

## Boundary Rules
- Build runs offline, not at plugin runtime (Principle #5, Constraint #11)
- Generated WAV files are committed so the plugin works without running the build
- synth is included as a git submodule (Constraint #10)
- Python 3.11+ required (Constraint #4)
- Output format: WAV at 44100 Hz
- Output directory: `plugin/sounds/`

## Internal Design Notes

### generate.sh

```bash
#!/bin/bash
set -e
cd "$(dirname "$0")"

pip install -e synth/ -q
synth generate --config synth.toml

echo "Done. WAV files written to plugin/sounds/"
```

Identical to beepboop's generate.sh.

### synth.toml

```toml
[synth]
sounds_file = "moods.py"
output_dir = "plugin/sounds"
```

The `sounds_file` points to `moods.py` (instead of beepboop's `sounds.py`). The `output_dir` places WAV files inside the plugin directory where `play-sound.sh` expects them.

### Submodule Setup

```bash
git submodule add ~/code/synth synth
```

### Output Files

The build produces 16 files:
```
plugin/sounds/Eureka.wav
plugin/sounds/Flow.wav
plugin/sounds/Excitement.wav
plugin/sounds/Satisfaction.wav
plugin/sounds/Calm.wav
plugin/sounds/Contentment.wav
plugin/sounds/Frustration.wav
plugin/sounds/Anxiety.wav
plugin/sounds/Urgency.wav
plugin/sounds/Confusion.wav
plugin/sounds/Tedium.wav
plugin/sounds/Doubt.wav
plugin/sounds/Focus.wav
plugin/sounds/Curiosity.wav
plugin/sounds/Determination.wav
plugin/sounds/Contemplation.wav
```

File naming matches the SOUNDS dict keys exactly. The synth tool uses dict keys as filenames.
