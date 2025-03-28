import streamlit as st
import openai

# Set up your OpenAI API key (ensure this is kept secure)
openai.api_key = "your-openai-api-key"

def generate_protocol_content(protocol_summary):
    response = openai.Completion.create(
        model="text-davinci-003",  # GPT-3 model
        prompt=f"Generate a scientific protocol based on the following summary: {protocol_summary}",
        max_tokens=500
    )
    return response.choices[0].text.strip()

def show_protocol_viewer():
    st.markdown("### Create a New Protocol")

    # User Input for Protocol Summary
    protocol_summary = st.text_area("Enter a brief summary of the protocol", "")

    if st.button("Generate Protocol Content"):
        if protocol_summary:
            # Call the GPT model to generate the protocol content
            protocol_content = generate_protocol_content(protocol_summary)
            st.markdown("### Generated Protocol")
            st.write(protocol_content)
        else:
            st.warning("Please enter a summary to generate the protocol.")

    st.markdown("### Existing Protocols")
    # Example protocols can go here, or this can list protocols already added in your system.
    featured_protocols = [
        {"name": "Protocol 1", "description": "Brief description of Protocol 1."},
        {"name": "Protocol 2", "description": "Brief description of Protocol 2."}
    ]

    # Display existing protocols
    for protocol in featured_protocols:
        st.markdown(f"**{protocol['name']}**")
        st.write(protocol['description'])
        if st.button(f"View {protocol['name']}"):
            st.experimental_set_query_params(protocol=protocol['name'])
