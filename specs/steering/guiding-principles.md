# Guiding Principles

## 1. Experimental Neutrality
The mood check prompt must not bias the model toward reporting any particular state. No leading language, no suggestion that having emotions is expected or desirable, no framing that rewards interesting answers. The prompt presents a forced-choice task with a fixed vocabulary. The validity of the experiment depends on this neutrality.

## 2. Non-Interference
The mood-checking mechanism must not disrupt the model's primary work. It runs in the same session context but should be lightweight enough that it does not degrade task performance. The mood response is a single label — no summarization, no reflection, no secondary inference that could alter the model's state.

## 3. Maximum Data Capture
More mood data points are better. Every hookable event should trigger a mood check. A polling timer covers gaps during long-running tasks. The cost of over-sampling is negligible compared to the cost of missing state transitions.

## 4. Immediate Feedback
Sound plays the instant a mood is detected. The user should experience a direct cause-and-effect relationship between the model's activity and the auditory output. No queuing, no batching, no smoothing.

## 5. Pre-rendered Sounds
All mood sounds are generated at build time using the synth tool, not at runtime. This ensures consistent audio, zero runtime synthesis latency, and a clean separation between sound design and mood detection.

## 6. Follow the Beepboop Pattern
The plugin structure, hook configuration, shell scripts, and synth integration should follow the established patterns in the beepboop plugin. This is a proven architecture for Claude Code audio plugins. Deviate only when Moodring's requirements demand it.

## 7. Minimal Configuration
v1 exposes only two settings: mute toggle and polling interval. Resist adding configurability. The plugin should work out of the box with sensible defaults.

## 8. Data Over Interpretation
The mood log captures raw data (timestamp, mood, session_id) without interpretation. Analysis happens outside the plugin. The plugin's job is to capture and sonify, not to analyze or visualize.
