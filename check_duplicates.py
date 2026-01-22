
import sys
import os
import pandas as pd
from pathlib import Path

# Add server directory to path
sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'server'))
import main

# Load data
df = main.leer_excel(main.SHEET_NAME_INV)

print(f"Total Rows: {len(df)}")

# Check SKU duplicates
if 'codigo' in df.columns:
    unique_skus = df['codigo'].nunique()
    print(f"Unique SKUs: {unique_skus}")
    print(f"SKU Duplicates: {len(df) - unique_skus}")
else:
    print("Column 'codigo' not found")

# Check Location duplicates
if 'ubicacion' in df.columns:
    unique_locs = df['ubicacion'].astype(str).str.strip().nunique()
    print(f"Unique Locations: {unique_locs}")
    print(f"Location Duplicates: {len(df) - unique_locs}")
    
    # Check distinct Piso vs Altura
    locs = df['ubicacion'].astype(str).str.strip().unique()
    pisos = 0
    alturas = 0
    for loc in locs:
        if len(loc) >= 2:
            suffix = loc[-2:]
            if suffix == '01':
                pisos += 1
            elif suffix in ['02', '03', '04']:
                alturas += 1
    print(f"Unique Piso Locations: {pisos}")
    print(f"Unique Altura Locations: {alturas}")

else:
    print("Column 'ubicacion' not found")
