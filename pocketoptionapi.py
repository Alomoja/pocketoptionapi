from pocketoptionapi import PocketOption

ssid = "0{"sid":"Oiri0O_zQMWfnyVuGA86","upgrades":[],"pingInterval":25000,"pingTimeout":20000,"maxPayload":1000000}"
account = PocketOption(ssid)
account.connect()
balance = account.get_balance()
print(balance)
