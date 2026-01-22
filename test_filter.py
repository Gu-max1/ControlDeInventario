import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).parent))

from server.main import leer_excel, SHEET_NAME_GENERAL

print("Testing client filter logic...")
print("=" * 60)

df = leer_excel(SHEET_NAME_GENERAL)

print(f"\nTotal records: {len(df)}")
print(f"Columns: {df.columns.tolist()}")

# Check if 'cliente' column exists
if 'cliente' in df.columns:
    print(f"\n[OK] 'cliente' column found")
    print(f"Unique clients: {df['cliente'].nunique()}")
    print(f"\nClients list:")
    for i, client in enumerate(df['cliente'].dropna().unique(), 1):
        count = len(df[df['cliente'] == client])
        print(f"  {i}. {client} - {count} records")
    
    # Test filter logic
    test_client = df['cliente'].dropna().iloc[0]
    print(f"\n\nTesting filter with client: '{test_client}'")
    
    # Simulate backend filter
    cliente = [test_client]
    if isinstance(cliente, str):
        cliente = [cliente]
    if cliente and not (len(cliente) == 1 and cliente[0] == "Todos"):
        if 'cliente' in df.columns:
            filtered_df = df[df['cliente'].isin(cliente)]
            print(f"Filtered records: {len(filtered_df)}")
            print(f"Unique ubicaciones in filtered data: {filtered_df['ubicacion'].nunique()}")
else:
    print("\n[ERROR] 'cliente' column NOT FOUND!")
    print("This is the problem - filter cannot work without cliente column")

print("\n" + "=" * 60)
