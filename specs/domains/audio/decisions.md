# Decisions: Audio

## D-1: Pre-render all sounds at build time using the synth tool
- **Decision**: All 16 mood sounds are generated as WAV files at build time via `synth generate` and committed to the repository. No runtime synthesis.
- **Rationale**: Pre-rendering ensures consistent audio, zero runtime synthesis latency, and clean separation between sound design and mood detection.
- **Source**: archive/cycles/001/decision-log.md (DL3); steering/guiding-principles.md GP-5
- **Status**: settled

## D-2: Sound plays immediately, non-blocking via afplay
- **Decision**: `afplay sounds/${mood}.wav &` — invoked in background so playback does not block the handler script.
- **Rationale**: User should experience direct cause-and-effect between model activity and sound. No queuing or batching.
- **Source**: archive/cycles/001/decision-log.md (DL8); steering/guiding-principles.md GP-4
- **Status**: settled

## D-3: Use square waveform as substitute for sawtooth
- **Decision**: urgency() and determination() use square waveforms because the synth tool provides no sawtooth primitive.
- **Rationale**: Closest available waveform. Sawtooth was desired for its bright, driven quality; square is an acceptable approximation.
- **Source**: archive/cycles/001/decision-log.md (DL14); archive/incremental/ work item 002
- **Status**: settled

## D-4: Apply hardcoded defaults when settings.json is absent rather than suppressing playback
- **Decision**: play-sound.sh applies hardcoded defaults (unmuted, volume 0.2) when settings.json is absent. The module spec specified `exit 0` (suppress playback) — this is an intentional deviation.
- **Rationale**: Suppressing playback on missing config violates Principle 4 (Immediate Feedback) and Principle 7 (Minimal Configuration). The plugin should work out of the box.
- **Source**: archive/cycles/001/decision-log.md (DL18); archive/cycles/001/spec-adherence.md (D3)
- **Status**: settled

## D-5: Three sound shape corrections applied during execution
- **Decision**: (a) contemplation() harmonics aligned to 0.8s to fix array shape mismatch; (b) satisfaction() rewritten as major third chord resolving to unison; (c) confusion() detuning widened from 7 Hz to 25 Hz for audible effect.
- **Rationale**: Critical and significant findings from work item 002 incremental review.
- **Source**: archive/cycles/001/decision-log.md (DL15, DL16, DL17)
- **Status**: settled
