# submit_protocol.py
import streamlit as st
import json
import os
from utils.validators import validate_protocol_structure

def show_submit_protocol():
    st.title("📤 Submit a CureChain Protocol")

    title = st.text_input("Protocol Title")
    abstract = st.text_area("Abstract")
    introduction = st.text_area("Introduction")
    methods = st.text_area("Methods")
    results = st.text_area("Results")
    discussion = st.text_area("Discussion")
    conclusion = st.text_area("Conclusion")
    references = st.text_area("References (comma-separated URLs)")

    if st.button("Submit Protocol"):
        protocol = {
            "meta": {
                "title": title,
                "abstract": abstract
            },
            "introduction": introduction,
            "methods": methods,
            "results": results,
            "discussion": discussion,
            "conclusion": conclusion,
            "references": [r.strip() for r in references.split(",")]
        }

        valid, issues = validate_protocol_structure(protocol)

        if not valid:
            st.error("🚫 Submission failed. Protocol is missing required fields.")
            st.json(issues)
            return

        os.makedirs("protocols", exist_ok=True)
        filename = title.lower().replace(" ", "_") + ".json"
        with open(f"protocols/{filename}", "w") as f:
            json.dump(protocol, f, indent=2)

        st.success(f"✅ Protocol '{title}' saved successfully!")
