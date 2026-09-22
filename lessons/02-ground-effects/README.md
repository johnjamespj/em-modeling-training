# Lesson 2: Ground Effects and Antenna Height

**Target time:** 45–60 minutes

## Objective
Learn how the environment becomes part of the antenna. Compare the Lesson 1 dipole in free space with the same antenna above ground.

## Predict first
Before simulation, answer:
1. Will adding ground change feed impedance?
2. Will antenna height change the radiation pattern?
3. What do you expect when the antenna is very low compared with one wavelength?

## Experiment
Use the 10 m dipole near 15 MHz. Model it horizontally above ground at several heights:

| Height | Height / wavelength | Resonant frequency | R at resonance | Main-lobe elevation |
|---:|---:|---:|---:|---:|
| 2.5 m | | | | |
| 5 m | | | | |
| 10 m | | | | |
| 20 m | | | | |

Start with a perfect ground model. Keep antenna dimensions and segmentation constant.

Then repeat one height using a finite/conductive ground model supported by NEC.

## Investigate
Plot elevation patterns for every height. Compare input impedance and pattern shape.

Answer:
- Why does a ground plane alter radiation even though the antenna itself did not change?
- Which results are most sensitive to height?
- Why is "free-space gain" potentially misleading for an installed antenna?
- What real-world ground properties would you need for a better model?

## Numerical check
Repeat one case with approximately twice the segmentation. Verify that your conclusion about the radiation pattern is not caused by discretization.

## Deliverable
Submit the height table, overlaid or comparable elevation plots, one convergence comparison, and a paragraph explaining the physical mechanism.

## Engineering takeaway
Antenna performance belongs to the **antenna + environment**, not to the metal alone.
