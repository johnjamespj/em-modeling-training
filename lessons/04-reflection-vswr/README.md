# Lesson 04 — Reflection Coefficient, Return Loss, and VSWR

**Phase:** Antenna Theory Foundations  
**Target time:** 60 minutes

## Learning objectives

Calculate and interpret:
- reflection coefficient;
- return loss;
- VSWR;
- mismatch efficiency.

Understand why **good VSWR does not prove good radiation performance**.

## Theory

For load impedance ZL and line impedance Z0:

```
Gamma = (ZL - Z0) / (ZL + Z0)
```

Then:

```
VSWR = (1 + |Gamma|) / (1 - |Gamma|)
```

Return loss:

```
RL = -20 log10(|Gamma|)
```

Mismatch efficiency:

```
eta_m = 1 - |Gamma|^2
```

## Hand calculations

Use Z0 = 50 ohms.

Calculate Gamma and VSWR for:

1. 50 + j0 ohms
2. 75 + j0 ohms
3. 25 + j0 ohms
4. 50 + j50 ohms
5. 10 + j0 ohms

Predict which is best matched before calculating.

## Lab

Use the dipole frequency sweep.

At several frequencies:
1. record simulated Zin;
2. calculate Gamma by hand or script;
3. calculate VSWR;
4. compare against xnec2c.

## Resonance trap

Find:
- frequency where X ≈ 0;
- frequency of minimum 50-ohm VSWR.

Are they identical?

Explain.

## Thought experiment

A hypothetical network presents a perfect 50-ohm input to the transmitter while most accepted power is dissipated as heat.

What would the transmitter see?

Would that make the overall antenna system an efficient radiator?

This is why matching and radiation performance must be reported separately.

## NVIS connection

The 5–35 MHz project will report raw impedance, mismatch, radiation efficiency, and realized radiation performance separately. A wideband low-VSWR curve alone will never be accepted as proof of a successful NVIS antenna.
