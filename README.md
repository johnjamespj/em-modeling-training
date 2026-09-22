# EM Modeling Training

A structured antenna-theory and electromagnetic-modeling course for a new engineer, culminating in a reproducible **5–35 MHz HF/NVIS antenna design study**.

## Mission

The trainee starts with basic antenna physics, learns to build and defend NEC models, then applies those skills to low-HF high-angle radiation, ground interaction, deployable antenna geometries, wideband characterization, and a final NVIS-oriented design study.

An **AS-2259-style crossed/sloping architecture** is used as a reference benchmark. It is not treated as an assumed optimum.

## Start here

1. [Install xnec2c on Linux](setup/linux-xnec2c.md)
2. [Read the course roadmap](ROADMAP.md)
3. [Begin Lesson 01](lessons/01-wavelength-electrical-length/README.md)
4. Use [CURRICULUM.md](CURRICULUM.md) as the detailed syllabus

## Learning method

Every important exercise follows:

**Predict → calculate → model → simulate → explain → perturb → verify → document**

A plot is not an engineering conclusion.

## Course structure

| Phase | Lessons | Purpose | Checkout |
|---|---:|---|---|
| I — Antenna Theory | 01–07 | Build physical intuition | Lesson 07 gate |
| II — EM Modeling | 08–11 | Build trustworthy NEC models | [Phase II checkout](exercises/phase-2-checkout.md) |
| III — HF/NVIS Engineering | 12–18 | Apply theory to ground, height and deployable HF structures | [Phase III checkout](exercises/phase-3-checkout.md) |
| IV — 5–35 MHz Capstone | 19–24 | Characterize, compare and validate the final design | [Capstone](exercises/phase-4-capstone.md) |

## Repository map

```
lessons/      24 lessons in canonical order
models/       reusable NEC reference models
scripts/      analysis and post-processing utilities
templates/    run records, credibility and comparison templates
exercises/    phase checkouts and capstone
setup/        Linux/tool setup
references/   external documentation pointers
```

## Baseline model

The canonical introductory NEC model is:

```
models/dipoles/dipole-10m-free-space.nec
```

Lessons should reference reusable models from `models/` rather than keeping duplicate copies inside lesson folders.

## Core capstone outputs

The final study must address:
- R(f) and X(f)
- VSWR with a stated reference impedance
- accepted power and efficiency where supported
- realized gain where supported
- zenith and high-elevation radiation
- integrated high-angle versus low-angle radiation
- frequency/elevation behavior from 5–35 MHz
- soil sensitivity
- antenna height in wavelengths
- deployment tolerances
- current distributions
- numerical convergence
- model limitations
- prototype validation plan

## Terminology discipline

Do not use **ground radiation** as shorthand for low-angle radiation. Low-elevation radiation, downward-directed fields, and power dissipated in soil are distinct physical quantities.

Do not use **NVIS works at frequency X** as a conclusion from an antenna model alone. The antenna model describes radiation behavior; the ionospheric path is a separate propagation problem.

## Modeling rule

**Never trust a plot just because it looks smooth. A numerically converged answer to the wrong physical model is still the wrong answer.**
