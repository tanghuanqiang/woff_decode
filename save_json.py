# -*- coding: utf-8 -*-
"""
Created on Tue Mar 30 22:06:42 2021

@author: Tang_Huanqiang
"""
import os
import re
import json
code = ['result/code'+str(i)+'.txt' for i in range(1,44)]
words = ['result/words'+str(i)+'.txt' for i in range(1,44)]
dic = {}
for i in range(len(code)):
    code_file = open(code[i],'r')
    content = code_file.read()
    content = re.findall("'(.*?)'",content)
    words_file = open(words[i],'r')
    result = words_file.read()
    for j in range(len(content)):
        dic[content[j]] = result[j]
    code_file.close()
    words_file.close()

print(dic)
