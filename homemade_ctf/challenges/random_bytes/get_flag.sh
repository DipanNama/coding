#!/usr/bin/bash
# @Author: Dipan Nama
# @Date:   2022-10-08 17:41:18
# @Last Modified by:   Dipan Nama
# @Last Modified time: 2022-10-08 17:58:36

strings random_bytes | grep -o -E "flag{(.*)}" | tee flag.txt