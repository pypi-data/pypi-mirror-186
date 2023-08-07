#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author  : lhr (airhenry@gmail.com)
# @Link    : http://about.me/air.henry

"""
提供从docx文件提取图片和文字的函数
"""

import  re
import base64
from docx import Document
from docx.shared import Inches
import chardet

class Doc():
    '''
    self.image, self.text 都是数组
    '''
    def __init__(self,filename):
        self.text=self.extract_brief(filename)
        if self.text:
            # body='# ' + self.text[0]
            body=self.text[0]
            for i in range(1,len(self.text)):
                body=body+'\n\n'+self.text[i]
            self.markdown=body

        if self.text:
            body='<h3>'+self.text[0]+'</h3>'
            for i in range(1,len(self.text)):
                body=body+'<p>'+self.text[i]+'</p>'
            self.text=body

        self.image=self.extract_image(filename)
        # self.image=False
        if self.image:
            self.image=str(b'<img style="max-height: 200px" src="data:image/png;base64,'+base64.encodestring(self.image[0])+b'">')
            # self.image=str(b'data:image/png;base64,'+base64.encodestring(self.image[0]))


        self.filename=filename

    def extract_image(self,filename):
        '''
        返回匹配的图片列表, 每个列表项是一张图片的内容字符串
        extract images from .doc file, may be useful in other unzip files also
        gif:gif v87
            start tag : GIF87a
            end tag   : x3B
            output ext: gif
            re string : (GIF87a.+?\x3B)
        gif:gif v89
            start tag : GIF89a
            end tag   : x3B
            output ext: gif
            re string : (GIF89a.+?\x3B)
        png:
            start tag : \x89\x50\x4E\x47\x0D\x0A\x1A\x0A
            end tag   : \x00\x00\x00\x00\x49\x45\x4E\x44\xAE\x42\x60\x82
            output ext: png
            re string : (\x89\x50\x4E\x47\x0D\x0A\x1A\x0A.+?\x00\x00\x00\x00\x49\x45\x4E\x44\xAE\x42\x60\x82)
        jpg:
            start tag : \xFF\xD8
            end tag   : \xFF\xD9
            output ext: jpg
            re string : (\xFF\xD8.+?\xFF\xD8.+?\xFF\xD9.+?\xFF\xD9)   #jpg file has a content start with \xff\xd8 and end with \xff\xd9, so we should match 2 times
        '''
        file_format = {
            # 'gifv87':{'start':'GIF87a', 'end':'\x3B', 'ext':'gif','regstr':'(GIF87a.+?\x3B)'},
            # 'gifv89':{'start':'GIF89a', 'end':'\x3B', 'ext':'gif','regstr':'(GIF89a.+?\x3B)'},
            'png':{'start':'\x89\x50\x4E\x47\x0D\x0A\x1A\x0A', 'end':'\x00\x00\x00\x00\x49\x45\x4E\x44\xAE\x42\x60\x82', 'ext':'png','regstr':b'(\x89\x50\x4E\x47\x0D\x0A\x1A\x0A.+?\x00\x00\x00\x00\x49\x45\x4E\x44\xAE\x42\x60\x82)'},
            # 'jpg':{'start':'\xFF\xD8', 'end':'\xFF\xD9', 'ext':'jpg','regstr':'(\xFF\xD8.+?\xFF\xD8.+?\xFF\xD9.+?\xFF\xD9)'},
            }
        with open(filename, 'rb') as f:
            data = f.read()
            # encode_type = chardet.detect(data)
            # print(data)
            # print( encode_type)
            # data = data.decode(encode_type['encoding']) #进行相应解码，赋给原标识符（变量）
            for x in file_format.keys():
                reg = file_format[x]['regstr'] #use re str
                p = re.compile(reg, re.S)
                rs = p.findall(data)

                return rs
                # for i in range(len(rs)):
                    # with open('./file' + str(i) + '.' + file_format[x]['ext'], 'wb') as w:
                    #     w.write(rs[i])




    def extract_brief(self,filename):

        part1 = ''
        part2 = 'Brief introduction'
        part3 = 'Detailed illustration'

        document = Document(filename)
        paragraphs=document.paragraphs

        ans=[]
        ans.append(paragraphs[0].text)
        for i in range(1,len(paragraphs)):
            if paragraphs[i].text.find(part3)!=-1:
                break
            ans.append(paragraphs[i].text)
        return ans






if __name__ == '__main__':
    filename='databank/1-N-N/1-N-log.docx'
    doc=Doc(filename)
    # print doc.text
