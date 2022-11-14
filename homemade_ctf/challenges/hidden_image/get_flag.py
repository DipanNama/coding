#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Author: Dipan Nama
# @Date:   2022-10-08 23:20:48
# @Last Modified by:   Dipan Nama
# @Last Modified time: 2022-10-08 23:27:18


import pwn

key = "c3VwZXJfc2VjcmV0X21lc3NhZ2UK"
with open('hidden.jpg', 'rb') as f:
	contents = f.read()
	data = pwn.xor(key,contents)
	with open('hidden_output.jpg','wb') as handle:
		handle.write(data)
		handle.close()
	f.close()