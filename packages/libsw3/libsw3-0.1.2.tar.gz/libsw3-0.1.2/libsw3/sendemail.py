#!/usr/bin/python3
# -*- coding: utf8 -*-

__all__=["可靠邮件","普通邮件"]

from email import encoders
import smtplib,configparser,os
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart
import libsw3 as sw3

class 普通邮件(object):   #直接发送，如果发送失败，可能导致程序崩溃或者邮件发送失败
    def __init__(self,发送者,标题,正文,接收,抄送=[],暗送=[]):
        self.参数=[发送者,标题,正文,接收,抄送,暗送]
        self.msg=MIMEMultipart()
        self.msg.attach(MIMEText(正文, 'plain', 'gbk'))
        self.msg['Subject'] = 标题
        self.msg['From'] = "%s@mail.rtfund.com" %(发送者)
        self.dz=[]
        self.msg['To'] = ','.join(self.解析地址(接收))
        self.msg['Cc'] = ','.join(self.解析地址(抄送))
        self.msg['Bcc'] = ','.join(self.解析地址(暗送))
    def 解析地址(self,地址):
        if type(地址)!=type([]):
            地址=[地址]
        self.dz=self.dz + 地址
        return 地址
    def attachfile(self,attname,文件名):
        self.attach(attname,open(文件名, 'rb').read())
    def attach(self,attname,att):
        attmt = MIMEBase('application', 'octet-stream')
        attmt.set_payload(att)
        attmt.add_header('Content-Disposition', 'attachment', filename=('gbk', '', attname) )
        encoders.encode_base64(attmt)
        self.msg.attach(attmt)
    def send(self):
        rtmailcfg = configparser.ConfigParser()
        dh,_=os.path.splitdrive(os.getcwd())
        rtmailcfg.read(os.path.join(dh,"/etc","rtmail.cfg"))
        cfg=rtmailcfg[self.参数[0]]
        smtp=smtplib.SMTP(cfg["smtpserver"])
        smtp.starttls()
        smtp.login(cfg["user"],cfg["password"])
        smtp.sendmail(cfg["from"],self.dz,self.msg.as_string())
        smtp.close()

class 可靠邮件(object):   #把数据保存在本地硬盘，使用另一个扫描程序进行发送
    def __init__(self,发送者,标题,正文,接收,抄送=[],暗送=[]):
        self.参数=[发送者,标题,正文,接收,抄送,暗送]
    
def create_html_table(headlist,keylist,datalist):
    '''
		生成table样式的html内容。参数信息如下：
		headlist		- 字符list,用于表头显示的文本
		keylist			- 字符list,key顺序与thead保持一致
		datalist		- 对象list,用于存储表格中显示的数据
	'''
    _html, _head, _trs = ("", "<tr>", "")
    if len(headlist)==len(keylist):
        # head
        for headtitle in headlist:
            _head = _head + "<th>" + headtitle + "</th>"
        _head = _head + "</tr>"
        # body
        for d in datalist:
            _tr = "<tr>"
            for key in keylist:
                _tr = _tr + "<td>" + d.get(key,"") + "</td>"
            _tr = _tr + "</tr>"
            _trs = _trs + _tr
        _html = HTML_TEMP_TABLE.replace("$THEAD_TR$", _head).replace("$TBODY_TR$", _trs)
    return _html


HTML_TEMP_TABLE = '''
<html>
	<head>
		<style>
		table {
			border-collapse: collapse;
		}
		th,td {
			 padding: 8px;
		}
		th {
			background:#555;
			border: 1px solid #777;
			text-align: left;
			color: #fff;
			font-size:14px;
		}
		td {
			border: 1px solid #777;
			font-size:13px;
		}
		</style>
	</head>
	<body>
		<table align="center">
			<thead>
				$THEAD_TR$
			</thead>
			<tbody>
				$TBODY_TR$
			</tbody>
		</table>
	</body>

</html>
'''

