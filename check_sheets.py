
import pandas as pd
from pathlib import Path

file_path = Path(r"c:/Users/ga.castillo/OneDrive - Motta Internacional, S.A/Escritorio/CONTROL DE INVENTRIO/datos/DATA PARA EL CONTEO ANUAL.xlsx")

try:
    if file_path.exists():
        # Check REPORTE_WMS
        try:
            df_dash = pd.read_excel(file_path, sheet_name="REPORTE_WMS", nrows=5)
            print("Headers (REPORTE_WMS):", list(df_dash.columns))
        except Exception as e:
            print(f"Error reading REPORTE_WMS: {e}")

        # Check DT INV
        try:
            df_inv = pd.read_excel(file_path, sheet_name="DT INV", nrows=5)
            print("Headers (DT INV):", list(df_inv.columns))
        except Exception as e:
            print(f"Error reading DT INV: {e}")
            
    else:
        print("File not found")
except Exception as e:
    print(f"Error: {e}")
