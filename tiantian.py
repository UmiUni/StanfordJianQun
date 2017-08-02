# -*- coding: UTF-8 -*-  
import requests
import itchat
from itchat.content import *
import sys  
import json
import time
from time import sleep
reload(sys)  
sys.setdefaultencoding('utf8')
import re
itchat.auto_login(enableCmdQR=2,hotReload=True)
itchat.get_chatrooms(update=True)
usersDict = {}
chatGroups =[ 
u"天天刷题",u"天天健身",
u"北美CPA",u"Stanford湾区桌游",
u'Stanford湾区二手车',u'Stanford湾区二手货',
u'Stanford湾区租房',u'Stanford旧金山租房',
u'Stanford湾区厨艺',u'天天剁手',
u'Stanford湾区护肤品',u'北美妈妈',
u'2017湾区实习工作群',u'Stanford校友群',
u'北美信用',u'找莹颖',
u'Stanford,UCD',u'cmu湾区行李保管',
u'线上KTV',
]

v0= u"您好，😊Stanford加群建群小助手😊为您服务～\n"
v1= u"回复 0 加CS刷题、竞赛、面试;健身;\n"
v2= u"回复 1 北美CPA,REG刷题群;桌游群\n"
v3= u"回复 2 加湾区、旧金山二手货、车群;\n"
v4= u"回复 3 加湾区、旧金山租房群.\n"
v5= u"回复 4 加湾区厨艺分享;戒游戏群\n"
v6= u"回复 5 加湾区护肤品化妆品.加北美母婴总群.\n"
v7= u"回复 6 加湾区实习工作群；Stanford校友群，非校友请勿进此群，谢谢.\n"
v8= u"回复 7 加北美信用卡爱好者；Finding Yingying 群，家人校友都在努力～.\n"
v9= u"回复 8 加cmu湾区行李保管中美互运、Stanford,UCD拼车搭车群.\n"
v10= u"回复 9 加线上KTV开嗓🎙️北美总群;\n"
vT =v0+v1+v2+v3+v4+v5+v6+v7+v8+v9+v10

@itchat.msg_register('Friends')
def add_friend(msg):
    itchat.add_friend(**msg['Text'])
    itchat.send_msg(vT, msg['RecommendInfo']['UserName'])

def get_response(msg):
    # 这里我们就像在“3. 实现最简单的与图灵机器人的交互”中做的一样
    # 构造了要发送给服务器的数据
    apiUrl = 'http://www.tuling123.com/openapi/api'
    data = {
        'key'    : '8028064e9e2f46c78a111276823f94b1',
        'info'   : msg,
        'userid' : 'superchaoran',
    }
    try:
        r = requests.post(apiUrl, data=data).json()
        # 字典的get方法在字典没有'text'值的时候会返回None而不会抛出异常
        return r.get('text')
    # 为了防止服务器没有正常响应导致程序异常退出，这里用try-except捕获了异常
    # 如果服务器没能正常交互（返回非json或无法连接），那么就会进入下面的return
    except:
        # 将会返回一个None
        return msg
@itchat.msg_register(itchat.content.TEXT)
def tuling_reply(msg):
    CurUserName = msg['FromUserName']
    #print(json.dumps(response)+"\n")
    print("userid:"+CurUserName+"\n") 
    if(CurUserName in usersDict):
        usersDict[CurUserName] = usersDict[CurUserName] + 1
        if(usersDict[CurUserName] >= 10):
            itchat.send_msg(u'您已达到今日加群上限，请明日再来～😊', CurUserName)
            return
    else:
        usersDict[CurUserName] = 1
    msgText = msg['Text']
    x = re.findall(r'\d+', msgText)
    if(len(x) >0):
      y= int(x[0])
      if(y>=0 and y<=9):
        pullMembersMore(msg, chatGroups[y*2], CurUserName)
        sleep(0.5)
        if(y!=9):
          pullMembersMore(msg, chatGroups[y*2+1], CurUserName)
          sleep(0.5)
    itchat.send_msg(vT, CurUserName)
    sleep(0.5)

def pullMembersMore(msg, chatroomName, CurUserName):
    cur_chatrooms = itchat.search_chatrooms(name=chatroomName)
    chatRoomUserName = cur_chatrooms[0]['UserName']
    r = itchat.add_member_into_chatroom(chatRoomUserName,[{'UserName':CurUserName}],useInvitation=True)

@itchat.msg_register(TEXT, isGroupChat=True)
def text_reply(msg):
    msgS = msg.text
    if u'超然' in msg['ActualNickName']:
      content = msg['Content']
      if(content[0]=="@"):
        if u'广告' in content:
          delUser(msg['FromUserName'],content)

itchat.run() 




