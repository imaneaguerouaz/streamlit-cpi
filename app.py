import streamlit as st

# Titre de l'application
st.title("Évaluation Adaptative")

# Initialiser le niveau à 1 si ce n'est pas déjà fait
if 'niveau' not in st.session_state:
    st.session_state.niveau = 1

# Fonction pour poser une question en fonction du niveau
def poser_question(niveau):
    if niveau == 1:
        question = "Combien font 3 + 2 ?"
        bonne_reponse = "5"
    elif niveau == 2:
        question = "Quel est le produit de 7 et 6 ?"
        bonne_reponse = "42"
    elif niveau == 3:
        question = "Quelle est la racine carrée de 144 ?"
        bonne_reponse = "12"
    else:
        question = "Félicitations, vous avez terminé l'évaluation ! 🎉"
        bonne_reponse = None
    return question, bonne_reponse

# Afficher la question actuelle en fonction du niveau
question, bonne_reponse = poser_question(st.session_state.niveau)

# Afficher la question et obtenir la réponse de l'utilisateur
if question:
    reponse = st.text_input(f"Question (Niveau {st.session_state.niveau}): {question}")

    # Vérification de la réponse lorsque l'utilisateur clique sur le bouton "Suivant"
    if reponse and st.button("Suivant"):
        if bonne_reponse and reponse == bonne_reponse:
            st.success("Bonne réponse ! 😊")
            st.session_state.niveau += 1  # Passer au niveau suivant
            st.write(f"Passons à la question du niveau {st.session_state.niveau}.")
            # La page sera mise à jour automatiquement pour afficher la prochaine question
        else:
            st.error("Mauvaise réponse. Essayez à nouveau.")
