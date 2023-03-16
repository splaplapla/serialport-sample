# serialport-sample
* macosとraspiとでシリアル通信するためのサンプルコード集

## Setup
* $ cp dotenvrc .envrc

## 使い方
* .envrc に IAM=を書くと、`bundle exec ruby read` と `bundle exec ruby write`だけで送受信のテストができる
* python serialToPBM.py hoge\n -d /dev/tty.XXXX -b 9600
