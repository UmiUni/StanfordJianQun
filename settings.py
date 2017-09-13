# -*- coding: UTF-8 -*-
def init():
  global admins
  global chatGroups
  global vT
  global usersDict
  global ADMIN

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
  u'线上KTV',u'北美表情分享'
  ]

  v0= u"您好，😊Stanford加群建群小助手😊为您服务～\n"
  v00=u"每天只能加3个群哦;\n"
  v1= u"回复 0 加CS刷题、竞赛、面试;健身;\n"
  v2= u"回复 1 北美CPA,REG刷题群;桌游群\n"
  v3= u"回复 2 加湾区、旧金山二手货、车群;\n"
  v4= u"回复 3 加湾区、旧金山租房群.\n"
  v5= u"回复 4 加湾区厨艺分享;戒游戏群\n"
  v6= u"回复 5 加湾区护肤品化妆品.加北美母婴总群.\n"
  v7= u"回复 6 加湾区实习工作群；Stanford校友群，非校友请勿进此群，谢谢.\n"
  v8= u"回复 7 加北美信用卡爱好者；Finding Yingying 群，家人校友都在努力～.\n"
  v9= u"回复 8 加cmu湾区行李保管中美互运、Stanford,UCD拼车搭车群.\n"
  v10= u"回复 9 加线上KTV开嗓🎙️北美总群;北美表情分享总群\n"
  v11= u"回复 99 查看【北美加群小助手Jogchat.com】\n微信公众号二维码加纽约、芝加哥、三番、西雅图等群\n"
  vT =v0+v00+v1+v2+v3+v4+v5+v6+v7+v8+v9+v10+v11

  usersDict = {}
  admins=[]
  ADMIN = u'Stanford湾区加群助手🐰'
