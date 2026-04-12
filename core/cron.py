import threading
import time
import requests
from django.conf import settings

def ping_server():
    """
    Function that runs in a background thread to ping the server URL.
    """
    ping_url = getattr(settings, 'PING_URL', None)
    
    if not ping_url:
        print("PING_URL not configured. Pinger thread stopping.")
        return

    print(f"Starting background pinger for {ping_url}...")
    
    while True:
        try:
            response = requests.get(ping_url, timeout=10)
            print(f"Periodic ping to {ping_url} returned status: {response.status_code}")
        except Exception as e:
            print(f"Periodic ping to {ping_url} failed: {e}")
        
        # Wait for 5 minutes (300 seconds)
        time.sleep(300)

def start_pinger():
    """
    Starts the ping_server function in a daemon thread.
    """
    # Use a daemon thread so it doesn't block process exit
    thread = threading.Thread(target=ping_server, daemon=True)
    thread.start()
