# protocol_viewer.py
import streamlit as st
import json
import os

def show_protocol_viewer():
    st.title("🧬 CureChain Protocols")
    st.write("Browse open-source, science-ready healing protocols.")

    protocol_dir = "protocols"
    files = [f for f in os.listdir(protocol_dir) if f.endswith(".json")]

    if not files:
        st.warning("No protocols found.")
        return

    selected = st.selectbox("Choose a protocol:", files)
    with open(os.path.join(protocol_dir, selected), 'r') as f:
        data = json.load(f)

    st.subheader(data.get("meta", {}).get("title", "Untitled"))
    st.markdown(f"**Abstract:** {data.get('meta', {}).get('abstract', '')}")
    st.markdown(f"### Introduction\n{data.get('introduction', '')}")
    st.markdown(f"### Methods\n{data.get('methods', '')}")
    st.markdown(f"### Results\n{data.get('results', '')}")
    st.markdown(f"### Discussion\n{data.get('discussion', '')}")
    st.markdown(f"### Conclusion\n{data.get('conclusion', '')}")
    if "references" in data:
        st.markdown("### References")
        for ref in data["references"]:
            st.markdown(f"- [{ref}]({ref})")
