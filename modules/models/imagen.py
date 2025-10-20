import os
from PIL import Image
from config import TRAINING_DIR, VALID_EXTENSIONS

class Imagen:
    def __init__(self, id_value, eye_side):
        self.id_value = id_value
        self.eye_side = eye_side
        self.filename = None
        self.new_name = None
        self.new_path = None

    def upload(self):
        ojo = "izquierdo" if self.eye_side == "left" else "derecho"
        print(f"\nSeleccione la imagen del ojo {ojo} del paciente {self.id_value}")
        self.filename = input("Ingrese la ruta completa del archivo (.jpg): ").strip()

        if not os.path.isfile(self.filename):
            print("Archivo no encontrado.")
            return None

        ext = os.path.splitext(self.filename)[1].lower()
        if ext not in VALID_EXTENSIONS:
            print("Formato no válido. Solo se aceptan archivos .jpg")
            return None

        self.new_name = f"{self.id_value}_{self.eye_side}{ext}"
        self.new_path = os.path.join(TRAINING_DIR, self.new_name)

        try:
            img = Image.open(self.filename)
            img.save(self.new_path)
            print(f"Imagen guardada en: {self.new_path}")
            return self.new_name
        except Exception as e:
            print(f"Error al procesar la imagen: {e}")
            return None