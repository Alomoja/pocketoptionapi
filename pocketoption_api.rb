require 'net/http'
require 'uri'

class PocketOption
  attr_reader :ssid

  def initialize(ssid)
    @ssid = ssid
  end

  def connect
    # Implement the connection logic here
    puts "Connecting to PocketOption with ssid: #{@ssid}"
    # Simulating connection establishment
    sleep(1)
    puts "Connected!"
  end

  def get_balance
    # Implement the logic to fetch balance here
    # For this example, let's assume a simulated balance
    simulated_balance = 10000.0
    simulated_balance
  end
end
