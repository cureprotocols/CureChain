import streamlit as st

def show_protocol_detail(protocol_name):
    # Placeholder for detailed protocol information
    st.title(f"Protocol Details: {protocol_name}")
    st.markdown("""
    This is where detailed information about the protocol will go.
    You can include research, methodology, usage guidelines, and much more.
    """)
    st.write(f"Detailed data for {protocol_name} will be displayed here.")
    
    # Rating System
    st.markdown("### Rate this protocol")
    
    # Save the rating (in session state for simplicity)
    if 'rating' not in st.session_state:
        st.session_state['rating'] = 0
    
    rating = st.slider('Select Rating', 1, 5, value=st.session_state['rating'])
    
    if st.button("Submit Rating"):
        st.session_state['rating'] = rating
        st.write(f"Thank you for rating this protocol: {rating} stars!")
