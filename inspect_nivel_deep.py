import pandas as pd
import os

FILE_PATH = r"C:\Users\ga.castillo\OneDrive - Motta Internacional, S.A\Escritorio\CONTROL DE INVENTRIO\datos\INVENTARIO FOTON.xlsx"

try:
    print(f"Loading {FILE_PATH}...")
    df = pd.read_excel(FILE_PATH, sheet_name=0)
    
    # 1. Raw Column Names
    print("\n--- RAW DATAFRAME COLUMNS ---")
    print(df.columns.tolist())
    
    # 2. Check for NIVEL-like columns
    nivel_col = None
    for c in df.columns:
        if "NIVEL" in str(c).upper():
            nivel_col = c
            break
            
    if nivel_col:
        print(f"\nFound 'NIVEL' column: '{nivel_col}'")
        
        # 3. Unique Values Analysis
        settings = pd.option_context('display.max_rows', None, 'display.max_columns', None)
        with settings:
            print("\n--- UNIQUE VALUES IN NIVEL COLUMN (Raw) ---")
            unique_vals = df[nivel_col].unique()
            print(unique_vals)
            
            print("\n--- VALUE COUNTS ---")
            print(df[nivel_col].value_counts(dropna=False))
            
            print("\n--- SAMPLE ROWS WITH 'MUELLE' (Case Insensitive Search) ---")
            muelle_mask = df[nivel_col].astype(str).str.upper().str.contains("MUELLE", na=False)
            print(df[muelle_mask][[nivel_col]].head(10))

            print("\n--- SAMPLE ROWS WITH 'REVISAR' (Case Insensitive Search) ---")
            revisar_mask = df[nivel_col].astype(str).str.upper().str.contains("REVISAR", na=False)
            print(df[revisar_mask][[nivel_col]].head(10))
            
            # Check for whitespace issues
            print("\n--- WHITESPACE CHECK ---")
            # Show values wrapped in quotes to see trailing spaces
            dirty_vals = df[nivel_col].dropna().unique()
            print([f"'{x}'" for x in dirty_vals])

    else:
        print("\nCRITICAL: No column containing 'NIVEL' was found!")

except Exception as e:
    print(f"Error: {e}")
