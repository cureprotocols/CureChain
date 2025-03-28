import openai
import requests
import streamlit as st

# Function to fetch new research articles from an external source (e.g., PubMed)
def fetch_new_research(protocol_name):
    # Example: Fetching articles related to Baicalin and influenza (simulate this with API or web scraping)
    new_research = f"New study on {protocol_name} suggests Baicalin is more effective in treating new influenza strains. Research by [Author et al.] shows 50% improvement."
    return new_research

# Function to generate and update protocol content based on new research
def update_protocol_with_new_data(protocol_name):
    new_data = fetch_new_research(protocol_name)
    
    # Generate updated protocol using GPT
    response = openai.Completion.create(
        model="text-davinci-003",
        prompt=f"Update the protocol for {protocol_name} with the following new data: {new_data}. Provide a detailed protocol update.",
        max_tokens=500
    )
    return response.choices[0].text.strip()

def show_protocol_viewer():
    st.markdown("### Protocol Viewer")

    protocol_name = st.text_input("Enter the protocol name", "INFLUX-CORE")
    
    if st.button("Update Protocol with New Research"):
        # Automatically update the protocol with new research findings
        updated_protocol = update_protocol_with_new_data(protocol_name)
        st.write("### Updated Protocol Content")
        st.write(updated_protocol)
