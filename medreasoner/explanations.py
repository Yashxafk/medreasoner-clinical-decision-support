def build_evidence(patient, graph_matches):
    evidence = []
    if patient.heart_rate > 100:
        evidence.append("Heart rate is above the demonstration reference threshold (100 bpm).")
    if patient.systolic_bp > 140:
        evidence.append("Systolic blood pressure is above the demonstration reference threshold (140 mmHg).")
    if patient.oxygen_saturation < 95:
        evidence.append("Oxygen saturation is below the demonstration reference threshold (95%).")
    if patient.temperature_c > 38:
        evidence.append("Temperature is above the demonstration reference threshold (38 °C).")
    if patient.age >= 65:
        evidence.append("Age is 65 years or older in this demonstration input.")
    if not evidence:
        evidence.append("No configured demonstration threshold was crossed.")
    graph_evidence = [
        f'{item["concept"]}: {item["relation"]} {item["related_concept"]}.'
        for item in graph_matches
    ]
    return evidence, graph_evidence
