import os

def create_file(path, content):
    with open(path, 'w') as file:
        file.write(content)
    print(f"Fichier créé : {path}")