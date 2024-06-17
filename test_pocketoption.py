import time
from pocketoptionapi import PocketOption

ssid = 'G5mdKWqlLwD-SV_RAF4J'  # Replace with your actual SSID

def test_pocketoption():
    try:
        print(f"Connecting with SSID: {ssid}")
        client = PocketOption(ssid)
        client.connect()
        time.sleep(5)  # Wait for the connection to establish

        # Check connection status
