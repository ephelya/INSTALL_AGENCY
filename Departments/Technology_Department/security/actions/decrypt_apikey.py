import os
from cryptography.fernet import Fernet

# Charger la clé de chiffrement depuis un fichier sécurisé
with open("encryption_key.key", "rb") as key_file:
    encryption_key = key_file.read()

# Crée l'objet Fernet à partir de la clé
cipher_suite = Fernet(encryption_key)

# Fonction pour déchiffrer une clé API chiffrée
def decrypt_api_key(encrypted_api_key):
    plain_text = cipher_suite.decrypt(encrypted_api_key).decode('utf-8')  # Décodage en UTF-8
    return plain_text

