import streamlit as st
from medreasoner.validation import PatientInput, validate_patient_input
from medreasoner.knowledge_graph import LocalKnowledgeGraph
from medreasoner.model import predict_demo
from medreasoner.explanations import build_evidence
from medreasoner.uncertainty import assess_uncertainty

st.set_page_config(page_title="MedReasoner | Research Prototype", page_icon="🩺", layout="wide")
st.markdown("""
<style>
.stApp {background: #0b1220; color: #e7eef9;}
[data-testid="stSidebar"] {background: #111c2e;}
.block-container {padding-top: 2rem; max-width: 1200px;}
.metric-card {background:#142238;border:1px solid #263a55;padding:18px;border-radius:14px;}
.small-muted {color:#9fb0c7;font-size:0.9rem;}
</style>
""", unsafe_allow_html=True)

st.title("🩺 MedReasoner")
st.caption("Knowledge Graph-Augmented Clinical Decision Support · Research Prototype")
st.warning("Educational demonstration only. Not a diagnostic tool, not clinically validated, and not for real patient-care decisions.")

with st.sidebar:
    st.header("Patient demonstration input")
    age = st.number_input("Age", min_value=0, max_value=120, value=54)
    hr = st.number_input("Heart rate (bpm)", min_value=20.0, max_value=250.0, value=108.0)
    sbp = st.number_input("Systolic BP (mmHg)", min_value=40.0, max_value=300.0, value=148.0)
    spo2 = st.number_input("Oxygen saturation (%)", min_value=50.0, max_value=100.0, value=93.0)
    temp = st.number_input("Temperature (°C)", min_value=30.0, max_value=45.0, value=38.2, step=0.1)
    note = st.text_area("Clinical note (optional)", value="Fever and elevated heart rate reported in synthetic example.")
    threshold = st.slider("Demonstration deferral threshold", 0.0, 1.0, 0.80, 0.05)
    run = st.button("Analyze demonstration record", type="primary", use_container_width=True)

st.markdown("### System pipeline")
cols = st.columns(5)
for col, title in zip(cols, ["01 · Ingestion", "02 · KG retrieval", "03 · Prediction", "04 · Explanation", "05 · Uncertainty"]):
    col.markdown(f'<div class="metric-card"><b>{title}</b><p class="small-muted">Prototype module</p></div>', unsafe_allow_html=True)

if run:
    patient = PatientInput(int(age), float(hr), float(sbp), float(spo2), float(temp), note)
    try:
        validate_patient_input(patient)
        result = predict_demo(patient)
        terms = []
        if hr > 100: terms.append("tachycardia")
        if spo2 < 95: terms.append("hypoxemia")
        if temp > 38: terms.append("fever")
        if sbp > 140: terms.append("hypertension")
        graph = LocalKnowledgeGraph()
        graph_matches = graph.retrieve(terms)
        evidence, graph_evidence = build_evidence(patient, graph_matches)
        uncertainty = assess_uncertainty(result["probability"], threshold)

        st.divider()
        st.subheader("Demonstration output")
        a, b, c = st.columns(3)
        a.metric("Model output", result["label"])
        b.metric("Illustrative score", f'{result["probability"]:.1%}')
        c.metric("Reliability indicator", f'{uncertainty["reliability_demo"]:.1%}')
        st.progress(result["probability"], text="Illustrative model score — not a clinical probability")

        if uncertainty["defer"]:
            st.error("DEFER: This demonstration output falls below the selected reliability threshold. Human review would be required in a real CDSS.")
        else:
            st.info("No deferral triggered by this demonstration threshold. This does not establish clinical safety or reliability.")

        left, right = st.columns(2)
        with left:
            st.markdown("#### Input evidence")
            for item in evidence: st.write("• " + item)
        with right:
            st.markdown("#### Retrieved knowledge-graph relations")
            if graph_evidence:
                for item in graph_evidence: st.write("• " + item)
            else:
                st.write("No matching illustrative graph concepts found.")

        with st.expander("Technical details"):
            st.json({"prediction": result, "uncertainty": uncertainty, "retrieved_graph_items": graph_matches})
    except ValueError as exc:
        st.error(str(exc))
else:
    st.info("Adjust the synthetic values in the sidebar and select **Analyze demonstration record**.")
    st.markdown("#### About this prototype")
    st.write("The repository demonstrates modular data flow and a transparent baseline. The full Transformer + UMLS + ensemble architecture described in the research manuscript remains future implementation work.")
