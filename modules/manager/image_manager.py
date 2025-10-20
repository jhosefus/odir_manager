import pandas as pd
import os
import cv2
import matplotlib.pyplot as plt
from PIL import Image

from modules.models.paciente import Paciente
from modules.models.diagnostico import Diagnostico
from modules.models.imagen import Imagen
from modules.utils.io import load_metadata, save_metadata
from config import TRAINING_DIR, LABELS


class ImageManager:
    def __init__(self, csv_path):
        self.csv_path = csv_path
        self.df = load_metadata(csv_path)

    def register_image(self):
        paciente = Paciente(self.df)
        id_value = paciente.next_id
        print(f"ID del paciente: {id_value}")
        age = input("Edad: ")

        sex = ""
        while sex not in ["M", "F"]:
            sex = input("Sexo (M/F): ").strip().upper()
        sex = "Male" if sex == "M" else "Female"

        left_keywords = input("Palabras clave diagnóstico izquierdo: ")
        right_keywords = input("Palabras clave diagnóstico derecho: ")
        diagnosis_str = input("Diagnóstico general (N, D, G, C, A, H, M, O): ")

        diag = Diagnostico(diagnosis_str)

        left_img = Imagen(id_value, "left").upload()
        right_img = Imagen(id_value, "right").upload()

        for eye_side, filename in [("left", left_img), ("right", right_img)]:
            if filename:
                entry = {
                    "ID": id_value,
                    "Patient Age": age,
                    "Patient Sex": sex,
                    "Left-Fundus": f"{id_value}_left.jpg",
                    "Right-Fundus": f"{id_value}_right.jpg",
                    "Left-Diagnostic Keywords": left_keywords,
                    "Right-Diagnostic Keywords": right_keywords,
                    "filepath": os.path.join(TRAINING_DIR, filename),
                    "labels": [diag.primer_label],
                    "filename": filename,
                    "target": diag.target_vector
                }
                entry.update(diag.binary_dict)
                self.df = pd.concat([self.df, pd.DataFrame([entry])], ignore_index=True)

        if left_img or right_img:
            save_metadata(self.df, self.csv_path)
            print("Registro agregado exitosamente.")
        else:
            print("No se registró ninguna imagen.")

    def modify_image(self):
        id_value = input("Ingrese el ID del paciente a modificar: ").strip()
        self.df["ID"] = self.df["ID"].astype(str)
        registros = self.df[self.df["ID"] == id_value]

        if registros.empty:
            print("No se encontró ningún registro.")
            return

        campos = {
            "1": "Patient Age",
            "2": "Patient Sex",
            "3": "Left-Diagnostic Keywords",
            "4": "Right-Diagnostic Keywords",
            "5": "Diagnosis"
        }

        for k, v in campos.items():
            print(f"{k}. {v}")
        opcion = input("Seleccione campo a modificar: ").strip()

        if opcion not in campos:
            print("Opción inválida.")
            return

        campo = campos[opcion]

        if campo == "Patient Sex":
            nuevo = ""
            while nuevo not in ["M", "F"]:
                nuevo = input("Nuevo sexo (M/F): ").strip().upper()
            nuevo = "Male" if nuevo == "M" else "Female"
            self.df.loc[self.df["ID"] == id_value, campo] = nuevo

        elif campo == "Diagnosis":
            nuevo = input("Nuevo diagnóstico (N, D, G, C, A, H, M, O): ").strip()
            self.modify_encode_diagnosis(nuevo, id_value)

        else:
            nuevo = input(f"Nuevo valor para {campo}: ").strip()
            self.df.loc[self.df["ID"] == id_value, campo] = nuevo

        save_metadata(self.df, self.csv_path)
        print("Modificación aplicada.")

    def modify_encode_diagnosis(self, nuevo_valor, ID):
        self.df["ID"] = self.df["ID"].astype(str)
        mask = self.df["ID"] == str(ID)
        registros = self.df.loc[mask]

        if registros.empty:
            print("No se encontró ningún registro.")
            return

        diag = Diagnostico(nuevo_valor)
        self.df.loc[mask, "labels"] = [diag.primer_label] * len(registros)
        self.df.loc[mask, "target"] = [str(diag.target_vector)] * len(registros)

        for etiqueta, valor in diag.binary_dict.items():
            self.df.loc[mask, etiqueta] = valor

        save_metadata(self.df, self.csv_path)

    def delete_image(self):
        id_value = input("ID del paciente a eliminar: ").strip()
        self.df["ID"] = self.df["ID"].astype(str)
        registros = self.df[self.df["ID"] == id_value]

        if registros.empty:
            print("No se encontró ningún registro.")
            return

        confirm = input(f"¿Eliminar {len(registros)} registros? (S/N): ").strip().upper()
        if confirm != "S":
            print("Cancelado.")
            return

        for _, fila in registros.iterrows():
            ruta = fila.get("filepath")
            if ruta and os.path.isfile(ruta):
                try:
                    os.remove(ruta)
                    print(f"Archivo eliminado: {ruta}")
                except Exception as e:
                    print(f"Error al eliminar {ruta}: {e}")

        self.df = self.df[self.df["ID"] != id_value]
        save_metadata(self.df, self.csv_path)
        print("Registros eliminados.")

    def info_image(self):
        id_value = input("ID del paciente: ").strip()
        self.df["ID"] = self.df["ID"].astype(str)
        registros = self.df[self.df["ID"] == id_value]

        if registros.empty:
            print("No se encontró ningún registro.")
            return

        for _, fila in registros.iterrows():
            print(f"\nImagen: {fila['filename']}")
            print(f"Ruta: {fila['filepath']}")
            print(f"Edad: {fila['Patient Age']}")
            print(f"Sexo: {fila['Patient Sex']}")
            print(f"Diagnóstico izquierdo: {fila['Left-Diagnostic Keywords']}")
            print(f"Diagnóstico derecho: {fila['Right-Diagnostic Keywords']}")
            print(f"Label principal: {fila['labels']}")
            print(f"Vector target: {fila['target']}")
            for label in LABELS:
                print(f"  {label}: {fila.get(label, 'No disponible')}")

            image_path = fila['filepath']
            if os.path.isfile(image_path):
                try:
                    img = Image.open(image_path)
                    plt.imshow(img)
                    plt.title(f"ID: {id_value} - {fila['filename']}")
                    plt.show()
                except Exception as e:
                    print(f"Error al mostrar imagen: {e}")