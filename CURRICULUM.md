# EM Modeling Training — Restructured Curriculum

## End goal

Train a new engineer from basic antenna theory through a defensible **5–35 MHz HF/NVIS antenna design study**, using an AS-2259-style crossed/sloping dipole as a reference architecture rather than a design to blindly copy.

The engineer should finish the course able to:

- explain the antenna physics behind simulation results;
- build and debug NEC models independently;
- distinguish resonance, matching, radiation efficiency, and realized gain;
- characterize antennas across 5–35 MHz;
- quantify high-angle versus low-angle radiation;
- understand how ground and antenna height affect HF patterns;
- perform convergence and sensitivity studies;
- compare candidate NVIS geometries;
- state what a model can and cannot support;
- produce an engineering recommendation supported by simulation evidence.

## Training philosophy

Every practical lesson follows:

**Predict → calculate → model → simulate → explain → perturb → verify → document**

The trainee must make a prediction before running important simulations. A correct plot with no physical explanation is not considered mastery.

---

# Phase I — Antenna Theory Foundations

## Lesson 01 — Frequency, wavelength, and electrical length
Theory:
- frequency and wavelength
- lambda = c/f
- physical versus electrical length
- quarter-wave and half-wave structures
- why one antenna can behave radically differently from 5 to 35 MHz

Lab:
- calculate wavelength at 5, 10, 15, 20, 25, 30, and 35 MHz
- express a 10 m structure in wavelengths at each frequency
- model a simple dipole and compare predicted versus simulated resonance

## Lesson 02 — Current, voltage, and radiation
Theory:
- RF current distribution
- standing-wave intuition
- current maxima/minima
- relationship between current distribution and radiation
- near-field versus far-field concepts

Lab:
- inspect current distribution on a half-wave dipole
- change frequency without changing geometry
- explain changes before inspecting the far-field pattern

## Lesson 03 — Complex impedance and resonance
Theory:
- Z = R + jX
- radiation resistance
- loss resistance
- capacitive and inductive reactance
- resonance as X ≈ 0

Lab:
- sweep a dipole through resonance
- plot R and X
- identify electrically short and long behavior

## Lesson 04 — Reflection coefficient, return loss, and VSWR
Theory:
- transmission-line reference impedance
- Gamma = (ZL-Z0)/(ZL+Z0)
- return loss
- VSWR
- why resonance is not the same as matching
- why low VSWR does not prove good radiation

Lab:
- calculate Gamma and VSWR by hand
- compare with xnec2c
- investigate off-center feed locations

## Lesson 05 — Radiation patterns
Theory:
- azimuth and elevation cuts
- theta and phi
- beamwidth
- lobes and nulls
- directivity
- gain
- dBi
- polarization

Lab:
- predict the dipole pattern before simulation
- identify broadside maxima and axial nulls
- rotate antenna geometry and verify coordinate interpretation

## Lesson 06 — Efficiency and the RF power budget
Theory:

P_TX → mismatch → accepted power → radiated power + material/ground loss

Cover:
- mismatch efficiency
- radiation efficiency
- realized gain
- conductor loss
- ground loss
- why a broadband match can hide a poor radiator

Lab:
- construct and explain a complete power budget
- compare gain, directivity, and realized gain where solver outputs permit

## Lesson 07 — Bandwidth and antenna geometry
Theory:
- bandwidth
- Q intuition
- conductor diameter/radius
- geometry-dependent impedance
- multi-resonance behavior

Lab:
- sweep wire radius
- compare resonance and 2:1 VSWR bandwidth
- identify invalid/extreme wire-model assumptions

---

# Phase II — EM Modeling Foundations

## Lesson 08 — NEC/xnec2c model construction
Cover:
- NEC geometry cards
- segmentation
- excitation
- frequency sweeps
- ground definitions
- pattern requests
- coordinate systems
- model documentation

Lab:
- construct a dipole from a blank NEC file instead of modifying a supplied example

## Lesson 09 — Numerical convergence
Cover:
- discretization
- segmentation sensitivity
- frequency resolution
- convergence versus correctness

Lab:
- compare multiple segment counts
- calculate percent change in complex impedance
- determine when a quantity has stabilized sufficiently for the stated purpose

## Lesson 10 — Sensitivity and parameter sweeps
Cover:
- one-variable-at-a-time experiments
- local sensitivity
- parameter sweeps
- interpreting nonlinear responses
- tolerances

Lab:
- automate or systematically perform length, radius, and height sweeps
- estimate dy/dp
- rank important parameters

## Lesson 11 — Verification and validation
Distinguish:
1. Did we solve the chosen numerical model adequately?
2. Does the model represent the intended physical system?
3. Does independent evidence support the result?

Lab:
- deliberately create a numerically converged but physically wrong model
- write a short credibility statement

---

# Phase III — HF and NVIS Engineering

## Lesson 12 — Ground and image effects
Theory:
- intuitive image theory
- reflection from ground
- soil conductivity
- relative permittivity
- ground loss
- antenna height expressed as h/lambda

Lab:
- horizontal dipole over perfect and finite ground
- sweep height
- compare elevation patterns

## Lesson 13 — HF propagation versus antenna behavior
Theory:
- ground wave versus skywave
- takeoff/elevation angle
- NVIS concept
- ionospheric propagation is separate from the antenna EM model
- why a good high-angle antenna does not guarantee an NVIS path at every frequency

