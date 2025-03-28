import streamlit as st

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

    # Featured Protocol of the Week
    st.markdown("""
    <div style="padding: 1rem; background-color: #1a1a1a; border-radius: 1rem; border: 1px solid #333;">
        <h3 style='margin-bottom: 0.5rem;'>🔬 Featured Protocol of the Week</h3>
        <p style='font-size: 0.95rem;'>
            This protocol is highlighted for its significance in the healing community.
            It is chosen for its research-backed approach and proven effectiveness.
        </p>
    </div>
    """, unsafe_allow_html=True)

    # List of protocols (example placeholder, replace with actual protocol listing)
    protocols = ["Protocol 1", "Protocol 2", "Protocol 3"]
    
    for protocol in protocols:
        st.markdown(f"### {protocol}")
        st.write("Details about this protocol go here.")

