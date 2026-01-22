import pandas as pd
import os

FILE_PATH = r"C:\Users\ga.castillo\OneDrive - Motta Internacional, S.A\Escritorio\CONTROL DE INVENTRIO\datos\INVENTARIO FOTON.xlsx"

try:
    df = pd.read_excel(FILE_PATH, sheet_name=0)
    # Normalize headers
    df.columns = [str(c).strip().upper() for c in df.columns]
    
    print("Columns:", df.columns.tolist())
    
    # Check for likely location column
    loc_col = "UBICACION" if "UBICACION" in df.columns else "LOC"
    
    # Filter for specific locations seen in screenshot
    target_locs = ["178", "180", "181", "178.0", "180.0"]
    
    # Convert loc col to string for searching
    df[loc_col] = df[loc_col].astype(str).str.strip()
    
    subset = df[df[loc_col].isin(target_locs)]
    
    if not subset.empty:
        print("\nData for targets:")
        print(subset[[loc_col, "NIVEL", "CATEGORIA", "DESCR"] if "NIVEL" in df.columns else [loc_col]].to_string())
        
        # Check unique levels
        if "NIVEL" in df.columns:
            print("\nUnique levels:", df["NIVEL"].unique())
            
    else:
        print("\nTargets not found. Sample of locations:")
        print(df[loc_col].head(10).tolist())

except Exception as e:
    print(f"Error: {e}")
