require 'json'
require_relative 'pocketoption_api'

# Sample WebSocket messages
ws_messages = [
  '0{"sid":"m9MGiJVr4juxSSOLA52Z","upgrades":[],"pingInterval":25000,"pingTimeout":20000,"maxPayload":1000000}',
  '0{"sid":"DPBxVYF4L2APSC-7ACT9","upgrades":[],"pingInterval":45000,"pingTimeout":5000}'
]

# Function to extract the sid value
def extract_sid(messages)
  messages.each do |message|
    begin
      # Remove the leading "0" if present and parse the JSON data
      data = JSON.parse(message.sub(/^0/, ''))
      return data["sid"] if data.key?("sid")
    rescue JSON::ParserError
      next
    end
  end
  nil
end

# Extract the sid
ssid = extract_sid(ws_messages)

if ssid
  # Initialize the PocketOption class with the extracted sid
  account = PocketOption.new(ssid)
  account.connect

  # Get and print the balance
  balance = account.get_balance
  puts "Balance: #{balance}"
else
  puts "SSID not found in the provided WebSocket messages."
end
