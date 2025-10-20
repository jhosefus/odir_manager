#!/bin/bash

echo "Creando entorno virtual..."
python3 -m venv odir_env

echo "Activando entorno virtual..."
source odir_env/bin/activate

echo "Instalando dependencias..."
# pip install --upgrade pip
pip install -r requirements.txt

echo "Inicializando Git y DVC..."
git init
dvc init

echo "Versionando datos con DVC..."
dvc add dataset/full_df.csv

echo "Proyecto listo. Ejecutar con: source odir_env/bin/activate && python main.py"
