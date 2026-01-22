import requests

print("Testing parameter reception...")
print("=" * 60)

# Test how FastAPI receives the parameter
url = "http://localhost:8001/api/dashboard/completo"

# Test 1: Single cliente parameter
print("\n[TEST 1] Single cliente parameter:")
print(f"URL: {url}?cliente=CANNING+LATINOAMERICA")
response = requests.get(f"{url}?cliente=CANNING+LATINOAMERICA")
if response.status_code == 200:
    data = response.json()
    print(f"Total ubicaciones: {data['metricas']['total_productos']}")
    print(f"Expected: ~11 (CANNING only)")
    if data['metricas']['total_productos'] < 100:
        print("[OK] Filter working!")
    else:
        print("[ERROR] Filter NOT working - showing all data")
else:
    print(f"ERROR: {response.status_code}")

print("\n" + "=" * 60)
