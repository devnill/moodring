# Policies: Audio

## P-1: All sounds pre-rendered at build time; WAV files committed to repository
All 16 mood sounds are generated as WAV files during the build step and committed. No runtime synthesis. The plugin must work without running generate.sh.
- **Derived from**: GP-5 (Pre-rendered Sounds)
- **Established**: planning phase
- **Status**: active

## P-2: Sound playback is immediate and non-blocking
afplay is invoked in the background so sound plays the instant a mood is detected without blocking mood-handler.sh or subsequent processing.
- **Derived from**: GP-4 (Immediate Feedback)
- **Established**: planning phase
- **Status**: active

## P-3: WAV filenames are PascalCase mood labels verbatim
Files are named `<MoodLabel>.wav` (e.g., `Eureka.wav`, `Focus.wav`). Path is constructed as `sounds/${mood}.wav`. No transformation or mapping table required.
- **Derived from**: GP-6 (Follow Beepboop Pattern) + plan/architecture.md (Design Tension #3)
- **Established**: planning phase
- **Status**: active
