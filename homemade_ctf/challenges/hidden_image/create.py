#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Author: Dipan Nama
# @Date:   2022-10-08 23:00:12
# @Last Modified by:   Dipan Nama
# @Last Modified time: 2022-10-08 23:25:10

import pwn

key = "c3VwZXJfc2VjcmV0X21lc3NhZ2UK"
with open('hidden_original.jpg', 'rb') as f:
	contents = f.read()
	data = pwn.xor(key,contents)
	msg = bytes("The key is : echo super_secret_message | base64", 'utf-8')
	data += msg
	with open('hidden.jpg','wb') as handle:
		handle.write(data)

		handle.close()
	f.close()