import os

BASE_DIR = "/home/josealfredo/html/odir_manager/dataset/"

TARGET_DIR = BASE_DIR + "preprocessed_images"
TRAINING_DIR = BASE_DIR + "ODIR-5K/ODIR-5K/Training Images"
TESTING_DIR = BASE_DIR + "ODIR-5K/ODIR-5K/Testing Images"
CSV_PATH = BASE_DIR + "full_df.csv"

LABELS = {
    "N": "Normal",
    "D": "Diabetes",
    "G": "Glaucoma",
    "C": "Catarata",
    "A": "Degeneración macular por edad (Age related Macular Degeneration)",
    "H": "Hipertensión",
    "M": "Miopía patológica",
    "O": "Otras enfermedades"
}

VALID_EXTENSIONS = (".jpg",)

os.makedirs(TARGET_DIR, exist_ok=True)
print(f"Carpeta creada o existente: {TARGET_DIR}")