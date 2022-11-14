#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Author: Dipan Nama
# @Date:   2022-10-08 18:02:06
# @Last Modified by:   Dipan Nama
# @Last Modified time: 2022-10-08 18:28:15

import base64 as b
import subprocess

filename = 'doge64.jpg'
flag = "flag{a84e77825d527029732f354087298814}"
flag = flag.encode('utf-8')
flag = b.b64encode(flag)
flag = flag.decode('utf-8')
subprocess.call(('exiftool ' + filename + ' -comment=%s' % flag).split())