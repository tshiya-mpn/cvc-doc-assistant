
import streamlit as st
from ollama import chat

# Configuration de la page
st.set_page_config(
    page_title="CVC Doc Assistant",
    layout="wide",
    initial_sidebar_state="expanded",
)
