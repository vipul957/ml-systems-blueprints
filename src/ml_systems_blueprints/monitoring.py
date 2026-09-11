"""Small, dependency-light reliability checks for ML services."""
from __future__ import annotations
import numpy as np

def population_stability_index(expected, actual, bins=10) -> float:
    e, a = np.asarray(expected, float), np.asarray(actual, float)
    edges = np.linspace(min(e.min(), a.min()), max(e.max(), a.max()), bins + 1)
    ep, _ = np.histogram(e, edges); ap, _ = np.histogram(a, edges)
    ep = np.maximum(ep / max(len(e), 1), 1e-6); ap = np.maximum(ap / max(len(a), 1), 1e-6)
    return float(np.sum((ap-ep) * np.log(ap/ep)))

def risk_label(psi: float) -> str:
    return "stable" if psi < .1 else "watch" if psi < .25 else "investigate"
