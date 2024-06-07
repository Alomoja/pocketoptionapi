from pocketoptionapi import PocketOption

ssid = "0{"sid":"m9MGiJVr4juxSSOLA52Z","upgrades":[],"pingInterval":25000,"pingTimeout":20000,"maxPayload":1000000}"	
        #0{"sid":"DPBxVYF4L2APSC-7ACT9","upgrades":[],"pingInterval":45000,"pingTimeout":5000}
account = PocketOption(ssid)
account.connect()
balance = account.get_balance()
print(balance)
