#!/usr/bin/env python
# -*- coding:utf-8 -*-

import urllib2
import urllib
import re
import sys
#中文转码到url需要经过中间量，由于之前一直导出乱码，所以这里加的这些
defaultencoding = 'utf-8'
if sys.getdefaultencoding() != defaultencoding:
    reload(sys)
    sys.setdefaultencoding(defaultencoding)

# 进行转码
company_name = open("company.txt")
array = company_name.readlines()
print("-----------------dont`t worry,be happy!-----------------")
for company in array:
    company = company.decode('gb2312','ignore')
    url = "http://58.215.18.150:9090/egrantweb/psnactive/dealwith?way=dependorg&dependorg=%s"%company
    headers = {"User-Agent" : "Mozilla/5.0 (Windows NT 6.1; W…) Gecko/20100101 Firefox/57.0"}
    request = urllib2.Request(url, headers = headers)
    response = urllib2.urlopen(request)
     # 获取每页的HTML源码字符串
    html = response.read()
    # 创建正则表达式规则对象，匹配每页里的段子内容，re.S 表示匹配全部字符串内容
    pattern = re.compile('<ul>(.*?)</ul>', re.S)
    # 将正则匹配对象应用到html源码字符串里，返回这个页面里的所有段子的列表
    content_list = pattern.findall(html)
    for item in content_list:
        #设定一个参数用来存储是否含有电话号码
        num = 0
        # 将集合里的每个段子按个处理，替换掉无用数据
        item = item.replace("<li>","").replace("</li>", "").replace("<ul>", "").replace("</ul>", "").replace("</a>", "").replace('<span style="padding-right: 1em;"></span>', "").replace('<span style="padding-right: 2em;"></span>', "")
       #要是没电话，则跳过进入下一个
        number = ['0','1','2','3','4','5','6','7','8','9']
        for i in number:
            number_list = "电话： "
            number_list = number_list + i
            if number_list in item:
                num = num +1
        if num == 0:
            break
        # 处理完后调用writePage() 将每个段子写入文件内
        with open("look_here.txt", "a") as f:
            f.write("\n")
            f.write(item)
            f.close()
