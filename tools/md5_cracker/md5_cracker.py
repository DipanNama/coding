#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Author: Dipan Nama
# @Date:   2022-10-08 20:25:36
# @Last Modified by:   Dipan Nama
# @Last Modified time: 2022-10-09 22:25:40

import hashlib
import string

# plaintext = "pa$$word" 
# hash = hashlib.md5(plaintext.encode()).hexdigest()
# print(f"The actual password is : {plaintext} | {hash}")


i = 0
characters = ''
letters = string.ascii_letters
digits = string.digits
sysbols = string.punctuation
characters= letters + digits + sysbols

length = len(characters) # 94
string = ''

while ( i<length ):
	for j in range(length):
		string += characters[j]
		new_hash = hashlib.md5(string.encode()).hexdigest()
		print(f"{string} | {new_hash}")
		if len(string) == length:
			exit()
	i += 1



# pass_file = open('passwords.txt','r')

# for word in pass_file:
# 	enc_word = word.encode()
# 	digest = hashlib.md5(enc_word.strip()).hexdigest()
# 	enc_word = enc_word.decode('utf-8')
# 	if digest == hash:
# 		print(f"The cracked password is : {enc_word} | {digest}")
# 		break