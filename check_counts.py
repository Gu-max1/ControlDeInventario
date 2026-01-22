import pandas as pd
import os

f1 = r"c:\Users\ga.castillo\OneDrive - Motta Internacional, S.A\Escritorio\CONTROL DE INVENTRIO\datos\DATA PARA EL CONTEO ANUAL.xlsx"
f2 = r"c:\Users\ga.castillo\OneDrive - Motta Internacional, S.A\Escritorio\CONTROL DE INVENTRIO\datos\temp_data.xlsx"

def get_row_count(path):
    if not os.path.exists(path): return 0
    try:
        df = pd.read_excel(path, sheet_name="DT INV")
        return len(df)
    except:
        return 0

c1 = get_row_count(f1)
c2 = get_row_count(f2)

print(f"Main File Count: {c1}")
print(f"Temp File Count: {c2}")

if c2 > c1:
    print("Temp file has more rows. Using it as source.")
else:
    print("Counts are equal or temp is smaller. Will generate dummy data.")
