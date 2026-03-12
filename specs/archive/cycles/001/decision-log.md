## Decision Log

### Planning Phase

#### DL1: Adopt the beepboop plugin pattern as the structural template
- **When**: Planning — interview Q4 / guiding principle 6
- **Decision**: Moodring's plugin structure, hook configuration, shell scripts, and synth integration must follow the established patterns in the beepboop plugin.
- **Rationale**: Beepboop is a proven architecture for Claude Code audio plugins. Deviating without cause adds risk.

#### DL2: Use a fixed 16-mood vocabulary spanning the valence-arousal space
- **When**: Planning — interview Q3
- **Decision**: The mood palette is fixed at 16 labels organized across the valence-arousal space. The model selects freely from this set at each prompt.
- **Rationale**: A fixed vocabulary ensures consistent logging and sound mapping.

#### DL3: Pre-render all sounds at build time using the synth tool
- **When**: Planning — interview Q2 / guiding principle 5
- **Decision**: All 16 mood sounds are generated as WAV files at build time and committed to the repository. No runtime synthesis.
- **Rationale**: Pre-rendering ensures consistent audio, zero runtime synthesis latency, and clean separation between sound design and mood detection.

#### DL4: Capture mood on every hookable Claude Code lifecycle event
- **When**: Planning — interview Q4 / guiding principle 3
- **Decision**: All 18 Claude Code lifecycle events receive a prompt-type hook for mood capture. Frequency is not a constraint.
- **Rationale**: The cost of over-sampling is negligible compared to the cost of missing state transitions.

#### DL5: Use prompt-type hooks for mood elicitation followed by command hooks for dispatch
- **When**: Planning — architecture design / Design Tension #1
- **Decision**: Each lifecycle event gets a prompt hook that elicits the mood label, followed by a command hook that runs mood-handler.sh. The architecture assumes the prompt hook's response is available in the stdin JSON passed to the subsequent command hook.
- **Rationale**: Most direct path from mood elicitation to sound dispatch within the Claude Code hook system.
- **Alternatives rejected**: (a) Model calls Bash tool directly — violates non-interference; (b) Background scraping — loses immediacy; (c) External LLM API — requires different model instance.

#### DL6: Adopt a neutral forced-choice prompt framing
- **When**: Planning — interview Q5 / guiding principle 1
- **Decision**: The mood prompt uses neutral language with no suggestion that having emotions is expected or desirable.
- **Rationale**: Experimental neutrality is foundational. Any bias invalidates the data.

#### DL7: Log only timestamp, mood, and session_id — no task summarization
- **When**: Planning — interview Q6 / guiding principle 8
- **Decision**: Each log entry contains exactly three fields. No task context is captured.
- **Rationale**: Summarizing task context would require a secondary inference step that could influence mood state.

#### DL8: Sound plays immediately and non-blocking via afplay
- **When**: Planning — interview Q7 / guiding principle 4
- **Decision**: afplay is invoked in the background so sound plays immediately without blocking.

#### DL9: Expose only mute toggle and polling interval as v1 configuration
- **When**: Planning — interview Q8 / guiding principle 7
- **Decision**: settings.json exposes only two user-facing settings: muted and poll_interval.

#### DL10: Use PascalCase mood labels directly as WAV filenames
- **When**: Planning — architecture design / Design Tension #3
- **Decision**: WAV files are named after mood labels verbatim (e.g., Eureka.wav). Path constructed as `sounds/${mood}.wav`.

#### DL11: Accept approximate polling in the loop skill
- **When**: Planning — architecture design / Design Tension #5
- **Decision**: The /moodring:loop skill is model-driven. The poll interval is advisory, not a precise timer.

#### DL12: Start with prompt hooks on all 18 events; downgrade if specific events cause issues
- **When**: Planning — architecture design / Design Tension #6

#### DL13: Resolve session_id from CLAUDE_SESSION_ID env var with "unknown" fallback
- **When**: Planning — architecture design / Design Tension #4
- **Decision**: write-log.sh uses `${CLAUDE_SESSION_ID:-unknown}`.

---

### Execution Phase

#### DL14: Accept square waveform as substitute for sawtooth
- **When**: Execution — work item 002, incremental review
- **Decision**: urgency() and determination() use square waveforms because the synth tool has no sawtooth primitive.

