import serial
import argparse
import time
import threading

"""
シリアル通信クラス
"""
class SerialToPBM:
    def __init__(self):
        self.isPortOpen = False
        self.recvData = bytearray()
        self.event = threading.Event()
        self.comm = None

    def recv(self, timeout=3):
        time_start = time.time()
        time_end = time_start
        self.event.clear()
        self.recvData.clear()
        result = False

        # データ受信待ち
        while not self.event.is_set():
            time_end = time.time()
            if (time_end - time_start > timeout):
                result = False
                self.stop()
                print("timeout:{0}sec".format(timeout))
                break

            buff = self.comm.read()

            # 受信データ判定
            if len(buff) > 0:
                self.recvData.extend(buff)
                # (仮)¥nを受信済なら成功とする
                if (self.recvData.find(b'\n')) >= 0:
                    result = True
                    self.stop()
                    break

        return (result, self.recvData)

    def send(self, data):
        self.comm.write(data)

    def stop(self):
        self.event.set()

    def open(self, device, baud):
        try:
            self.comm = serial.Serial(device, baud, timeout=0.1)
            self.isPortOpen = True
        except Exception as e:
            print(e)
            self.isPortOpen = False

        return self.isPortOpen

    def close(self):
        self.stop()
        if (self.isPortOpen):
            self.comm.close()
        self.isPortOpen = False

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('--device', '-d', type=str, default='/dev/tty.')
    parser.add_argument('--baud', '-b', type=int, default=9600)
    parser.add_argument('data', type=str)
    args = parser.parse_args()
    print(args)

    serialToPBM = SerialToPBM()
    serialToPBM.open(args.device, args.baud)

    serialToPBM.send(args.data.encode())
    result, data = serialToPBM.recv(10)
    print(result)
    print(data)

    serialToPBM.close()
