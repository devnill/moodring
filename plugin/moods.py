"""Sound definitions for 16 mood labels.

Each function returns a numpy array of audio samples at 44100 Hz.
"""

import numpy as np
from synth import sine, square, sweep, fm, adsr, seq, silence


def eureka() -> np.ndarray:
    """Bright ascending FM burst — breakthrough discovery."""
    burst = adsr(fm(800, 800, 5, 0.15), 0.003, 0.04, 0.5, 0.08)
    note1 = adsr(sine(800, 0.10), 0.005, 0.04, 0.3, 0.04)
    note2 = adsr(sine(1000, 0.10), 0.005, 0.04, 0.3, 0.04)
    note3 = adsr(sine(1200, 0.15), 0.005, 0.04, 0.5, 0.08)
    return seq(burst, silence(0.02), note1, silence(0.02), note2, silence(0.02), note3)


def flow() -> np.ndarray:
    """Warm layered sines, steady pulse, open fifths."""
    root = adsr(sine(350, 0.8), 0.08, 0.15, 0.7, 0.2)
    fifth = adsr(sine(525, 0.8), 0.08, 0.15, 0.6, 0.2)
    return root + 0.6 * fifth


def excitement() -> np.ndarray:
    """Bouncy ascending bursts, fast syncopated, rising."""
    t1 = adsr(sine(500, 0.06), 0.005, 0.02, 0.4, 0.02)
    t2 = adsr(sine(700, 0.06), 0.005, 0.02, 0.4, 0.02)
    t3 = adsr(sine(900, 0.06), 0.005, 0.02, 0.4, 0.02)
    t4 = adsr(sine(1100, 0.08), 0.005, 0.02, 0.5, 0.03)
    t5 = adsr(sine(1200, 0.10), 0.005, 0.03, 0.5, 0.04)
    gap = silence(0.015)
    return seq(t1, gap, t2, gap, t3, gap, t4, gap, t5)


def satisfaction() -> np.ndarray:
    """Warm sine, resolving major third to unison."""
    root = adsr(sine(300, 0.35), 0.05, 0.08, 0.7, 0.15)
    third = adsr(sine(375, 0.35), 0.05, 0.08, 0.5, 0.15)
    chord = root + 0.6 * third
    resolve = adsr(sine(300, 0.45), 0.05, 0.10, 0.7, 0.25)
    return seq(chord, resolve)


def calm() -> np.ndarray:
    """Pure low sine, very slow, breathing envelope."""
    return adsr(sine(200, 1.2), 0.3, 0.15, 0.6, 0.4)


def contentment() -> np.ndarray:
    """Sine+triangle layer, gentle rocking, major sixth."""
    root = adsr(sine(300, 0.6), 0.06, 0.10, 0.7, 0.15)
    sixth = adsr(sine(500, 0.6), 0.06, 0.10, 0.5, 0.15)
    return root + 0.5 * sixth


def frustration() -> np.ndarray:
    """Square wave, buzzy, tritone interval."""
    hit1 = adsr(square(350, 0.12), 0.003, 0.03, 0.6, 0.02)
    hit2 = adsr(square(494, 0.12), 0.003, 0.03, 0.6, 0.02)
    gap = silence(0.01)
    return seq(hit1, gap, hit2, gap, hit1, gap, hit2)


def anxiety() -> np.ndarray:
    """FM inharmonic, jittery, oscillating pitch."""
    jitter1 = adsr(fm(500, 730, 8, 0.08), 0.003, 0.02, 0.4, 0.02)
    jitter2 = adsr(fm(600, 870, 9, 0.08), 0.003, 0.02, 0.4, 0.02)
    jitter3 = adsr(fm(450, 680, 7, 0.08), 0.003, 0.02, 0.4, 0.02)
    gap = silence(0.01)
    return seq(jitter1, gap, jitter2, gap, jitter3, gap, jitter1, gap, jitter2)


