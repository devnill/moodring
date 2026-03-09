# Moodring

## What We Are Building
Moodring is a Claude Code plugin that sonifies an AI model's self-reported internal state. Inspired by the question of whether frontier language models experience something analogous to mood or affect, Moodring treats the problem empirically: it periodically asks the model to label its current state from a fixed vocabulary of 16 moods, plays a corresponding synthesized sound, and logs the result.

The plugin hooks into Claude Code's lifecycle events — every tool use, every task completion, every session boundary — and fires a neutral prompt asking the model to choose a mood label. Each mood maps to a pre-rendered WAV file designed using psychoacoustic research (the Bouba/Kiki effect, valence-arousal models, sound-emotion correspondences). The sound plays immediately via macOS `afplay`, giving the user a real-time auditory signal of the model's self-reported state. A JSONL log captures every mood data point with timestamp and session ID for offline analysis.

The 16-mood palette spans the full valence-arousal space: from Eureka and Flow (positive, high arousal) through Calm and Contentment (positive, low arousal) to Frustration and Anxiety (negative, high arousal) and Tedium and Doubt (negative, low arousal), plus cross-cutting states like Focus, Curiosity, Determination, and Contemplation.

## Key Components
- **Hook Configuration** — Prompt-type hooks on every Claude Code lifecycle event to capture mood
- **Mood Prompt** — Neutrally-framed forced-choice prompt presenting 16 mood labels
- **Mood Handler** — Central dispatch script that receives a mood label and triggers playback + logging
- **Sound Playback** — `afplay`-based WAV playback with volume and mute controls
- **Mood Log** — Append-only JSONL file recording timestamp, mood, and session ID
- **Sound Definitions** — 16 Python functions defining synthesizer parameters per mood
- **Build Pipeline** — `synth` tool integration for pre-rendering WAV files
- **Loop Skill** — `/moodring:loop` command for periodic polling during long tasks
- **Config Skill** — `/moodring:config` command for mute and interval settings

## Project Structure
```
moodring/
├── .claude-plugin/
│   └── plugin.json
├── hooks/
│   └── hooks.json
├── scripts/
│   ├── mood-handler.sh
│   ├── play-sound.sh
│   └── write-log.sh
├── skills/
│   ├── loop/
│   │   └── SKILL.md
│   └── config/
│       └── SKILL.md
├── sounds/
│   └── <Mood>.wav (x16)
├── settings.json
├── mood-log.jsonl (runtime)
├── moods.py
├── synth.toml
├── generate.sh
└── synth/ (git submodule)
```

## Workflow
1. User installs the Moodring plugin into Claude Code
2. On every lifecycle event, a prompt hook asks Claude to choose a mood
3. The mood label triggers immediate sound playback and a log entry
4. For long-running tasks, the user invokes `/moodring:loop` for periodic polling
5. The user can mute sounds or adjust interval via `/moodring:config`
6. The `mood-log.jsonl` file accumulates data for offline analysis across sessions and models
