import unittest
import os
import shutil
from pathlib import Path
from app import trier_dossier 

class TestTrierDossier(unittest.TestCase):

    def setUp(self):
        """Configure un dossier temporaire pour les tests."""
        self.test_dir = Path("test_downloads")
        self.test_dir.mkdir(exist_ok=True)

        # Crée des fichiers de test
        (self.test_dir / "image.jpg").touch()
        (self.test_dir / "video.mp4").touch()
        (self.test_dir / "document.pdf").touch()
        (self.test_dir / "archive.zip").touch()
        (self.test_dir / "unknownfile.xyz").touch()

    def tearDown(self):
        """Supprime le dossier temporaire après chaque test."""
        shutil.rmtree(self.test_dir)

    def test_trier_dossier(self):
        """Teste que les fichiers sont correctement triés dans les bonnes catégories."""
        trier_dossier(self.test_dir)

        # Vérifie que les fichiers sont déplacés dans les bons dossiers
        self.assertTrue((self.test_dir / "Images" / "image.jpg").exists())
        self.assertTrue((self.test_dir / "Vidéos" / "video.mp4").exists())
        self.assertTrue((self.test_dir / "Documents" / "document.pdf").exists())
        self.assertTrue((self.test_dir / "Archives" / "archive.zip").exists())
        self.assertTrue((self.test_dir / "Divers" / "unknownfile.xyz").exists())


if __name__ == "__main__":
    unittest.main()