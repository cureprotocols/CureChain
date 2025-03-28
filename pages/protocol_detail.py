import streamlit as st

def show_protocol_detail(protocol_name):
    # Placeholder for detailed protocol information
    st.title(f"Protocol Details: {protocol_name}")
    st.markdown("""
    This is where detailed information about the protocol will go.
    You can include research, methodology, usage guidelines, and much more.
    """)
    st.write(f"Detailed data for {protocol_name} will be displayed here.")

    # Social Sharing
    st.markdown("### Share this protocol:")
    
    twitter_url = f"https://twitter.com/intent/tweet?text=Check%20out%20this%20protocol!%20{protocol_name}&url=https://yourwebsite.com/{protocol_name}"
    facebook_url = f"https://www.facebook.com/sharer/sharer.php?u=https://yourwebsite.com/{protocol_name}"

    # Share buttons
    st.markdown(f"[Share on Twitter]( {twitter_url} )")
    st.markdown(f"[Share on Facebook]( {facebook_url} )")
