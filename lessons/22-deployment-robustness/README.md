# Lesson 22 — Deployment Robustness

**Phase:** 5–35 MHz NVIS Capstone | **Target:** 2–4 hr plus compute

## Objective
Determine whether a candidate remains useful after realistic deployment variation.

Investigate mast/apex height, element length, stake position, included angle, wire sag approximation, crossed-element asymmetry, ground properties, and justified feed-routing/common-mode variables.

Use nominal and bounded perturbations such as ±2% and ±5% where physically meaningful.

## Method
Start one variable at a time and rank sensitivities. Then perform a bounded multi-parameter study.

If random/Monte Carlo sampling is used, justify parameter distributions/ranges and record the random seed.

## Define failure before running
Possible criteria include excessive mismatch beyond the assumed matching system, inadequate high-angle metric, excessive low-angle dominance, unacceptable azimuth nonuniformity, or a severe null in the desired angular region.

Requirements-derived thresholds are preferred. Otherwise label them provisional.

## Deliverable
Sensitivity ranking, combined-tolerance results, failure cases, nominal-versus-spread comparison, and recommended deployment checks/tolerances.
