#!/usr/bin/env python3
"""Integrate linear radiation data over elevation/azimuth regions.

Elevation convention: 0 deg = horizon, 90 deg = zenith.
Input power must be linear, not dB.
"""
import numpy as np

def db_to_linear(db):
    return 10.0 ** (np.asarray(db, dtype=float) / 10.0)

def integrate_region(power_linear, elevation_deg, azimuth_deg, el_min, el_max):
    p = np.asarray(power_linear, dtype=float)
    el_deg = np.asarray(elevation_deg, dtype=float)
    az_deg = np.asarray(azimuth_deg, dtype=float)
    if p.shape != (el_deg.size, az_deg.size):
        raise ValueError("power shape must be (n_elevation, n_azimuth)")
    mask = (el_deg >= el_min) & (el_deg <= el_max)
    if mask.sum() < 2 or az_deg.size < 2:
        raise ValueError("insufficient angular samples")
    el = np.deg2rad(el_deg)
    az = np.deg2rad(az_deg)
    weighted = p[mask, :] * np.cos(el[mask])[:, None]
    per_az = np.trapz(weighted, el[mask], axis=0)
    return float(np.trapz(per_az, az))

def ratio_db(p_high, p_low):
    if p_high <= 0 or p_low <= 0:
        raise ValueError("integrated powers must be positive")
    return 10.0 * np.log10(p_high / p_low)
