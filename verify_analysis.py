
import sys
import os
import pandas as pd
from pathlib import Path

# Add server directory to path to import main
sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'server'))
import main

# Force reload to get fresh data
print("Reloading data...")
df = main.leer_excel(main.SHEET_NAME_INV, force_reload=True)

if df.empty:
    print("Error: Could not load data from Excel.")
    exit()

print(f"\nSuccessfully loaded {len(df)} rows from sheet '{main.SHEET_NAME_INV}'")
print("-" * 50)

# Run Analysis Logic Manually (simulating the endpoint)
total_items = len(df)
items_with_stock = int(df[df['cantidad_sistema'] > 0]['cantidad_sistema'].count())

if 'total_monetario' in df.columns:
    total_value = float(df['total_monetario'].sum())
elif 'cantidad_sistema' in df.columns and 'costo' in df.columns:
    total_value = float((df['cantidad_sistema'] * df['costo']).sum())
else:
    total_value = 0.0

pisos = 0
alturas = 0
otros = 0

if 'ubicacion' in df.columns:
    locs = df['ubicacion'].astype(str).str.strip()
    for loc in locs:
        if len(loc) >= 2:
            suffix = loc[-2:]
            if suffix == '01':
                pisos += 1
            elif suffix in ['02', '03', '04']:
                alturas += 1
            else:
                otros += 1
        else:
            otros += 1

print("\n--- INVENTORY ANALYSIS RESULTS ---")
print(f"Total Items/Locations: {total_items}")
print(f"Items with Stock (>0): {items_with_stock}")
print(f"Total Inventory Value: ${total_value:,.2f}")
print("\n--- LOCATION ANALYSIS ---")
print(f"Piso (01):     {pisos}")
print(f"Altura (02-04): {alturas}")
print(f"Other:          {otros}")
print("-" * 50)
