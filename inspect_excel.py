import pandas as pd
import os

files = [
    r"c:\Users\ga.castillo\OneDrive - Motta Internacional, S.A\Escritorio\CONTROL DE INVENTRIO\datos\temp_data.xlsx",
    r"c:\Users\ga.castillo\OneDrive - Motta Internacional, S.A\Escritorio\CONTROL DE INVENTRIO\datos\DATA PARA EL CONTEO ANUAL.xlsx"
]

for f in files:
    print(f"\n--- Checking {os.path.basename(f)} ---")
    if not os.path.exists(f):
        print("File not found.")
        continue
    
    try:
        xl = pd.ExcelFile(f)
        print("Sheets:", xl.sheet_names)
        for sheet in xl.sheet_names:
            print(f"\n[Sheet: {sheet}]")
            df = pd.read_excel(f, sheet_name=sheet, nrows=5)
            print("Columns:", df.columns.tolist())
            print(df.head())
    except Exception as e:
        print("Error reading file:", e)
