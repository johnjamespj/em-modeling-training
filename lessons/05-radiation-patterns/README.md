# Lesson 05 — Radiation Patterns, Gain, and Polarization

**Phase:** Antenna Theory Foundations  
**Target time:** 60–75 minutes

## Learning objectives

Understand:
- azimuth and elevation;
- lobes and nulls;
- beamwidth;
- directivity and gain;
- polarization;
- why coordinate-system mistakes can invalidate an interpretation.

## Start with geometry

Before viewing any plot, draw:
- the antenna axes;
- zenith;
- horizon;
- the plane of the requested pattern cut.

A radiation plot without coordinate context is dangerous.

## Prediction

For a straight half-wave dipole in free space:

1. Where should radiation be strongest relative to the wire?
2. Where should the nulls be?
3. What should the 3D pattern resemble conceptually?

Sketch it.

## Lab A

Simulate the fundamental dipole.

Inspect:
- 3D pattern if available;
- azimuth cut;
- elevation cut.

Identify maxima and nulls.

Rotate the physical antenna in the model and verify that the pattern rotates in the expected coordinate system.

## Lab B — frequency

Keep the physical wire fixed.

Compare patterns at 5, 15, 25, and 35 MHz.

Record:

| f | Electrical length | Major lobes | Major nulls | Peak direction |
|---:|---:|---|---|---|
| 5 | | | | |
| 15 | | | | |
| 25 | | | | |
| 35 | | | | |

## Gain versus directivity

Explain:
- directivity describes angular concentration;
- gain includes radiation efficiency;
- realized gain additionally accounts for mismatch when defined that way by the tool/workflow.

Always document the exact quantity plotted.

## Polarization

Introduce the electric-field orientation and why a linear dipole is linearly polarized in its principal radiation.

For later crossed-wire designs, polarization can become frequency-, angle-, and feed-dependent.

## NVIS connection

The final project cares strongly about **elevation pattern**, especially high elevation angles. Peak gain by itself is insufficient. A low-angle peak can look impressive while being contrary to the desired high-angle objective.
