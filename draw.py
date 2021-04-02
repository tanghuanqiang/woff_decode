# -*- coding: utf-8 -*-
"""
Created on Sun Mar 28 12:43:14 2021

@author: Tang_Huanqiang
"""

import matplotlib.pyplot as plt
from fontTools.ttLib import TTFont
font = TTFont('123.woff')
order = font['glyf'].glyphOrder[2:]
for num in order:
    coordinate = list(font['glyf'][num].coordinates)
    print(coordinate)
    fig, ax = plt.subplots()    
    x = [i[0] for i in coordinate]
    y = [i[1] for i in coordinate]
    plt.fill(x, y, color="k", alpha=1)
    # 取消边框
    for key, spine in ax.spines.items():
        if key =='rigth' or key=='top' or key == 'bottom' or key =='left':
            spine.set_visible(False)
    plt.plot(x, y)
    # 取消坐标：
    plt.axis('off')
    filename = num + '.png'
    plt.savefig(filename)
