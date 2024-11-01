#!/bin/bash

# Vérifie si un dépôt Git est déjà initialisé
if [ ! -d .git ]; then
    echo "Initialisation du dépôt Git local..."
    git init
fi

# Vérifie si un dépôt distant est configuré
remote_url=$(git config --get remote.origin.url)

if [ -z "$remote_url" ]; then
    read -p "Entrez l'URL de votre dépôt GitHub (ex: https://github.com/username/repository.git) : " repo_url
    git remote add origin "$repo_url"
    echo "Dépôt GitHub configuré avec l'URL : $repo_url"
else
    echo "Dépôt distant déjà configuré avec l'URL : $remote_url"
fi

# Vérifie si des modifications ont été faites
if git diff --quiet && git diff --cached --quiet; then
    echo "Aucune modification détectée."
    exit 0
fi

# Ajoute toutes les modifications au staging
git add .

# Demande un message de commit à l'utilisateur
read -p "Entrez un message de commit : " commit_message

# Effectue le commit
git commit -m "$commit_message"

# Pousse les modifications vers le dépôt distant
git push -u origin main

echo "Les modifications ont été poussées sur GitHub avec succès."