def urgency() -> np.ndarray:
    """Sawtooth-like, very fast driving, rising."""
    pulse1 = adsr(square(600, 0.06), 0.003, 0.02, 0.5, 0.01)
    pulse2 = adsr(square(800, 0.06), 0.003, 0.02, 0.5, 0.01)
    pulse3 = adsr(square(1000, 0.06), 0.003, 0.02, 0.5, 0.01)
    pulse4 = adsr(square(1200, 0.08), 0.003, 0.02, 0.5, 0.02)
    gap = silence(0.01)
    return seq(pulse1, gap, pulse2, gap, pulse3, gap, pulse4, gap, pulse1, gap, pulse4)


def confusion() -> np.ndarray:
    """Detuned oscillators, wandering, irregular."""
    detune = adsr(sine(400, 0.35), 0.02, 0.05, 0.6, 0.08)
    detune2 = adsr(sine(425, 0.35), 0.02, 0.05, 0.5, 0.08)
    wander = adsr(sweep(350, 450, 0.25), 0.02, 0.05, 0.5, 0.08)
    layer = detune + 0.8 * detune2
    return seq(layer, wander)


def tedium() -> np.ndarray:
    """Static square, low, metronomic, flat, unchanging."""
    pulse = adsr(square(180, 0.08), 0.005, 0.02, 0.7, 0.02)
    gap = silence(0.04)
    return seq(pulse, gap, pulse, gap, pulse, gap, pulse, gap, pulse)


def doubt() -> np.ndarray:
    """Hesitant, questioning contour — rise then fall."""
    rise = adsr(sweep(350, 500, 0.18), 0.03, 0.04, 0.5, 0.04)
    fall = adsr(sweep(480, 330, 0.22), 0.03, 0.04, 0.5, 0.06)
    gap = silence(0.03)
    return seq(rise, gap, fall)


def focus() -> np.ndarray:
    """Clean single sine, stable, with perfect fifth grace note."""
    grace = adsr(sine(600, 0.08), 0.005, 0.02, 0.3, 0.03)
    main = adsr(sine(400, 0.65), 0.03, 0.10, 0.8, 0.12)
    return seq(grace, silence(0.02), main)


def curiosity() -> np.ndarray:
    """Evolving FM, stepwise rising, playful."""
    step1 = adsr(fm(440, 440, 3, 0.10), 0.005, 0.03, 0.4, 0.03)
    step2 = adsr(fm(494, 494, 3.5, 0.10), 0.005, 0.03, 0.4, 0.03)
    step3 = adsr(fm(554, 554, 4, 0.12), 0.005, 0.03, 0.4, 0.04)
    step4 = adsr(fm(587, 587, 4.5, 0.15), 0.005, 0.04, 0.5, 0.06)
    gap = silence(0.02)
    return seq(step1, gap, step2, gap, step3, gap, step4)


def determination() -> np.ndarray:
    """Filtered sawtooth-like, heavy downbeats, power chord."""
    root = adsr(square(200, 0.15), 0.003, 0.04, 0.8, 0.03)
    fifth = adsr(square(300, 0.15), 0.003, 0.04, 0.6, 0.03)
    hit = root + 0.6 * fifth
    gap = silence(0.03)
    sustain = adsr(square(200, 0.20), 0.003, 0.05, 0.7, 0.08)
    sustain5 = adsr(square(300, 0.20), 0.003, 0.05, 0.5, 0.08)
    held = sustain + 0.6 * sustain5
    return seq(hit, gap, hit, gap, held)


def contemplation() -> np.ndarray:
    """Sine with harmonic sweeps, slow arcs, open fourths."""
    root = adsr(sine(250, 0.8), 0.15, 0.15, 0.6, 0.3)
    fourth = adsr(sine(333, 0.8), 0.15, 0.15, 0.4, 0.3)
    harmonic = adsr(sweep(500, 666, 0.8), 0.2, 0.10, 0.2, 0.25)
    return root + 0.5 * fourth + 0.15 * harmonic


SOUNDS = {
    "Eureka":         eureka,
    "Flow":           flow,
    "Excitement":     excitement,
    "Satisfaction":   satisfaction,
    "Calm":           calm,
    "Contentment":    contentment,
    "Frustration":    frustration,
    "Anxiety":        anxiety,
    "Urgency":        urgency,
    "Confusion":      confusion,
    "Tedium":         tedium,
    "Doubt":          doubt,
    "Focus":          focus,
    "Curiosity":      curiosity,
    "Determination":  determination,
    "Contemplation":  contemplation,
}
