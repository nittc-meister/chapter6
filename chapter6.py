# -*- coding: utf-8 -*-
  
import smbus
import time
import datetime  #課題2用
import json  #課題2用

i2c = smbus.SMBus(1)
address = 0x48
json_file = open('result.json', 'w')  #課題2用
now = datetime.datetime.now()

for i in range(10):
    block = i2c.read_i2c_block_data(address, 0x00, 12)
    temp = (block[0] << 8 | block[1]) >> 3
    if(temp >= 4096):
        temp -= 8192
    print("Temperature:%6.2f" % (temp / 16.0))
    time.sleep(1)

    dic = {"id" + str(i): {"time": str(now), "temp": temp}}

json.dump(dic, json_file, ensure_ascii=False, indent=4, sort_keys=True, separators=(',', ': '))
json_file.close()