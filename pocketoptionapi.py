import inspect
from pocketoptionapi import PocketOption

ssid = 'G5mdKWqlLwD-SV_RAF4J'  # Replace with your actual SSID
ws_url = 'wss://demo-api-eu.po.market'  # Replace with the correct WebSocket URL

# Initialize API client
api_client = PocketOption(ssid, ws_url)
print(inspect.getmembers(api_client, predicate=inspect.ismethod))

# Connect to PocketOption
print("Connecting to API client...")
api_client.connect()
print("Connected to API client.")

# Switch to demo balance and fetch balance
try:
    print("Attempting to change balance to: PRACTICE")
    api_client.change_balance('PRACTICE')
    print("Balance changed to: PRACTICE")

    print("Fetching balance...")
    balance = api_client.get_balance()
    print(f"Raw balance response: {balance}")
    if balance:
        print(f"Demo Balance: {balance}")
    else:
        print("Balance response is None, no valid data received.")
except Exception as e:
    print(f"Error during balance operations: {e}")

# Fetch candle data
try:
    end_time = int(time.time())
    offset = 120  # 2 minutes
    period = 60   # 1-minute candles
    print(f"Fetching candles for asset: EURUSD, end_time: {end_time}, offset: {offset}, period: {period}")
    candles = api_client.get_candles("EURUSD", period, offset)
    print(f"Raw candles response: {candles}")

    if candles and "data" in candles:
        valid_candles = [c for c in candles["data"] if 'o' in c and 'c' in c and 'h' in c and 'l' in c]
        print("Valid candles fetched:", valid_candles)
    else:
        print("No valid candle data received.")
except Exception as e:
    print(f"Error during candle fetching: {e}")

# Disconnect from the API
finally:
    api_client.disconnect()
    print("WebSocket connection closed")
