def generate_dynamic_palette(base_color):
    """
    Fonction pour générer des variations de couleurs à partir d'une couleur de base.
    Utilisation de la fonction lighten pour obtenir des nuances plus claires.
    """
    return {
        'light_color': f'lighten({base_color}, 30%)',
        'vlight_color': f'lighten({base_color}, 50%)',
        'dark_color': f'darken({base_color}, 20%)',
    }
