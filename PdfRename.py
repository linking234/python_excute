#_*_ coding: utf-8 _*_
"""
Created on Sun Mar 12 10:53:10 2017
@author: Luyi Lin
"""
#用于将对应文件夹下的图纸内容提取出来，并将其中的作者，文件编码以及版本号用于文件名，减少工程师重命名的工作，降低错误率

import os
import sys
from PyPDF2.pdf import PdffileReader


#逐字翻译成GBK编码
def ascii2unicode(ascii_str):
    ascii_str_temp = ''
    for i in ascii_str:
        ascii_str_temp += chr(ord(i))
    return ascii_str_temp.decode('gbk')


#提取文字内容
def getDataUsingPyPdf2(filename):
    pdf = PdfFileReader(open(filename,'rb'))
    content = ""
    for i in range(0,pdf.getNumPages()):
        extractedText = pdf.getPage(i).extractText()
        content += extractedText + "\n"
        return ascii2unicode(content)


print getDataUsingPyPdf2(u'E:\\work\\^')


