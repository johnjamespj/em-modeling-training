# EM Modeling Training

A hands-on introduction to electromagnetic modeling for engineers using Linux and **xnec2c/NEC2**.

The goal is not to teach button-clicking. Each lesson follows the engineering loop:

1. Predict the physics.
2. Build the model.
3. Run the simulation.
4. Check whether the result makes physical sense.
5. Test numerical convergence.
6. Explain what the model does and does not prove.

## Course path

### Lesson 1: Half-wave dipole
Build and analyze a center-fed wire dipole near 15 MHz.

You will learn:
- wavelength and electrical length
- NEC wire geometry
- source placement
- frequency sweeps
- input impedance and resonance
- VSWR versus resonance
- current distribution
- radiation patterns
- segmentation and convergence

Start here: [Lesson 1](lessons/01-dipole-basics/README.md)

## Linux setup

See [setup/linux-xnec2c.md](setup/linux-xnec2c.md).

## Expected background

Basic circuits, complex impedance, and introductory electromagnetics are useful. No prior EM-solver experience is required.

## Modeling rule

**Never trust a plot just because it looks smooth.** Predict first, vary the numerical model, and document assumptions.
