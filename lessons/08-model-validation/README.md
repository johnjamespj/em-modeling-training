# Lesson 8: Verification, Validation, and Model Credibility

**Target time:** 60 minutes

## Objective
Learn the difference between getting a solver result and having evidence that the result is useful.

## Three questions

### 1. Did I solve the equations correctly?
This is **numerical verification**.

Examples:
- segmentation convergence
- frequency-step convergence
- solver warnings
- numerical stability

### 2. Did I model the intended physical system?
This is **model validation / physical adequacy**.

Examples:
- correct geometry
- appropriate ground
- conductor properties
- feed representation
- nearby structures
- boundary assumptions

### 3. Does independent evidence agree?
Compare against:
- analytical limits
- textbook behavior
- another solver when appropriate
- measurement when available

## Exercise: deliberately build bad models
Take one previously trusted case and introduce three mistakes, one at a time:

1. insufficient segmentation
2. incorrect physical dimension
3. omitted environmental feature

For each, ask whether a normal-looking radiation plot exposes the mistake.

## Credibility matrix

| Check | Result | Evidence | Remaining limitation |
|---|---|---|---|
| Physics sanity check | | | |
| Segmentation convergence | | | |
| Frequency resolution | | | |
| Geometry review | | | |
| Environment review | | | |
| Independent comparison | | | |

## Final question
A simulation converges to six decimal places but disagrees with measurement by 4 dB. Which result should you trust, and what should you investigate before answering?

## Deliverable
Write a one-page **model credibility statement** for one model from this course. State what has been verified, what has not been validated, and what decisions the model is appropriate to support.
