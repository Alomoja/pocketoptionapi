from pocketoptionapi import PocketOption

ssid = "0{"sid":"G5mdKWqlLwD-SV_RAF4J","upgrades":[],"pingInterval":25000,"pingTimeout":20000,"maxPayload":1000000}	"
account = PocketOption(ssid)
account.connect()
balance = account.get_balance()
print(balance)
