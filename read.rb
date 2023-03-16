require 'serialport'

case ENV["IAM"]
when "mac"
  port_str = "/dev/tty.usbserial-AB0N63JR"
when "raspi"
  port_str = "/dev/serial0"
else
  raise "unknown iam"
end
baud_rate = 9600
data_bits = nil
stop_bits = nil
parity = nil

sp = SerialPort.new(port_str, baud_rate, data_bits, stop_bits, parity)

puts "start..."
while (line = sp.gets) do
  print line
end

puts "end..."
sp.close
