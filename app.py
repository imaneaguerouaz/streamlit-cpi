import streamlit as st

# Titre de l'application
st.title("Évaluation Adaptative - SVT")

# Initialiser le niveau à 1 si ce n'est pas déjà fait
if 'niveau' not in st.session_state:
    st.session_state.niveau = 1

# Fonction pour poser une question en fonction du niveau
def poser_question(niveau):
    if niveau == 1:
        question = "Quelle est la fonction des racines chez une plante ?"
        bonne_reponse = "Absorber l'eau et les nutriments"
    elif niveau == 2:
        question = "Qu'est-ce que la photosynthèse ?"
        bonne_reponse = "Le processus par lequel les plantes fabriquent leur nourriture à partir de la lumière, de l'eau et du dioxyde de carbone"
    elif niveau == 3:
        question = "Quel est le rôle des globules rouges dans le sang ?"
        bonne_reponse = "Transporter l'oxygène"
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
        if bonne_reponse and reponse.lower() == bonne_reponse.lower():  # Comparaison insensible à la casse
            st.success("Bonne réponse ! 😊")
            st.session_state.niveau += 1  # Passer au niveau suivant
            st.write(f"Passons à la question du niveau {st.session_state.niveau}.")
            # La page sera mise à jour automatiquement pour afficher la prochaine question
        else:
            st.error("Mauvaise réponse. Essayez à nouveau.")
