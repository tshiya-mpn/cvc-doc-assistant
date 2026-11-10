
import streamlit as st
from ollama import chat
import pymupdf

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
    st.caption("Étape 1 : Ajoutez un extrait de document technique ou importez un document PDF")

    # Zone de saisie extrait document technique
    texte_saisi = st.text_area(
        "Contenu du document",
        height=280,
        placeholder="Extrait de CCTP...",
        label_visibility="collapsed",
    )

    # Import PDF
    fichier_pdf = st.file_uploader(
        "Importer un document PDF",
        type=["pdf"],
        label_visibility="collapsed",
    )

    texte_pdf = ""

    if fichier_pdf is not None:
        try:
            pages = []
            with pymupdf.open(
                stream=fichier_pdf.getvalue(),
                filetype="pdf",
            ) as pdf:
                for numero, page in enumerate(pdf, start=1): # numérotation des pages
                    contenu = page.get_text("text").strip()
                    if contenu:
                        pages.append(
                            f"[PAGE {numero}]\n{contenu}" # vérifie si la page contient du texte
                        )
            texte_pdf = "\n\n".join(pages)

            if texte_pdf:
                st.success(f"PDF importé : {fichier_pdf.name}")
                with st.expander("Voir le texte extrait du PDF"): # visualtion d'un extrait du PDF importé
                    st.text_area(
                        "Aperçu du PDF",
                        value=texte_pdf[:10000],
                        height=200,
                        disabled=True,
                    )
            else:
                st.warning("Aucun texte détecté dans ce PDF.")
        except Exception as erreur:
            st.error("Impossible de lire ce PDF.")
            st.code(str(erreur))

    # Combinaison des deux sources
    parties = []

    if texte_saisi.strip():
        parties.append(texte_saisi.strip())

    if texte_pdf.strip():
        parties.append(texte_pdf.strip())

    document = "\n\n".join(parties)

    if document:
        st.success(
            f"Document prêt — {len(document):,} caractères"
        )
    else:
        st.info("Ajoutez un texte ou importez un PDF.")

# Poser une question et afficher la réponse du LLM
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
                                    "Tu es un assistant documentaire spécialisé en CVC (chauffage, ventilation, climatisation). "
                                    "Réponds en français, uniquement à partir du document fourni. "
                                    "Si une information est absente, dis-le. "
                                    "N'invente aucune valeur technique. "
                                    "Ne prétends jamais valider la conformité d'un équipement."
                                    "Si le document contient des marqueurs [PAGE N], indique la page contenant l'information utilisée. "
                                    "Ne cite jamais une page sans justification dans le document. "
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
                         options={"temperature": 0}, #neutralise la créativité et le hasard pour obtenir des réponses déterministes, précises et fidèles aux données textuelles
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