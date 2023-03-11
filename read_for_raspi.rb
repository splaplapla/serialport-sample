require 'serialport'

# シリアルポートの設定
port_str = "/dev/serial0"
baud_rate = 9600
#  data_bits = 8
# stop_bits = 1
# parity = SerialPort::NONE
data_bits = nil
stop_bits = nil
parity = nil

# シリアルポートのオープン
sp = SerialPort.new(port_str, baud_rate, data_bits, stop_bits, parity)

sp.write "hello from raspi\n"

sp.close
