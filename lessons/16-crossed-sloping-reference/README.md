# Lesson 16 — Crossed/Sloping HF Reference Architecture

**Phase:** HF/NVIS Engineering  
**Target time:** 2–3 hours

## Objective

Build a crossed/sloping multi-wire reference inspired by field-deployable high-angle HF antenna architectures such as the AS-2259 family.

This is a **reference and learning model**, not an instruction to reproduce a specific military configuration.

## Why build a reference?

A reference architecture gives the project:
- a consistent benchmark;
- a realistic deployment concept;
- a multi-element geometry that exposes coupling;
- a structure whose behavior changes substantially across HF.

## Step 1 — Define the reference

Before modeling, create a geometry specification containing:
- mast/apex height;
- number of wires;
- wire lengths;
- slopes;
- endpoint positions;
- wire radius;
- feed topology;
- ground model.

Every dimension must be explicit.

## Step 2 — Build incrementally

Do not create the entire structure at once.

Build:
1. one sloping dipole;
2. verify it;
3. add the crossed structure;
4. verify geometry;
5. add additional intended wire elements;
6. re-check currents and impedance after each change.

## Step 3 — Frequency checkpoints

Characterize:

```
5, 7, 10, 15, 20, 25, 30, 35 MHz
```

At each frequency record:
- R+jX;
- current distribution on every element;
- zenith gain;
- gain at 60°, 70°, 80°;
- peak elevation angle;
- high-elevation azimuth variation.

## Current-distribution requirement

At every checkpoint identify:
- which wires carry substantial current;
- current maxima/minima;
- whether current is symmetric;
- whether a wire appears electrically short, near resonance, or electrically long.

Use current to explain pattern changes.

## Comparison

Compare against the low horizontal dipole and inverted-V using the same:
- frequency;
- ground;
- normalization;
- angular definitions.

## Deliverable

Submit:
- reference geometry drawing;
- NEC model;
- frequency table;
- current plots;
- elevation patterns;
- high-elevation azimuth plots;
- limitations.

## Key lesson

A complicated antenna should be understood as interacting conductors carrying frequency-dependent currents, not as a mysterious named object with a guaranteed pattern.
