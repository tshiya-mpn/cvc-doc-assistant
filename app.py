
import streamlit as st
from ollama import chat

# Configuration de la page
st.set_page_config(
    page_title="CVC Doc Assistant",
    layout="wide",
    initial_sidebar_state="expanded",
)
# Code couleur de BEMING
st.markdown("""
<style>
    :root {
        --rose: #D2267B;
        --framboise: #97114F;
        --anthracite: #252525;
    }

    .stApp {
        background-color: #F5F5F7;
    }

    h1, h2, h3 {
        color: #252525;
    }

    .stButton > button[kind="primary"] {
        background-color: #D2267B;
        border-color: #D2267B;
        color: white;
        border-radius: 10px;
    }

    .stButton > button[kind="primary"]:hover {
        background-color: #97114F;
        border-color: #97114F;
    }

    .brand-label {
        color: #D2267B;
        font-size: 0.85rem;
        font-weight: 700;
        letter-spacing: 0.12em;
    }

    .subtitle {
        color: #666666;
        margin-bottom: 1.5rem;
    }
</style>
""", unsafe_allow_html=True)


# Page d'accueil
st.markdown(
    '<div class="brand-label">ASSISTANT DOCUMENTAIRE PÔLE CHAUFFAGE, VENTILATION, CLIMATISATION</div>',
    unsafe_allow_html=True,
)
st.title("CVC Doc Assistant")
st.markdown(
    '<div class="subtitle">'
    "Analysez des extraits de cahiers des clauses techniques particulières ou de fiches techniques "
    "avec une intelligence artificielle"
    "</div>",
    unsafe_allow_html=True,
)

# Deux colonnes principales
col_document, col_assistant = st.columns([1, 1.25], gap="large")

with col_document:
    st.subheader("Document CVC")
    st.caption("Étape 1 — Ajoutez un extrait de document technique")

    document = st.text_area(
        "Contenu du document",
        height=280,
        placeholder="Extrait de CCTP...",
    )

    if document.strip():
        st.success(f"Document prêt — {len(document)} caractères")
    else:
        st.info("Ajoutez un document pour commencer")

    st.caption("L'import PDF sera ajouté à la prochaine étape")

with col_assistant:
    st.subheader("Assistant IA")
    st.caption("Étape 2 — Posez une question sur le document")

    question = st.text_input(
        "Votre question",
        placeholder="Ex. Quel est le débit nominal exigé ?",
    )

    analyser = st.button(
        "Analyser le document",
        type="primary",
        use_container_width=True,
    )

 