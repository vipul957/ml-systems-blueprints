import numpy as np
from ml_systems_blueprints.monitoring import population_stability_index, risk_label

def test_stable_distribution(): assert risk_label(population_stability_index(np.arange(100), np.arange(100))) == "stable"

def test_labels(): assert risk_label(.3) == "investigate"
