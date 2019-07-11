# -*- coding: utf-8 -*-

import smbus
import time
import datetime  #課題2用
import json  #課題2用

i2c = smbus.SMBus(1)
address = 0x48
json_file = open('result.json', 'w')  #課題2用
dict = {}

for i in range(10):
    key = "id"+str(i)
    block = i2c.read_i2c_block_data(address, 0x00, 12)
    temp = (block[0] << 8 | block[1]) >> 3
    if(temp >= 4096):
        temp -= 8192
    dict[key]={}
    print("Temperature:%6.2f" % (temp / 16.0))
    print("Time:"+str(datetime.datetime.now()))
    dict[key]["time"] = str(datetime.datetime.now())
    dict[key]["temp"] = str(temp / 16.0)
    time.sleep(1)

json.dump(dict, json_file, indent=4, sort_keys=True)
json_file.close()
