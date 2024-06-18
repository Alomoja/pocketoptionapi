from websocket import WebSocketApp
import threading
import json
import time

# Event handler functions for WebSocket events
def on_message(ws, message):
    print(f"Received message: {message}")

def on_error(ws, error):
    print(f"Error: {error}")

def on_close(ws, close_status_code, close_msg):
    print(f"Connection closed with code: {close_status_code}, message: {close_msg}")

def on_open(ws):
    print("Connection opened")
    # If you need to send a message or authenticate on opening, do it here
    # Example: ws.send(json.dumps({'action': 'subscribe', 'channel': 'ticker'}))

class PocketOption:
    def __init__(self, ssid, ws_url="wss://demo-api-eu.po.market"):
        self.ssid = ssid
        self.ws_url = ws_url
        self.ws = None
        self.connected = False

    def connect(self):
        websocket_url = f"{self.ws_url}?ssid={self.ssid}"
        self.ws = WebSocketApp(websocket_url,
                               on_message=on_message,
                               on_error=on_error,
                               on_close=on_close)
        self.ws.on_open = on_open

        # Run WebSocket in a separate thread to avoid blocking
        self.thread = threading.Thread(target=self.ws.run_forever)
        self.thread.daemon = True
        self.thread.start()

        # Wait briefly to allow connection to establish
        time.sleep(3)

        if self.ws.sock and self.ws.sock.connected:
            self.connected = True
            print("WebSocket connected successfully.")
        else:
            print("Failed to establish WebSocket connection.")

    def disconnect(self):
        if self.ws:
            self.ws.close()
            self.connected = False
            print("WebSocket disconnected.")

    def get_balance(self):
        if not self.connected:
            raise Exception("WebSocket is not connected")
        # Example of sending a message to fetch balance
        # Adjust the message according to your API documentation
        request = json.dumps({'action': 'get_balance'})
        self.ws.send(request)

    def change_balance(self, balance_type):
        if not self.connected:
            raise Exception("WebSocket is not connected")
        # Example of sending a message to change balance
        # Adjust the message according to your API documentation
        request = json.dumps({'action': 'change_balance', 'balance_type': balance_type})
        self.ws.send(request)

    def get_candles(self, asset, period, count):
        if not self.connected:
            raise Exception("WebSocket is not connected")
        # Example of sending a message to fetch candles
        # Adjust the message according to your API documentation
        request = json.dumps({
            'action': 'get_candles',
            'asset': asset,
            'period': period,
            'count': count
        })
        self.ws.send(request)

# Example usage
if __name__ == "__main__":
    ssid = "your_ssid_here"  # Replace with your actual SSID

    # Initialize the PocketOption client
    pocket_option = PocketOption(ssid)

    # Connect to the WebSocket
    pocket_option.connect()

    # Fetch balance as a test (make sure to replace this with your actual implementation)
    try:
        pocket_option.get_balance()
    except Exception as e:
        print(f"Error fetching balance: {e}")

    # Keep the script running to maintain the WebSocket connection
    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        print("Interrupted by user, closing connection.")
        pocket_option.disconnect()
