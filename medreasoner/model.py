import numpy as np

FEATURE_NAMES = ["age", "heart_rate", "systolic_bp", "oxygen_saturation", "temperature_c"]

def _sigmoid(x):
    return 1.0 / (1.0 + np.exp(-np.clip(x, -30, 30)))

def predict_demo(patient):
    """
    Transparent synthetic scoring baseline.
    This is NOT a validated clinical model and is NOT trained on patient data.
    """
    score = (
        -3.0
        + 0.012 * max(patient.age - 40, 0)
        + 0.018 * max(patient.heart_rate - 90, 0)
        + 0.012 * max(patient.systolic_bp - 140, 0)
        + 0.22 * max(96 - patient.oxygen_saturation, 0)
        + 0.35 * max(patient.temperature_c - 37.5, 0)
    )
    probability = float(_sigmoid(score))
    return {
        "label": "Elevated demonstration score" if probability >= 0.5 else "Lower demonstration score",
        "probability": probability,
        "score": float(score),
        "model_type": "Illustrative hand-crafted baseline (not clinically validated)"
    }
