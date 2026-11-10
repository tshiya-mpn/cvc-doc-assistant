# CVC Doc Assistant

**Assistant documentaire CVC basé sur une intelligence artificielle locale**

## Présentation

CVC Doc Assistant est un prototype développé en Python permettant d'interroger des documents techniques liés au **chauffage, à la ventilation et à la climatisation (CVC)**.

Son objectif est de faciliter la recherche d'informations dans les cahiers des clauses techniques particulières (CCTP) et les fiches techniques fabricants.

## Fonctionnalités

- Saisie d'extraits de documents techniques.
- Importation et extraction de texte PDF.
- Questions en langage naturel.
- Réponses générées par une IA locale.
- Interface web simple et intuitive.

## Technologies utilisées

- **Python 3.11** — Développement
- **Streamlit** — Interface web
- **PyMuPDF** — Extraction PDF
- **Ollama + Qwen 2.5 (1.5B)** — Intelligence artificielle locale
- **Git / GitHub** — Versionnement

## Installation

Prérequis : Python 3.11 et Ollama

```bash
git clone https://github.com/tshiya-mpn/cvc-doc-assistant.git
cd cvc-doc-assistant

python3.11 -m venv .venv
source .venv/bin/activate

python -m pip install -r requirements.txt
ollama pull qwen2.5:1.5b

python -m streamlit run app.py
```

Ollama doit être en cours d'exécution (`ollama serve` si nécessaire).


## Perspectives d'évolution

- Intégration d'un système **RAG** pour améliorer la recherche documentaire et les références aux sources.
- Comparaison des exigences CCTP avec les fiches fabricants.
- Export de tableaux et de rapports d'analyse.
- OCR, analyse multidocument et gestion des accès.

## Limites

Ce projet est un **POC**. Les réponses de l'IA peuvent contenir des erreurs et doivent être vérifiées dans les documents d'origine. L'application ne valide pas automatiquement la conformité technique.

## Auteur

Projet personnel réalisé dans une démarche de montée en compétences en Python, IA locale et gestion de projet informatique.

**GitHub :** [tshiya-mpn](https://github.com/tshiya-mpn)