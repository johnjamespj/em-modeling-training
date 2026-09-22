# Lesson 10 — Parameter Sweeps and Sensitivity

**Phase:** EM Modeling Foundations  
**Target time:** 90 minutes

## Objective

Turn isolated solver runs into controlled engineering experiments.

## Experimental discipline

Start with **one variable at a time**.

For every sweep:
1. define the baseline;
2. identify the independent variable;
3. identify the response metrics;
4. hold everything else fixed;
5. record units;
6. retain failed or invalid cases;
7. explain trends physically.

## Experiment A — length

Sweep total dipole length around nominal.

Suggested:
- 8 m
- 9 m
- 10 m
- 11 m
- 12 m

Record:
- fundamental resonant frequency;
- R at resonance;
- X at a fixed reference frequency.

## Experiment B — radius

Sweep wire radius while holding length fixed.

Record:
- resonant frequency;
- impedance near resonance;
- approximate matched bandwidth.

## Experiment C — local sensitivity

For response y and parameter p:

```
dy/dp ≈ [y(p + Δp) - y(p - Δp)] / (2Δp)
```

Estimate sensitivity of resonant frequency to antenna length near the 10 m baseline.

State units.

## Normalize when useful

A normalized sensitivity can help compare parameters with different units:

```
S = (p/y) * dy/dp
```

Explain what a large magnitude means.

## Plotting requirement

Do not submit a folder containing dozens of screenshots.

Reduce sweeps to engineering plots:
- response versus parameter;
- clearly labeled units;
- baseline identified;
- invalid cases marked rather than silently deleted.

## Connection to NVIS

Later you will sweep:
- frequency;
- height;
- soil properties;
- element angle;
- element length;
- deployment errors.

This lesson establishes the experimental method used for those studies.

## Deliverable

Submit the raw table, at least two parameter-response plots, one sensitivity calculation, and a paragraph ranking which tested parameter most strongly controls resonance.
