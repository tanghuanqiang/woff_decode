# -*- coding: utf-8 -*-
"""
Created on Sat Apr  3 00:53:51 2021

@author: Tang_Huanqiang
"""

from BaiduOcr import run
files = ['result/result' + str(i) + '.png' for i in range(1,44)]
for i in range(len(files)):
    words = run(files[i])
    filename = 'result/words' + str(i+1) + '.txt'
    with open(filename,'w') as f:
        f.write(words)
