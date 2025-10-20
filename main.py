from modules.manager.image_manager import ImageManager
from config import CSV_PATH

def menu():
    manager = ImageManager(CSV_PATH)
    while True:
        print("\n--- Menú ODIR ---")
        print("1. Registrar imagen")
        print("2. Modificar imagen")
        print("3. Eliminar imagen")
        print("4. Ver Metadatos de imagen")
        print("5. Salir")

        choice = input("Seleccione una opción: ")
        if choice == "1":
            manager.register_image()
        elif choice == "2":
            manager.modify_image()
        elif choice == "3":
            manager.delete_image()
        elif choice == "4":
            manager.info_image()
        elif choice == "5":
            print("Saliendo...")
            break
        else:
            print("Opción inválida.")

menu()