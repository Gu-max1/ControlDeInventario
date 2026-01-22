import requests
import json

print("Testing Dashboard API Client Filter")
print("=" * 70)

base_url = "http://localhost:8001"

try:
    # Test 1: No filter
    print("\n[TEST 1] Without client filter:")
    print("URL: /api/dashboard/completo")
    response = requests.get(f"{base_url}/api/dashboard/completo", timeout=5)
    
    if response.status_code == 200:
        data = response.json()
        total = data['metricas']['total_productos']
        num_clients = len(data['datos_categoria'])
        print(f"  Status: OK")
        print(f"  Total ubicaciones: {total}")
        print(f"  Number of clients in response: {num_clients}")
        if num_clients > 0:
            print(f"  Clients:")
            for cat in data['datos_categoria'][:3]:
                print(f"    - {cat['nombre']}: {cat['total_ubicaciones']} ubicaciones")
            if num_clients > 3:
                print(f"    ... and {num_clients - 3} more")
    else:
        print(f"  ERROR: Status {response.status_code}")
        print(f"  Response: {response.text[:200]}")

    # Test 2: With client filter
    print("\n[TEST 2] With client filter (MAXELL LATIN AMERICA, S.A.):")
    print("URL: /api/dashboard/completo?cliente=MAXELL+LATIN+AMERICA%2C+S.A.")
    response = requests.get(
        f"{base_url}/api/dashboard/completo",
        params={'cliente': 'MAXELL LATIN AMERICA, S.A.'},
        timeout=5
    )
    
    if response.status_code == 200:
        data = response.json()
        total = data['metricas']['total_productos']
        num_clients = len(data['datos_categoria'])
        print(f"  Status: OK")
        print(f"  Total ubicaciones: {total}")
        print(f"  Number of clients in response: {num_clients}")
        if num_clients > 0:
            print(f"  Clients:")
            for cat in data['datos_categoria']:
                print(f"    - {cat['nombre']}: {cat['total_ubicaciones']} ubicaciones")
        
        # Verify filter worked
        print(f"\n  [VERIFICATION]")
        if total < 1000:  # Should be ~381 for MAXELL
            print(f"    ✓ Filter WORKING! Total reduced to {total}")
        else:
            print(f"    ✗ Filter NOT WORKING! Total still {total} (should be ~381)")
            
        if num_clients == 1:
            print(f"    ✓ Only 1 client in response (correct)")
        else:
            print(f"    ✗ {num_clients} clients in response (should be 1)")
    else:
        print(f"  ERROR: Status {response.status_code}")
        print(f"  Response: {response.text[:200]}")

except requests.exceptions.ConnectionError:
    print("\n[ERROR] Cannot connect to server at http://localhost:8001")
    print("Make sure the backend server is running!")
except Exception as e:
    print(f"\n[ERROR] {type(e).__name__}: {e}")

print("\n" + "=" * 70)
