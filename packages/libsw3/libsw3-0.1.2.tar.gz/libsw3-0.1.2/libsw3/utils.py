#!/usr/bin/python3
# -*- coding: utf8 -*-

__all__=["读简单配置","获取组成员"]

import time,base64,sys,json,urllib.request,ssl,os,datetime
import libsw3 as sw3

def 读简单配置(文件名,项目):
    '''读简单配置文件，一行一条数据，第一列是项目，返回项目后的内容'''
    dh,_=os.path.splitdrive(os.getcwd())
    fn=os.path.join(dh,"/etc",文件名)
    if os.path.isfile(fn):
        f=open(fn,"r")
    else:
        sw3.swexit(-1,"无法打开连接串配置文件%s" %(fn))
    wjnr=f.readlines()
    f.close()
    for i in wjnr:
        s=i.split()
        if len(s)<2:
            continue
        if s[0]==项目:
            return " ".join(s[1:])
    return ""

def 获取组成员(组id):
    pass
    