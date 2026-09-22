# Lesson 03 — Complex Impedance and Resonance

**Phase:** Antenna Theory Foundations  
**Target time:** 60 minutes

## Learning objectives

Understand:
- Z = R + jX;
- resistance versus reactance;
- capacitive versus inductive behavior;
- resonance;
- why resistance at resonance does not automatically equal 50 ohms.

## Theory

Antenna input impedance is:

```
Zin = R + jX
```

R contains the effects represented at the feed as real power flow, including radiation and modeled losses.

X represents stored reactive behavior.

A useful sign convention:
- X < 0: capacitive
- X > 0: inductive
- X ≈ 0: resonant

## Prediction

For a dipole near its fundamental resonance, predict how X changes as frequency passes from below resonance to above resonance.

Write the prediction before simulation.

## Lab

Sweep the 10 m dipole through its first resonance.

Plot or record R and X.

Find:
1. the frequency where X crosses zero;
2. R at that frequency;
3. X below resonance;
4. X above resonance.

| Frequency | R | X | Interpretation |
|---:|---:|---:|---|
| Below resonance | | | |
| Resonance | | | |
| Above resonance | | | |

## Important question

Suppose:

```
Zin = 72 + j0 ohms
```

Is the antenna resonant?

Is it perfectly matched to a 50-ohm line?

Those are two different questions.

## Wideband exercise

Record R and X for the fixed 10 m wire at:

5, 10, 15, 20, 25, 30, 35 MHz.

Plotting the impedance trajectory is encouraged.

Identify:
- zero crossings of X;
- rapid impedance changes;
- possible higher-order resonant behavior.

## NVIS connection

A future broadband matching network must deal with the impedance the antenna actually presents across 5–35 MHz. Before discussing tuners, you must understand the raw antenna impedance.

## Checkpoint

Explain in your own words:

> What exactly does "the antenna is resonant" mean?