Lab:
- classify antenna outputs versus propagation/environment inputs
- identify what NEC can and cannot answer

## Lesson 14 — Low horizontal dipole for NVIS
Lab:
- characterize a horizontal dipole at several h/lambda values
- examine zenith and 60–90° radiation
- examine 0–30° radiation
- find height/frequency combinations that change pattern topology

## Lesson 15 — Inverted-V geometry
Theory:
- slope angle
- apex height
- endpoint height
- pattern and impedance consequences

Lab:
- compare horizontal dipole and inverted-V with controlled variables
- sweep apex height and element angle

## Lesson 16 — Crossed/sloping dipoles and AS-style reference architecture
Build an **AS-2259-style reference geometry** for learning and benchmarking.

Study:
- crossed elements
- multiple wire lengths where applicable
- sloping geometry
- azimuth coverage
- feed interactions
- frequency-dependent current distribution

The reference is a benchmark, not automatically the desired final design.

## Lesson 17 — Mutual coupling
Theory:
- induced current
- mutual impedance intuition
- interaction between nearby radiators

Lab:
- vary element spacing/orientation
- observe driven-element impedance and pattern changes
- connect results to the crossed NVIS architecture

## Lesson 18 — Feed line, balance, and common-mode behavior
Theory:
- balanced versus unbalanced feeds
- balun/choke purpose
- feed-line radiation
- model limitations

Lab:
- progressively introduce feed-structure effects where NEC representation is appropriate
- identify results that require a more sophisticated model or measurement

---

# Phase IV — 5–35 MHz NVIS Design Project

## Lesson 19 — Define the performance metrics

The engineer must stop thinking in terms of a single "gain" number.

For each frequency characterize:

- R(f)
- X(f)
- |S11(f)| / return loss
- VSWR(f)
- accepted power
- radiation efficiency
- realized gain
- zenith gain
- gain at selected high elevation angles
- azimuth uniformity at high elevation
- current distribution
- pattern topology

### High-angle metric

Calculate or post-process integrated radiation over a high-elevation region such as:

P_high = integral over 60–90 degrees

Compare against low-elevation radiation:

P_low = integral over 0–30 degrees

A useful project KPI is:

R_high/low = 10 log10(P_high / P_low)

Do **not** casually call P_low "ground radiation." Low-angle radiation, downward-directed fields, and power dissipated in ground are different quantities.

## Lesson 20 — 5–35 MHz wideband characterization

Sweep the complete band.

Perform detailed checkpoints at approximately:

5, 7, 10, 15, 20, 25, 30, and 35 MHz

Use finer frequency sampling wherever resonances or rapid pattern changes occur.

Primary visualization:

**G(f, elevation)** heatmap

This should reveal when the antenna transitions between electrically small, useful high-angle, and increasingly multi-lobed regimes.

## Lesson 21 — Soil study

Test representative:
- poor/dry ground
- intermediate ground
- good/wet conductive ground

Record conductivity and relative permittivity assumptions explicitly.

Compare:
- impedance
- efficiency
- high-angle integrated power
- low-angle integrated power
- elevation pattern

## Lesson 22 — Deployment robustness

Perturb realistic field variables:
- mast height
- element length
- element angle
- endpoint/stake location
- wire sag/asymmetry
- soil properties
- feed asymmetry where modelable

Suggested dimensional perturbations include nominal, ±2%, and ±5% where meaningful.

Determine which deployment errors dominate performance.

## Lesson 23 — Candidate design comparison

Compare at least:
1. low horizontal dipole
2. inverted-V
3. AS-style crossed/sloping reference
4. trainee's candidate design

Use identical frequencies, soil assumptions, power normalization, angular metrics, and numerical-quality requirements.

No design wins because of one attractive plot.

## Lesson 24 — Final design and credibility review

The final report must contain:
- requirements
- geometry
- assumptions
- NEC files and solver settings
- convergence evidence
- 5–35 MHz impedance results
- VSWR
- efficiency
- realized gain
- G(f,elevation) visualization
- high-angle/low-angle integrated radiation comparison
- soil sensitivity
- deployment sensitivity
- limitations
- comparison against the reference architectures
- recommended prototype configuration
- measurement plan

The engineer must explicitly state which conclusions are:
- numerically verified;
- physically supported;
- still unvalidated;
- dependent on uncertain environmental assumptions.

---

# Capstone acceptance criteria

The capstone is successful when the trainee can defend the model rather than merely operate the solver.

The trainee should be able to answer:

1. Why does this geometry radiate at high elevation?
2. How does that explanation change across 5–35 MHz?
3. Where does accepted transmitter power go?
4. What portion of the result depends strongly on soil?
5. What does changing antenna height do in units of wavelength?
6. Is a good VSWR masking poor efficiency?
7. Which deployment tolerances matter most?
8. Has the numerical model converged?
9. What important physical effects remain unmodeled?
10. What measurements would falsify or validate the simulation?

# Tool progression

Start with **xnec2c/NEC2** because the trainee can see the antenna physics and model assumptions directly.

Introduce **openEMS** later only when volumetric/full-wave 3D effects justify the added complexity.

The solver is a tool. The course objective is engineering judgment.
