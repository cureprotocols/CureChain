import streamlit as st
from streamlit_lottie import st_lottie
import requests

def show_protocol_viewer():
    # Welcome Banner
    st.markdown("""
    <div style="padding: 1rem; background-color: #1a1a1a; border-radius: 1rem; border: 1px solid #333;">
        <h3 style='margin-bottom: 0.5rem;'>👋 Welcome to CureChain</h3>
        <p style='font-size: 0.95rem;'>
            This is a decentralized, open-source healing protocol registry.
            All protocols published here are sovereign, unpatentable, and science-ready.
        </p>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("### 🔬 Browse Available Protocols")

    # Lottie Animation URL for carousel
    lottie_url = "https://assets8.lottiefiles.com/packages/lf20_H5xgcm.json"  # You can customize this with your own animation
    lottie_response = requests.get(lottie_url)
    lottie_json = lottie_response.json()
    
    # Display carousel animation
    st_lottie(lottie_json, speed=1, width=600, height=400, key="featured_protocols")

    # Featured Protocols (You can customize this section further)
    featured_protocols = [
        {"name": "Protocol 1", "description": "Brief description of Protocol 1.", "link": "protocol_1"},
        {"name": "Protocol 2", "description": "Brief description of Protocol 2.", "link": "protocol_2"},
        {"name": "Protocol 3", "description": "Brief description of Protocol 3.", "link": "protocol_3"},
    ]

    st.markdown("### Featured Protocols")
    
    cols = st.columns(3)  # Adjust columns as needed
    for i, protocol in enumerate(featured_protocols):
        with cols[i % 3]:
            st.markdown(f"**{protocol['name']}**")
            st.write(protocol['description'])
            if st.button(f"View {protocol['name']}"):
                st.experimental_set_query_params(protocol=protocol['link'])
