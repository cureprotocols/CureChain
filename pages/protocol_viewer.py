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

    # New Protocols Notification
    subscribe = st.checkbox("Subscribe to notifications for new protocols")

    if subscribe:
        # Simulate sending a notification (e.g., an email)
        st.success("You're subscribed to notifications for new protocols!")
    else:
        st.write("Unsubscribed from notifications.")
    
    # List of protocols (example)
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
