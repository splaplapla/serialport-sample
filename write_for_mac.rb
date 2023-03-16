require 'serialport'

# シリアルポートの設定
port_str = "/dev/tty.usbserial-AB0N63JR"
baud_rate = 9600
#  data_bits = 8
# stop_bits = 1
# parity = SerialPort::NONE
data_bits = nil
stop_bits = nil
parity = nil

sp = SerialPort.new(port_str, baud_rate, data_bits, stop_bits, parity)

puts "start..."
sp.write "hello from mac\n"

puts "end..."
sp.close
