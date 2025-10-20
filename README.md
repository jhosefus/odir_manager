# odir_manager
Software para el análisis de Reconocimiento de enfermedades oculares con una base de datos oftalmológica estructurada de 5000 pacientes 

## Estructura del proyecto

odir_trabajo/ 

├── main.py # Menú interactivo principal 

├── config.py # Rutas y constantes globales 

├── modules/ 

│ ├── manager/ 

│ │ └── image_manager.py # Clase principal de gestión 

│ ├── models/ 

│ │ ├── paciente.py # Clase para ID automático 

│ │ ├── diagnostico.py # Codificación multiclase 

│ │ └── imagen.py # Carga local de imágenes 

│ ├── utils/ 

│ │ ├── io.py # Carga y guardado de CSV 

│ │ └── validation.py # Validación de extensiones


---

## Requisitos

- Python 3.8+
- VS Code o cualquier entorno local
- Librerías:
  - pandas
  - Pillow
  - matplotlib
  - opencv-python

Instalación rápida:

pip install pandas pillow matplotlib opencv-python

## Instalación (Alternativa)

Ejecuta los siguientes comandos para instalar dependencias automaticamente y usar el sistema:

- chmod +x setup.sh
- ./setup.sh


## Ejecución

Clona o descarga el proyecto.

Asegúrate de tener el archivo full_df.csv en la ruta indicada en config.py.

Ejecuta el menú principal:

- python main.py


## Flujo de trabajo
- Registro: Carga dos imágenes (izquierda y derecha) desde tu sistema local, asigna ID automático, codifica diagnóstico y guarda en CSV.
- Modificación: Edita campos como edad, sexo o diagnóstico por ID.
- Eliminación: Borra imágenes físicas y registros asociados.
- Visualización: Muestra metadatos y la imagen con matplotlib.

## Notas importantes
- Las imágenes deben estar en formato .jpg.
- El sistema no depende de Google Colab.
- Las rutas están definidas en config.py.