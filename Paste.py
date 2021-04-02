# -*- coding: utf-8 -*-
"""
Created on Sun Mar 28 23:49:02 2021

@author: Tang_Huanqiang
"""

from PIL import Image
import os

def paste_png(files,num):
    files = [file for file in files if file.endswith('.png')]
    if not os.path.exists('result'):
        os.mkdir('result')
    text_name = 'result/code'+str(num)+'.txt'
    with open(text_name,'w') as f:
        f.write(str(files))
    png_name = 'result/result'+str(num)+'.png'
    images = [Image.open(file) for file in files]
    width, height = images[0].size
    widths = []
    for j,image in enumerate(images):
        width, height = image.size
        widths.append(width)
    whole = sum(widths)
    result = Image.new(images[0].mode,(whole,height))
    heights = []
    c = 0
    for j,image in enumerate(images):
        if c==0:
            width=0
        else:
            width = sum(heights)
        heights.append(widths[c])
        c+=1
        result.paste(image,box=(width,0))
    result.save(png_name)

files = os.listdir()
files = [file for file in files if file.endswith('.png')]
num = 1
while(files!=[]):
    if len(files)>=14:
        paste_png(files[:14], num)
        num = num +1
        files = files[14:]
    else:
        paste_png(files, num)
        files = []

    
    
    
    
    
    
    
    
    
    
    