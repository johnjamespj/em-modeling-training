# Lesson 1: Model a Half-Wave Dipole

**Target time:** 30–45 minutes

## Objective

Use simulation to answer a physical question:

> How does the length of a dipole affect its resonant frequency?

Then determine whether the answer is a physical result or a numerical artifact.

---

## Part 1 — Predict before simulating

The starting antenna is 10 m long and the target frequency is 15 MHz.

Calculate the free-space wavelength:

```
lambda = c / f
```

Use `c = 3e8 m/s`.

Write down:

1. Wavelength at 15 MHz.
2. The antenna length as a fraction of wavelength.
3. Your prediction: if the antenna is shortened, does resonance move higher or lower in frequency?
4. Explain your prediction in one sentence.

Do this **before running the solver**.

---

## Part 2 — Inspect the model

Open `dipole.nec`.

Starting model:

| Parameter | Value |
|---|---:|
| Total length | 10 m |
| Wire endpoints | -5 m to +5 m |
| Wire radius | 1 mm |
| Segments | 41 |
| Feed segment | 21 |
| Sweep | 12–18 MHz |
| Step | 0.1 MHz |
| Environment | Free space |

Identify the NEC cards responsible for:

- wire geometry
- excitation
- frequency
- radiation pattern

Do not change anything yet.

---

## Part 3 — Find resonance

Run the frequency sweep.

Plot or inspect:

- real input impedance R
- imaginary input impedance X
- VSWR using 50 ohms as the reference
- maximum gain

Find the frequency where the reactance crosses zero:

```
X ≈ 0
```

Record:

| Quantity | Result |
|---|---|
| Resonant frequency | |
| R at resonance | |
| X at resonance | |
| Minimum VSWR | |
| Frequency of minimum VSWR | |

### Question

Is the frequency of minimum VSWR necessarily identical to the resonant frequency? Explain why.

---

## Part 4 — Change one physical variable

Repeat the model for three total lengths.

| Length | Endpoints | Resonant frequency | R at resonance |
|---:|---|---:|---:|
| 9 m | -4.5 to +4.5 m | | |
| 10 m | -5.0 to +5.0 m | | |
| 11 m | -5.5 to +5.5 m | | |

Keep everything else unchanged.

### Questions

1. Which antenna resonates at the highest frequency?
2. Does the trend agree with your prediction?
3. Approximately how does resonant frequency scale with length?
4. Why is physical length alone not enough to describe an antenna?

---

## Part 5 — Look at the fields through their consequences

Return to the 10 m model.

Inspect:

- current distribution along the wire
- radiation pattern at or near resonance

Answer:

1. Where is current largest?
2. Where does current approach zero?
3. Where are the radiation-pattern maxima?
4. Where are the nulls?
5. Does the pattern make sense for the orientation of the wire?

Sketch the pattern before comparing it with the solver.

---

## Part 6 — Numerical convergence

A simulation result is not automatically correct.

Run the 10 m antenna at **15 MHz** using:

- 41 segments
- 81 segments

For 81 segments, keep the feed at the physical center. The center segment therefore changes from 21 to 41.

Record:

| Segments | R at 15 MHz | X at 15 MHz |
|---:|---:|---:|
| 41 | | |
| 81 | | |

Compare the complex impedances:

```
percent difference = |Z81 - Z41| / |Z81| * 100
```

For this exercise, use **2%** as a classroom convergence target. This is an exercise criterion, not a universal accuracy specification.

### Question

Why would increasing segmentation forever not necessarily make every EM model more trustworthy?

---

## Part 7 — Engineering interpretation

Answer without running another simulation:

> Can an antenna be resonant but poorly matched to a 50-ohm system?

Give a numerical example.

---

## Deliverable

Submit one short engineering note containing:

1. original prediction
2. 9/10/11 m results table
3. impedance versus frequency plot
4. radiation-pattern screenshot
5. 41-versus-81 segment comparison
6. answers to the interpretation questions
7. two assumptions or limitations of this model

## Pass criteria

You should be able to explain **why** the resonance moved, distinguish resonance from impedance matching, identify the major features of the dipole radiation pattern, and demonstrate that you checked numerical convergence.
