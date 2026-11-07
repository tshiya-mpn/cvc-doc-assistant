
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
    st.caption("Étape 1 : Ajoutez un extrait de document technique")

    document = st.text_area(
        "Contenu du document",
        height=280,
        placeholder="Extrait de CCTP...",
    )

    if document.strip():
        st.success(f"Document ajouté — {len(document)} caractères")
    else:
        st.info("Ajoutez un document pour commencer")

    st.caption("Ajoutez un PDF")

with col_assistant:
    st.subheader("Assistant IA")
    st.caption("Étape 2 : Posez une question sur le document")

    question = st.text_input(
        "Votre question",
        placeholder="Ex. Quel est le débit nominal exigé ?",
    )

    analyser = st.button(
        "Analyser le document",
        type="primary",
        use_container_width=True,
    )

    if analyser:
         if not document.strip() or not question.strip():
             st.warning("Veuillez renseigner un document et une question")
         else:
             with st.spinner("Qwen analyse votre document..."):
                 try:
                     response = chat(
                         model="qwen2.5:1.5b",
                         messages=[
                             {
                                 "role": "system",
                                 "content": (
                                     "Tu es un assistant documentaire spécialisé "
                                     "en CVC (chauffage, ventilation, climatisation). "
                                     "Réponds en français, uniquement à partir "
                                     "du document fourni. "
                                     "Si une information est absente, dis-le. "
                                     "N'invente aucune valeur technique. "
                                     "Ne prétends jamais valider la conformité "
                                     "d'un équipement."
                                 ),
                             },
                             {
                                 "role": "user",
                                 "content": (
                                     f"DOCUMENT :\n{document}\n\n"
                                     f"QUESTION :\n{question}"
                                 ),
                             },
                         ],
                         options={"temperature": 0},
                     )
 
                     st.markdown("#### Résultat de l'analyse")
                     st.markdown(response.message.content)
 
                 except Exception as erreur:
                     st.error(
                         "Impossible de contacter le modèle local. "
                         "Vérifiez qu'Ollama fonctionne."
                     )
                     st.code(str(erreur))
 
    st.divider()
    st.markdown("**Exemples de questions**")
    st.caption("• Quel est le débit nominal demandé ?")
    st.caption("• Quelle puissance thermique est exigée ?")
    st.caption("• Quelles sont les exigences techniques mentionnées ?")