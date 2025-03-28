import streamlit as st

def show_protocol_detail(protocol_name):
    # Placeholder for detailed protocol information
    st.title(f"Protocol Details: {protocol_name}")
    st.markdown("""
    This is where detailed information about the protocol will go.
    You can include research, methodology, usage guidelines, and much more.
    """)
    st.write(f"Detailed data for {protocol_name} will be displayed here.")

    # User Comment Section
    st.markdown("### Leave a Comment")
    
    # Get user comment
    comment = st.text_area("Enter your comment:")
    
    if st.button("Submit Comment"):
        if comment:
            st.success("Your comment has been submitted!")
            st.write(f"**{comment}**")
        else:
            st.warning("Please enter a comment before submitting.")
