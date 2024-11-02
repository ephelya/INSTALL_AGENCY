
from files.backend.src.services.Marketing_Department.design.actions.get_theme_base_values  import get_theme_base_values
from files.backend.src.services.Technology_Department.production.generate_scss_from_theme import generate_scss_from_theme
import os

def generate_scss_file():
    """
    Fonction principale pour générer un fichier SCSS à partir de la base de données.
    """
    # Récupérer les valeurs de base depuis la base de données
    theme_data = get_theme_base_values()

    # Spécifier le chemin de sortie pour le fichier SCSS
    output_path = os.path.join("assets", "styles", "theme_styles.scss")

    # Générer le fichier SCSS
    generate_scss_from_theme(theme_data, output_path)

# Appel de la fonction pour générer le fichier SCSS
if __name__ == "__main__":
    generate_scss_file()
