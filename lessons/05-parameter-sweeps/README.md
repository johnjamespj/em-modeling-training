# Lesson 5: Parameter Sweeps and Sensitivity

**Target time:** 60 minutes

## Objective
Turn individual simulations into an engineering experiment.

## Problem
A nominal dipole design will not be manufactured or installed at exactly one dimension. Determine which parameter changes matter.

## Parameters
Choose a nominal model and sweep:
- total length
- wire radius
- antenna height above ground

Change **one parameter at a time** first.

For each run record:
- resonant frequency
- R and X at a fixed operating frequency
- VSWR
- peak gain
- direction of the main lobe

## Sensitivity
For a response y and parameter p, estimate locally:

```
dy/dp ≈ (y(p + Δp) - y(p - Δp)) / (2Δp)
```

Use this to identify which dimensions most strongly affect resonant frequency and matching.

## Questions
1. Which parameter has the largest effect on resonance?
2. Which has the largest effect on pattern?
3. Are the relationships linear over your sweep?
4. Which manufacturing or installation tolerance deserves the most attention?
5. What is dangerous about changing several parameters simultaneously before understanding individual sensitivity?

## Deliverable
Produce a compact sensitivity table and recommend one parameter that should receive a tighter engineering tolerance. Support the recommendation with simulation evidence.
