def generate_dynamic_dimensions(base_width, base_padding, base_radius):
    """
    Fonction pour générer des variations de dimensions à partir de valeurs de base.
    """
    return {
        'large_width': f'calc({base_width} * 2)',
        'small_width': f'calc({base_width} / 2)',
        'large_padding': f'calc({base_padding} * 1.5)',
        'small_padding': f'calc({base_padding} / 2)',
        'large_radius': f'calc({base_radius} * 2)',
        'small_radius': f'calc({base_radius} / 2)',
    }
