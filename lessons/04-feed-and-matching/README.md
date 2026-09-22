# Lesson 4: Resonance Is Not Matching

**Target time:** 45–60 minutes

## Objective
Separate three ideas that beginners often blend together: resonance, feed-point resistance, and transmission-line matching.

## Part 1: Find resonance
Use a dipole model and find the frequency where:

```
Im{Zin} = X ≈ 0
```

Record the real resistance at that frequency.

## Part 2: Calculate reflection
For a 50-ohm reference system, calculate:

```
Gamma = (ZL - Z0) / (ZL + Z0)
```

and

```
VSWR = (1 + |Gamma|) / (1 - |Gamma|)
```

Compare your hand calculation with the software.

## Part 3: Change feed location
Move the source away from the center while keeping geometry fixed.

Record:

| Feed position | R | X | VSWR |
|---|---:|---:|---:|
| Center | | | |
| Moderately off-center | | | |
| Further off-center | | | |

Choose segment locations that remain valid for your segmentation.

## Questions
- Why does moving the feed change impedance when the wire itself is unchanged?
- Can an antenna be resonant and have a 3:1 VSWR?
- Can an antenna have a low VSWR without being exactly resonant?
- What does a matching network change, and what does it not necessarily change about the far-field pattern?

## Deliverable
Show one hand calculation of Gamma and VSWR, the feed-location table, and a short explanation of resonance versus matching.
