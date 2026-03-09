# 003: Build Pipeline

## Objective
Set up the synth git submodule, synth.toml configuration, and generate.sh build script. Run the build to produce 16 WAV files in the sounds/ directory.

## Acceptance Criteria
- [ ] Directory `synth/` exists as a git submodule pointing to `~/code/synth`
- [ ] File `synth.toml` exists with `sounds_file = "moods.py"` and `output_dir = "sounds"`
- [ ] File `generate.sh` exists and is executable (`chmod +x`)
- [ ] Running `./generate.sh` produces 16 WAV files in `sounds/`
- [ ] All 16 WAV files exist: `Eureka.wav`, `Flow.wav`, `Excitement.wav`, `Satisfaction.wav`, `Calm.wav`, `Contentment.wav`, `Frustration.wav`, `Anxiety.wav`, `Urgency.wav`, `Confusion.wav`, `Tedium.wav`, `Doubt.wav`, `Focus.wav`, `Curiosity.wav`, `Determination.wav`, `Contemplation.wav`
- [ ] Each WAV file is non-empty and playable via `afplay`

## File Scope
- `synth/` (create — git submodule)
- `synth.toml` (create)
- `generate.sh` (create)
- `sounds/*.wav` (create — 16 generated files)

## Dependencies
- Depends on: 002 (moods.py must exist for synth to generate sounds)
- Blocks: 004

## Implementation Notes

### synth.toml
```toml
[synth]
sounds_file = "moods.py"
output_dir = "sounds"
```

### generate.sh
```bash
#!/bin/bash
set -e
cd "$(dirname "$0")"

pip install -e synth/ -q
synth generate --config synth.toml

echo "Done. WAV files written to sounds/"
```

### Submodule Setup
```bash
cd /Users/dan/code/moodring/plugin
git submodule add ~/code/synth synth
```

Note: The submodule lives inside the plugin directory, alongside moods.py and synth.toml. The generate.sh script `cd`s to its own directory before running.

### Build Verification
After running generate.sh, verify each WAV file:
```bash
for f in sounds/*.wav; do
  afplay -v 0.1 "$f"  # Quick playback test
done
```

## Complexity
Medium
