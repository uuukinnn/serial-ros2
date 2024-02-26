#!/usr/bin/env python

import serial, sys

if len(sys.argv) != 2:
    print ("python: Usage_serial_test <port name like: /dev/ttyUSB0>")
    sys.exit(1)

sio = serial.Serial(sys.argv[1], 38400)
sio.timeout = 250
cmd = [0x80,0x23,0x04,0x31,0x50,0x02,0x01,0x0a,0x40]

while True:
    #sio.write("1,getp".encode('utf-16be'))
    sio.write(cmd)
    print (sio.read(11))

