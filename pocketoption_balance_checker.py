import json
from pocketoptionapi import PocketOption

# Sample WebSocket messages
ws_messages = [
<<<<<<< HEAD
    '0{"sid":"G5mdKWqlLwD-SV_RAF4J","upgrades":[],"pingInterval":25000,"pingTimeout":20000,"maxPayload":1000000}'
=======
    '0{"sid":"G5mdKWqlLwD-SV_RAF4J","upgrades":[],"pingInterval":25000,"pingTimeout":20000,"maxPayload":1000000}	'
>>>>>>> a184c9cb430ee90ce5f06cbc1787977dee68b8fa
]

# Function to extract the sid value
def extract_sid(messages):
    for message in messages:
        try:
            # Remove the leading "0" if present and load the JSON data
            data = json.loads(message.lstrip('0'))
            if "sid" in data:
                print(f"Extracted sid: {data['sid']}")
                return data["sid"]
        except json.JSONDecodeError:
            print(f"Failed to decode JSON from message: {message}")
            continue
    return None

# Extract the sid
ssid = extract_sid(ws_messages)

if ssid:
    print(f"Using ssid: {ssid}")
    # Initialize the PocketOption class with the extracted sid
    account = PocketOption(ssid)
    
    try:
        print("Connecting to the API...")
        account.connect()
        print("Connected to the API.")

        print("Fetching balance...")
        balance = account.get_balance()
        print(f"Balance fetched: {balance}")
    except Exception as e:
        print(f"An error occurred: {e}")
    finally:
        # Ensure to close the client if 'close' method is available
        if hasattr(account, 'close'):
            account.close()
            print("Closed the API client.")
else:
    print("ssid not found in the provided WebSocket messages.")
