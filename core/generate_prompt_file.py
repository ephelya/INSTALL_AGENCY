import os
import datetime

def generate_prompt_file(prompt_name, description, context="", agent_role="", agent_persona="", 
                         user_persona="", agent_mission="", prompt_text="", style="", 
                         expected_format="", author="default_author"):
    """
    Génère un fichier de template de prompt en remplissant les placeholders si les valeurs sont fournies.

    Args:
        prompt_name (str): Nom du prompt.
        description (str): Brève description de l'objectif du prompt.
        context (str, optional): Contexte d'utilisation du prompt.
        agent_role (str, optional): Rôle assigné à l'agent IA.
        agent_persona (str, optional): Caractéristiques de personnalité de l'agent IA.
        user_persona (str, optional): Profil ou tempérament supposé de l'utilisateur.
        agent_mission (str, optional): Mission de l'agent pour ce prompt.
        prompt_text (str, optional): Texte du prompt avec placeholders.
        style (str, optional): Style attendu pour la réponse.
        expected_format (str, optional): Format attendu de la réponse.
        author (str, optional): Auteur du prompt.
    """
    # Chemin des templates
    template_path = os.path.join(os.getcwd(), "Templates", "prompt_template.txt")
    metadata_template_path = os.path.join(os.getcwd(), "Templates", "metadata_template.txt")
    
    # Générer les métadonnées à partir du template
    last_update = datetime.datetime.now().strftime("%y%m%d-%H%M")
    with open(metadata_template_path, "r") as metadata_template_file:
        metadata_content = metadata_template_file.read()
        metadata_content = metadata_content.replace("<prompt_name>", prompt_name)
        metadata_content = metadata_content.replace("<description>", description)
        metadata_content = metadata_content.replace("<last_update>", last_update)
        metadata_content = metadata_content.replace("<author>", author)

    # Lecture du contenu du template de prompt
    with open(template_path, "r") as template_file:
        template_content = template_file.read()

    # Remplacement conditionnel des placeholders
    file_content = template_content.replace("<metadatas>", metadata_content)
    file_content = file_content.replace("<context>", context if context else "")
    file_content = file_content.replace("<agent_role>", agent_role if agent_role else "")
    file_content = file_content.replace("<agent_persona>", agent_persona if agent_persona else "")
    file_content = file_content.replace("<user_persona>", user_persona if user_persona else "")
    file_content = file_content.replace("<agent_mission>", agent_mission if agent_mission else "")
    file_content = file_content.replace("<prompt_text>", prompt_text if prompt_text else "")
    file_content = file_content.replace("<style>", style if style else "")
    file_content = file_content.replace("<expected_format>", expected_format if expected_format else "")

    # Création du répertoire pour les prompts si nécessaire
    prompt_dir = os.path.join("Templates", "prompts")
    os.makedirs(prompt_dir, exist_ok=True)
    
    # Chemin final du fichier de prompt
    prompt_file_path = os.path.join(prompt_dir, f"{prompt_name}.txt")

    # Écriture du contenu dans le fichier
    with open(prompt_file_path, "w") as prompt_file:
        prompt_file.write(file_content)

    print(f"Fichier de prompt généré : {prompt_file_path}")

# Exemple d'utilisation
if __name__ == "__main__":
    generate_prompt_file(
        prompt_name="Support Client",
        description="Aide l'agent IA à répondre aux demandes des clients.",
        context="L'agent IA aide le service client en répondant aux demandes des clients.",
        agent_role="Agent IA - Support Client, assistant virtuel pour les réponses client.",
        agent_persona="Amical, patient, encourageant",
        user_persona="Client stressé recherchant des solutions rapides",
        agent_mission="Fournir des réponses précises et rapides aux questions des clients.",
        prompt_text="Bonjour, <client_name>! Comment puis-je vous aider aujourd'hui?",
        style="Formel, concis",
        expected_format="Réponse en JSON avec le statut de la demande et les actions recommandées.",
        author="Equipe Support"
    )
