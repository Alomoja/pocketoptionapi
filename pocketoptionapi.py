import websocket
import time
import json

class PocketOption:
    def __init__(self, ssid, ws_url="wss://demo-api-eu.po.market"):  # Replace with the actual WebSocket URL
        self.ssid = ssid
        self.ws_url = ws_url
        self.connected = False
        self.ws = None

    def connect(self):
        def on_message(ws, message):
            print(f"Received message: {message}")

        def on_error(ws, error):
            print(f"WebSocket error: {error}")

        def on_close(ws, close_status_code, close_msg):
            print("WebSocket connection closed")

        def on_open(ws):
            print("WebSocket connection opened")
            self.connected = True
            self.authenticate()

        print(f"Connecting to WebSocket URL: {self.ws_url}")
        self.ws = websocket.WebSocketApp(self.ws_url,
                                         on_message=on_message,
                                         on_error=on_error,
                                         on_close=on_close)
        self.ws.on_open = on_open
        self.ws.run_forever()

    def authenticate(self):
        auth_payload = json.dumps({"ssid": self.ssid})
        self.ws.send(auth_payload)
        print(f"Sent authentication payload: {auth_payload}")

    def get_balance(self):
        if not self.connected:
            print("Not connected, unable to fetch balance")
            return None
        # Simulate fetching balance
        balance_request = json.dumps({"action": "get_balance"})
        self.ws.send(balance_request)
        print(f"Sent balance request: {balance_request}")

    def change_balance(self, balance_type):
        if not self.connected:
            print("Not connected, unable to change balance")
            return None
        # Simulate changing balance
        balance_change_request = json.dumps({"action": "change_balance", "balance_type": balance_type})
        self.ws.send(balance_change_request)
        print(f"Sent balance change request: {balance_change_request}")

    def get_candles(self, asset, period, count):
        if not self.connected:
            print("Not connected, unable to fetch candles")
            return None
        # Simulate fetching candles
        candle_request = json.dumps({"action": "get_candles", "asset": asset, "period": period, "count": count})
        self.ws.send(candle_request)
        print(f"Sent candle request: {candle_request}")

    def disconnect(self):
        if self.ws:
            self.ws.close()
            print("Disconnected from WebSocket")

# Example usage in the main block or other script
if __name__ == "__main__":
    ssid = 'G5mdKWqlLwD-SV_RAF4J'  # Replace with your actual SSID
    client = PocketOption(ssid)
    client.connect()
    time.sleep(5)  # Wait for connection to establish
    client.get_balance()
    client.change_balance('PRACTICE')
    client.get_candles('EURUSD', 60, 120)
    client.disconnect()
