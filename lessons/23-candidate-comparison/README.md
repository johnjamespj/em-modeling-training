# Lesson 23 — Candidate Design Comparison

**Phase:** 5–35 MHz NVIS Capstone | **Target:** 2–3 hr plus compute

## Objective
Compare candidate architectures under common assumptions and numerical-quality standards.

## Minimum set
1. low horizontal dipole
2. inverted-V
3. crossed/sloping AS-style reference
4. trainee candidate

Use a common frequency grid, soil cases, normalization, angular grid, metric definitions, and convergence requirements.

## Compare
Summarize impedance/tuner burden, efficiency, P_high, P_low, high/low ratio, zenith behavior, high-angle azimuth uniformity, pattern-failure regions, soil sensitivity, deployment sensitivity, footprint, and deployment complexity.

## Required plots
Use directly comparable axes:
- R and X vs frequency
- VSWR vs frequency
- high-angle metric vs frequency
- high/low ratio vs frequency
- frequency/elevation heatmaps
- selected elevation patterns

## Multi-objective discipline
Do not hide the problem inside one arbitrary score. Expose trade spaces such as radiation versus footprint, broadband behavior versus complexity, and nominal performance versus robustness.

## Deliverable
A comparison package that narrows the design space while preserving weaknesses and uncertainty.
