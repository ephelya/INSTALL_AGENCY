import datetime
import os

def add_metadata(file_path, file_type, author, file_version, file_mission, inputs_params=None, output_params=None):
    """
    Ajoute des métadonnées standard au début d'un fichier.
    
    Args:
        file_path (str): Le chemin du fichier où les métadonnées seront ajoutées.
        file_type (str): Le type du fichier (action, agent, html_template, etc.).
        author (str): L'auteur du fichier.
        file_version (str): La version du fichier.
        file_mission (str): Description de la mission du fichier.
        inputs_params (list): Liste des paramètres requis pour l'exécution de la fonction.
        output_params (list): Liste des paramètres retournés (nom et description).
    """
    # Génération de la date et heure actuelle pour last_update
    last_update = datetime.datetime.now().strftime("%y%m%d-%H%M")
    
    # Prépare le contenu des inputs et outputs
    inputs_params_str = ", ".join(inputs_params) if inputs_params else "None"
    output_params_str = ", ".join(output_params) if output_params else "None"

    # Lecture du template de métadonnées
    with open("Templates/metadata_template.txt", "r") as template_file:
        metadata = template_file.read()
    
    # Remplace les placeholders dans le template
    metadata = metadata.replace("<file_type>", file_type)
    metadata = metadata.replace("<file_name>", os.path.basename(file_path))
    metadata = metadata.replace("<last_update>", last_update)
    metadata = metadata.replace("<author>", author)
    metadata = metadata.replace("<file_path>", file_path)
    metadata = metadata.replace("<file_version>", file_version)
    metadata = metadata.replace("<file_mission>", file_mission)
    metadata = metadata.replace("<inputs_params>", inputs_params_str)
    metadata = metadata.replace("<output_params>", output_params_str)

    # Lecture du contenu original du fichier
    with open(file_path, "r") as f:
        content = f.read()
    
    # Écriture des métadonnées et du contenu original dans le fichier
    with open(file_path, "w") as f:
        f.write(metadata + "\n\n" + content)
    
    print(f"Métadonnées ajoutées au fichier {file_path}.")

# Exemple d'utilisation
if __name__ == "__main__":
    add_metadata(
        file_path="Departments/General_Direction/actions/create_project.py",
        file_type="action",
        author="General_Direction",
        file_version="1.0",
        file_mission="Crée un projet et configure les répertoires",
        inputs_params=["project_name", "project_type"],
        output_params=["status"]
    )
