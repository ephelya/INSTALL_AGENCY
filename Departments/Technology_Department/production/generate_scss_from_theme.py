from files.backend.src.services.Marketing_Department.design.actions.g  import get_theme_base_values


def generate_scss_from_theme(theme_data, output_path):
    """
    Fonction générique pour générer un fichier SCSS à partir des thèmes de couleurs et dimensions.
    """
    scss_content = ""
    
    # Générer les variables de couleurs
    base_palette = generate_dynamic_palette(theme_data['base_color'])
    accent_palette = generate_dynamic_palette(theme_data['accent_color'])
    neutral_palette = generate_dynamic_palette(theme_data['neutral_color'])
    
    # Générer les dimensions
    dimensions = generate_dynamic_dimensions(theme_data['base_width'], theme_data['base_padding'], theme_data['base_radius'])
    
    # Ajouter les variables de couleurs
    scss_content += f"$base-color: {theme_data['base_color']};\n"
    scss_content += f"$accent-color: {theme_data['accent_color']};\n"
    scss_content += f"$neutral-color: {theme_data['neutral_color']};\n"
    
    for key, value in base_palette.items():
        scss_content += f"${key}: {value};\n"
    
    for key, value in accent_palette.items():
        scss_content += f"${key}: {value};\n"
    
    for key, value in neutral_palette.items():
        scss_content += f"${key}: {value};\n"
    
    # Ajouter les variables de dimensions
    for key, value in dimensions.items():
        scss_content += f"${key}: {value};\n"
    
    # Ajouter des styles de base utilisant ces variables
    scss_content += """
body {
    background-color: $neutral-color;
    padding: $base_padding;
    border-radius: $base_radius;
}

.button {
    background-color: $accent-color;
    padding: $large_padding;
    border-radius: $large_radius;
}
"""
    # Écrire le contenu SCSS dans un fichier
    with open(output_path, 'w') as scss_file:
        scss_file.write(scss_content)

    print(f"Fichier SCSS généré avec succès : {output_path}")
