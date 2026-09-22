# Lesson 19 — NVIS Performance Metrics

**Phase:** 5–35 MHz NVIS Capstone | **Target:** 90 min

## Objective
Define "better" before optimizing.

## Electrical metrics
At each frequency record R(f), X(f), VSWR with stated Z0, accepted-power fraction, radiation efficiency when supported, and realized gain when supported. Keep matching and radiation metrics separate.

## Angular metrics
Record zenith gain, gain at 60/70/80 degrees elevation, peak gain/elevation, high-elevation azimuth variation, nulls, and pattern topology.

## Integrated angular power
Peak gain alone is insufficient. Define a high region such as 60–90 degrees and a low region such as 0–30 degrees.

For radiation intensity U and elevation e measured from the horizon:

```
dOmega = cos(e) de dphi
P_region proportional to integral integral U(e,phi) dOmega
R_high_low_dB = 10 log10(P_high/P_low)
```

Confirm solver coordinates first. Never integrate dB values directly.

Do not call P_low "ground radiation." Low-angle radiation, downward fields, and soil dissipation are different quantities.

## Azimuth uniformity
At a stated high elevation calculate, for example:

```
DeltaG = Gmax(phi) - Gmin(phi)
```

## Deliverable
Complete `templates/metric-definition-sheet.md`. Metric definitions remain fixed during candidate comparison unless the change is documented and affected runs are repeated.
