# -*- coding: utf-8 -*-

import LINETCR
from LINETCR.lib.curve.ttypes import *
from datetime import datetime
import time, random, sys, ast, re, os, io, json, subprocess, threading, string, codecs, requests, ctypes, urllib, urllib2, tempfile
import timeit
import json
import html5lib
import base64
import subprocess as cmd
from bs4 import BeautifulSoup
from urllib import urlopen
from io import StringIO
from threading import Thread
from gtts import gTTS
from googletrans import Translator

ar1 = LINETCR.LINE()
ar1.login(token="YOUR TOKEN"
ar1.loginResult()

ar2 = LINETCR.LINE()
ar2.login(token="YOUR TOKEN"
ar2.loginResult()

ar3 = LINETCR.LINE()
ar3.login(token="YOUR TOKEN"
ar3.loginResult()

ar4 = LINETCR.LINE()
ar4.login(token="YOUR TOKEN"
ar4.loginResult()

ar5 = LINETCR.LINE()
ar5.login(token="YOUR TOKEN"
ar5.loginResult()

ar6 = LINETCR.LINE()
ar6.login(token="YOUR TOKEN"
ar6.loginResult()

ar7 = LINETCR.LINE()
ar7.login(token="YOUR TOKEN"
ar7.loginResult()

ar8 = LINETCR.LINE()
ar8.login(token="YOUR TOKEN"
ar8.loginResult()

ar9 = LINETCR.LINE()
ar9.login(token="YOUR TOKEN"
ar9.loginResult()

ar10 = LINETCR.LINE()
ar10.login(token="YOUR TOKEN"
ar10.loginResult()

print "╔═════════════════════════\n║╔════════════════════════\n║╠❂➣ ║ARIFISTIFIK LOGIN BERHASIL \n║╚════════════════════════\n╚═════════════════════════"
reload(sys)
sys.setdefaultencoding('utf-8')

helpmsg ="""
╔═════════════
║║HELP MESSAGE
╠═════════════
║╔════════════
║╠❂➣time
║╠❂➣Salam1/Salam2
║╠❂➣Creator
║╠❂➣Kelahiran
║╠❂➣Kalender/waktu
║╠❂➣say
║╠❂➣time
║╠❂➣Kapan
║╠❂➣Apakah
║╠❂➣Nah
║╠❂➣Absen
║╠❂➣runtime
║╠❂➣nama saya
║╠❂➣foto saya
║╠❂➣cover saya
║╠❂➣video saya
║╠❂➣nama bot
║╠❂➣foto bot
║╠❂➣cover bot
║╠❂➣video bot
║╠❂➣keybot
║╚════════════
╚═════════════"""

keymsg ="""
╔═════════════
║║KEY MESSAGE
╠═════════════
╠═════════════
║╔════════════
║╠❂➣keypro
║╠❂➣keyself
║╠❂➣keygrup
║╠❂➣keyset
║╠❂➣keytran
║╠❂➣mode on/off
║╚════════════
╚═════════════"""

helppro ="""
╔═════════════
║║PROTECTION
╠═════════════
╠═════════════
║╔════════════
║╠❂➣mode on/off
║╠❂➣protect on/off
║╠❂➣qr on/off
║╠❂➣invite on/off
║╠❂➣cancel on/off
║╚════════════
╚═════════════"""

helpself ="""
╔═════════════
║║HELP SELF
╠═════════════
╠═════════════
║╔════════════
║╠❂➣Myname
║╠❂➣Mybot
║╠❂➣Mybio
║╠❂➣Mypict
║╠❂➣Myvid
║╠❂➣Urlpict
║╠❂➣Mycover
║╠❂➣Urlcover
║╚════════════
╚═════════════
line.me/R/ti/p/~arif.mh"""

helpset ="""
╔═════════════
║║SETTINGS
╠═════════════
╠═════════════
║╔════════════
║╠❂➣Gurl
║╠❂➣Grup cancel:
║╠❂➣share on/off
║╠❂➣Poto on/off
║╠❂➣Sambut on/off
║╠❂➣Pergi on/off
║╠❂➣contact on/off
║╠❂➣autojoin on/off
║╠❂➣autoleave on/off
║╠❂➣autoadd on/off
║╠❂➣like friend
║╠❂➣Like me
║╠❂➣link on/off
║╠❂➣update
║╠❂➣Pesan set:
║╠❂➣Coment Set:
║╠❂➣Comment on/off
║╠❂➣Comment
║╠❂➣Com hapus Bl
║╠❂➣Com Bl cek
║╠❂➣jam on/off
║╠❂➣Jam say:
║╚════════════
╚═════════════
line.me/R/ti/p/~arif.mh"""

helpgrup ="""
╔═════════════
║ ║GROUP HELP
╠═════════════
╠═════════════
║╔════════════
║╠❂➣Link on
║╠❂➣Url
║╠❂➣Cancel
║╠❂➣Gcreator
║╠❂➣Kick @
║╠❂➣Kill @
║╠❂➣Infogrup
║╠❂➣Gruplist
║╠❂➣Friendlist
║╠❂➣Blacklist
║╠❂➣Ban @
║╠❂➣Unban @
║╠❂➣Clearban
║╠❂➣Banlist
║╠❂➣Contact ban
║╠❂➣Midban
║╠❂➣Kick @
║╠❂➣cancel
║╠❂➣Friendlist
║╠❂➣Memlist
║╠❂➣Friendinfo:
║╠❂➣Friendpict:
║╠❂➣Friendlistmid
║╠❂➣Blocklist
║╠❂➣Gruplist
║╠❂➣Gruplistmid
║╠❂➣Glist
║╠❂➣gcancel
║╠❂➣DPK/. (manggil bot)
║╠❂➣Bye All
║╠❂➣Bye1/Bye2
║╠❂➣absen/ats @ (tagall)
║╠❂➣Ban @
║╠❂➣Unban @
║╠❂➣Ban:
║╠❂➣Unban:
║╠❂➣Clear
║╠❂➣Ban:on
║╠❂➣Unban:on
║╠❂➣Banlist
║╠❂➣Conban/Contact ban
║╠❂➣Midban
║╠❂➣scan blacklist
║╚════════════
╚═════════════
line.me/R/ti/p/~arif.mh"""

helptranslate ="""
╔═════════════
║ ║ARIFISTIFIK
╠═════════════
╠═════════════
║╔════════════
║╠❂➣Translate-id
║╠❂➣Translate-en
║╠❂➣Translate-ar
║╠❂➣Translate-jp
║╠❂➣Translate-ko
║╠❂➣Id@en
║╠❂➣En@id
║╠❂➣Id@jp
║╠❂➣Jp@id
║╠❂➣Id@th
║╠❂➣Th@id
║╠❂➣Id@ar
║╠❂➣Ar@id
║╠❂➣Id@ko
║╠❂➣Ko@id
║╠❂➣Say-id
║╠❂➣Say-en
║╠❂➣Say-jp
║╠❂➣Say-ar
║╠❂➣Say-ko
║╠❂➣welcome
║╚════════════
╚═════════════
line.me/R/ti/p/~arif.mh"""

helprhs ="""
╔═════════════
║ ║ARIFISTIFIK
╠═════════════
╠═════════════
║╔════════════
║╠❂➣Bantai
║╠❂➣ifconfig
║╠❂➣system
║╠❂➣kernel
║╠❂➣cpu
║╠❂➣Turn off
║╠❂➣Speed
║╠❂➣Invite
║╠❂➣Restart
║╚════════════
╚═════════════
line.me/R/ti/p/~arif.mh"""

DEF=[ar1,ar2,ar3,ar4,ar5,ar6,ar7,ar8,ar9,ar10]
KAC=[ar1,ar2,ar3,ar4,ar5,ar6,ar7,ar8,ar9,ar10]
mid = ar1.getProfile().mid
mid2 = ar2.getProfile().mid
mid3 = ar3.getProfile().mid
mid4 = ar4.getProfile().mid
mid5 = ar5.getProfile().mid
mid6 = ar6.getProfile().mid
mid7 = ar7.getProfile().mid
mid8 = ar8.getProfile().mid
mid9 = ar9.getProfile().mid
mid10 = ar10.getProfile().mid
Bots=[mid,mid2,mid3,mid4,mid5,mid6,mid7,mid8,mid9,mid10,"MID YG MAU DI JADIKAN ADMIN"]
admin=["mid admin buat tambahan aja"]
staff=["mid staff"]
owner=["mid owner"]

wait = {
    "'contact":True,
    "likeOn":False,
    "Sider": True,
    "Wc":False,
    "Lv":False,
    "MENTION":True,
    "steal":False,
    'invite':{},
    "spam":{},
    'contact':False,
    'autoJoin':True,
    'autoCancel':{"on":False,"members":1},
    'leaveRoom':False,
    'timeline':True,
    'autoAdd':True,
    'sticker':{},
    'tag':False,
    'message':"Thanks for add me\n\nBOTS by ║ARIFISTIFIK\n\nhttps://line.me/R/ti/p/~arif.mh",
    "lang":"JP",
    "comment":"Thanks for add me\n\nBOTS by ║ARIFISTIFIK\n\nhttps://line.me/R/ti/p/~arif.mh",
    "commentOn":True,
    "winvite":False,
    "Welcomemessage":False,
    "Byemessage":False,
    "commentBlack":{},
    "wblack":False,
    "dblack":False,
    "clock":False,
    "cName":"",
    "cNames":"",
    "blacklist":{},
    "wblacklist":False,
    "dblacklist":False,
    "protect":{},
    "cancelprotect":{},
    "inviteprotect":{},
    "linkprotect":{},
    "Protectguest":{},
    "Protectjoin":{},
}

wait2 = {
    'readPoint':{},
    'readMember':{},
    'setTime':{},
    'ROM':{},
    'ricoinvite':{},
    'copy':True,
    'target':{},
    'midsTarget':{},
    }

setTime = {}
setTime = wait2['setTime']
mulai = time.time() 

mulai = time.time()

agent = {'User-Agent' : "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1; .NET CLR 1.1.4322; .NET CLR 2.0.50727; .NET CLR 3.0.04506.30)"}

#Finding 'Next Image' from the given raw page
def _images_get_next_item(s):
    start_line = s.find('rg_di')
    if start_line == -1:    #If no links are found then give an error!
        end_quote = 0
        link = "no_links"
        return link, end_quote
    else:
        start_line = s.find('"class="rg_meta"')
        start_content = s.find('"ou"',start_line+90)
        end_content = s.find(',"ow"',start_content-90)
        content_raw = str(s[start_content+6:end_content-1])
        return content_raw, end_content

#Getting all links with the help of '_images_get_next_image'
def _images_get_all_items(page):
    items = []
    while True:
        item, end_content = _images_get_next_item(page)
        if item == "no_links":
            break
        else:
            items.append(item)      #Append all the links in the list named 'Links'
            time.sleep(0.1)        #Timer could be used to slow down the request for image downloads
            page = page[end_content:]
    return items

def yt(query):
    with requests.session() as s:
         isi = []
         if query == "":
             query = "S1B tanysyz"
         s.headers['user-agent'] = 'Mozilla/5.0'
         url    = 'http://www.youtube.com/results'
         params = {'search_query': query}
         r    = s.get(url, params=params)
         soup = BeautifulSoup(r.content, 'html5lib')
         for a in soup.select('.yt-lockup-title > a[title]'):
            if '&list=' not in a['href']:
                if 'watch?v' in a['href']:
                    b = a['href'].replace('watch?v=', '')
                    isi += ['youtu.be' + b]
         return isi

def waktu(secs):
    mins, secs = divmod(secs,60)
    hours, mins = divmod(mins,60)
    return '%02d Jam %02d Menit %02d Detik' % (hours, mins, secs)

def upload_tempimage(client):
     '''
         Upload a picture of a kitten. We don't ship one, so get creative!
     '''
     config = {
         'album': album,
         'name':  'bot auto upload',
         'title': 'bot auto upload',
         'description': 'bot auto upload'
     }

     print("Uploading image... ")
     image = ar1.upload_from_path(image_path, config=config, anon=False)
     print("Done")
     print()

     return image


def sendMessage(to, text, contentMetadata={}, contentType=0):
    mes = Message()
    mes.to, mes.from_ = to, profile.mid
    mes.text = text
    mes.contentType, mes.contentMetadata = contentType, contentMetadata
    if to not in messageReq:
        messageReq[to] = -1
    messageReq[to] += 1

def sendImage(self, to_, path):
      M = Message(to=to_,contentType = 1)
      M.contentMetadata = None
      M.contentPreview = None
      M_id = self.Talk.ar1.sendMessage(0,M).id
      files = {
         'file': open(path, 'rb'),
      }
      params = {
         'name': 'media',
         'oid': M_id,
         'size': len(open(path, 'rb').read()),
         'type': 'image',
         'ver': '1.0',
      }
      data = {
         'params': json.dumps(params)
      }
      r = self.post_content('https://os.line.naver.jp/talk/m/upload.nhn', data=data, files=files)
      if r.status_code != 201:
         raise Exception('Upload image failure.')
      return True

def sendImageWithURL(self, to_, url):
      path = '%s/pythonLine-%i.data' % (tempfile.gettempdir(), randint(0, 9))
      r = requests.get(url, stream=True)
      if r.status_code == 200:
         with open(path, 'w') as f:
            shutil.copyfileobj(r.raw, f)
      else:
         raise Exception('Download image failure.')
      try:
         self.sendImage(to_, path)
      except Exception as e:
         raise e

def restart_program():
    python = sys.executable
    os.execl(python, python, * sys.argv)

def post_content(self, urls, data=None, files=None):
        return self._session.post(urls, headers=self._headers, data=data, files=files)

def NOTIFIED_READ_MESSAGE(op):
    try:
        if op.param1 in wait2['readPoint']:
            Name = ar1.getContact(op.param2).displayName
            if Name in wait2['readMember'][op.param1]:
                pass
            else:
                wait2['readMember'][op.param1] += "\n9§9" + Name
                wait2['ROM'][op.param1][op.param2] = "9§9" + Name
        else:
            pass
    except:
        pass

def sendAudio(self, to_, path):
        M = Message(to=to_, text=None, contentType = 3)
        M_id = self.Talk.ar1.sendMessage(0,M).id
        files = {
            'file': open(path, 'rb'),
        }
        params = {
            'name': 'media',
            'oid': M_id,
            'size': len(open(path, 'rb').read()),
            'type': 'audio',
            'ver': '1.0',
        }
        data = {
            'params': json.dumps(params)
        }

        r = self.post_content('https://os.line.naver.jp/talk/m/upload.nhn', data=data, files=files)
        print r
        if r.status_code != 201:
            raise Exception('Upload audio failure.')


def sendAudioWithURL(self, to_, url):
      path = '%s/pythonLine-%i.data' % (tempfile.gettempdir(), randint(0, 9))
      r = requests.get(url, stream=True)
      if r.status_code == 200:
         with open(path, 'w') as f:
            shutil.copyfileobj(r.raw, f)
      else:
         raise Exception('Download audio failure.')
      try:
         self.sendAudio(to_, path)
      except Exception as e:
            raise e
def sendAudioWithURL(self, to_, url):
      path = 'pythonLiness.data'
      r = requests.get(url, stream=True)
      if r.status_code == 200:
         with open(path, 'w') as f:
            shutil.copyfileobj(r.raw, f)
      else:
         raise Exception('Download Audio failure.')
      try:
         self.sendAudio(to_, path)
      except Exception as e:
         raise e

def mention(to,nama):
    aa = ""
    bb = ""
    strt = int(12)
    akh = int(12)
    nm = nama
    #print nm
    for mm in nm:
        akh = akh + 2
        aa += """{"S":"""+json.dumps(str(strt))+""","E":"""+json.dumps(str(akh))+""","M":"""+json.dumps(mm)+"},"""
        strt = strt + 6
        akh = akh + 4
        bb += "► @c \n"
    aa = (aa[:int(len(aa)-1)])
    msg = Message()
    msg.to = to
    msg.text = "「Mention」\n"+bb
    msg.contentMetadata = {'MENTION':'{"MENTIONEES":['+aa+']}','EMTVER':'4'}
    #print msg
    try:
         ar1.sendMessage(msg)
    except Exception as error:
        print error
def summon(to, nama):
    aa = ""
    bb = ""
    strt = int(14)
    akh = int(14)
    nm = nama
    for mm in nm:
      akh = akh + 2
      aa += """{"S":"""+json.dumps(str(strt))+""","E":"""+json.dumps(str(akh))+""","M":"""+json.dumps(mm)+"},"""
      strt = strt + 6
      akh = akh + 4
      bb += "\xe2\x95\xa0 @x \n"
    aa = (aa[:int(len(aa)-1)])
    msg = Message()
    msg.to = to
    msg.text = "\xe2\x95\x94\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\n"+bb+"\xe2\x95\x9a\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90"
    msg.contentMetadata ={"MENTION":'{"MENTIONEES":['+aa+']}','EMTVER':'4'}
    print "[Command] Tag All"
    try:
       ar1.sendMessage(msg)
    except Exception as error:
       print error

def removeAllMessages(self, lastMessageId):
     return self._ar1.removeAllMessages(0, lastMessageId)
def cms(string, commands): #/XXX, >XXX, ;XXX, ^XXX, %XXX, $XXX...
    tex = ["+","@","/",">",";","^","%","$","＾","サテラ:","サテラ:","サテラ：","サテラ："] 
    for tex in tex:
      for command in commands:
        if string ==command:
          return True
     
def sendText(self, Tomid, text):
        msg = Message()
        msg.to = Tomid
        msg.text = text

def bot(op):
    try:
        if op.type == 0:
            return
        if op.type == 5:
            if wait['autoAdd'] == True:
                ar1.findAndAddContactsByMid(op.param1)
                if (wait['message'] in [""," ","\n",None]):
                    pass
                else:
                    ar1.sendText(op.param1,str(wait['message']))
        if op.type == 26:
            msg = op.message
            if msg.from_ in mimic["target"] and mimic["status"] == True and mimic["target"][msg.from_] == True:
                    text = msg.text
                    if text is not None:
                        ar1.sendText(msg.to,text)
        if op.type == 13:
            print op.param3
            if op.param3 in mid:
                if op.param2 in owner:
                    ar1.acceptGroupInvitation(op.param1)
            if op.param3 in mid2:
                if op.param2 in owner:
                    ar2.acceptGroupInvitation(op.param1)
            if op.param3 in mid3:
                if op.param2 in owner:
                    ar3.acceptGroupInvitation(op.param1)
            if op.param3 in mid4:
                if op.param2 in owner:
                    ar4.acceptGroupInvitation(op.param1)
            if op.param3 in mid5:
                if op.param2 in owner:
                    ar5.acceptGroupInvitation(op.param1)
            if op.param3 in mid:
                if op.param2 in owner:
                    ar6.acceptGroupInvitation(op.param1)
            if op.param3 in mid2:
                if op.param2 in owner:
                    ar7.acceptGroupInvitation(op.param1)
            if op.param3 in mid3:
                if op.param2 in owner:
                    ar8.acceptGroupInvitation(op.param1)
            if op.param3 in mid4:
                if op.param2 in owner:
                    ar9.acceptGroupInvitation(op.param1)
            if op.param3 in mid5:
                if op.param2 in owner:
                    ar10.acceptGroupInvitation(op.param1)
                    
            if op.param3 in mid:
                if op.param2 in mid2:
                    ar1.acceptGroupInvitation(op.param1)
            if op.param3 in mid:
                if op.param2 in mid3:
                    ar1.acceptGroupInvitation(op.param1)
            if op.param3 in mid:
                if op.param2 in mid4:
                    ar1.acceptGroupInvitation(op.param1)
            if op.param3 in mid:
                if op.param2 in mid5:
                    ar1.acceptGroupInvitation(op.param1)
                    
            if op.param3 in mid2:
                if op.param2 in mid:
                    ar2.acceptGroupInvitation(op.param1)
            if op.param3 in mid2:
                if op.param2 in mid3:
                    ar2.acceptGroupInvitation(op.param1)
            if op.param3 in mid2:
                if op.param2 in mid4:
                    ar2.acceptGroupInvitation(op.param1)
            if op.param3 in mid2:
                if op.param2 in mid5:
                    ar2.acceptGroupInvitation(op.param1)
                    
            if op.param3 in mid3:
                if op.param2 in mid:
                    ar3.acceptGroupInvitation(op.param1)
            if op.param3 in mid3:
                if op.param2 in mid2:
                    ar3.acceptGroupInvitation(op.param1)
            if op.param3 in mid3:
                if op.param2 in mid4:
                    ar3.acceptGroupInvitation(op.param1)
            if op.param3 in mid3:
                if op.param2 in mid5:
                    ar3.acceptGroupInvitation(op.param1)
                    
            if op.param3 in mid4:
                if op.param2 in mid:
                    ar4.acceptGroupInvitation(op.param1)
            if op.param3 in mid4:
                if op.param2 in mid2:
                    ar4.acceptGroupInvitation(op.param1)
            if op.param3 in mid4:
                if op.param2 in mid3:
                    ar4.acceptGroupInvitation(op.param1)
            if op.param3 in mid4:
                if op.param2 in mid5:
                    ar4.acceptGroupInvitation(op.param1)
                    
            if op.param3 in mid5:
                if op.param2 in mid:
                    ar5.acceptGroupInvitation(op.param1)
            if op.param3 in mid5:
                if op.param2 in mid2:
                    ar5.acceptGroupInvitation(op.param1)
            if op.param3 in mid5:
                if op.param2 in mid3:
                    ar5.acceptGroupInvitation(op.param1)
            if op.param3 in mid5:
                if op.param2 in mid4:
                    ar5.acceptGroupInvitation(op.param1)
            
            if op.param3 in mid6:
                if op.param2 in mid2:
                    ar6.acceptGroupInvitation(op.param1)
            if op.param3 in mid:
                if op.param2 in mid3:
                    ar6.acceptGroupInvitation(op.param1)
            if op.param3 in mid:
                if op.param2 in mid4:
                    ar6.acceptGroupInvitation(op.param1)
            if op.param3 in mid:
                if op.param2 in mid5:
                    ar6.acceptGroupInvitation(op.param1)
                    
            if op.param3 in mid7:
                if op.param2 in mid:
                    ar7.acceptGroupInvitation(op.param1)
            if op.param3 in mid2:
                if op.param2 in mid3:
                    ar7.acceptGroupInvitation(op.param1)
            if op.param3 in mid2:
                if op.param2 in mid4:
                    ar7.acceptGroupInvitation(op.param1)
            if op.param3 in mid2:
                if op.param2 in mid5:
                    ar7.acceptGroupInvitation(op.param1)
                    
            if op.param3 in mid8:
                if op.param2 in mid:
                    ar8.acceptGroupInvitation(op.param1)
            if op.param3 in mid3:
                if op.param2 in mid2:
                    ar8.acceptGroupInvitation(op.param1)
            if op.param3 in mid3:
                if op.param2 in mid4:
                    ar8.acceptGroupInvitation(op.param1)
            if op.param3 in mid3:
                if op.param2 in mid5:
                    ar8.acceptGroupInvitation(op.param1)
                    
            if op.param3 in mid9:
                if op.param2 in mid:
                    ar9.acceptGroupInvitation(op.param1)
            if op.param3 in mid4:
                if op.param2 in mid2:
                    ar9.acceptGroupInvitation(op.param1)
            if op.param3 in mid4:
                if op.param2 in mid3:
                    ar9.acceptGroupInvitation(op.param1)
            if op.param3 in mid4:
                if op.param2 in mid5:
                    ar9.acceptGroupInvitation(op.param1)
                    
            if op.param3 in mid10:
                if op.param2 in mid:
                    ar10.acceptGroupInvitation(op.param1)
            if op.param3 in mid5:
                if op.param2 in mid2:
                    ar10.acceptGroupInvitation(op.param1)
            if op.param3 in mid5:
                if op.param2 in mid3:
                    ar10.acceptGroupInvitation(op.param1)
            if op.param3 in mid5:
                if op.param2 in mid4:
                    ar10.acceptGroupInvitation(op.param1)
                    
        if op.type == 13:
            if mid in op.param3:
              if wait['autoJoin'] == True:
                if op.param2 in Bots or owner:
                  ar1.acceptGroupInvitation(op.param1)
                else:
                  ar1.rejectGroupInvitation(op.param1)
              else:
                print "autoJoin is Off"
                
            if mid2 in op.param3:
              if wait['autoJoin'] == True:
                if op.param2 in Bots or owner:
                  ar2.acceptGroupInvitation(op.param1)
                else:
                  ar2.rejectGroupInvitation(op.param1)
              else:
                print "autoJoin is Off"
                
            if mid3 in op.param3:
              if wait['autoJoin'] == True:
                if op.param2 in Bots or owner:
                  ar3.acceptGroupInvitation(op.param1)
                else:
                  ar3.rejectGroupInvitation(op.param1)
              else:
                print "autoJoin is Off"
                
            if mid4 in op.param3:
              if wait['autoJoin'] == True:
                if op.param2 in Bots or owner:
                  ar4.acceptGroupInvitation(op.param1)
                else:
                  ar4.rejectGroupInvitation(op.param1)
              else:
                print "autoJoin is Off"
                
            if mid5 in op.param3:
              if wait['autoJoin'] == True:
                if op.param2 in Bots or owner:
                  ar5.acceptGroupInvitation(op.param1)
                else:
                  ar5.rejectGroupInvitation(op.param1)
              else:
                print "autoJoin is Off"
                
            if mid6 in op.param3:
              if wait['autoJoin'] == True:
                if op.param2 in Bots or owner:
                  ar6.acceptGroupInvitation(op.param1)
                else:
                  ar6.rejectGroupInvitation(op.param1)
              else:
                print "autoJoin is Off"
                
            if mid7 in op.param3:
              if wait['autoJoin'] == True:
                if op.param2 in Bots or owner:
                  ar7.acceptGroupInvitation(op.param1)
                else:
                  ar7.rejectGroupInvitation(op.param1)
              else:
                print "autoJoin is Off"
                
            if mid8 in op.param3:
              if wait['autoJoin'] == True:
                if op.param2 in Bots or owner:
                  ar8.acceptGroupInvitation(op.param1)
                else:
                  ar8.rejectGroupInvitation(op.param1)
              else:
                print "autoJoin is Off"
                
            if mid9 in op.param3:
              if wait['autoJoin'] == True:
                if op.param2 in Bots or owner:
                  ar9.acceptGroupInvitation(op.param1)
                else:
                  ar9.rejectGroupInvitation(op.param1)
              else:
                print "autoJoin is Off"
                
            if mid10 in op.param3:
              if wait['autoJoin'] == True:
                if op.param2 in Bots or owner:
                  ar10.acceptGroupInvitation(op.param1)
                else:
                  ar10.rejectGroupInvitation(op.param1)
              else:
                print "autoJoin is Off"
                
        if op.type == 19: #bot Ke Kick
          if op.param2 in Bots:
            pass
          if op.param2 in admin:
            pass
          else:
            if op.param3 in mid:
              if op.param2 not in Bots or admin:
                try:
                  G = ar2.getGroup(op.param1)
                  G = ar3.getGroup(op.param1)
                  ar2.kickoutFromGroup(op.param1,[op.param2])
                  G.preventJoinByTicket = False
                  ar3.updateGroup(G)
                  Ticket = ar3.reissueGroupTicket(op.param1)
                  ar1.acceptGroupInvitationByTicket(op.param1,Ticket)
                  time.sleep(0.01)
                  G.preventJoinByTicket = True
                  ar1.updateGroup(G)
                  wait["blacklist"][op.param2] = True
                  f=codecs.open('st2__b.json','w','utf-8')
                  json.dump(wait["blacklist"], f, sort_keys=True, indent=4,ensure_ascii=False)
                except:
                  G = random.choice(KAC).getGroup(op.param1) #Sanji Bertindak
                  random.choice(KAC).kickoutFromGroup(op.param1,[op.param2])
                  G.preventJoinByTicket = False
                  random.choice(KAC).updateGroup(G)
                  Ticket = random.choice(KAC).reissueGroupTicket(op.param1)
                  ar1.acceptGroupInvitationByTicket(op.param1,Ticket)
                  time.sleep(0.01)
                  G.preventJoinByTicket = True
                  random.choice(KAC).updateGroup(G)
                  wait["blacklist"][op.param2] = True
                  f=codecs.open('st2__b.json','w','utf-8')
                  json.dump(wait["blacklist"], f, sort_keys=True, indent=4,ensure_ascii=False)
                  
            if op.param3 in mid2:
              if op.param2 not in Bots or admin:
                try:
                  G = ar3.getGroup(op.param1)
                  G = ar4.getGroup(op.param1)
                  ar3.kickoutFromGroup(op.param1,[op.param2])
                  G.preventJoinByTicket = False
                  ar4.updateGroup(G)
                  Ticket = ar4.reissueGroupTicket(op.param1)
                  ar2.acceptGroupInvitationByTicket(op.param1,Ticket)
                  time.sleep(0.01)
                  G.preventJoinByTicket = True
                  ar2.updateGroup(G)
                  wait["blacklist"][op.param2] = True
                  f=codecs.open('st2__b.json','w','utf-8')
                  json.dump(wait["blacklist"], f, sort_keys=True, indent=4,ensure_ascii=False)
                except:
                  G = random.choice(KAC).getGroup(op.param1) #Sanji Bertindak
                  random.choice(KAC).kickoutFromGroup(op.param1,[op.param2])
                  G.preventJoinByTicket = False
                  random.choice(KAC).updateGroup(G)
                  Ticket = random.choice(KAC).reissueGroupTicket(op.param1)
                  ar2.acceptGroupInvitationByTicket(op.param1,Ticket)
                  time.sleep(0.01)
                  G.preventJoinByTicket = True
                  random.choice(KAC).updateGroup(G)
                  wait["blacklist"][op.param2] = True
                  f=codecs.open('st2__b.json','w','utf-8')
                  json.dump(wait["blacklist"], f, sort_keys=True, indent=4,ensure_ascii=False)
                  
            if op.param3 in mid3:
              if op.param2 not in Bots or admin:
                try:
                  G = ar4.getGroup(op.param1)
                  G = ar5.getGroup(op.param1)
                  ar4.kickoutFromGroup(op.param1,[op.param2])
                  G.preventJoinByTicket = False
                  ar5.updateGroup(G)
                  Ticket = ar5.reissueGroupTicket(op.param1)
                  ar3.acceptGroupInvitationByTicket(op.param1,Ticket)
                  time.sleep(0.01)
                  G.preventJoinByTicket = True
                  ar3.updateGroup(G)
                  wait["blacklist"][op.param2] = True
                  f=codecs.open('st2__b.json','w','utf-8')
                  json.dump(wait["blacklist"], f, sort_keys=True, indent=4,ensure_ascii=False)
                except:
                  G = random.choice(KAC).getGroup(op.param1) #Sanji Bertindak
                  random.choice(KAC).kickoutFromGroup(op.param1,[op.param2])
                  G.preventJoinByTicket = False
                  random.choice(KAC).updateGroup(G)
                  Ticket = random.choice(KAC).reissueGroupTicket(op.param1)
                  ar3.acceptGroupInvitationByTicket(op.param1,Ticket)
                  time.sleep(0.01)
                  G.preventJoinByTicket = True
                  random.choice(KAC).updateGroup(G)
                  wait["blacklist"][op.param2] = True
                  f=codecs.open('st2__b.json','w','utf-8')
                  json.dump(wait["blacklist"], f, sort_keys=True, indent=4,ensure_ascii=False)
                  
            if op.param3 in mid4:
              if op.param2 not in Bots or admin:
                try:
                  G = ar5.getGroup(op.param1)
                  G = ar1.getGroup(op.param1)
                  ar5.kickoutFromGroup(op.param1,[op.param2])
                  G.preventJoinByTicket = False
                  ar1.updateGroup(G)
                  Ticket = ar1.reissueGroupTicket(op.param1)
                  ar4.acceptGroupInvitationByTicket(op.param1,Ticket)
                  time.sleep(0.01)
                  G.preventJoinByTicket = True
                  ar4.updateGroup(G)
                  wait["blacklist"][op.param2] = True
                  f=codecs.open('st2__b.json','w','utf-8')
                  json.dump(wait["blacklist"], f, sort_keys=True, indent=4,ensure_ascii=False)
                except:
                  G = random.choice(KAC).getGroup(op.param1) #Sanji Bertindak
                  random.choice(KAC).kickoutFromGroup(op.param1,[op.param2])
                  G.preventJoinByTicket = False
                  random.choice(KAC).updateGroup(G)
                  Ticket = random.choice(KAC).reissueGroupTicket(op.param1)
                  ar4.acceptGroupInvitationByTicket(op.param1,Ticket)
                  time.sleep(0.01)
                  G.preventJoinByTicket = True
                  random.choice(KAC).updateGroup(G)
                  wait["blacklist"][op.param2] = True
                  f=codecs.open('st2__b.json','w','utf-8')
                  json.dump(wait["blacklist"], f, sort_keys=True, indent=4,ensure_ascii=False)
                  
            if op.param3 in mid5:
              if op.param2 not in Bots or admin:
                try:
                  G = ar1.getGroup(op.param1)
                  G = ar2.getGroup(op.param1)
                  ar2.kickoutFromGroup(op.param1,[op.param2])
                  G.preventJoinByTicket = False
                  ar1.updateGroup(G)
                  Ticket = ar1.reissueGroupTicket(op.param1)
                  ar5.acceptGroupInvitationByTicket(op.param1,Ticket)
                  time.sleep(0.01)
                  G.preventJoinByTicket = True
                  ar5.updateGroup(G)
                  wait["blacklist"][op.param2] = True
                  f=codecs.open('st2__b.json','w','utf-8')
                  json.dump(wait["blacklist"], f, sort_keys=True, indent=4,ensure_ascii=False)
                except:
                  G = random.choice(KAC).getGroup(op.param1) #Sanji Bertindak
                  random.choice(KAC).kickoutFromGroup(op.param1,[op.param2])
                  G.preventJoinByTicket = False
                  random.choice(KAC).updateGroup(G)
                  Ticket = random.choice(KAC).reissueGroupTicket(op.param1)
                  ar5.acceptGroupInvitationByTicket(op.param1,Ticket)
                  time.sleep(0.01)
                  G.preventJoinByTicket = True
                  random.choice(KAC).updateGroup(G)
                  wait["blacklist"][op.param2] = True
                  f=codecs.open('st2__b.json','w','utf-8')
                  json.dump(wait["blacklist"], f, sort_keys=True, indent=4,ensure_ascii=False)
                  
            if op.param3 in mid6:
              if op.param2 not in Bots or admin:
                try:
                  G = ar1.getGroup(op.param1)
                  G = ar2.getGroup(op.param1)
                  ar2.kickoutFromGroup(op.param1,[op.param2])
                  G.preventJoinByTicket = False
                  ar1.updateGroup(G)
                  Ticket = ar1.reissueGroupTicket(op.param1)
                  ar6.acceptGroupInvitationByTicket(op.param1,Ticket)
                  time.sleep(0.01)
                  G.preventJoinByTicket = True
                  ar5.updateGroup(G)
                  wait["blacklist"][op.param2] = True
                  f=codecs.open('st2__b.json','w','utf-8')
                  json.dump(wait["blacklist"], f, sort_keys=True, indent=4,ensure_ascii=False)
                except:
                  G = random.choice(KAC).getGroup(op.param1) #Sanji Bertindak
                  random.choice(KAC).kickoutFromGroup(op.param1,[op.param2])
                  G.preventJoinByTicket = False
                  random.choice(KAC).updateGroup(G)
                  Ticket = random.choice(KAC).reissueGroupTicket(op.param1)
                  ar6.acceptGroupInvitationByTicket(op.param1,Ticket)
                  time.sleep(0.01)
                  G.preventJoinByTicket = True
                  random.choice(KAC).updateGroup(G)
                  wait["blacklist"][op.param2] = True
                  f=codecs.open('st2__b.json','w','utf-8')
                  json.dump(wait["blacklist"], f, sort_keys=True, indent=4,ensure_ascii=False)
                  
            if op.param3 in mid7:
              if op.param2 not in Bots or admin:
                try:
                  G = ar4.getGroup(op.param1)
                  G = ar3.getGroup(op.param1)
                  ar1.kickoutFromGroup(op.param1,[op.param2])
                  G.preventJoinByTicket = False
                  ar4.updateGroup(G)
                  Ticket = ar4.reissueGroupTicket(op.param1)
                  ar7.acceptGroupInvitationByTicket(op.param1,Ticket)
                  time.sleep(0.01)
                  G.preventJoinByTicket = True
                  ar5.updateGroup(G)
                  wait["blacklist"][op.param2] = True
                  f=codecs.open('st2__b.json','w','utf-8')
                  json.dump(wait["blacklist"], f, sort_keys=True, indent=4,ensure_ascii=False)
                except:
                  G = random.choice(KAC).getGroup(op.param1) #Sanji Bertindak
                  random.choice(KAC).kickoutFromGroup(op.param1,[op.param2])
                  G.preventJoinByTicket = False
                  random.choice(KAC).updateGroup(G)
                  Ticket = random.choice(KAC).reissueGroupTicket(op.param1)
                  ar7.acceptGroupInvitationByTicket(op.param1,Ticket)
                  time.sleep(0.01)
                  G.preventJoinByTicket = True
                  random.choice(KAC).updateGroup(G)
                  wait["blacklist"][op.param2] = True
                  f=codecs.open('st2__b.json','w','utf-8')
                  json.dump(wait["blacklist"], f, sort_keys=True, indent=4,ensure_ascii=False)
                  
            if op.param3 in mid8:
              if op.param2 not in Bots or admin:
                try:
                  G = ar3.getGroup(op.param1)
                  G = ar1.getGroup(op.param1)
                  ar5.kickoutFromGroup(op.param1,[op.param2])
                  G.preventJoinByTicket = False
                  ar4.updateGroup(G)
                  Ticket = ar1.reissueGroupTicket(op.param1)
                  ar8.acceptGroupInvitationByTicket(op.param1,Ticket)
                  time.sleep(0.01)
                  G.preventJoinByTicket = True
                  ar6.updateGroup(G)
                  wait["blacklist"][op.param2] = True
                  f=codecs.open('st2__b.json','w','utf-8')
                  json.dump(wait["blacklist"], f, sort_keys=True, indent=4,ensure_ascii=False)
                except:
                  G = random.choice(KAC).getGroup(op.param1) #Sanji Bertindak
                  random.choice(KAC).kickoutFromGroup(op.param1,[op.param2])
                  G.preventJoinByTicket = False
                  random.choice(KAC).updateGroup(G)
                  Ticket = random.choice(KAC).reissueGroupTicket(op.param1)
                  ar8.acceptGroupInvitationByTicket(op.param1,Ticket)
                  time.sleep(0.01)
                  G.preventJoinByTicket = True
                  random.choice(KAC).updateGroup(G)
                  wait["blacklist"][op.param2] = True
                  f=codecs.open('st2__b.json','w','utf-8')
                  json.dump(wait["blacklist"], f, sort_keys=True, indent=4,ensure_ascii=False)
                  
            if op.param3 in mid9:
              if op.param2 not in Bots or admin:
                try:
                  G = ar6.getGroup(op.param1)
                  G = ar7.getGroup(op.param1)
                  ar3.kickoutFromGroup(op.param1,[op.param2])
                  G.preventJoinByTicket = False
                  ar6.updateGroup(G)
                  Ticket = ar1.reissueGroupTicket(op.param1)
                  ar9.acceptGroupInvitationByTicket(op.param1,Ticket)
                  time.sleep(0.01)
                  G.preventJoinByTicket = True
                  ar1.updateGroup(G)
                  wait["blacklist"][op.param2] = True
                  f=codecs.open('st2__b.json','w','utf-8')
                  json.dump(wait["blacklist"], f, sort_keys=True, indent=4,ensure_ascii=False)
                except:
                  G = random.choice(KAC).getGroup(op.param1) #Sanji Bertindak
                  random.choice(KAC).kickoutFromGroup(op.param1,[op.param2])
                  G.preventJoinByTicket = False
                  random.choice(KAC).updateGroup(G)
                  Ticket = random.choice(KAC).reissueGroupTicket(op.param1)
                  ar9.acceptGroupInvitationByTicket(op.param1,Ticket)
                  time.sleep(0.01)
                  G.preventJoinByTicket = True
                  random.choice(KAC).updateGroup(G)
                  wait["blacklist"][op.param2] = True
                  f=codecs.open('st2__b.json','w','utf-8')
                  json.dump(wait["blacklist"], f, sort_keys=True, indent=4,ensure_ascii=False)
                  
            if op.param3 in mid10:
              if op.param2 not in Bots or admin:
                try:
                  G = ar6.getGroup(op.param1)
                  G = ar7.getGroup(op.param1)
                  ar9.kickoutFromGroup(op.param1,[op.param2])
                  G.preventJoinByTicket = False
                  ar8.updateGroup(G)
                  Ticket = ar5.reissueGroupTicket(op.param1)
                  ar10.acceptGroupInvitationByTicket(op.param1,Ticket)
                  time.sleep(0.01)
                  G.preventJoinByTicket = True
                  ar2.updateGroup(G)
                  wait["blacklist"][op.param2] = True
                  f=codecs.open('st2__b.json','w','utf-8')
                  json.dump(wait["blacklist"], f, sort_keys=True, indent=4,ensure_ascii=False)
                except:
                  G = random.choice(KAC).getGroup(op.param1) #Sanji Bertindak
                  random.choice(KAC).kickoutFromGroup(op.param1,[op.param2])
                  G.preventJoinByTicket = False
                  random.choice(KAC).updateGroup(G)
                  Ticket = random.choice(KAC).reissueGroupTicket(op.param1)
                  ar10.acceptGroupInvitationByTicket(op.param1,Ticket)
                  time.sleep(0.01)
                  G.preventJoinByTicket = True
                  random.choice(KAC).updateGroup(G)
                  wait["blacklist"][op.param2] = True
                  f=codecs.open('st2__b.json','w','utf-8')
                  json.dump(wait["blacklist"], f, sort_keys=True, indent=4,ensure_ascii=False)
                  
            if op.param3 in admin:
              if op.param2 not in Bots:
                try:
                  ar1.kickoutFromGroup(op.param1,[op.param2])
                  ar1.inviteIntoGroup(op.param1,[op.param3])
                  wait["blacklist"][op.param2] = True
                except:
                  try:
                    ar1.kickoutFromGroup(op.param1,[op.param2])
                    ar1.inviteIntoGroup(op.param1,[admin])
                    wait["blacklist"][op.param2] = True
                  except:
                    try:
                      random.choice(KAC).kickoutFromGroup(op.param1,[op.param2])
                      random.choice(KAC).inviteIntoGroup(op.param1,[op.param3])
                      wait["blacklist"][op.param2] = True
                    except:
                      random.choice(KAC).kickoutFromGroup(op.param1,[op.param2])
                      random.choice(KAC).inviteIntoGroup(op.param1,[admin])
                      wait["blacklist"][op.param2] = True

            if op.param3 in admin or Bots:
                if op.param2 in admin or Bots:
                    try:
                        ar1.inviteIntoGroup(op.param1,admin)
                    except:
                        random.choice(KAC).inviteIntoGroup(op.param1,[admin])

        if op.type == 19:
            if mid in op.param3:
                wait["blacklist"][op.param2] = True
        if op.type == 22:
            if wait['leaveRoom'] == True:
                ar1.leaveRoom(op.param1)
                ar2.leaveRoom(op.param1)
                ar3.leaveRoom(op.param1)
                ar4.leaveRoom(op.param1)
                ar5.leaveRoom(op.param1)
                ar6.leaveRoom(op.param1)
                ar7.leaveRoom(op.param1)
                ar8.leaveRoom(op.param1)
                ar9.leaveRoom(op.param1)
                ar10.leaveRoom(op.param1)
        if op.type == 24:
            if wait['leaveRoom'] == True:
                ar1.leaveRoom(op.param1)
                ar2.leaveRoom(op.param1)
                ar3.leaveRoom(op.param1)
                ar4.leaveRoom(op.param1)
                ar5.leaveRoom(op.param1)
                ar6.leaveRoom(op.param1)
                ar7.leaveRoom(op.param1)
                ar8.leaveRoom(op.param1)
                ar9.leaveRoom(op.param1)
                ar10.leaveRoom(op.param1)
        if op.type == 26:
            msg = op.message
            if msg.toType == 0:
                msg.to = msg.from_
                if msg.from_ == mid:
                    if "join:" in msg.text:
                        list_ = msg.text.split(":")
                        try:
                            ar1.acceptGroupInvitationByTicket(list_[1],list_[2])
                            G = ar1.getGroup(list_[1])
                            G.preventJoinByTicket = True
                            ar1.updateGroup(G)
                        except:
                            ar1.sendText(msg.to,"error")
            if msg.toType == 1:
                if wait['leaveRoom'] == True:
                    ar1.leaveRoom(msg.to)
            if msg.contentType == 16:
                url = msg.contentMetadata["postEndUrl"]
                ar1.like(url[25:58], url[66:], likeType=1001)
            
            if msg.contentType == 13:
                if wait['invite'] == True:
                     _name = msg.contentMetadata["displayName"]
                     invite = msg.contentMetadata["mid"]
                     groups = ar1.getGroup(msg.to)
                     pending = groups.invitee
                     targets = []
                     for s in groups.members:
                         if _name in s.displayName:
                             ar1.sendText(msg.to, _name + " Berada DiGrup Ini")
                         else:
                             targets.append(invite)
                     if targets == []:
                         pass
                     else:
                         for target in targets:
                             try:
                                 ar1.findAndAddContactsByMid(target)
                                 ar1.inviteIntoGroup(msg.to,[target])
                                 ar1.sendText(msg.to,"Invite " + _name)
                                 wait['invite'] = False
                                 break                              
                             except:             
                                      ar1.sendText(msg.to,"Error")
                                      wait['invite'] = False
                                      break

        if op.type == 26:
            msg = op.message
            if msg.contentType == 13:
                if wait["winvite"] == True:
                    if msg.from_ in admin or owner:
                        _name = msg.contentMetadata["displayName"]
                        invite = msg.contentMetadata["mid"]
                        groups = ar1.getGroup(msg.to)
                        pending = groups.invitee
                        targets = []
                        for s in groups.members:
                            if _name in s.displayName:
                                ar1.sendText(msg.to,"-> " + _name + " ada di room ini")
                                break
                            elif invite in wait["blacklist"]:
                                ar1.sendText(msg.to,"Maaf, " + _name + " kena Blacklist")
                                ar1.sendText(msg.to,"hubungi owner kami ya !, \n➡Unban: " + invite)
                                break
                            else:
                                targets.append(invite)
                        if targets == []:
                            pass
                        else:
                            for target in targets:
                                try:
                                    ar1.findAndAddContactsByMid(target)
                                    ar1.inviteIntoGroup(msg.to,[target])
                                    ar1.sendText(msg.to,"Selesai di Invite : \n➡" + _name)
                                    wait["winvite"] = False
                                    break
                                except:
                                    try:
                                        ar1.findAndAddContactsByMid(invite)
                                        ar1.inviteIntoGroup(op.param1,[invite])
                                        wait["winvite"] = False
                                    except:
                                        ar1.sendText(msg.to,"Negative, Error detected")
                                        wait["winvite"] = False
                                        break

                    if msg.from_ in admin or owner:
                        _name = msg.contentMetadata["displayName"]
                        invite = msg.contentMetadata["mid"]
                        groups = ar2.getGroup(msg.to)
                        pending = groups.invitee
                        targets = []
                        for s in groups.members:
                            if _name in s.displayName:
                                ar2.sendText(msg.to,"-> " + _name + " ada di room ini")
                                break
                            elif invite in wait["blacklist"]:
                                ar2.sendText(msg.to,"Maaf, " + _name + " kena Blacklist")
                                ar2.sendText(msg.to,"hubungi owner kami ya !, \n➡Unban: " + invite)
                                break
                            else:
                                targets.append(invite)
                        if targets == []:
                            pass
                        else:
                            for target in targets:
                                try:
                                    ar2.findAndAddContactsByMid(target)
                                    ar2.inviteIntoGroup(msg.to,[target])
                                    ar2.sendText(msg.to,"Selesai di Invite : \n➡" + _name)
                                    wait["winvite"] = False
                                    break
                                except:
                                    try:
                                        ar2.findAndAddContactsByMid(invite)
                                        ar2.inviteIntoGroup(op.param1,[invite])
                                        wait["winvite"] = False
                                    except:
                                        ar2.sendText(msg.to,"Negative, Error detected")
                                        wait["winvite"] = False
                                        break
        if op.type == 26:
            msg = op.message
            if msg.contentType == 13:
                if wait["wblack"] == True:
                    if msg.contentMetadata["mid"] in wait["commentBlack"]:
                        ar1.sendText(msg.to,"In Blacklist")
                        wait["wblack"] = False
                    else:
                        wait["commentBlack"][msg.contentMetadata["mid"]] = True
                        wait["wblack"] = False
                        ar1.sendText(msg.to,"Nothing")
                elif wait["dblack"] == True:
                    if msg.contentMetadata["mid"] in wait["commentBlack"]:
                        del wait["commentBlack"][msg.contentMetadata["mid"]]
                        ar1.sendText(msg.to,"Done")
                        wait["dblack"] = False
                    else:
                        wait["dblack"] = False
                        ar1.sendText(msg.to,"Not in Blacklist")
                elif wait["wblacklist"] == True:
                    if msg.contentMetadata["mid"] in wait["blacklist"]:
                        ar1.sendText(msg.to,"In Blacklist")
                        wait["wblacklist"] = False
                    else:
                        wait["blacklist"][msg.contentMetadata["mid"]] = True
                        wait["wblacklist"] = False
                        ar1.sendText(msg.to,"Done")
                elif wait["dblacklist"] == True:
                    if msg.contentMetadata["mid"] in wait["blacklist"]:
                        del wait["blacklist"][msg.contentMetadata["mid"]]
                        ar1.sendText(msg.to,"Done")
                        wait["dblacklist"] = False
                    else:
                        wait["dblacklist"] = False
                        ar1.sendText(msg.to,"Done")
                elif wait['contact'] == True:
                    msg.contentType = 0
                    ar1.sendText(msg.to,msg.contentMetadata["mid"])
                    if 'displayName' in msg.contentMetadata:
                        contact = ar1.getContact(msg.contentMetadata["mid"])
                        try:
                            cu = ar1.channel.getCover(msg.contentMetadata["mid"])
                        except:
                            cu = ""
                        ar1.sendText(msg.to,"[displayName]:\n" + msg.contentMetadata["displayName"] + "\n[mid]:\n" + msg.contentMetadata["mid"] + "\n[statusMessage]:\n" + contact.statusMessage + "\n[pictureStatus]:\nhttp://dl.profile.line-cdn.net/" + contact.pictureStatus + "\n[coverURL]:\n" + str(cu))
                    else:
                        contact = ar1.getContact(msg.contentMetadata["mid"])
                        try:
                            cu = ar1.channel.getCover(msg.contentMetadata["mid"])
                        except:
                            cu = ""
                        ar1.sendText(msg.to,"[displayName]:\n" + contact.displayName + "\n[mid]:\n" + msg.contentMetadata["mid"] + "\n[statusMessage]:\n" + contact.statusMessage + "\n[pictureStatus]:\nhttp://dl.profile.line-cdn.net/" + contact.pictureStatus + "\n[coverURL]:\n" + str(cu))
            elif msg.contentType == 16:
                if wait['timeline'] == True:
                    msg.contentType = 0
                    if wait["lang"] == "JP":
                        msg.text = "menempatkan URL\n" + msg.contentMetadata["postEndUrl"]
                    else:
                        msg.text = msg.contentMetadata["postEndUrl"]
                    ar1.sendText(msg.to,msg.text)
            elif msg.text is None:
                return
            elif msg.text.lower() == 'help':
                if msg.from_ in admin:
                    if wait["lang"] == "JP":
                        ar1.sendText(msg.to,helpmsg)
                    else:
                        ar1.sendText(msg.to,helpmsg)
            elif msg.text.lower() == 'keybot':
                if msg.from_ in admin:
                    if wait["lang"] == "JP":
                        ar1.sendText(msg.to,keymsg)
                    else:
                        ar1.sendText(msg.to,keymsg)
            elif msg.text.lower() == 'keypro':
                if msg.from_ in admin:
                    if wait["lang"] == "JP":
                        ar1.sendText(msg.to,helppro)
                    else:
                        ar1.sendText(msg.to,helppro)
            elif msg.text.lower() == 'keyself':
                if msg.from_ in admin:
                    if wait["lang"] == "JP":
                        ar1.sendText(msg.to,helpself)
                    else:
                        ar1.sendText(msg.to,helpself)
            elif msg.text.lower() == 'keygrup':
                if msg.from_ in admin:
                    if wait["lang"] == "JP":
                        ar1.sendText(msg.to,helpgrup)
                    else:
                        ar1.sendText(msg.to,helpgrup)
            elif msg.text.lower() == 'keyset':
                if msg.from_ in admin:
                    if wait["lang"] == "JP":
                        ar1.sendText(msg.to,helpset)
                    else:
                        ar1.sendText(msg.to,helpset)
            elif msg.text.lower() == 'keytran':
                if msg.from_ in admin:
                    if wait["lang"] == "JP":
                        ar1.sendText(msg.to,helptranslate)
                    else:
                        ar1.sendText(msg.to,helptranslate)
            elif msg.text.lower() == 'keyrhs':
                if msg.from_ in admin:
                    if wait["lang"] == "JP":
                        ar1.sendText(msg.to,helprhs)
                    else:
                        ar1.sendText(msg.to,helprhs)                        
#======================== FOR COMMAND MODE ON STARTING ==========================#
            elif msg.text.lower() == 'protect on':
                if wait["protect"] == True:
                    if wait["lang"] == "JP":
                        ar1.sendText(msg.to,"Protection set to on")
                    else:
                        ar1.sendText(msg.to,"Protection already on")
                else:
                    wait["protect"] = True
                    if wait["lang"] == "JP":
                        ar1.sendText(msg.to,"Protection set to on")
                    else:
                        ar1.sendText(msg.to,"Protection already on")
            elif msg.text.lower() == 'qr on':
                if wait["linkprotect"] == True:
                    if wait["lang"] == "JP":
                        ar1.sendText(msg.to,"Protection Qr set to on")
                    else:
                        ar1.sendText(msg.to,"Protection Qr already on")
                else:
                    wait["linkprotect"] = True
                    if wait["lang"] == "JP":
                        ar1.sendText(msg.to,"Protection Qr set to on")
                    else:
                        ar1.sendText(msg.to,"Protection Qr already on")
            elif msg.text.lower() == 'invit on':
                if wait["inviteprotect"] == True:
                    if wait["lang"] == "JP":
                        ar1.sendText(msg.to,"Protection Invite set to on")
                    else:
                        ar1.sendText(msg.to,"Protection Invite already on")
                else:
                    wait["inviteprotect"] = True
                    if wait["lang"] == "JP":
                        ar1.sendText(msg.to,"Protection Invite set to on")
                    else:
                        ar1.sendText(msg.to,"Protection Invite already on")
            elif msg.text.lower() == 'cancel on':
                if wait["cancelprotect"] == True:
                    if wait["lang"] == "JP":
                        ar1.sendText(msg.to,"Cancel Protection set to on")
                    else:
                        ar1.sendText(msg.to,"Cancel Protection already on")
                else:
                    wait["cancelprotect"] = True
                    if wait["lang"] == "JP":
                        ar1.sendText(msg.to,"Cancel Protection set to on")
                    else:
                        ar1.sendText(msg.to,"Cancel Protection already on")
            elif msg.text.lower() == 'protect off':
                if wait["protect"] == False:
                    if wait["lang"] == "JP":
                        ar1.sendText(msg.to,"Protection set to off")
                    else:
                        ar1.sendText(msg.to,"Protection already off")
                else:
                    wait["protect"] = False
                    if wait["lang"] == "JP":
                        ar1.sendText(msg.to,"Protection set to off")
                    else:
                        ar1.sendText(msg.to,"Protection already off")
            elif msg.text.lower() == 'qr off':
                if wait["linkprotect"] == False:
                    if wait["lang"] == "JP":
                        ar1.sendText(msg.to,"Protection Qr set to off")
                    else:
                        ar1.sendText(msg.to,"Protection Qr already off")
                else:
                    wait["linkprotect"] = False
                    if wait["lang"] == "JP":
                        ar1.sendText(msg.to,"Protection Qr set to off")
                    else:
                        ar1.sendText(msg.to,"Protection Qr already off")
            elif msg.text.lower() == 'invit off':
                if wait["inviteprotect"] == False:
                    if wait["lang"] == "JP":
                        ar1.sendText(msg.to,"Protection Invite set to off")
                    else:
                        ar1.sendText(msg.to,"Protection Invite already off")
                else:
                    wait["inviteprotect"] = False
                    if wait["lang"] == "JP":
                        ar1.sendText(msg.to,"Protection Invite set to off")
                    else:
                        ar1.sendText(msg.to,"Protection Invite already off")
            elif msg.text.lower() == 'cancel off':
                if wait["cancelprotect"] == False:
                    if wait["lang"] == "JP":
                        ar1.sendText(msg.to,"Cancel Protection Invite set to off")
                    else:
                        ar1.sendText(msg.to,"Cancel Protection Invite already off")
                else:
                    wait["cancelprotect"] = False
                    if wait["lang"] == "JP":
                        ar1.sendText(msg.to,"Cancel Protection Invite set to off")
                    else:
                        ar1.sendText(msg.to,"Cancel Protection Invite already off")
            elif msg.text in ["Thekick on","thekick on"]:
              if msg.from_ in owner:
                if wait["Protectjoin"] == True:
                    if wait["lang"] == "JP":
                        ar1.sendText(msg.to,"Kick Join Group Enable")
                    else:
                        ar1.sendText(msg.to,"done")
                else:
                    wait["Protectjoin"] = True
                    if wait["lang"] == "JP":
                        ar1.sendText(msg.to,"Kick Join Group Enable")
                    else:
                        ar1.sendText(msg.to,"done")
            elif msg.text in ["Thekick off","thekick off"]:
              if msg.from_ in owner:
                if wait["Protectjoin"] == False:
                    if wait["lang"] == "JP":
                        ar1.sendText(msg.to,"Kick Join Group Disable")
                    else:
                        ar1.sendText(msg.to,"done")
                else:
                    wait["Protectjoin"] = False
                    if wait["lang"] == "JP":
                        ar1.sendText(msg.to,"Kick Join Group Disable")
                    else:
                        ar1.sendText(msg.to,"done")
            elif msg.text in ["Guest on","guest on"]:
              if msg.from_ in admin:
                if wait["Protectguest"] == True:
                    if wait["lang"] == "JP":
                        ar1.sendText(msg.to,"Guest Stranger On")
                    else:
                        ar1.sendText(msg.to,"done")
                else:
                    wait["Protectguest"] = True
                    if wait["lang"] == "JP":
                        ar1.sendText(msg.to,"Guest Stranger On")
                    else:
                        ar1.sendText(msg.to,"done")
            elif msg.text in ["Guest off","guest off"]:
              if msg.from_ in admin:
                if wait["Protectguest"] == False:
                    if wait["lang"] == "JP":
                        ar1.sendText(msg.to,"Guest Stranger Off")
                    else:
                        ar1.sendText(msg.to,"done")
                else:
                    wait["Protectguest"] = False
                    if wait["lang"] == "JP":
                        ar1.sendText(msg.to,"Guest Stranger Off")
                    else:
                        ar1.sendText(msg.to,"done")

            elif msg.text in ["Mode on"]:
              if msg.from_ in admin:
                if wait["inviteprotect"] == True:
                    if wait["lang"] == "JP":
                        ar1.sendText(msg.to,"Ini sudah on 􀜁􀇔􏿿👈")
                    else:
                        ar1.sendText(msg.to,"Already on")
                else:
                    wait["inviteprotect"] = True
                    if wait["lang"] == "JP":
                        ar1.sendText(msg.to,"Protect invite on 􀜁􀇔􏿿")
                if wait["cancelprotect"] == True:
                    if wait["lang"] == "JP":
                        ar1.sendText(msg.to,"Ini sudah on 􀜁􀇔􏿿👈")
                    else:
                        ar1.sendText(msg.to,"Already on")
                else:
                    wait["cancelprotect"] = True
                    if wait["lang"] == "JP":
                        ar1.sendText(msg.to,"Protect cancel on 􀜁􀇔􏿿")
                if wait["protect"] == True:
                    if wait["lang"] == "JP":
                        ar1.sendText(msg.to,"Ini sudah on 􀜁􀇔􏿿👈")
                    else:
                        ar1.sendText(msg.to,"Already on")
                else:
                    wait["protect"] = True
                    if wait["lang"] == "JP":
                        ar1.sendText(msg.to,"Protect on 􀜁􀇔􏿿")
                    else:
                        ar1.sendText(msg.to,"Already on")
                if wait["linkprotect"] == True:
                    if wait["lang"] == "JP":
                        ar1.sendText(msg.to,"Ini sudah on 􀜁􀇔􏿿👈")
                    else:
                        ar1.sendText(msg.to,"Already on")
                else:
                    wait["linkprotect"] = True
                    if wait["lang"] == "JP":
                        ar1.sendText(msg.to,"Protect QR on 􀜁􀇔􏿿")
                    else:
                        ar1.sendText(msg.to,"Already on")
                if wait["Protectguest"] == True:
                    if wait["lang"] == "JP":
                        ar1.sendText(msg.to,"Ini sudah On 􀜁􀇔􏿿👈")
                    else:
                        ar1.sendText(msg.to,"Already On..")
                else:
                    wait["Protectguest"] = True
                    if wait["lang"] == "JP":
                        ar1.sendText(msg.to,"Protect Guest On.. 􀜁􀇔􏿿")
                    else:
                        ar1.sendText(msg.to,"Already On..")
                if wait["Protectjoin"] == True:
                    if wait["lang"] == "JP":
                        ar1.sendText(msg.to,"Ini sudah On 👈")
                    else:
                        ar1.sendText(msg.to,"Already off")
                else:
                    wait["Protectjoin"] = True
                    if wait["lang"] == "JP":
                        ar1.sendText(msg.to,"Protect Join Kick On 􀜁􀇔􏿿")
                    else:
                        ar1.sendText(msg.to,"Already On..")


            elif msg.text in ["Mode off"]:
              if msg.from_ in admin:
                if wait["inviteprotect"] == False:
                    if wait["lang"] == "JP":
                        ar1.sendText(msg.to,"Ini sudah off 􀜁􀇔􏿿👈")
                    else:
                        ar1.sendText(msg.to,"Already off")
                else:
                    wait["inviteprotect"] = False
                    if wait["lang"] == "JP":
                        ar1.sendText(msg.to,"Protect invite off 􀜁􀇔􏿿")
                if wait["cancelprotect"] == False:
                    if wait["lang"] == "JP":
                        ar1.sendText(msg.to,"Ini sudah off 􀜁􀇔􏿿👈")
                    else:
                        ar1.sendText(msg.to,"Already off")
                else:
                    wait["cancelprotect"] = False
                    if wait["lang"] == "JP":
                        ar1.sendText(msg.to,"Protect cancel off 􀜁􀇔􏿿")
                if wait["protect"] == False:
                    if wait["lang"] == "JP":
                        ar1.sendText(msg.to,"Ini sudah off 􀜁􀇔􏿿👈")
                    else:
                        ar1.sendText(msg.to,"Already off")
                else:
                    wait["protect"] = False
                    if wait["lang"] == "JP":
                        ar1.sendText(msg.to,"Protect off 􀜁􀇔􏿿")
                    else:
                        ar1.sendText(msg.to,"Already off")
                if wait["linkprotect"] == False:
                    if wait["lang"] == "JP":
                        ar1.sendText(msg.to,"Ini sudah off 􀜁􀇔􏿿👈")
                    else:
                        ar1.sendText(msg.to,"Already off")
                else:
                    wait["linkprotect"] = False
                    if wait["lang"] == "JP":
                        ar1.sendText(msg.to,"Protect QR off 􀜁􀇔􏿿")
                    else:
                        ar1.sendText(msg.to,"Already off")
                if wait["Protectguest"] == False:
                    if wait["lang"] == "JP":
                        ar1.sendText(msg.to,"Ini sudah off 􀜁􀇔􏿿👈")
                    else:
                        ar1.sendText(msg.to,"Already off")
                else:
                    wait["Protectguest"] = False
                    if wait["lang"] == "JP":
                        ar1.sendText(msg.to,"Protect Guest off 􀜁􀇔􏿿")
                    else:
                        ar1.sendText(msg.to,"Already off")
                if wait["Protectjoin"] == False:
                    if wait["lang"] == "JP":
                        ar1.sendText(msg.to,"Ini sudah off 􀜁􀇔􏿿👈")
                    else:
                        ar1.sendText(msg.to,"Already off")
                else:
                    wait["Protectjoin"] = False
                    if wait["lang"] == "JP":
                        ar1.sendText(msg.to,"Protect Join Kick off 􀜁􀇔􏿿")
                    else:
                        ar1.sendText(msg.to,"Already off")


#========================== FOR COMMAND BOT STARTING =============================#
            elif msg.text.lower() == 'contact on':
                if msg.from_ in admin:
                    if wait['contact'] == True:
                        if wait["lang"] == "JP":
                            ar1.sendText(msg.to,"ɕσηϯαɕϯ ςεϯ ϯσ ση")
                        else:
                            ar1.sendText(msg.to,"ɕσηϯαɕϯ ςεϯ ϯσ ση")
                    else:
                        wait['contact'] = True
                        if wait["lang"] == "JP":
                            ar1.sendText(msg.to,"ɕσηϯαɕϯ ςεϯ ϯσ ση")
                        else:
                            ar1.sendText(msg.to,"ɕσηϯαɕϯ ςεϯ ϯσ ση")
            elif msg.text.lower() == 'contact off':
                if msg.from_ in admin:
                    if wait['contact'] == False:
                        if wait["lang"] == "JP":
                            ar1.sendText(msg.to,"ɕσηϯαɕϯ ςεϯ ϯσ σƒƒ")
                        else:
                            ar1.sendText(msg.to,"ɕσηϯαɕϯ αʆɾεαδψ σƒƒ")
                    else:
                        wait['contact'] = False
                        if wait["lang"] == "JP":
                            ar1.sendText(msg.to,"ɕσηϯαɕϯ ςεϯ ϯσ σƒƒ")
                        else:
                            ar1.sendText(msg.to,"ɕσηϯαɕϯ αʆɾεαδψ σƒƒ")
            elif msg.text.lower() == 'autojoin on':
                if msg.from_ in admin:
                    if wait['autoJoin'] == True:
                        if wait["lang"] == "JP":
                            ar1.sendText(msg.to,"αυтσʝσιи ѕєт тσ σи")
                        else:
                            ar1.sendText(msg.to,"αυтσʝσιи αℓяєα∂у σи")
                    else:
                        wait['autoJoin'] = True
                        if wait["lang"] == "JP":
                            ar1.sendText(msg.to,"αυтσʝσιи ѕєт тσ σи")
                        else:
                            ar1.sendText(msg.to,"αυтσʝσιи αℓяєα∂у σи")
            elif msg.text.lower() == 'autojoin off':
                if msg.from_ in admin:
                    if wait['autoJoin'] == False:
                        if wait["lang"] == "JP":
                            ar1.sendText(msg.to,"αυтσʝσιи ѕєт тσ σff")
                        else:
                            ar1.sendText(msg.to,"αυтσʝσιи αℓяєα∂у σff")
                    else:
                        wait['autoJoin'] = False
                        if wait["lang"] == "JP":
                            ar1.sendText(msg.to,"αυтσʝσιи ѕєт тσ σff")
                        else:
                            ar1.sendText(msg.to,"αυтσʝσιи αℓяєα∂у σff")
            elif "Grup cancel:" in msg.text:
                if msg.from_ in admin:
                    try:
                        strnum = msg.text.replace("Grup cancel:","")
                        if strnum == "off":
                            wait['autoCancel']["on"] = False
                            if wait["lang"] == "JP":
                                ar1.sendText(msg.to,"Itu off undangan ditolak??\nSilakan kirim dengan menentukan jumlah orang ketika Anda menghidupkan")
                            else:
                                ar1.sendText(msg.to,"Off undangan ditolak??Sebutkan jumlah terbuka ketika Anda ingin mengirim")
                        else:
                            num =  int(strnum)
                            wait['autoCancel']["on"] = True
                            if wait["lang"] == "JP":
                                ar1.sendText(msg.to,strnum + "Kelompok berikut yang diundang akan ditolak secara otomatis")
                            else:
                                ar1.sendText(msg.to,strnum + "The team declined to create the following automatic invitation")
                    except:
                        if wait["lang"] == "JP":
                            ar1.sendText(msg.to,"Nilai tidak benar")
                        else:
                            ar1.sendText(msg.to,"Weird value")
            elif msg.text.lower() == 'autoleave on':
                if msg.from_ in admin:
                    if wait['leaveRoom'] == True:
                        if wait["lang"] == "JP":
                            ar1.sendText(msg.to,"Auto Leave room set to on")
                        else:
                            ar1.sendText(msg.to,"Auto Leave room already on")
                    else:
                        wait['leaveRoom'] = True
                        if wait["lang"] == "JP":
                            ar1.sendText(msg.to,"Auto Leave room set to on")
                        else:
                            ar1.sendText(msg.to,"Auto Leave room already on")
            elif msg.text.lower() == 'autoleave off':
                if msg.from_ in admin:
                    if wait['leaveRoom'] == False:
                        if wait["lang"] == "JP":
                            ar1.sendText(msg.to,"Auto Leave room set to off")
                        else:
                            ar1.sendText(msg.to,"Auto Leave room already off")
                    else:
                        wait['leaveRoom'] = False
                        if wait["lang"] == "JP":
                            ar1.sendText(msg.to,"Auto Leave room set to off")
                        else:
                            ar1.sendText(msg.to,"Auto Leave room already off")
            elif msg.text.lower() == 'share on':
                if msg.from_ in admin:
                    if wait['timeline'] == True:
                        if wait["lang"] == "JP":
                            ar1.sendText(msg.to,"Share set to on")
                        else:
                            ar1.sendText(msg.to,"Share already on")
                    else:
                        wait['timeline'] = True
                        if wait["lang"] == "JP":
                            ar1.sendText(msg.to,"Share set to on")
                        else:
                            ar1.sendText(msg.to,"Share already on")
            elif msg.text.lower() == 'share off':
                if msg.from_ in admin:
                    if wait['timeline'] == False:
                        if wait["lang"] == "JP":
                            ar1.sendText(msg.to,"Share set to off")
                        else:
                            ar1.sendText(msg.to,"Share already off")
                    else:
                        wait['timeline'] = False
                        if wait["lang"] == "JP":
                            ar1.sendText(msg.to,"Share set to off")
                        else:
                            ar1.sendText(msg.to,"Share already off")
            elif msg.text.lower() == "status":
                if msg.from_ in admin:
                    md = """╔═════════════\n"""
                    if wait['contact'] == True: md+="╠❂➣Contact:on [✅]\n"
                    else: md+="╠❂➣Contact:off [❌]\n"
                    if wait['autoJoin'] == True: md+="╠❂➣Auto Join:on [✅]\n"
                    else: md +="╠❂➣Auto Join:off [❌]\n"
                    if wait['autoCancel']["on"] == True:md+="╠❂➣Auto cancel:" + str(wait['autoCancel']["members"]) + "[✅]\n"
                    else: md+= "╠❂➣Group cancel:off [❌]\n"
                    if wait['leaveRoom'] == True: md+="╠❂➣Auto leave:on [✅]\n"
                    else: md+="╠❂➣Auto leave:off [❌]\n"
                    if wait['timeline'] == True: md+="╠❂➣Share:on [✅]\n"
                    else:md+="╠❂➣Share:off [❌]\n"
                    if wait['autoAdd'] == True: md+="╠❂➣Auto add:on [✅]\n"
                    else:md+="╠❂➣Auto add:off [❌]\n"
                    if wait["protect"] == True: md+="╠❂➣Protect:on [✅]\n"
                    else:md+="╠❂➣Protect:off [❌]\n"
                    if wait["linkprotect"] == True: md+="╠❂➣Link Protect:on [✅]\n"
                    else:md+="╠❂➣Link Protect:off [❌]\n"
                    if wait["inviteprotect"] == True: md+="╠❂➣Invitation Protect:on [✅]\n"
                    else:md+="╠❂➣Invitation Protect:off [❌]\n"
                    if wait["cancelprotect"] == True: md+="╠❂➣Cancel Protect:on [✅]\n"
                    else:md+="╠❂➣Cancel Protect:off [❌]\n╚═════════════"
                    ar1.sendText(msg.to,md)
            elif cms(msg.text,["creator","Creator"]):
                msg.contentType = 13
                msg.contentMetadata = {'mid': "uc721ad1f11fb7e128453ba5a27424998"}
                ar1.sendMessage(msg)
                ar1.sendText(msg.to,'❂➣ This My Creator 􀜁􀄯􏿿')
            elif msg.text.lower() == 'autoadd on':
                if msg.from_ in admin:
                    if wait['autoAdd'] == True:
                        if wait["lang"] == "JP":
                            ar1.sendText(msg.to,"Auto add set to on")
                        else:
                            ar1.sendText(msg.to,"Auto add already on")
                    else:
                        wait['autoAdd'] = True
                        if wait["lang"] == "JP":
                            ar1.sendText(msg.to,"Auto add set to on")
                        else:
                            ar1.sendText(msg.to,"Auto add already on")
            elif msg.text.lower() == 'autoadd off':
                if msg.from_ in admin:
                    if wait['autoAdd'] == False:
                        if wait["lang"] == "JP":
                            ar1.sendText(msg.to,"Auto add set to off")
                        else:
                            ar1.sendText(msg.to,"Auto add already off")
                    else:
                        wait['autoAdd'] = False
                        if wait["lang"] == "JP":
                            ar1.sendText(msg.to,"Auto add set to off")
                        else:
                            ar1.sendText(msg.to,"Auto add already off")
            elif "Pesan set:" in msg.text:
                if msg.from_ in admin:
                    wait['message'] = msg.text.replace("Pesan set:","")
                    ar1.sendText(msg.to,"We changed the message")
            elif msg.text.lower() == 'pesan cek':
                if msg.from_ in admin:
                    if wait["lang"] == "JP":
                        ar1.sendText(msg.to,"Pesan tambahan otomatis telah ditetapkan sebagai berikut \n\n" + wait['message'])
                    else:
                        ar1.sendText(msg.to,"Pesan tambahan otomatis telah ditetapkan sebagai berikut \n\n" + wait['message'])
            elif "Coment Set:" in msg.text:
                if msg.from_ in admin:
                    c = msg.text.replace("Coment Set:","")
                    if c in [""," ","\n",None]:
                        ar1.sendText(msg.to,"Merupakan string yang tidak bisa diubah")
                    else:
                        wait["comment"] = c
                        ar1.sendText(msg.to,"Ini telah diubah\n\n" + c)
            elif msg.text in ["Comment on"]:
                if msg.from_ in admin:
                    if wait["commentOn"] == True:
                        if wait["lang"] == "JP":
                            ar1.sendText(msg.to,"Aku berada di")
                        else:
                            ar1.sendText(msg.to,"To open")
                    else:
                        wait["commentOn"] = True
                        if wait["lang"] == "JP":
                            ar1.sendText(msg.to,"Comment Actived")
                        else:
                            ar1.sendText(msg.to,"Comment Has Been Active")
            elif msg.text in ["Coment off"]:
                if msg.from_ in admin:
                    if wait["commentOn"] == False:
                        if wait["lang"] == "JP":
                            ar1.sendText(msg.to,"Hal ini sudah off")
                        else:
                            ar1.sendText(msg.to,"It is already turned off")
                    else:
                        wait["commentOn"] = False
                        if wait["lang"] == "JP":
                            ar1.sendText(msg.to,"Off")
                        else:
                            ar1.sendText(msg.to,"To turn off")
            elif msg.text in ["Com","Comment"]:
                if msg.from_ in admin:
                    ar1.sendText(msg.to,"Auto komentar saat ini telah ditetapkan sebagai berikut:??\n\n" + str(wait["comment"]))
            elif msg.text in ["Com Bl"]:
                if msg.from_ in admin:
                    wait["dblack"] = True
                    ar1.sendText(msg.to,"Please send contacts from the person you want to add to the blacklist")
            elif msg.text in ["Com hapus Bl"]:
                if msg.from_ in admin:
                    wait["dblack"] = True
                    ar1.sendText(msg.to,"Please send contacts from the person you want to add from the blacklist")
            elif msg.text in ["Com Bl cek"]:
                if msg.from_ in admin:
                    if wait["commentBlack"] == {}:
                        ar1.sendText(msg.to,"Nothing in the blacklist")
                    else:
                        ar1.sendText(msg.to,"The following is a blacklist")
                        mc = ""
                        for mi_d in wait["commentBlack"]:
                            mc += "ãƒ»" +ar1.getContact(mi_d).displayName + "\n"
                        ar1.sendText(msg.to,mc)
            elif msg.text.lower() == 'jam on':
                if msg.from_ in admin:
                    if wait["clock"] == True:
                        ar1.sendText(msg.to,"Jam already on")
                    else:
                        wait["clock"] = True
                        now2 = datetime.now()
                        nowT = datetime.strftime(now2,"?%H:%M?")
                        profile = ar1.getProfile()
                        profile.displayName = wait["cName"] + nowT
                        ar1.updateProfile(profile)
                        ar1.sendText(msg.to,"Jam set on")
            elif msg.text.lower() == 'jam off':
                if msg.from_ in admin:
                    if wait["clock"] == False:
                        ar1.sendText(msg.to,"Jam already off")
                    else:
                        wait["clock"] = False
                        ar1.sendText(msg.to,"Jam set off")
            elif "Jam say:" in msg.text:
                if msg.from_ in admin:
                    n = msg.text.replace("Jam say:","")
                    if len(n.decode("utf-8")) > 30:
                        ar1.sendText(msg.to,"terlalu lama")
                    else:
                        wait["cName"] = n
                        ar1.sendText(msg.to,"Nama Jam Berubah menjadi:" + n)
            elif msg.text.lower() == 'update':
                if msg.from_ in admin:
                    if wait["clock"] == True:
                        now2 = datetime.now()
                        nowT = datetime.strftime(now2,"?%H:%M?")
                        profile = ar1.getProfile()
                        profile.displayName = wait["cName"] + nowT
                        ar1.updateProfile(profile)
                        ar1.sendText(msg.to,"Diperbarui")
                    else:
                        ar1.sendText(msg.to,"Silahkan Aktifkan Jam")
            elif "Image " in msg.text:
                if msg.from_ in admin and staff:
                    search = msg.text.replace("Image ","")
                    url = 'https://www.google.com/search?espv=2&biw=1366&bih=667&tbm=isch&oq=kuc&aqs=mobile-gws-lite.0.0l5&q=' + search
                    raw_html = (download_page(url))
                    items = []
                    items = items + (_images_get_all_items(raw_html))
                    path = random.choice(items)
                    print path
                    try:
                        ar1.sendImageWithURL(msg.to,path)
                    except:
                        pass
#==============================================================================#
            elif msg.text in ["Invite"]:
                if msg.from_ in admin:
                    wait["invite"] = True
                    ar1.sendText(msg.to,"Kirim Contact")
            elif msg.text in ["Jepit"]:
                if msg.from_ in admin:
                    wait["invite"] = True
                    ar1.sendText(msg.to,"Kirim Contact")
                    
            elif msg.text in ["Undang"]:
                if msg.from_ in admin:
                    wait["winvite"] = True
                    ar2.sendText(msg.to,"Kirim Contact")
            
            elif msg.text in ["Steal contact"]:
                if msg.from_ in admin:
                    wait['contact'] = True
                    ar1.sendText(msg.to,"Send Contact")
                
            elif msg.text in ["Like:me","Like me"]: #Semua Bot Ngelike Status Akun Utama
                if msg.from_ in admin:
                    print "[Command]Like executed"
                    ar1.sendText(msg.to,"Like Status Owner")
                    try:
                        likeme()
                    except:
                        pass
                
            elif msg.text in ["Like:friend","Like friend"]: #Semua Bot Ngelike Status Teman
                if msg.from_ in admin:
                    print "[Command]Like executed"
                    ar1.sendText(msg.to,"Like Status Teman")
                    try:
                        likefriend()
                    except:
                        pass
            
            elif msg.text in ["Like:on","Like on"]:
                if msg.from_ in admin:
                    if wait['likeOn'] == True:
                        if wait["lang"] == "JP":
                            ar1.sendText(msg.to,"Done")
                    else:
                        wait['likeOn'] = True
                        if wait["lang"] == "JP":
                            ar1.sendText(msg.to,"Already")
                        
            elif msg.text in ["Like off","Like:off"]:
                if msg.from_ in admin:
                    if wait['likeOn'] == False:
                        if wait["lang"] == "JP":
                            ar1.sendText(msg.to,"Done")
                    else:
                        wait['likeOn'] = False
                        if wait["lang"] == "JP":
                            ar1.sendText(msg.to,"Already")
                        
            elif "Time" in msg.text:
                if msg.toType == 2:
                    ar1.sendText(msg.to,datetime.today().strftime('%H:%M:%S'))
#==============================================================================#
            elif msg.text in ["Sambut on","sambut on"]:
                if msg.from_ in admin:
                    if wait["Wc"] == True:
                        if wait["lang"] == "JP":
                            ar1.sendText(msg.to,"noтιғ yg joιn on")
                    else:
                        wait["Wc"] = True
                        if wait["lang"] == "JP":
                            ar1.sendText(msg.to,"already on")
            elif msg.text in ["Sambut off","sambut off"]:
                if msg.from_ in admin:
                    if wait["Wc"] == False:
                        if wait["lang"] == "JP":
                            ar1.sendText(msg.to,"noтιғ yg joιn oғғ")
                    else:
                        wait["Wc"] = False
                        if wait["lang"] == "JP":
                            ar1.sendText(msg.to,"already oғғ")
#==============================================================================#
            elif msg.text in ["Pergi on","pergi on"]:
                if msg.from_ in admin:
                    if wait["Lv"] == True:
                        if wait["lang"] == "JP":
                            ar1.sendText(msg.to,"noтιғ yg leave on")
                    else:
                        wait["Lv"] = True
                        if wait["lang"] == "JP":
                            ar1.sendText(msg.to,"already on")
            elif msg.text in ["Pergi off","pergi off"]:
                if msg.from_ in admin:
                    if wait["Lv"] == False:
                        if wait["lang"] == "JP":
                            ar1.sendText(msg.to,"noтιғ yg leave oғғ")
                    else:
                        wait["Lv"] = False
                        if wait["lang"] == "JP":
                            ar1.sendText(msg.to,"already oғғ")
#==============================================================================#
            elif "Bantai" in msg.text:
                if msg.from_ in owner:
                    if msg.toType == 2:
                        if msg.toType == 2:
                            print "ok"
                            _name = msg.text.replace("Dadas","")
                            gs = ar1.getGroup(msg.to)
                            gs = ar2.getGroup(msg.to)
                            gs = ar3.getGroup(msg.to)
                            gs = ar4.getGroup(msg.to)
                            gs = ar5.getGroup(msg.to)
                            gs = ar6.getGroup(msg.to)
                            gs = ar7.getGroup(msg.to)
                            gs = ar8.getGroup(msg.to)
                            gs = ar9.getGroup(msg.to)
                            gs = ar10.getGroup(msg.to)
                            ar1.sendText(msg.to,"Jangan panik, santai aja ya ô")
                            ar2.sendText(msg.to,"Group di bersihkan...!!")
                            targets = []
                            for g in gs.members:
                                if _name in g.displayName:
                                    targets.append(g.mid)
                            if targets == []:
                                ar1.sendText(msg.to,"Tidak di temukan")
                                ar2.sendText(msg.to,"Tidak di temukan")
                            else:
                                for target in targets:
                                    try:
                                        klist=[ar1,ar2,ar3,ar4,ar5,ar6,ar7,ar8,ar9,ar10]
                                        kicker=random.choice(klist)
                                        kicker.kickoutFromGroup(msg.to,[target])
                                        print (msg.to,[g.mid])
                                    except:
                                        ar1.sendText(msg.to,"Group Bersih")
                                        ar2.sendText(msg.to,"Group Bersih")
            elif msg.text in ["Salam1"]:
                ar1.sendText(msg.to,"السَّلاَمُ عَلَيْكُمْ وَرَحْمَةُ اللهِ وَبَرَكَاتُهُ")
                ar2.sendText(msg.to,"Assalamu'alaikum")
            elif msg.text in ["Salam2"]:
                ar1.sendText(msg.to,"وَعَلَيْكُمْ السَّلاَمُرَحْمَةُ اللهِ وَبَرَكَاتُهُ")
                ar2.sendText(msg.to,"Wa'alaikumsallam.Wr,Wb")

            elif ("Kick " in msg.text):
                if msg.from_ in admin:
                   targets = []
                   key = eval(msg.contentMetadata["MENTION"])
                   key["MENTIONEES"] [0] ["M"]
                   for x in key["MENTIONEES"]:
                       targets.append(x["M"])
                   for target in targets:
                       try:
                           ar1.kickoutFromGroup(msg.to,[target])
                       except:
                           ar1.sendText(msg.to,"Error")
            
            elif ("Kill " in msg.text):
                if msg.from_ in admin:
                   targets = []
                   key = eval(msg.contentMetadata["MENTION"])
                   key["MENTIONEES"] [0] ["M"]
                   for x in key["MENTIONEES"]:
                       targets.append(x["M"])
                   for target in targets:
                       try:
                           ar1.kickoutFromGroup(msg.to,[target])
                           ar1.inviteIntoGroup(msg.to,[target])
                           ar1.cancelGroupInvitation(msg.to,[target])
                       except:
                           ar1.sendText(msg.to,"Error")
                           
            elif 'invite ' in msg.text.lower():
                if msg.from_ in admin:
                    key = msg.text[-33:]
                    ar1.findAndAddContactsByMid(key)
                    ar1.inviteIntoGroup(msg.to, [key])
                    contact = ar1.getContact(key)
            
            elif msg.text.lower() == 'cancel':
                if msg.from_ in owner:
                    if msg.toType == 2:
                        group = ar1.getGroup(msg.to)
                        if group.invitee is not None:
                            gInviMids = [contact.mid for contact in group.invitee]
                            ar1.cancelGroupInvitation(msg.to, gInviMids)
                        else:
                            if wait["lang"] == "JP":
                                ar1.sendText(msg.to,"Tidak ada undangan")
                            else:
                                ar1.sendText(msg.to,"Invitan tidak ada")
                    else:
                        if wait["lang"] == "JP":
                            ar1.sendText(msg.to,"Tidak ada undangan")
                        else:
                            ar1.sendText(msg.to,"Invitan tidak ada")
            
            elif msg.text.lower() == 'link on':
                if msg.from_ in admin:
                    if msg.toType == 2:
                        group = ar1.getGroup(msg.to)
                        group.preventJoinByTicket = False
                        ar1.updateGroup(group)
                        if wait["lang"] == "JP":
                            ar1.sendText(msg.to,"URL open")
                        else:
                            ar1.sendText(msg.to,"URL open")
                    else:
                        if wait["lang"] == "JP":
                            ar1.sendText(msg.to,"It can not be used outside the group")
                        else:
                            ar1.sendText(msg.to,"Can not be used for groups other than")
            
            elif msg.text.lower() == 'link off':
                if msg.from_ in admin:
                    if msg.toType == 2:
                        group = ar1.getGroup(msg.to)
                        group.preventJoinByTicket = True
                        ar1.updateGroup(group)
                        if wait["lang"] == "JP":
                            ar1.sendText(msg.to,"URL close")
                        else:
                            ar1.sendText(msg.to,"URL close")
                    else:
                        if wait["lang"] == "JP":
                            ar1.sendText(msg.to,"It can not be used outside the group")
                        else:
                            ar1.sendText(msg.to,"Can not be used for groups other than")
            
            elif msg.text in ["Url","Gurl"]:
                if msg.from_ in owner and admin:
                    if msg.toType == 2:
                        g = ar1.getGroup(msg.to)
                        if g.preventJoinByTicket == True:
                            g.preventJoinByTicket = False
                            ar1.updateGroup(g)
                        gurl = ar1.reissueGroupTicket(msg.to)
                        ar1.sendText(msg.to,"line://ti/g/" + gurl)
                    
            elif "Gcreator" == msg.text:
                try:
                    group = ar1.getGroup(msg.to)
                    GS = group.creator.mid
                    M = Message()
                    M.to = msg.to
                    M.contentType = 13
                    M.contentMetadata = {'mid': GS}
                    ar1.sendMessage(M)
                except:
                    W = group.members[0].mid
                    M = Message()
                    M.to = msg.to
                    M.contentType = 13
                    M.contentMetadata = {'mid': W}
                    ar1.sendMessage(M)
                    ar1.sendText(msg.to,"Creator Grup")
            
            elif msg.text.lower() == 'invite:gcreator':
                if msg.from_ in owner:
                    if msg.toType == 2:
                           ginfo = ar1.getGroup(msg.to)
                           try:
                               gcmid = ginfo.creator.mid
                           except:
                               gcmid = "Error"
                           if wait["lang"] == "JP":
                               ar1.inviteIntoGroup(msg.to,[gcmid])
                           else:
                               ar1.inviteIntoGroup(msg.to,[gcmid])
            
            elif msg.text.lower() == 'infogrup':
                if msg.from_ in admin:
                    group = ar1.getGroup(msg.to)
                    try:
                        gCreator = group.creator.displayName
                    except:
                        gCreator = "Error"
                    md = "[Nama Grup : ]\n" + group.name + "\n\n[Id Grup : ]\n" + group.id + "\n\n[Pembuat Grup :]\n" + gCreator + "\n\n[Gambar Grup : ]\nhttp://dl.profile.line-cdn.net/" + group.pictureStatus
                    if group.preventJoinByTicket is False: md += "\n\nKode Url : Diizinkan"
                    else: md += "\n\nKode Url : Diblokir"
                    if group.invitee is None: md += "\nJumlah Member : " + str(len(group.members)) + " Orang" + "\nUndangan Yang Belum Diterima : 0 Orang"
                    else: md += "\nJumlah Member : " + str(len(group.members)) + " Orang" + "\nUndangan Yang Belum Diterima : " + str(len(group.invitee)) + " Orang"
                    ar1.sendText(msg.to,md)
            
            elif msg.text.lower() == 'grup id':
                if msg.from_ in owner:
                    gid = ar1.getGroupIdsJoined()
                    h = ""
                    for i in gid:
                        h += "[%s]:%s\n" % (ar1.getGroup(i).name,i)
                    ar1.sendText(msg.to,h)
#==============================================================================#
            elif msg.text in ["Group list"]:
                if msg.from_ in admin:
                    gid = ar1.getGroupIdsJoined()
                    h = ""
                    for i in gid:
                        h += "%s\n" % (ar1.getGroup(i).name +" ? ["+str(len(ar1.getGroup(i).members))+"]")
                    ar1.sendText(msg.to,"-- List Groups --\n\n"+ h +"\nTotal groups =" +" ["+str(len(gid))+"]")
#==============================================================================#
            elif "Admin add @" in msg.text:
              if msg.from_ in owner:
                print "[Command]Admin add executing"
                _name = msg.text.replace("Admin add @","")
                _nametarget = _name.rstrip('  ')
                gs = ar1.getGroup(msg.to)
                gs = ar2.getGroup(msg.to)
                gs = ar3.getGroup(msg.to)
                gs = ar4.getGroup(msg.to)
                gs = ar5.getGroup(msg.to)
                gs = ar6.getGroup(msg.to)
                gs = ar7.getGroup(msg.to)
                gs = ar8.getGroup(msg.to)
                gs = ar9.getGroup(msg.to)
                gs = ar10.getGroup(msg.to)
                targets = []
                for g in gs.members:
                    if _nametarget == g.displayName:
                        targets.append(g.mid)
                if targets == []:
                   random.choice(KAC).sendText(msg.to,"Contact not found")
                else:
                   for target in targets:
                        try:
                            Bots.append(target)
                            ar1.sendText(msg.to,"Admin Ditambahkan")
                            ar2.sendText(msg.to,"Admin Ditambahkan")
                            ar3.sendText(msg.to,"Admin Ditambahkan")
                            ar4.sendText(msg.to,"Admin Ditambahkan")
                            ar5.sendText(msg.to,"Admin Ditambahkan")
                            ar6.sendText(msg.to,"Admin Ditambahkan")
                            ar7.sendText(msg.to,"Admin Ditambahkan")
                            ar8.sendText(msg.to,"Admin Ditambahkan")
                            ar9.sendText(msg.to,"Admin Ditambahkan")
                            ar10.sendText(msg.to,"Admin Ditambahkan")
                        except:
                            pass
                print "[Command]Admin add executed"
              else:
                ar1.sendText(msg.to,"Perintah Ditolak.")
                ar1.sendText(msg.to,"Hanya Owner Yang bisa Gunain Perintah ini.")
                
            elif "Admin remove @" in msg.text:
              if msg.from_ in owner:
                print "[Command]Admin remove executing"
                _name = msg.text.replace("Admin remove @","")
                _nametarget = _name.rstrip('  ')
                gs = ar1.getGroup(msg.to)
                gs = ar2.getGroup(msg.to)
                gs = ar3.getGroup(msg.to)
                gs = ar4.getGroup(msg.to)
                gs = ar5.getGroup(msg.to)
                gs = ar6.getGroup(msg.to)
                gs = ar7.getGroup(msg.to)
                gs = ar8.getGroup(msg.to)
                gs = ar9.getGroup(msg.to)
                gs = ar10.getGroup(msg.to)
                targets = []
                for g in gs.members:
                    if _nametarget == g.displayName:
                        targets.append(g.mid)
                if targets == []:
                   random.choice(KAC).sendText(msg.to,"Contact not found")
                else:
                   for target in targets:
                        try:
                            Bots.remove(target)
                            ar1.sendText(msg.to,"Admin Dihapus")
                            ar2.sendText(msg.to,"Admin Dihapus")
                            ar3.sendText(msg.to,"Admin Dihapus")
                            ar4.sendText(msg.to,"Admin Dihapus")
                            ar5.sendText(msg.to,"Admin Dihapus")
                            ar6.sendText(msg.to,"Admin Dihapus")
                            ar7.sendText(msg.to,"Admin Dihapus")
                            ar8.sendText(msg.to,"Admin Dihapus")
                            ar9.sendText(msg.to,"Admin Dihapus")
                            ar10.sendText(msg.to,"Admin Dihapus")
                        except:
                            pass
                print "[Command]Admin remove executed"
              else:
                ar1.sendText(msg.to,"Perintah Ditolak.")
                ar1.sendText(msg.to,"Hanya Owner Yang bisa Gunain Perintah ini.")
                
            elif msg.text in ["Adminlist","adminlist"]:
              if Bots == []:
                  ar1.sendText(msg.to,"The Admin is empty")
              else:
                  ar1.sendText(msg.to,"Tunggu...")
                  mc = "╔═════════════\n║Admin ՏվղժíϲɑԵҽ ԹɾօԵҽϲԵ\n╠═════════════\n"
                  for mi_d in Bots:
                      mc += "║••>" +ar1.getContact(mi_d).displayName + "\n╠═════════════\n"
                  ar1.sendText(msg.to,mc)
                  print "[Command]Admin executed"

#==============================================================================#
            elif "Staff add @" in msg.text:
              if msg.from_ in owner:
                print "[Command]Staff add executing"
                _name = msg.text.replace("Staff add @","")
                _nametarget = _name.rstrip('  ')
                gs = ar1.getGroup(msg.to)
                gs = ar2.getGroup(msg.to)
                gs = ar3.getGroup(msg.to)
                gs = ar4.getGroup(msg.to)
                gs = ar5.getGroup(msg.to)
                gs = ar6.getGroup(msg.to)
                gs = ar7.getGroup(msg.to)
                gs = ar8.getGroup(msg.to)
                gs = ar9.getGroup(msg.to)
                gs = ar10.getGroup(msg.to)
                targets = []
                for g in gs.members:
                    if _nametarget == g.displayName:
                        targets.append(g.mid)
                if targets == []:
                   random.choice(KAC).sendText(msg.to,"Contact not found")
                else:
                   for target in targets:
                        try:
                            staff.append(target)
                            ar1.sendText(msg.to,"Staff Ditambahkan")
                            ar2.sendText(msg.to,"Staff Ditambahkan")
                            ar3.sendText(msg.to,"Staff Ditambahkan")
                            ar4.sendText(msg.to,"Staff Ditambahkan")
                            ar5.sendText(msg.to,"Staff Ditambahkan")
                            ar6.sendText(msg.to,"Staff Ditambahkan")
                            ar7.sendText(msg.to,"Staff Ditambahkan")
                            ar8.sendText(msg.to,"Staff Ditambahkan")
                            ar9.sendText(msg.to,"Staff Ditambahkan")
                            ar10.sendText(msg.to,"Staff Ditambahkan")
                        except:
                            pass
                print "[Command]Staff add executed"
              else:
                ar1.sendText(msg.to,"Perintah Ditolak.")
                ar1.sendText(msg.to,"Hanya Owner Yang bisa Gunain Perintah ini.")
                
            elif "Staff remove @" in msg.text:
              if msg.from_ in owner:
                print "[Command]staff remove executing"
                _name = msg.text.replace("Staff remove @","")
                _nametarget = _name.rstrip('  ')
                gs = ar1.getGroup(msg.to)
                gs = ar2.getGroup(msg.to)
                gs = ar3.getGroup(msg.to)
                gs = ar4.getGroup(msg.to)
                gs = ar5.getGroup(msg.to)
                gs = ar6.getGroup(msg.to)
                gs = ar7.getGroup(msg.to)
                gs = ar8.getGroup(msg.to)
                gs = ar9.getGroup(msg.to)
                gs = ar10.getGroup(msg.to)
                targets = []
                for g in gs.members:
                    if _nametarget == g.displayName:
                        targets.append(g.mid)
                if targets == []:
                   random.choice(KAC).sendText(msg.to,"Contact not found")
                else:
                   for target in targets:
                        try:
                            staff.remove(target)
                            ar1.sendText(msg.to,"Staff Dihapus")
                            ar2.sendText(msg.to,"Staff Dihapus")
                            ar3.sendText(msg.to,"Staff Dihapus")
                            ar4.sendText(msg.to,"Staff Dihapus")
                            ar5.sendText(msg.to,"Staff Dihapus")
                            ar6.sendText(msg.to,"Staff Dihapus")
                            ar7.sendText(msg.to,"Staff Dihapus")
                            ar8.sendText(msg.to,"Staff Dihapus")
                            ar9.sendText(msg.to,"Staff Dihapus")
                            ar10.sendText(msg.to,"Staff Dihapus")
                        except:
                            pass
                print "[Command]Staff remove executed"
              else:
                ar1.sendText(msg.to,"Perintah Ditolak.")
                ar1.sendText(msg.to,"Hanya Owner Yang bisa Gunain Perintah ini.")
                
            elif msg.text in ["Adminlist","adminlist"]:
              if staff == []:
                  ar1.sendText(msg.to,"The stafflist is empty")
              else:
                  ar1.sendText(msg.to,"Tunggu...")
                  mc = "╔═════════════\n║Admin ՏվղժíϲɑԵҽ ԹɾօԵҽϲԵ\n╠═════════════\n"
                  for mi_d in staff:
                      mc += "║••>" +ar1.getContact(mi_d).displayName + "\n╠═════════════\n"
                  ar1.sendText(msg.to,mc)
                  print "[Command]Admin executed"
#==============================================================================#
            elif msg.text in ["DPK"]: #Panggil Semua Bot
                if msg.from_ in owner:
                    G = ar1.getGroup(msg.to)
                    ginfo = ar1.getGroup(msg.to)
                    G.preventJoinByTicket = False
                    ar1.updateGroup(G)
                    invsend = 0
                    Ticket = ar1.reissueGroupTicket(msg.to)
                    ar2.acceptGroupInvitationByTicket(msg.to,Ticket)
                    time.sleep(0.01)
                    ar3.acceptGroupInvitationByTicket(msg.to,Ticket)
                    time.sleep(0.01)
                    ar4.acceptGroupInvitationByTicket(msg.to,Ticket)
                    time.sleep(0.01)
                    ar5.acceptGroupInvitationByTicket(msg.to,Ticket)
                    time.sleep(0.01)
                    ar6.acceptGroupInvitationByTicket(msg.to,Ticket)
                    time.sleep(0.01)
                    ar7.acceptGroupInvitationByTicket(msg.to,Ticket)
                    time.sleep(0.01)
                    ar8.acceptGroupInvitationByTicket(msg.to,Ticket)
                    time.sleep(0.01)
                    ar9.acceptGroupInvitationByTicket(msg.to,Ticket)
                    time.sleep(0.01)
                    ar10.acceptGroupInvitationByTicket(msg.to,Ticket)
                    time.sleep(0.01)
                    G = ar1.getGroup(msg.to)
                    ginfo = ar1.getGroup(msg.to)
                    G.preventJoinByTicket = True
                    ar1.updateGroup(G)
                    ar10.sendText(msg.to,"Hallo...!!! " + str(ginfo.name) + "\n\nSemoga Selalu Bahagia...!!!")
                    print "Semua Sudah Lengkap"
#==============================================================================#
            elif "absen" == msg.text.lower():
                if msg.from_ in admin and staff:
                    group = ar1.getGroup(msg.to)
                    nama = [contact.mid for contact in group.members]
                    nm1, nm2, nm3, nm4, nm5, jml = [], [], [], [], [], len(nama)
                    if jml <= 100:
                        summon(msg.to, nama)
                    if jml > 100 and jml < 200:
                        for i in range(0, 99):
                            nm1 += [nama[i]]
                        summon(msg.to, nm1)
                        for j in range(100, len(nama)-1):
                            nm2 += [nama[j]]
                        summon(msg.to, nm2)
                    if jml > 200  and jml < 500:
                        for i in range(0, 99):
                            nm1 += [nama[i]]
                        summon(msg.to, nm1)
                        for j in range(100, 199):
                            nm2 += [nama[j]]
                        summon(msg.to, nm2)
                        for k in range(200, 299):
                            nm3 += [nama[k]]
                        summon(msg.to, nm3)
                        for l in range(300, 399):
                            nm4 += [nama[l]]
                        summon(msg.to, nm4)
                        for m in range(400, len(nama)-1):
                            nm5 += [nama[m]]
                        summon(msg.to, nm5)
                    if jml > 500:
                         print "Terlalu Banyak Men 500+"
                    cnt = Message()
                    cnt.text = "Jumlah:\n" + str(jml) +  " Members"
                    cnt.to = msg.to
                    ar1.sendMessage(cnt)

            elif msg.text in ["Mybot"]:
            	if msg.from_ in owner:
                    h = ar1.getContact(mid)
                    h = ar2.getContact(mid2)
                    h = ar3.getContact(mid3)
                    h = ar4.getContact(mid4)
                    h = ar5.getContact(mid5)
                    h = ar6.getContact(mid6)
                    h = ar7.getContact(mid7)
                    h = ar8.getContact(mid8)
                    h = ar9.getContact(mid9)
                    h = ar10.getContact(mid10)
                    ar1.sendText(msg.to,"═══[DisplayName]═══\n" + h.displayName)
                    ar2.sendText(msg.to,"═══[DisplayName]═══\n" + h.displayName)
                    ar3.sendText(msg.to,"═══[DisplayName]═══\n" + h.displayName)
                    ar4.sendText(msg.to,"═══[DisplayName]═══\n" + h.displayName)
                    ar5.sendText(msg.to,"═══[DisplayName]═══\n" + h.displayName)
                    ar6.sendText(msg.to,"═══[DisplayName]═══\n" + h.displayName)
                    ar7.sendText(msg.to,"═══[DisplayName]═══\n" + h.displayName)
                    ar8.sendText(msg.to,"═══[DisplayName]═══\n" + h.displayName)
                    ar9.sendText(msg.to,"═══[DisplayName]═══\n" + h.displayName)
                    ar10.sendText(msg.to,"═══[DisplayName]═══\n" + h.displayName)
#==============================================================================#
            elif "Responsename" in msg.text:
                if msg.from_ in admin:
                    ar1.sendText(msg.to,"▄▄▄▄▄▄▄▄▄▄▄▄ ")
                    ar2.sendText(msg.to,"▄▄▄▄▄▄▄▄▄▄▄▄")
                    ar3.sendText(msg.to,"▄▄▄▄▄▄▄▄▄▄▄▄")
                    ar4.sendText(msg.to,"▄▄▄▄▄▄▄▄▄▄▄▄")
                    ar5.sendText(msg.to,"▄▄▄▄▄▄▄▄▄▄▄▄")
                    ar6.sendText(msg.to,"▄▄▄▄▄▄▄▄▄▄▄▄ ")
                    ar7.sendText(msg.to,"▄▄▄▄▄▄▄▄▄▄▄▄")
                    ar8.sendText(msg.to,"▄▄▄▄▄▄▄▄▄▄▄▄")
                    ar9.sendText(msg.to,"▄▄▄▄▄▄▄▄▄▄▄▄")
                    ar10.sendText(msg.to,"▄▄▄▄▄▄▄▄▄▄▄▄")
                    ar1.sendText(msg.to,"👉 Readdy on")
            
            elif 'Youtube ' in msg.text:
                if msg.from_ in admin and staff:
                    try:
                        textToSearch = (msg.text).replace('Youtube ', "").strip()
                        query = urllib.quote(textToSearch)
                        url = "https://www.youtube.com/results?search_query=" + query
                        response = urllib2.urlopen(url)
                        html = response.read()
                        soup = BeautifulSoup(html, "html.parser")
                        results = soup.find(attrs={'class': 'yt-uix-tile-link'})
                        ght = ('https://www.youtube.com' + results['href'])
                        ar1.sendVideoWithURL(msg.to, ght)
                    except:
                        ar1.sendText(msg.to, "Could not find it")
            
            elif "Yt " in msg.text:
                if msg.from_ in admin and staff:
                    query = msg.text.replace("Yt ","")
                    with requests.session() as s:
                        s.headers['user-agent'] = 'Mozilla/5.0'
                        url = 'http://www.youtube.com/results'
                        params = {'search_query': query}
                        r = s.get(url, params=params)
                        soup = BeautifulSoup(r.content, 'html5lib')
                        hasil = ""
                        for a in soup.select('.yt-lockup-title > a[title]'):
                            if '&list=' not in a['href']:
                                hasil += ''.join((a['title'],'\nUrl : http://www.youtube.com' + a['href'],'\n\n'))
                        ar1.sendText(msg.to,hasil)
                        print '[Command] Youtube Search'
                        
            elif "Lirik " in msg.text:
                if msg.from_ in admin and staff:
                    try:
                        songname = msg.text.lower().replace("Lirik ","")
                        params = {'songname': songname}
                        r = requests.get('http://ide.fdlrcn.com/workspace/yumi-apis/joox?' + urllib.urlencode(params))
                        data = r.text
                        data = json.loads(data)
                        for song in data:
                            hasil = 'Lyric Lagu ('
                            hasil += song[0]
                            hasil += ')\n\n'
                            hasil += song[5]
                            ar1.sendText(msg.to, hasil)
                    except Exception as wak:
                            ar1.sendText(msg.to, str(wak))
                            
            elif "Wikipedia " in msg.text:
                if msg.from_ in admin and staff:
                    try:
                        wiki = msg.text.lower().replace("Wikipedia ","")
                        wikipedia.set_lang("id")
                        pesan="Title ("
                        pesan+=wikipedia.page(wiki).title
                        pesan+=")\n\n"
                        pesan+=wikipedia.summary(wiki, sentences=1)
                        pesan+="\n"
                        pesan+=wikipedia.page(wiki).url
                        ar1.sendText(msg.to, pesan)
                    except:
                        try:
                            pesan="Over Text Limit! Please Click link\n"
                            pesan+=wikipedia.page(wiki).url
                            ar1.sendText(msg.to, pesan)
                        except Exception as e:
                            ar1.sendText(msg.to, str(e))                            

            elif "Kelahiran " in msg.text:
                if msg.from_ in admin and staff:
                    tanggal = msg.text.replace("Kelahiran ","")
                    r=requests.get('https://script.google.com/macros/exec?service=AKfycbw7gKzP-WYV2F5mc9RaR7yE3Ve1yN91Tjs91hp_jHSE02dSv9w&nama=ervan&tanggal='+tanggal)
                    data=r.text
                    data=json.loads(data)
                    lahir = data["data"]["lahir"]
                    usia = data["data"]["usia"]
                    ultah = data["data"]["ultah"]
                    zodiak = data["data"]["zodiak"]
                    ar1.sendText(msg.to,"============ I N F O R M A S I ============\n"+"Date Of Birth : "+lahir+"\nAge : "+usia+"\nUltah : "+ultah+"\nZodiak : "+zodiak+"\n============ I N F O R M A S I ============")

            elif msg.text in ["Kalender","Waktu"]:
                timeNow = datetime.now()
                timeHours = datetime.strftime(timeNow,"(%H:%M)")
                day = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday","Friday", "Saturday"]
                hari = ["Minggu", "Senin", "Selasa", "Rabu", "Kamis", "Jumat", "Sabtu"]
                bulan = ["Januari", "Februari", "Maret", "April", "Mei", "Juni", "Juli", "Agustus", "September", "Oktober", "November", "Desember"]
                inihari = datetime.today()
                hr = inihari.strftime('%A')
                bln = inihari.strftime('%m')
                for i in range(len(day)):
                    if hr == day[i]: hasil = hari[i]
                for k in range(0, len(bulan)):
                    if bln == str(k): bln = bulan[k-1]
                rst = hasil + ", " + inihari.strftime('%d') + " - " + bln + " - " + inihari.strftime('%Y') + "\nJam : [ " + inihari.strftime('%H:%M:%S') + " ]"
                ar1.sendText(msg.to, rst)
#==============================================================================#
            elif msg.text.lower() == 'ifconfig':
                if msg.from_ in owner:
                    botKernel = subprocess.Popen(["ifconfig"], stdout=subprocess.PIPE).communicate()[0]
                    ar1.sendText(msg.to, botKernel + "\n\n===SERVER INFO NetStat===")
            elif msg.text.lower() == 'system':
                if msg.from_ in owner:
                    botKernel = subprocess.Popen(["df","-h"], stdout=subprocess.PIPE).communicate()[0]
                    ar1.sendText(msg.to, botKernel + "\n\n===SERVER INFO SYSTEM===")
            elif msg.text.lower() == 'kernel':
                if msg.from_ in owner:
                    botKernel = subprocess.Popen(["uname","-srvmpio"], stdout=subprocess.PIPE).communicate()[0]
                    ar1.sendText(msg.to, botKernel + "\n\n===SERVER INFO KERNEL===")
            elif msg.text.lower() == 'cpu':
                if msg.from_ in owner:
                    botKernel = subprocess.Popen(["cat","/proc/cpuinfo"], stdout=subprocess.PIPE).communicate()[0]
                    ar1.sendText(msg.to, botKernel + "\n\n===SERVER INFO CPU===")
                    
            elif msg.text in ["Speed"]:
                start = time.time()
                print("Speed")                
                elapsed_time = time.time() - start
		cl.sendText(msg.to, "Progress...")
                random.choice(KAC).sendText(msg.to, "%sseconds" % (elapsed_time))
                
            elif msg.text in ["Sp"]:
                start = time.time()
                cl.sendText(msg.to, "Progress......")
                elapsed_time = time.time() - start
                random.choice(KAC).sendText(msg.to, "%sseconds" % (elapsed_time))                
            elif "Restart" in msg.text:
                if msg.from_ in owner:
                    print "[Command]Restart"
                    try:
                        ar1.sendText(msg.to,"Restarting...")
                        ar1.sendText(msg.to,"Restart Success")
                        restart_program()
                    except:
                        ar1.sendText(msg.to,"Please wait")
                        restart_program()
                        pass
                    
            elif "Turn off" in msg.text:
                if msg.from_ in owner:
                    try:
                        import sys
                        sys.exit()
                    except:
                        pass
                
            elif msg.text.lower() == 'runtime':
                if msg.from_ in owner:
                    eltime = time.time() - mulai
                    van = "Bot has been active "+waktu(eltime)
                    ar1.sendText(msg.to,van)

            elif msg.text in ["Remove all chat"]:
                if msg.from_ in owner:
                    ar1.removeAllMessages(op.param2)
                    ar2.removeAllMessages(op.param2)
                    ar3.removeAllMessages(op.param2)
                    ar4.removeAllMessages(op.param2)
                    ar5.removeAllMessages(op.param2)
                    ar6.removeAllMessages(op.param2)
                    ar7.removeAllMessages(op.param2)
                    ar8.removeAllMessages(op.param2)
                    ar9.removeAllMessages(op.param2)
                    ar10.removeAllMessages(op.param2)
                    ar1.sendText(msg.to,"Removed all chat Finish")
#-----------------------------------------------
            elif msg.text in ["Owner bye"]:
				if msg.from_ in owner:
					if msg.toType == 2:
						ginfo = ar1.getGroup(msg.to)
						try:
							ar1.leaveGroup(msg.to)
							ar2.leaveGroup(msg.to)
							ar3.leaveGroup(msg.to)
							ar4.leaveGroup(msg.to)
							ar5.leaveGroup(msg.to)
							ar6.leaveGroup(msg.to)
							ar7.leaveGroup(msg.to)
							ar8.leaveGroup(msg.to)
							ar9.leaveGroup(msg.to)
							ar10.leaveGroup(msg.to)
						except:
							pass
                        
#================================ KRIS SCRIPT STARTED ==============================================#
            elif "google " in msg.text:
                if msg.from_ in admin and admin:
                    a = msg.text.replace("google ","")
                    b = urllib.quote(a)
                    ar1.sendText(msg.to,"Sedang Mencari om...")
                    ar1.sendText(msg.to, "https://www.google.com/" + b)
                    ar1.sendText(msg.to,"Ketemu om ^")

            elif msg.text in ["Friendlist"]:
                if msg.from_ in owner:
                    contactlist = ar1.getAllContactIds()
                    kontak = ar1.getContacts(contactlist)
                    num=1
                    msgs="═════════List Friend═════════"
                    for ids in kontak:
                        msgs+="\n[%i] %s" % (num, ids.displayName)
                        num=(num+1)
                    msgs+="\n═════════List Friend═════════\n\nTotal Friend : %i" % len(kontak)
                    ar1.sendText(msg.to, msgs)
                
            elif msg.text in ["Memlist"]:
                if msg.from_ in owner:
                    kontak = ar1.getGroup(msg.to)
                    group = kontak.members
                    num=1
                    msgs="═════════List Member═════════-"
                    for ids in group:
                        msgs+="\n[%i] %s" % (num, ids.displayName)
                        num=(num+1)
                    msgs+="\n═════════List Member═════════\n\nTotal Members : %i" % len(group)
                    ar1.sendText(msg.to, msgs)
                
            elif msg.text in ["Blocklist"]:
                if msg.from_ in admin:
                    blockedlist = ar1.getBlockedContactIds()
                    kontak = ar1.getContacts(blockedlist)
                    num=1
                    msgs="═════════List Blocked═════════"
                    for ids in kontak:
                        msgs+="\n[%i] %s" % (num, ids.displayName)
                        num=(num+1)
                    msgs+="\n═════════List Blocked═════════\n\nTotal Blocked : %i" % len(kontak)
                    ar1.sendText(msg.to, msgs)
                
            elif msg.text in ["Gruplist"]:
                if msg.from_ in admin:
                    gruplist = ar1.getGroupIdsJoined()
                    kontak = ar1.getGroups(gruplist)
                    num=1
                    msgs="═════════List Grup═════════"
                    for ids in kontak:
                        msgs+="\n[%i] %s" % (num, ids.name)
                        num=(num+1)
                    msgs+="\n═════════List Grup═════════\n\nTotal Grup : %i" % len(kontak)
                    ar1.sendText(msg.to, msgs)
            
            elif msg.text in ["Gruplistmid"]:
                if msg.from_ in owner:
                    gruplist = ar1.getGroupIdsJoined()
                    kontak = ar1.getGroups(gruplist)
                    num=1
                    msgs="═════════List GrupMid═════════"
                    for ids in kontak:
                        msgs+="\n[%i] %s" % (num, ids.id)
                        num=(num+1)
                    msgs+="\n═════════List GrupMid═════════\n\nTotal Grup : %i" % len(kontak)
                    ar1.sendText(msg.to, msgs)
                    
            elif "Grupname" in msg.text:
                if msg.from_ in admin:
                    saya = msg.text.replace('Grupname','')
                    gid = ar1.getGroup(msg.to)
                    ar1.sendText(msg.to, "[Nama Grup : ]\n" + gid.name)
            
            elif "Grupid" in msg.text:
                if msg.from_ in admin:
                    saya = msg.text.replace('Grupid','')
                    gid = ar1.getGroup(msg.to)
                    ar1.sendText(msg.to, "[ID Grup : ]\n" + gid.id)
                    
            elif "Grupinfo: " in msg.text:
                if msg.from_ in admin:
                    saya = msg.text.replace('Grupinfo: ','')
                    gid = ar1.getGroupIdsJoined()
                    for i in gid:
                        h = ar1.getGroup(i).name
                        group = ar1.getGroup(i)
                        if h == saya:
                            try:
                                creator = group.creator.mid 
                                msg.contentType = 13
                                msg.contentMetadata = {'mid': creator}
                                md = "Nama Grup :\n" + group.name + "\n\nID Grup :\n" + group.id
                                if group.preventJoinByTicket is False: md += "\n\nKode Url : Diizinkan"
                                else: md += "\n\nKode Url : Diblokir"
                                if group.invitee is None: md += "\nJumlah Member : " + str(len(group.members)) + " Orang" + "\nUndangan Yang Belum Diterima : 0 Orang"
                                else: md += "\nJumlah Member : " + str(len(group.members)) + " Orang" + "\nUndangan Yang Belum Diterima : " + str(len(group.invitee)) + " Orang"
                                ar1.sendText(msg.to,md)
                                ar1.sendMessage(msg)
                                ar1.sendImageWithURL(msg.to,"http://dl.profile.line.naver.jp/"+ group.pictureStatus)
                            except:
                                creator = "Error"
#=================================KRIS SCRIPT FINISHED =============================================#
            
            elif "Ban @" in msg.text:
                if msg.from_ in admin:
                    if msg.toType == 2:
                        _name = msg.text.replace("Ban @","")
                        _nametarget = _name.rstrip()
                        gs = ar1.getGroup(msg.to)
                        targets = []
                        for g in gs.members:
                            if _nametarget == g.displayName:
                                targets.append(g.mid)
                        if targets == []:
                            ar1.sendText(msg.to,_nametarget + " Not Found")
                        else:
                            for target in targets:
                                try:
                                    wait["blacklist"][target] = True
                                    ar1.sendText(msg.to,_nametarget + " Succes Add to Blacklist")
                                except:
                                    ar1.sendText(msg.to,"Error")
                                
            elif "Unban @" in msg.text:
                if msg.from_ in admin:
                    if msg.toType == 2:
                        _name = msg.text.replace("Unban @","")
                        _nametarget = _name.rstrip()
                        gs = ar1.getGroup(msg.to)
                        targets = []
                        for g in gs.members:
                            if _nametarget == g.displayName:
                                targets.append(g.mid)
                        if targets == []:
                            ar1.sendText(msg.to,_nametarget + " Not Found")
                        else:
                            for target in targets:
                                try:
                                    del wait["blacklist"][target]
                                    ar1.sendText(msg.to,_nametarget + " Delete From Blacklist")
                                except:
                                    ar1.sendText(msg.to,_nametarget + " Not In Blacklist")

            elif "Ban:" in msg.text:
                if msg.from_ in admin:
                    nk0 = msg.text.replace("Ban:","")
                    nk1 = nk0.lstrip()
                    nk2 = nk1.replace("","")
                    nk3 = nk2.rstrip()
                    _name = nk3
                    gs = ar1.getGroup(msg.to)
                    targets = []
                    for s in gs.members:
                        if _name in s.displayName:
                            targets.append(s.mid)
                    if targets == []:
                        sendMessage(msg.to,"user does not exist")
                        pass
                    else:
                        for target in targets:
                            try:
                                wait["blacklist"][target] = True
                                f=codecs.open('st2__b.json','w','utf-8')
                                json.dump(wait["blacklist"], f, sort_keys=True, indent=4,ensure_ascii=False)
                                ar1.sendText(msg.to,_name + " Succes Add to Blacklist")
                            except:
                                ar1.sendText(msg.to,"Error")

            elif "Unban:" in msg.text:
                if msg.from_ in admin:
                    nk0 = msg.text.replace("Unban:","")
                    nk1 = nk0.lstrip()
                    nk2 = nk1.replace("","")
                    nk3 = nk2.rstrip()
                    _name = nk3
                    gs = ar1.getGroup(msg.to)
                    targets = []
                    for s in gs.members:
                        if _name in s.displayName:
                            targets.append(s.mid)
                    if targets == []:
                        sendMessage(msg.to,"user does not exist")
                        pass
                    else:
                        for target in targets:
                            try:
                                del wait["blacklist"][target]
                                f=codecs.open('st2__b.json','w','utf-8')
                                json.dump(wait["blacklist"], f, sort_keys=True, indent=4,ensure_ascii=False)
                                ar1.sendText(msg.to,_name + " Delete From Blacklist")
                            except:
                                ar1.sendText(msg.to,_name + " Not In Blacklist")
            elif msg.text in ["Clear"]:
                if msg.from_ in admin:
                    wait["blacklist"] = {}
                    ar1.sendText(msg.to,"Blacklist Telah Dibersihkan")
            elif msg.text in ["Ban:on"]:
                if msg.from_ in admin:
                    wait["wblacklist"] = True
                    ar1.sendText(msg.to,"Send Contact")
            elif msg.text in ["Unban:on"]:
                if msg.from_ in admin:
                    wait["dblacklist"] = True
                    ar1.sendText(msg.to,"Send Contact")
            elif msg.text in ["Banlist"]:
                if msg.from_ in admin:
                    if wait["blacklist"] == {}:
                        ar1.sendText(msg.to,"Tidak Ada Blacklist")
                    else:
                        ar1.sendText(msg.to,"Daftar Banlist")
                        num=1
                        msgs="*Blacklist*"
                        for mi_d in wait["blacklist"]:
                            msgs+="\n[%i] %s" % (num, ar1.getContact(mi_d).displayName)
                            num=(num+1)
                            h = ar1.getContact(mi_d)
                            M = Message()
                            M.to = msg.to
                            M.contentType = 13
                            M.contentMetadata = {'mid': mi_d}
                            ar1.sendMessage(M)
                        msgs+="\n*Blacklist*\n\nTotal Blacklist : %i" % len(wait["blacklist"])
                        ar1.sendText(msg.to, msgs)
            elif msg.text in ["Conban","Contactban","Contact ban"]:
                if msg.from_ in admin:
                    if wait["blacklist"] == {}:
                        ar1.sendText(msg.to,"Tidak Ada Blacklist")
                    else:
                        ar1.sendText(msg.to,"Daftar Blacklist")
                        h = ""
                        for i in wait["blacklist"]:
                            h = ar1.getContact(i)
                            M = Message()
                            M.to = msg.to
                            M.contentType = 13
                            M.contentMetadata = {'mid': i}
                            ar1.sendMessage(M)
            elif msg.text in ["Midban","Mid ban"]:
                if msg.from_ in admin:
                    if msg.toType == 2:
                        group = ar1.getGroup(msg.to)
                        gMembMids = [contact.mid for contact in group.members]
                        matched_list = []
                        for tag in wait["blacklist"]:
                            matched_list+=filter(lambda str: str == tag, gMembMids)
                        num=1
                        cocoa = "══════════List Blacklist═════════"
                        for mm in matched_list:
                            cocoa+="\n[%i] %s" % (num, mm)
                            num=(num+1)
                            cocoa+="\n═════════List Blacklist═════════\n\nTotal Blacklist : %i" % len(matched_list)
                        ar1.sendText(msg.to,cocoa)
            elif msg.text.lower() == 'scan blacklist':
                if msg.from_ in admin:
                    if msg.toType == 2:
                        group = ar1.getGroup(msg.to)
                        gMembMids = [contact.mid for contact in group.members]
                        matched_list = []
                        for tag in wait["blacklist"]:
                            matched_list+=filter(lambda str: str == tag, gMembMids)
                        if matched_list == []:
                            ar1.sendText(msg.to,"Tidak ada Daftar Blacklist")
                            return
                        for jj in matched_list:
                            try:
                                ar1.kickoutFromGroup(msg.to,[jj])
                                print (msg.to,[jj])
                            except:
                                pass       
            elif "Allban" in msg.text:
              if msg.from_ in admin:
                  if msg.toType == 2:
                       print "ok"
                       _name = msg.text.replace("Allban","")
                       gs = ar1.getGroup(msg.to)
                       ar1.sendText(msg.to,"Banned all")
                       targets = []
                       for g in gs.members:
                           if _name in g.displayName:
                                targets.append(g.mid)
                       if targets == []:
                            ar1.sendText(msg.to,"Maaf")
                       else:
                           for target in targets:
                               if not target in Bots:
                                   try:
                                       wait["blacklist"][target] = True
                                       f=codecs.open('st2__b.json','w','utf-8')
                                       json.dump(wait["blacklist"], f, sort_keys=True, indent=4,ensure_ascii=False)
                                       ar1.sendText(msg.to,"Success Boss")
                                   except:
                                       ar1.sentText(msg.to,"Berhasil Di Banned")
#==============================================#
        if op.type == 26:
            msg = op.message
            if msg.contentType == 13:
               if wait["wblack"] == True:
                    if msg.contentMetadata["mid"] in wait["commentBlack"]:
                        ar1.sendText(msg.to,"already")
                        wait["wblack"] = False
                    else:
                        wait["commentBlack"][msg.contentMetadata["mid"]] = True
                        wait["wblack"] = False
                        ar1.sendText(msg.to,"decided not to comment")

        if op.type == 17:
           if wait["Wc"] == True:
               if op.param2 in Bots:
                 return
               ginfo = ar1.getGroup(op.param1)
               G = ar1.getGroup(op.param1)
               h = ar1.getContact(op.param2)
               cu = ar1.channel.getCover(op.param2)
               path = str(cu)
               group = ar1.getGroup(op.param1)
               nama = [contact.mid for contact in group.members]
               nm1, nm2, nm3, nm4, nm5, jml = [], [], [], [], [], len(nama)
               if jml <= 100:
                    summon(op.param1, nama)
               if jml > 100 and jml < 200:
                  for i in range(0, 99):
                      nm1 += [nama[i]]
                  summon(op.param1, nm1)
                  for j in range(100, len(nama)-1):
                      nm2 += [nama[j]]
                  summon(op.param1, nm2)
               if jml > 200  and jml < 500:
                  for i in range(0, 99):
                      nm1 += [nama[i]]
                  summon(op.param1, nm1)
                  for j in range(100, 199):
                      nm2 += [nama[j]]
                  summon(op.param1, nm2)
                  for k in range(200, 299):
                      nm3 += [nama[k]]
                  summon(op.param1, nm3)
                  for l in range(300, 399):
                      nm4 += [nama[l]]
                  summon(op.param1, nm4)
                  for m in range(400, len(nama)-1):
                      nm5 += [nama[m]]
                  summon(op.param1, nm5)
               if jml > 500:
                   print "Terlalu Banyak Men 500+"
               cnt = Message()
               cnt.text = "╔═════════════\n║Kedatangan Anggota baru\n║Jumlah Menjadi:" + str(jml) +  "\n║Anggota \n╚═════════════"
               cnt.to = op.param1
               random.choice(KAC).sendMessage(cnt)
               random.choice(KAC).sendText(op.param1,"Bernama: " + h.displayName + "\nStatus:\n" + h.statusMessage)
               random.choice(KAC).sendText(op.param1, "╔═════════════\n║🏠 WELCOME TO 🏠 " + str(ginfo.name) + "\n╠═════════════\n" + "║ADMIN =>>> " + str(ginfo.name) + " :\n║" + ginfo.creator.displayName + "\n╠═════════════\n" + "║🙏 Semoga Betah Kaka 😘 \n╚═════════════")
               random.choice(KAC).sendText(op.param1,"Jam " + datetime.today().strftime('%H:%M:%S') + " Waktu Taiwan")
               random.choice(KAC).sendImageWithURL(op.param1, "http://dl.profile.line-cdn.net/" + h.pictureStatus)
               random.choice(KAC).sendImageWithURL(op.param1, path)
               print "MEMBER HAS JOIN THE GROUP"
        if op.type == 15:
            if wait["Lv"] == True:
                if op.param2 in Bots:
                    return
                ginfo = ar1.getGroup(op.param1)
                G = ar1.getGroup(op.param1)
                h = ar1.getContact(op.param2)
                cu = ar1.channel.getCover(op.param2)
                path = str(cu)
                random.choice(KAC).sendText(op.param1,"Bernama: " + h.displayName + "\nStatus:\n" + h.statusMessage)
                random.choice(KAC).sendText(op.param1,"╔═════════════\n║Telah Berpulang Ke Anu\n╚═════════════")
                random.choice(KAC).sendText(op.param1, "╔═════════════\n║Selamat Jalan Kaka\n║Semoga Bahagia disana 😊 \n║Salam Dari " + str(ginfo.name) + " \n╚═════════════")
                random.choice(KAC).sendText(op.param1,"Jam " + datetime.today().strftime('%H:%M:%S') + " Waktu Taiwan")
                random.choice(KAC).sendImageWithURL(op.param1, "http://dl.profile.line-cdn.net/" + h.pictureStatus)
                random.choice(KAC).sendImageWithURL(op.param1, path)
                print "MEMBER HAS LEFT THE GROUP"
#--------------------------------------------------------
            elif msg.text is None:
                return
#--------------------------------------------------------
#==============================================#
        if op.type == 17:
            if op.param2 not in Bots or admin:
                if op.param2 in Bots:
                    pass
            if wait["protect"] == True:
                if wait["blacklist"][op.param2] == True:
                    try:
                        random.choice(KAC).kickoutFromGroup(op.param1,[op.param2])
                        G = ar1.getGroup(op.param1)
                        G.preventJoinByTicket = True
                        ar1.updateGroup(G)
                    except:
                        try:
                            random.choice(KAC).kickoutFromGroup(op.param1,[op.param2])
                            G = ar1.getGroup(op.param1)
                            G.preventJoinByTicket = True
                            ar1.updateGroup(G)
                        except:
                            pass
        if op.type == 19:
            if op.param2 not in Bots or admin:
                if op.param2 in Bots:
                    pass
                elif wait["protect"] == True:
                    wait ["blacklist"][op.param2] = True
                    random.choice(KAC).kickoutFromGroup(op.param1,[op.param2])
                    random.choice(KAC).inviteIntoGroup(op.param1,[op.param3])
        if op.type == 13:
            if op.param2 not in Bots or admin:
                if op.param2 in Bots:
                    pass
                elif wait["inviteprotect"] == True:
                    wait ["blacklist"][op.param2] = True
                    random.choice(KAC).cancelGroupInvitation(op.param1,[op.param3])
                    random.choice(KAC).kickoutFromGroup(op.param1,[op.param2])
                    if op.param2 not in Bots and admin:
                        if op.param2 in Bots:
                            pass
                        elif wait["inviteprotect"] == True:
                            wait ["blacklist"][op.param2] = True
                            random.choice(KAC).cancelGroupInvitation(op.param1,[op.param3])
                            random.choice(KAC).kickoutFromGroup(op.param1,[op.param2])
                            if op.param2 not in Bots or admin:
                                if op.param2 in Bots:
                                    pass
                                elif wait["cancelprotect"] == True:
                                    wait ["blacklist"][op.param2] = True
                                    random.choice(KAC).cancelGroupInvitation(op.param1,[op.param3])
        if op.type == 11:
            if op.param2 not in Bots or admin:
                if op.param2 in Bots:
                    pass
                elif wait["linkprotect"] == True:
                    wait ["blacklist"][op.param2] = True
                    G = ar1.getGroup(op.param1)
                    G.preventJoinByTicket = True
                    ar1.updateGroup(G)
                    random.choice(KAC).kickoutFromGroup(op.param1,[op.param2])
        if op.type == 5:
            if wait["autoAdd"] == True:
                if (wait["message"] in [""," ","\n",None]):
                    pass
                else:
                    ar1.sendText(op.param1,str(wait["message"]))

        if op.type == 11:
            if wait["linkprotect"] == True:
                if op.param2 not in Bots or admin:
                    G = ar1.getGroup(op.param1)
                    G.preventJoinByTicket = True
                    random.choice(KAC).kickoutFromGroup(op.param1,[op.param3])
                    ar1.updateGroup(G)

        if op.type == 13:
           if wait["Protectguest"] == True:
               if op.param2 not in Bots or admin:
                if op.param2 in Bots:
                    random.choice(KAC).cancelGroupInvitation(op.param1,[op.param3])
                    random.choice(KAC).kickoutFromGroup(op.param1,[op.param2])

        if op.type == 17:
           if wait["Protectjoin"] == True:
               if op.param2 not in Bots or admin:
                if op.param2 in Bots:
                    random.choice(DEF).kickoutFromGroup(op.param1,[op.param2])
#==============================================================================#
#------------------------------------------------------------------------------#

        if op.type == 55:
            try:
                if op.param1 in wait2['readPoint']:
           
                    if op.param2 in wait2['readMember'][op.param1]:
                        pass
                    else:
                        wait2['readMember'][op.param1] += op.param2
                    wait2['ROM'][op.param1][op.param2] = op.param2
                    with open('sider.json', 'w') as fp:
                     json.dump(wait2, fp, sort_keys=True, indent=4)
                else:
                    pass
            except:
                pass           
            
        
        if op.type == 59:
            print op
    
    
    except Exception as error:
        print error

def autolike():
    count = 1
    while True:
        try:
           for posts in ar1.activity(1)["result"]["posts"]:
             if posts["postInfo"]["liked"] is False:
                if wait['likeOn'] == True:
                   ar1.like(posts["userInfo"]["writerMid"], posts["postInfo"]["postId"], 1001)
                   print "Like"
                   if wait["commentOn"] == True:
                      if posts["userInfo"]["writerMid"] in wait["commentBlack"]:
                         pass
                      else:
                          ar1.comment(posts["userInfo"]["writerMid"],posts["postInfo"]["postId"],wait["comment"])
        except:
            count += 1
            if(count == 50):
                sys.exit(0)
            else:
                pass
thread2 = threading.Thread(target=autolike)
thread2.daemon = True
thread2.start()

def likefriend():
    for zx in range(0,20):
      hasil = ar1.activity(limit=20)
      if hasil['result']['posts'][zx]['postInfo']['liked'] == False:
        try:
          ar1.like(hasil['result']['posts'][zx]['userInfo']['mid'],hasil['result']['posts'][zx]['postInfo']['postId'],likeType=1001)
          ar1.comment(hasil['result']['posts'][zx]['userInfo']['mid'],hasil['result']['posts'][zx]['postInfo']['postId'],"Auto Like by ՏվղժíϲɑԵҽ")
          print "Like"
        except:
          pass
      else:
          print "Already Liked Om"
time.sleep(0.60)

def likeme():
    for zx in range(0,20):
        hasil = ar1.activity(limit=20)
        if hasil['result']['posts'][zx]['postInfo']['liked'] == False:
            if hasil['result']['posts'][zx]['userInfo']['mid'] in mid:
                try:
                    ar1.like(hasil['result']['posts'][zx]['userInfo']['mid'],hasil['result']['posts'][zx]['postInfo']['postId'],likeType=1002)
                    ar1.comment(hasil['result']['posts'][zx]['userInfo']['mid'],hasil['result']['posts'][zx]['postInfo']['postId'],"Auto Like by ՏվղժíϲɑԵҽ")
                    print "Like"
                except:
                    pass
            else:
                print "Status Sudah di Like Om"


while True:
    try:
        Ops = ar1.fetchOps(ar1.Poll.rev, 5)
    except EOFError:
        raise Exception("It might be wrong revision\n" + str(ar1.Poll.rev))

    for Op in Ops:
        if (Op.type != OpType.END_OF_OPERATION):
            ar1.Poll.rev = max(ar1.Poll.rev, Op.revision)
            bot(Op)
