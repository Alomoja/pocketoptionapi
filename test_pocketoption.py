import json
from pocketoptionapi import PocketOption

ssid = 'G5mdKWqlLwD-SV_RAF4J'  # Example SSID, replace with your actual one

def test_pocketoption():
    try:
        print(f"Connecting with SSID: {ssid}")
        client = PocketOption(ssid)
        client.connect()

        # Check connection status
        if not client.connected:
            print("Not connected, unable to fetch balance")
            return

        print("Connected to the API.")

        # Fetch and print balance
        try:
            balance = client.get_balance()
            print(f"Fetched balance: {balance}")
        except AttributeError as e:
            print(f"Failed to fetch balance: {e}")
        
        # Attempt to change balance to demo (if the method exists)
        if hasattr(client, 'change_balance'):
            try:
                client.change_balance('PRACTICE')
                print("Successfully switched to practice balance")
            except Exception as e:
                print(f"Failed to switch balance: {e}")
        else:
            print("Method change_balance not found in PocketOption class.")
        
        # Fetch candle data
        try:
            # Assuming you have a method to fetch candles in the client
            candles = client.get_candles(asset='EURUSD', period=60, count=120)
            print(f"Fetched candles: {candles}")
        except AttributeError as e:
            print(f"Failed to fetch candles: {e}")

    except Exception as e:
        print(f"WebSocket error: {e}")
    finally:
        # Check if there is a method to properly close the client
        if hasattr(client, 'disconnect'):
            client.disconnect()
            print("WebSocket connection closed")
        else:
            print("No disconnect method found, ensure connection is properly closed.")

if __name__ == "__main__":
    test_pocketoption()
