# Trier Downloads - Organisation automatique des fichiers

Ce projet a pour objectif de simplifier la gestion des fichiers dans le dossier **Téléchargements**. Il organise automatiquement les fichiers en les triant par type dans des sous-dossiers spécifiques (Images, Vidéos, Documents, etc.).

---

## 🎯 Objectif

Avec le temps, le dossier de téléchargements peut devenir encombré et difficile à naviguer. Ce projet propose une solution automatisée pour maintenir ce dossier propre et structuré, sans effort manuel.

---

## ✨ Fonctionnalités principales

- Classement automatique des fichiers par catégorie :
  - **Images**, **Vidéos**, **Documents**, **Archives**, etc.
- Création automatique des sous-dossiers nécessaires.
- Gestion des fichiers non catégorisés avec un dossier "Divers".
- Possibilité de choisir le dossier à organiser.

---

## 🛠️ Technologies utilisées

- **Python** : Langage principal pour le développement du script.
- **Modules standards** :
  - `os` et `shutil` pour la manipulation des fichiers et des dossiers.

---

## 🚀 Inspirations et perspectives

Ce projet est né d'un besoin personnel d'automatisation pour gagner du temps et améliorer l'organisation. À l'avenir, il pourrait être enrichi par :

- Une interface graphique (GUI) pour une utilisation plus intuitive.
- Une planification automatique intégrée.

---

## 📂 Structure simple du projet

- `app.py` : Script principal pour le tri des fichiers.
- `README.md` : Document de présentation du projet.

---

## 🔧 Conversion du script en exécutable (.exe)

Pour rendre le script exécutable sans nécessiter Python, voici les étapes :

1. Installez **PyInstaller** (une seule fois) :

   ```bash
   pip install pyinstaller
   ```

2. Convertissez le fichier Python (app.py) en exécutable :
   ```bash
   pyinstaller --onefile app.py
   ```
   L'exécutable généré se trouve dans le dossier dist/.
