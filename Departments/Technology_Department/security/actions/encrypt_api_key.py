import os
from cryptography.fernet import Fernet
from files.backend.src.services.Technology_Department.security.actions.generate_encryption_key import generate_encryption_key  # Importer la fonction générique

def encrypt_api_key(api_key, key_path="encryption_key.key"):
    """
    Chiffre la clé API envoyée en paramètre.
    
    :param api_key: Clé API à chiffrer (chaîne de caractères).
    :param key_path: Chemin de la clé de chiffrement (par défaut "encryption_key.key").
    :return: Clé API chiffrée (bytes).
    """
    # Récupérer ou générer la clé de chiffrement
    encryption_key = generate_encryption_key(key_path)
    
    # Créer l'objet Fernet
    cipher_suite = Fernet(encryption_key)
    
    # Chiffrer la clé API
    cipher_text = cipher_suite.encrypt(api_key.encode('utf-8'))  # Encodage en UTF-8
    return cipher_text
