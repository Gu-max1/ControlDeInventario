import pandas as pd
import os
import shutil
from datetime import datetime

# Paths
base_dir = r"c:\Users\ga.castillo\OneDrive - Motta Internacional, S.A\Escritorio\CONTROL DE INVENTRIO\datos"
file_path = os.path.join(base_dir, "DATA PARA EL CONTEO ANUAL.xlsx")
backup_path = os.path.join(base_dir, f"DATA_BACKUP_{datetime.now().strftime('%Y%m%d_%H%M%S')}.xlsx")

# 1. Backup First
print(f"Creating backup at: {backup_path}")
shutil.copy2(file_path, backup_path)

# 2. Load Existing Data
print("Loading existing Excel...")
try:
    xl = pd.ExcelFile(file_path)
    sheet_name = 'DT INV'
    df = pd.read_excel(file_path, sheet_name=sheet_name)
except Exception as e:
    print(f"Error reading file: {e}")
    exit(1)

# 3. Create Dummy Data
print("Generating new products...")
new_rows = []

# Use string IDs to facilitate safety
start_id_val = 90000

for i in range(1, 6):
    row = {
        'SKU': f"NUEVO-PROD-{i:03d}",
        'DESCR': f"Producto de Prueba Generado {i}",
        'LOC': f"0000010{i}",
        'QTY': 50,
        'QTYAVAILABLE': 50,
        'ID': str(start_id_val + i), # Force String
        'CATEGORIA': 'NUEVOS_ITEMS',
        'COSTO UNITARIO': 100.00,
        'Valor Total Monetario': 5000.00
    }
    new_rows.append(row)

new_df = pd.DataFrame(new_rows)
print(f"Created {len(new_df)} new rows.")

# 4. Append
combined_df = pd.concat([df, new_df], ignore_index=True)

# 5. Write Back
try:
    with pd.ExcelWriter(file_path, engine='openpyxl', mode='a', if_sheet_exists='replace') as writer:
        combined_df.to_excel(writer, sheet_name=sheet_name, index=False)
        print("Successfully wrote to Excel.")
except Exception as e:
    print(f"Error writing excel: {e}")
    print("Trying fallback...")
    # Fallback
    all_sheets = {}
    for sh in xl.sheet_names:
        if sh == sheet_name:
            all_sheets[sh] = combined_df
        else:
            all_sheets[sh] = pd.read_excel(file_path, sheet_name=sh)
            
    with pd.ExcelWriter(file_path, engine='openpyxl') as writer:
        for sh_name, sh_df in all_sheets.items():
            sh_df.to_excel(writer, sheet_name=sh_name, index=False)
    print("Full rewrite complete.")

print("Done.")
