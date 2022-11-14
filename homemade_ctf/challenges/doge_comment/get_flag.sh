#!/usr/bin/bash
# @Author: Dipan Nama
# @Date:   2022-10-08 18:30:07
# @Last Modified by:   Dipan Nama
# @Last Modified time: 2022-10-08 18:32:57

exiftool doge64.jpg | grep -i comment | cut -d ":" -f2 | cut -d " " -f2 | base64 -d | tee flag.txt