
import sys
import os
from fastapi.testclient import TestClient
import traceback

# Add server directory to path
sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'server'))

try:
    from main import app
    client = TestClient(app)
    
    print("Attempting to hit /api/inventory...")
    response = client.get("/api/inventory")
    
    if response.status_code != 200:
        print(f"Error Status: {response.status_code}")
        print("Response Text:", response.text)
    else:
        print("Success! Response length:", len(response.json()))
        
except Exception:
    traceback.print_exc()
