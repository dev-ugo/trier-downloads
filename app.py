import os
import shutil

def trier_dossier(downloads_folder):
    # Dictionnaire pour mapper les extensions aux dossiers
    file_categories = {
        "Images": [".jpg", ".jpeg", ".png", ".gif", ".bmp", ".tiff", ".svg"],
        "Vidéos": [".mp4", ".mkv", ".avi", ".mov", ".wmv"],
        "Documents": [".pdf", ".doc", ".docx", ".xls", ".xlsx", ".ppt", ".pptx", ".txt"],
        "Archives": [".zip", ".rar", ".7z", ".tar", ".gz"],
        "Audio": [".mp3", ".wav", ".aac", ".flac"],
        "Programmes": [".exe", ".msi", ".dmg"],
        "Scripts": [".py", ".js", ".html", ".css", ".sh", ".bat"],
        "Divers": []  # Par défaut pour les fichiers non catégorisés
    }

    # Créer les sous-dossiers si nécessaire
    created_folders = set()

    # Trier les fichiers
    for item in os.listdir(downloads_folder):
        item_path = os.path.join(downloads_folder, item)

        # Ignorer les dossiers
        if os.path.isdir(item_path):
            continue

        # Trouver la catégorie du fichier
        file_ext = os.path.splitext(item)[1].lower()
        moved = False
        for category, extensions in file_categories.items():
            if file_ext in extensions:
                if category not in created_folders:
                    os.makedirs(os.path.join(downloads_folder, category), exist_ok=True)
                    created_folders.add(category)
                shutil.move(item_path, os.path.join(downloads_folder, category, item))
                moved = True
                break

        # Si aucune catégorie trouvée, déplacer dans "Divers"
        if not moved:
            if "Divers" not in created_folders:
                os.makedirs(os.path.join(downloads_folder, "Divers"), exist_ok=True)
                created_folders.add("Divers")
            shutil.move(item_path, os.path.join(downloads_folder, "Divers", item))

    print(f"Trier les fichiers dans '{downloads_folder}' est terminé !")
    input("Appuyez sur Entrée pour fermer le programme...")

# Demander à l'utilisateur le chemin du dossier
user_folder = input("Entrez le chemin du dossier à trier (par défaut: ~/Downloads) : ").strip()
if not user_folder:
    user_folder = os.path.expanduser("~/Downloads")

# Vérifier si le dossier existe
if os.path.exists(user_folder) and os.path.isdir(user_folder):
    trier_dossier(user_folder)
else:
    print(f"Le chemin spécifié '{user_folder}' n'existe pas ou n'est pas un dossier.")
