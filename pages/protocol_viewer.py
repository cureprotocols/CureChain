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

    # Pagination controls
    page_size = 3  # Number of protocols per page
    page_number = st.session_state.get("page_number", 1)

    # List of protocols
    featured_protocols = [
        {"name": "Protocol 1", "description": "Brief description of Protocol 1.", "link": "protocol_1"},
        {"name": "Protocol 2", "description": "Brief description of Protocol 2.", "link": "protocol_2"},
        {"name": "Protocol 3", "description": "Brief description of Protocol 3.", "link": "protocol_3"},
        {"name": "Protocol 4", "description": "Brief description of Protocol 4.", "link": "protocol_4"},
        {"name": "Protocol 5", "description": "Brief description of Protocol 5.", "link": "protocol_5"},
        {"name": "Protocol 6", "description": "Brief description of Protocol 6.", "link": "protocol_6"},
        {"name": "Protocol 7", "description": "Brief description of Protocol 7.", "link": "protocol_7"},
        {"name": "Protocol 8", "description": "Brief description of Protocol 8.", "link": "protocol_8"},
    ]

    # Calculate the range of protocols to display based on the current page
    start = (page_number - 1) * page_size
    end = start + page_size
    protocols_to_display = featured_protocols[start:end]

    # Display the protocols for the current page
    cols = st.columns(3)  # Adjust columns as needed
    for i, protocol in enumerate(protocols_to_display):
        with cols[i % 3]:
            st.markdown(f"**{protocol['name']}**")
            st.write(protocol['description'])
            if st.button(f"View {protocol['name']}"):
                st.experimental_set_query_params(protocol=protocol['link'])

    # Pagination buttons
    if page_number > 1:
        if st.button("Previous Page"):
            st.session_state.page_number -= 1
    if end < len(featured_protocols):
        if st.button("Next Page"):
            st.session_state.page_number += 1
