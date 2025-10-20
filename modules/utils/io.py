import pandas as pd

def load_metadata(csv_path):
    try:
        df = pd.read_csv(csv_path)
        print(f"CSV cargado con {len(df)} registros.")
        return df
    except Exception as e:
        print(f"Error al cargar CSV: {e}")
        return pd.DataFrame()

def save_metadata(df, path):
    try:
        df.to_csv(path, index=False)
        print(f"CSV actualizado en: {path}")
    except Exception as e:
        print(f"Error al guardar CSV: {e}")