#### DL15: Fix contemplation array shape by aligning harmonic duration to 0.8s
- **When**: Execution — work item 002, critical finding C1

#### DL16: Fix satisfaction to use a major third chord resolving to unison
- **When**: Execution — work item 002, significant finding S3

#### DL17: Widen confusion() detuning from 7 Hz to 25 Hz
- **When**: Execution — work item 002, minor finding M3

#### DL18: Apply defaults when settings.json is absent rather than suppressing playback
- **When**: Execution — work item 004, significant finding S1
- **Decision**: play-sound.sh applies hardcoded defaults (unmuted, volume 0.2) when settings.json is absent.
- **Rationale**: Suppressing playback on missing settings violates Principles 4 (Immediate Feedback) and 7 (Minimal Configuration).
- **Deviation**: This intentionally deviates from the playback module spec which specified `exit 0`.

#### DL19: Use grep -qwF (fixed-string matching) for mood validation
- **When**: Execution — work item 006, critical finding C1
- **Rationale**: Defense against regex injection on mood label input.

#### DL20: Suppress stdout/stderr from write-log.sh invocation
- **When**: Execution — work item 006, significant finding S1

#### DL21: Add CLAUDE_PLUGIN_ROOT fallback path resolution to config skill
- **When**: Execution — work item 009, significant finding S1

#### DL22: Add explicit Read-before-Edit instruction to config skill
- **When**: Execution — work item 009, significant finding S2

#### DL23: Fix loop skill prompt text to include JSON response instruction
- **When**: Execution — work item 008, significant finding S1

---

### Review Phase

#### DL24: Accept two spec documentation inconsistencies as documentation errors
- **When**: Review — spec-adherence findings D1, D2
- **Decision**: architecture.md showing `commands/` instead of `skills/` and synth.toml output_dir showing `"plugin/sounds"` instead of `"sounds"` are documentation errors, not implementation errors.

---

## Open Questions

### OQ1: Loop skill lacks CLAUDE_PLUGIN_ROOT fallback that config skill has
- **Source**: Code-quality S1; incremental review 009
- **Impact**: Loop skill fails silently when CLAUDE_PLUGIN_ROOT is unset.
- **Resolution**: Add the find-based fallback pattern from config skill.

### OQ2: Hook data-passing assumption is unvalidated
- **Source**: Architecture Design Tension #1; gap-analysis II1
- **Impact**: If prompt hook responses are NOT passed to command hooks, the primary 18-event capture path produces nothing. Total silent failure.
- **Resolution**: Test with a minimal prompt+command hook pair.

### OQ3: CLAUDE_SESSION_ID availability is undocumented
- **Source**: Architecture Design Tension #4; gap-analysis II2
- **Impact**: If not exported, every log entry carries session_id = "unknown". Session-level analysis is impossible.

### OQ4: Three documentation files inconsistent with implementation
- **Source**: Spec-adherence D1, D2, D3, R1, R2, R3
- **Impact**: Future contributors receive incorrect information.

### OQ5: No README exists
- **Source**: Gap-analysis MI1

### OQ6: No .gitignore; __pycache__ already present
- **Source**: Gap-analysis MI2; code-quality M1

---

## Cross-References

### CR1: CLAUDE_PLUGIN_ROOT asymmetry between loop and config skills
Code review S1 + incremental review 009 S1. The config skill fix (DL21) was not propagated to the loop skill. OQ1 tracks remediation.

### CR2: Hook data-passing — the central architectural assumption
Gap analysis II1 + Architecture Design Tension #1 + DL5. No reviewer found evidence the assumption was validated. OQ2 tracks resolution.

### CR3: Session ID and log data quality
Gap analysis II2 + DL13 + DL7. If OQ3 is not resolved, the session grouping dimension is permanently lost.

### CR4: play-sound.sh spec deviation
Spec-adherence D3 + DL18. Intentional deviation driven by Principles 4 and 7. OQ4 tracks documentation update.

### CR5: Build artifacts and repository hygiene
Code review M1 + M2 + gap analysis MI2. Three reviewers converge on missing .gitignore. OQ6 tracks remediation.
