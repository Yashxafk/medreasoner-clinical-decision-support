# MedReasoner
### Knowledge Graph-Augmented, Self-Explaining Clinical Decision Support — Research Prototype

MedReasoner is an educational research prototype demonstrating a modular workflow for clinical decision support:

1. Validated synthetic patient-input ingestion
2. Retrieval from a small local illustrative knowledge graph
3. A transparent structured-feature baseline score
4. Human-readable evidence/rationale generation
5. Entropy-based uncertainty demonstration and deferral flag

> **Research and safety notice:** This repository is an educational prototype, not a medical device. It does not diagnose, recommend treatment, or replace a qualified clinician. It uses synthetic example data and a lightweight hand-crafted baseline. It does **not** implement or reproduce the paper's full clinical Transformer, UMLS graph, MIMIC-III/IV experiments, reported AUROC/F1/ECE values, or GPU inference benchmark. Those are research targets described in the paper, not verified results of this codebase. Do not use with real patient records or for patient-care decisions.

## Run locally

```bash
python -m venv .venv
# Windows:
.venv\Scripts\activate
# macOS/Linux:
source .venv/bin/activate

pip install -r requirements.txt
streamlit run app.py
```

Open the local URL printed by Streamlit (usually http://localhost:8501).

## Project structure

```text
.
├── app.py
├── requirements.txt
├── README.md
├── LICENSE
├── .gitignore
├── data/
│   └── knowledge_graph.json
├── medreasoner/
│   ├── __init__.py
│   ├── validation.py
│   ├── knowledge_graph.py
│   ├── model.py
│   ├── explanations.py
│   └── uncertainty.py
└── tests/
    ├── test_validation.py
    └── test_knowledge_graph.py
```

## Prototype pipeline

Synthetic inputs → validation → local graph lookup → illustrative baseline score → evidence summary → entropy-based uncertainty / demonstration deferral.

## Input fields

Age, heart rate, systolic blood pressure, oxygen saturation, temperature, and an optional short clinical note. Thresholds and scoring coefficients are illustrative only and are not a validated clinical risk score.

## Implementation status

| Paper component | Current repository |
|---|---|
| Data ingestion and preprocessing | Input validation for demo fields |
| UMLS knowledge graph retrieval | Small illustrative local JSON graph; not UMLS |
| Clinical text + code Transformers | Not implemented; hand-crafted baseline used |
| Gated cross-attention fusion | Not implemented |
| Self-explaining rationale head | Human-readable feature/evidence summary |
| MC dropout + deep ensemble + temperature scaling | Not implemented; entropy of one illustrative score shown |
| Selective deferral | Configurable demonstration threshold |
| MIMIC-III/IV evaluation | Not included; no real patient data |

## Tests

Install requirements and run:

```bash
pytest -q
```

## Responsible use

- Use synthetic data only.
- Do not upload identifiable patient records.
- Do not use outputs to make clinical decisions.
- A clinician must independently assess every real-world case.
- The local graph is illustrative and requires domain-expert review before any research extension.

## Suggested research extensions

1. Add a properly licensed clinical dataset and patient-level train/validation/test splits.
2. Integrate a clinically validated terminology source such as UMLS, subject to its license and access terms.
3. Implement clinical text and code encoders with gated cross-attention.
4. Train rationale generation jointly with the prediction objective.
5. Evaluate calibration, explanation faithfulness, subgroup performance, and selective prediction.
6. Conduct prospective evaluation with clinical oversight.
