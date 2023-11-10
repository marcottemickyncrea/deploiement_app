import requests
import streamlit as st

def api_predict(text: str) -> dict:
    """
    appel de l'API pour faire la prédiction
    :text: data recueili par le textarea
    """
    response = requests.post(
        'http://127.0.0.1:8000/predict', json={'text': text})
    return response.json()

def response_st(response: list):
    for ner in response:
        # Accéder aux clés et aux valeurs
        for cle, valeur in ner.items():
            st.success(f"{cle}: {valeur}")