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

    # Add a search bar
    search_query = st.text_input("Search Protocols")

    # List of protocols
    featured_protocols = [
        {"name": "Protocol 1", "description": "Brief description of Protocol 1.", "link": "protocol_1"},
        {"name": "Protocol 2", "description": "Brief description of Protocol 2.", "link": "protocol_2"},
        {"name": "Protocol 3", "description": "Brief description of Protocol 3.", "link": "protocol_3"},
        {"name": "Protocol 4", "description": "Brief description of Protocol 4.", "link": "protocol_4"},
        {"name": "Protocol 5", "description": "Brief description of Protocol 5.", "link": "protocol_5"},
    ]

    # Filter protocols based on the search query
    filtered_protocols = [protocol for protocol in featured_protocols if search_query.lower() in protocol["name"].lower()]

    # Display the filtered protocols
    if filtered_protocols:
        cols = st.columns(3)  # Adjust columns as needed
        for i, protocol in enumerate(filtered_protocols):
            with cols[i % 3]:
                st.markdown(f"**{protocol['name']}**")
                st.write(protocol['description'])
                if st.button(f"View {protocol['name']}"):
                    st.experimental_set_query_params(protocol=protocol['link'])
    else:
        st.write("No protocols found matching your search.")
