import streamlit as st

def show_user_profile():
    st.title("User Profile")

    # User information form
    with st.form(key="user_profile_form"):
        name = st.text_input("Name", value="John Doe")
        email = st.text_input("Email", value="johndoe@example.com")
        bio = st.text_area("Bio", value="This is my bio")

        submit_button = st.form_submit_button("Save Profile")

    if submit_button:
        # You could save this data to a database or session state for persistence
        st.success("Profile saved!")
        st.write(f"Name: {name}")
        st.write(f"Email: {email}")
        st.write(f"Bio: {bio}")
