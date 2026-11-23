from dataclasses import dataclass

@dataclass
class PatientInput:
    age: int
    heart_rate: float
    systolic_bp: float
    oxygen_saturation: float
    temperature_c: float
    clinical_note: str = ""

def validate_patient_input(data: PatientInput) -> None:
    checks = {
        "age": (data.age, 0, 120),
        "heart_rate": (data.heart_rate, 20, 250),
        "systolic_bp": (data.systolic_bp, 40, 300),
        "oxygen_saturation": (data.oxygen_saturation, 50, 100),
        "temperature_c": (data.temperature_c, 30, 45),
    }
    for name, (value, low, high) in checks.items():
        if not low <= value <= high:
            raise ValueError(f"{name} must be between {low} and {high}.")
    if len(data.clinical_note) > 2000:
        raise ValueError("Clinical note must be 2,000 characters or fewer.")
