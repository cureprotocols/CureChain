import openai
import streamlit as st

# Set up OpenAI API key
openai.api_key = "your-openai-api-key"

# Function to generate protocol recommendations
def recommend_protocols(user_condition):
    # Use GPT to generate protocol suggestions based on user condition
    response = openai.Completion.create(
        model="text-davinci-003",
        prompt=f"Recommend the most suitable protocols for the following health condition: {user_condition}. Provide a brief summary of why each protocol is relevant.",
        max_tokens=500
    )
    return response.choices[0].text.strip()

def show_protocol_viewer():
    st.markdown("### Protocol Discovery and Recommendation")

    # User Input for Condition or Goal
    user_condition = st.text_input("Enter your health condition or goal", "flu")

    if st.button("Get Protocol Recommendations"):
        if user_condition:
            # Use GPT to generate protocol recommendations
            recommended_protocols = recommend_protocols(user_condition)
            st.write("### Recommended Protocols:")
            st.write(recommended_protocols)
        else:
            st.warning("Please enter a health condition or goal to get recommendations.")
