# EM Modeling Training

A hands-on antenna-theory and electromagnetic-modeling course for engineers, culminating in a **5–35 MHz HF/NVIS antenna design study**.

The trainee is assumed to be new to antenna engineering. The course therefore teaches the physics and the solver together.

## End goal

The capstone is to design and characterize a rapidly deployable HF/NVIS antenna, using an **AS-2259-style crossed/sloping architecture as a reference benchmark**.

The final study examines impedance, matching, efficiency, high-angle radiation, low-angle radiation, soil, antenna height, deployment tolerances, and wideband behavior from 5–35 MHz.

## Start here

- [Detailed 24-lesson curriculum](CURRICULUM.md)
- [Course roadmap and phase gates](ROADMAP.md)
- [Linux/xnec2c setup](setup/linux-xnec2c.md)

## Learning method

Every major experiment follows:

**Predict → calculate → model → simulate → explain → perturb → verify → document**

The goal is not to teach button-clicking. The trainee must understand why the solver produces a result and what evidence is required before trusting it.

## Four phases

### I — Antenna Theory Foundations
Wavelength, electrical length, current distribution, impedance, resonance, matching, radiation patterns, polarization, gain, efficiency, and bandwidth.

### II — EM Modeling Foundations
NEC construction, segmentation, convergence, parameter sweeps, sensitivity, verification, validation, and model credibility.

### III — HF/NVIS Engineering
Ground effects, height in wavelengths, HF/NVIS concepts, low dipoles, inverted-V antennas, crossed/sloping reference geometries, mutual coupling, and feed/common-mode effects.

### IV — 5–35 MHz NVIS Capstone
Wideband characterization, frequency/elevation maps, integrated high-angle versus low-angle radiation, soil sensitivity, deployment robustness, candidate comparison, final design, and a measurement/validation plan.

## Existing practical material

The original introductory dipole exercise remains available at [lessons/01-dipole-basics](lessons/01-dipole-basics/README.md). Existing later lessons remain useful lab material, but the new [curriculum](CURRICULUM.md) is now the authoritative course sequence while the repository is reorganized around it.

## Modeling rule

**Never trust a plot just because it looks smooth.** A numerically converged answer to the wrong physical model is still the wrong answer.
