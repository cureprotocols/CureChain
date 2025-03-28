# app.py
import streamlit as st
from pages.protocol_viewer import show_protocol_viewer
from pages.submit_protocol import show_submit_protocol
from pages.about import show_about  # <-- Added

st.set_page_config(page_title="CureChain | Open Protocol Library", layout="centered")

st.sidebar.title("CureChain Navigation")
option = st.sidebar.radio("Go to:", (
    "View Protocols",
    "Submit a Protocol",
    "About"  # <-- Added to sidebar
))

if option == "View Protocols":
    show_protocol_viewer()
elif option == "Submit a Protocol":
    show_submit_protocol()
elif option == "About":
    show_about()
