from websocket import WebSocketApp

def on_message(ws, message):
    print(f"Received message: {message}")

def on_error(ws, error):
    print(f"Error: {error}")

def on_close(ws):
    print("Connection closed")

def on_open(ws):
    print("Connection opened")

from websocket import create_connection

class PocketOption:
    def __init__(self, ssid):
        self.ssid = ssid
        self.ws = None
    
    def connect(self):
        try:
            self.ws = create_connection(f"wss://some.websocket.endpoint?ssid={self.ssid}")
            print("WebSocket connected.")
        except Exception as e:
            print(f"WebSocket connection failed: {e}")

ws = WebSocketApp("wss://echo.websocket.org/",
                  on_message=on_message,
                  on_error=on_error,
                  on_close=on_close)
ws.on_open = on_open
ws.run_forever()
