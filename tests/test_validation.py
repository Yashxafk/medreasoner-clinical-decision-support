import pytest
from medreasoner.validation import PatientInput, validate_patient_input

def test_valid_input():
    validate_patient_input(PatientInput(45, 80, 120, 98, 36.8, "synthetic"))

def test_invalid_oxygen():
    with pytest.raises(ValueError):
        validate_patient_input(PatientInput(45, 80, 120, 40, 36.8))
