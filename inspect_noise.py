import pandas as pd

FILE_PATH = r"C:\Users\ga.castillo\OneDrive - Motta Internacional, S.A\Escritorio\CONTROL DE INVENTRIO\datos\INVENTARIO FOTON.xlsx"

try:
    df = pd.read_excel(FILE_PATH, sheet_name=0)
    
    # 1. Normalize Columns
    rename_map = {}
    for c in df.columns:
        cu = str(c).upper().strip()
        if "LOC" in cu or "UBICACION" in cu:
            rename_map[c] = "ubicacion"
        elif "NIVEL" in cu:
            rename_map[c] = "nivel"
            
    if rename_map:
        df = df.rename(columns=rename_map)
        
    print("Columns:", df.columns.tolist())
    
    # 2. Inspect Target Locations
    targets = ["72310206", "80150102A", "80150202A", "801502B", "178", "180"]
    
    # Flexible clean
    df['clean_loc'] = df['ubicacion'].astype(str).str.strip()
    
    print("\n--- TARGET INSPECTION ---")
    subset = df[df['clean_loc'].isin(targets)]
    
    if not subset.empty:
        cols_to_show = ['ubicacion', 'nivel'] if 'nivel' in df.columns else ['ubicacion']
        print(subset[cols_to_show].to_string())
    else:
        print("Targets not found exact match.")
        
    # 3. Check what 'REVISAR' and 'MUELLE' actually look like in Nivel
    if 'nivel' in df.columns:
        print("\n--- NIVEL VALUES ---")
        print(df['nivel'].value_counts().head(10))

except Exception as e:
    print(f"Error: {e}")
