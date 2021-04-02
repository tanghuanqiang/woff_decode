# woff_decode
a application used to decode woff file into json-form word
## version：1.0
针对的是固定woff文件中相应编码对应的文字（如大众点评）
[字体](https://github.com/tanghuanqiang/woff_decode/blob/main/123.woff)
### 1
woff字体在文件中以点的方式存在，所以我们可以把woff文件中的字体利用plt将字体保存为图片
```python
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
```
### 2
利用百度智能云手写字体识别接口进行识别，但因为免费额度一天50次，如果每次只检测一个汉字，不仅浪费并且效率低下。
### 2.1
把单个字体的按照一定顺序合并（例子中有600+个汉字所以分为14个汉字一组比较合适，大于14时图片过长接口不允许）并保存在result下

[源码](https://github.com/tanghuanqiang/woff_decode/blob/main/Paste.py)
```python
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
```
### 2.2
利用百度智能云接口进行文字识别
[百度智能云官网quickstart教程]（https://cloud.baidu.com/doc/OCR/s/dk3iqnq51）
[源码](https://github.com/tanghuanqiang/woff_decode/blob/main/self_ocr.py)
### 3
通过文字识别的结果和相应编码匹配，保存为json文件
[源码](https://github.com/tanghuanqiang/woff_decode/blob/main/save_json.py)
```python
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
    break
print(dic)
```


