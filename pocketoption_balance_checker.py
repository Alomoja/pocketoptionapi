import json
from pocketoptionapi import PocketOption

# Sample WebSocket messages
ws_messages = [
    '0{"sid":"Oiri0O_zQMWfnyVuGA86","upgrades":[],"pingInterval":25000,"pingTimeout":20000,"maxPayload":1000000}'
]

# Function to extract the sid value
def extract_sid(messages):
    for message in messages:
        try:
            # Remove the leading "0" if present and load the JSON data
            data = json.loads(message.lstrip('0'))
            if "sid" in data:
                return data["sid"]
        except json.JSONDecodeError:
            continue
    return None

# Extract the sid
ssid = extract_sid(ws_messages)

if ssid:
    # Initialize the PocketOption class with the extracted sid
    account = PocketOption(ssid)
    account.connect()

    # Get and print the balance
    balance = account.get_balance()
    print(balance)
else:
    print("ssid not found in the provided WebSocket messages.")
