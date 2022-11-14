#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Author: Dipan Nama
# @Date:   2022-10-08 16:28:21
# @Last Modified by:   Dipan Nama
# @Last Modified time: 2022-10-08 18:27:24

from random import shuffle, randint

handle = open('random_bytes','w')

total_bytes = 1000
mess=[]
for i in range(total_bytes):
	random_value = randint(0,255)
	for j in range(0,random_value):
		new_random_value = randint(0,255)
		mess.append(chr(new_random_value))
	if i == total_bytes/2:
		mess.append("flag{e7a3f8590f1182f400d1a4b4a6842874}")

content = "".join(mess)
handle.write(content)
handle.close()