
import pandas as pd
from pathlib import Path

base_dir = Path(r"c:/Users/ga.castillo/OneDrive - Motta Internacional, S.A/Escritorio/CONTROL DE INVENTRIO")
file_path = base_dir / "datos" / "DATA PARA EL CONTEO ANUAL.xlsx"

try:
    if file_path.exists():
        df = pd.read_excel(file_path, nrows=5)
        print("Headers:", list(df.columns))
        # Print a few example locations to verify format
        if 'Ubicacion' in df.columns:
            print("Examples Ubicacion:", df['Ubicacion'].head().tolist())
        elif 'UBICACION' in df.columns:
            print("Examples UBICACION:", df['UBICACION'].head().tolist())
            
        # Check for Cost/Price columns
        print("Potential Cost columns:", [c for c in df.columns if "COST" in c.upper() or "PRECIO" in c.upper()])
    else:
        print(f"File not found: {file_path}")
        # Try the other file
        file_path2 = base_dir / "data" / "inventario.xlsx"
        if file_path2.exists():
            df = pd.read_excel(file_path2, nrows=5)
            print(f"Headers from {file_path2.name}:", list(df.columns))
except Exception as e:
    print(f"Error: {e}")
