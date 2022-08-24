#!/usr/bin/env python
#coding:utf-8
# =============================================================================
# Created on 2020/4/15/7:36:56 PM
# @ author SRMebius
# =============================================================================

import base64

strs = '4955566670-66707048-48564948-705649'
strs = '6670696670-66707048-48485648-546967'
strs = '6670696670-66707048-48485748-546967'
str = strs.replace('-', '')
serial_number = ''
for i in range(0,len(str),2):
    s = str[i:i+2]
    x = chr(int(s))
    serial_number += x
authorization_code = base64.b64encode(serial_number.encode())
print(f'CPU序列号为：{serial_number}')
print(f'授权码为：{authorization_code}')
