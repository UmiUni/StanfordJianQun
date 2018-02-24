# -*- coding: UTF-8 -*-
import datetime
def init():
  global admins
  global chatGroups
  global vT
  global usersDict
  global ADMIN
  global previousDay

  chatGroups =[ 
  u"leetcode天天",u"天天健身",
  u"北美CPA",u"Stanford湾区活动",
  u'Stanford湾区二手车',u'Stanford湾区二手货',
  u'Stanford湾区租房群2',u'Stanford旧金山租房',
  u'Stanford湾区厨艺',u'北美游戏交流',
  u'Stanford湾区护肤品',u'北美妈妈',
  u'Stanford硅谷工作内推',u'北美信用',
  u'Stanford,UCD',u'cmu湾区行李保管',
  u'线上KTV',u'北美表情分享',
  u'开战leetcode',u'Chuck郭律师',
  u'2018 H1B 中中中',u'北美区块链技术交流总群',
  u'Google内推面试刷题群',u'Twitter内推面试刷题群',
  u'Apple内推面试刷题群',u'Linkedin内推面试刷题群',
  u'Amazon内推面试刷题群',u'PettingPet 伴你宠 官方微信群1',
  u'北美股市Trading技术交流总群1'
  ]

  v0= u"您好，😊Stanford加群建群小助手😊为您服务～\n"
  v00=u"每天只能加2个群哦;\n"
  v1= u"回复 0 加CS刷题竞赛面试(leetcode);天天健身;\n"
  v2= u"回复 1 北美CPA,REG刷题群;Stanford湾区活动群\n"
  v3= u"回复 2 加湾区二手货、二手车群;\n"
  v4= u"回复 3 加湾区、旧金山租房群.\n"
  v5= u"回复 4 加湾区厨艺分享;北美游戏交流总群\n"
  v6= u"回复 5 加湾区护肤品化妆品;加北美母婴总群.\n"
  v7= u"回复 6 Stanford硅谷工作内推群;北美信用卡爱好者群.\n"
  v8= u"回复 7 加cmu湾区行李保管中美互运;Stanford,UCD拼车搭车群.\n"
  v9= u"回复 8 加线上KTV开嗓🎙️北美总群;北美表情分享总群.\n"
  v10= u"回复 9 加开战leetcode群(每周一战);加Chuck郭律师美帝绿卡讨论群.\n"
  v11= u"回复 10 加 H1B中中中群,北美区块链技术交流总群.\n"
  v12= u"回复 11 加 Google内推面试刷题群,Twitter内推面试刷题群\n"
  v13= u"回复 12 加 Applen内推面试刷题群,Linkedin内推面试刷题群\n"
  v14= u"回复 13 加 Amazon内推面试刷题群,PettingPet 伴你宠 官方微信群1\n"
  v15= u"回复 99 查看【北美加群小助手Jogchat.com】\n微信公众号二维码加纽约、芝加哥、三番、西雅图等群\n"
  v16= u"回复 100 加北美股市Trading技术交流总群1(无次数限制)\n"
  vT =v0+v00+v1+v2+v3+v4+v5+v6+v7+v8+v9+v10+v11+v12+v13+v14+v15+v16

  usersDict = {}
  admins=[]
  ADMIN = u'Stanford湾区加群助手jogchat.com'
  previousDay = datetime.datetime.now().day

