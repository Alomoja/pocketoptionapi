import inspect
from pocketoptionapi import PocketOption

<<<<<<< HEAD
# Your valid SSID
ssid = '0{"sid":"G5mdKWqlLwD-SV_RAF4J","upgrades":[],"pingInterval":25000,"pingTimeout":20000,"maxPayload":1000000}	' 

# Initialize API client
api_client = PocketOption('your_ssid')
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
    candles = api_client.get_candle("EURUSD", end_time, offset, period)
    print(f"Raw candles response: {candles}")

    if candles and "data" in candles:
        valid_candles = [c for c in candles["data"] if 'o' in c and 'c' in c and 'h' in c and 'l' in c]
        print("Valid candles fetched:", valid_candles)
    else:
        print("No valid candle data received.")
except Exception as e:
    print(f"Error during candle fetching: {e}")
=======
ssid = "0{"sid":"G5mdKWqlLwD-SV_RAF4J","upgrades":[],"pingInterval":25000,"pingTimeout":20000,"maxPayload":1000000}	"
account = PocketOption(ssid)
account.connect()
balance = account.get_balance()
print(balance)
>>>>>>> a184c9cb430ee90ce5f06cbc1787977dee68b8fa
