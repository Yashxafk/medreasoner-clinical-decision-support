import math

def binary_entropy(probability):
    p = min(max(float(probability), 1e-9), 1 - 1e-9)
    return -(p * math.log(p) + (1 - p) * math.log(1 - p)) / math.log(2)

def assess_uncertainty(probability, threshold=0.80):
    entropy = binary_entropy(probability)
    reliability = 1.0 - entropy
    return {
        "normalized_entropy": entropy,
        "reliability_demo": reliability,
        "defer": reliability < threshold,
        "threshold": threshold,
        "method": "Normalized binary entropy of a single illustrative score"
    }
