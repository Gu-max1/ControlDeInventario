
import sys
import os
import traceback

# Add server directory to path
sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'server'))

try:
    from main import get_inventory
    
    print("Attempting to call get_inventory() directly...")
    result = get_inventory()
    print(f"Success! Result type: {type(result)}")
    print(f"First item: {result[0] if result else 'Empty'}")
        
except Exception:
    traceback.print_exc()
