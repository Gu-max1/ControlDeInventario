"""
System Health Check Tool
Run this script to verify that your environment is correctly set up.
It checks Python dependencies, Node.js, and port availability.
"""
import sys
import subprocess
import socket
import importlib.util
from pathlib import Path
import os

# Colors
GREEN = "\033[92m"
RED = "\033[91m"
YELLOW = "\033[93m"
RESET = "\033[0m"

def print_status(component, status, message=""):
    if status == "OK":
        print(f"[{GREEN} OK {RESET}] {component:<20} {message}")
    elif status == "WARN":
        print(f"[{YELLOW}WARN{RESET}] {component:<20} {message}")
    else:
        print(f"[{RED}FAIL{RESET}] {component:<20} {message}")

def check_python_version():
    ver = sys.version_info
    if ver.major == 3 and ver.minor == 11:
        print_status("Python Version", "OK", f"v{ver.major}.{ver.minor}.{ver.micro}")
    else:
        print_status("Python Version", "WARN", f"Found v{ver.major}.{ver.minor} (Recommended: 3.11)")

def check_import(module_name):
    if importlib.util.find_spec(module_name):
        print_status(f"Module: {module_name}", "OK")
        return True
    else:
        print_status(f"Module: {module_name}", "FAIL", "Not installed")
        return False

def check_node():
    try:
        # Try to use the portable node if available
        tools_dir = Path(__file__).parent
        portable_node = tools_dir / "node-v20.11.0-win-x64"
        
        env = os.environ.copy()
        if portable_node.exists():
            env["PATH"] = str(portable_node) + os.pathsep + env.get("PATH", "")
            
        output = subprocess.check_output(["node", "--version"], env=env, shell=True).decode().strip()
        print_status("Node.js", "OK", f"{output}")
        return True
    except:
        print_status("Node.js", "FAIL", "Not found in PATH or tools directory")
        return False

def check_node_modules():
    client_dir = Path(__file__).resolve().parent.parent / "client"
    if (client_dir / "node_modules").exists():
        print_status("node_modules", "OK", "Found in client directory")
    else:
        print_status("node_modules", "FAIL", "Missing. Run 'npm install' in client dir")

def check_port(port, name):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    result = sock.connect_ex(('127.0.0.1', port))
    sock.close()
    if result == 0:
        print_status(f"Port {port}", "WARN", f"Occupied (Likely {name} is running)")
    else:
        print_status(f"Port {port}", "OK", "Available")

def main():
    print("\n=== Inventory System Health Check ===\n")
    
    check_python_version()
    
    print("\n--- Python Dependencies ---")
    deps = ["fastapi", "uvicorn", "pandas", "openpyxl", "pydantic", "jose", "passlib"]
    all_deps_ok = all([check_import(dep) for dep in deps])
    
    print("\n--- Frontend Environment ---")
    check_node()
    check_node_modules()
    
    print("\n--- System Ports ---")
    check_port(8001, "Backend")
    check_port(3000, "Frontend")
    
    print("\n=====================================")
    if all_deps_ok:
        print(f"{GREEN}System looks ready to launch!{RESET}")
    else:
        print(f"{RED}Some dependencies are missing. Run the installation script.{RESET}")
    print("=====================================\n")

if __name__ == "__main__":
    main()
