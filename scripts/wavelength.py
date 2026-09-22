#!/usr/bin/env python3
"""Wavelength and electrical-length training utility."""
C = 299_792_458.0

def wavelength_m(freq_mhz):
    return C / (freq_mhz * 1e6)

def electrical_length(length_m, freq_mhz):
    return length_m / wavelength_m(freq_mhz)

if __name__ == "__main__":
    print(" f (MHz)   lambda (m)   10m/lambda")
    for f in [5, 7, 10, 15, 20, 25, 30, 35]:
        lam = wavelength_m(f)
        print(f"{f:8.1f} {lam:12.3f} {10.0/lam:12.3f}")
