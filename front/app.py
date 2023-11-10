import streamlit as st
import utils

# Fonction principale pour la génération de la page
def main():
    # Titre de la page
    st.title("Spacy Science")

    # Ajout d'un textarea
    user_input = st.text_area("Entrez du texte ici:")

    # Ajout d'un bouton de validation
    if st.button("Valider"):
        # Action à effectuer lorsque le bouton est cliqué
        response = utils.api_predict(user_input)
        utils.response_st(response['response'])

# Exécution de la fonction principale
if __name__ == "__main__":
    main()


