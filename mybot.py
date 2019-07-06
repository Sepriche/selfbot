# -*- coding: utf-8 -*- 
import sepriche
from sepriche import *
from sepri.ttypes import *
from thrift.TMultiplexedProcessor import *
from thrift.TSerialization import *
from thrift.TRecursive import *
from thrift import transport, protocol, server
from datetime import datetime
import pytz, pafy, time, asyncio, random, multiprocessing, timeit, sys, json, ctypes, codecs, tweepy, threading, glob, re, ast, six, os, subprocess, wikipedia, atexit, goslate, urllib, urllib.parse, urllib3, string, tempfile, shutil, unicodedata
from humanfriendly import format_timespan, format_size, format_number, format_length
import html5lib
import requests,json,urllib3
from random import randint
from bs4 import BeautifulSoup
from time import sleep
from googletrans import Translator
import youtube_dl
#===============================#
sepri = LINE('EGwAAHyiqkF6TqeDC1V0.dJDcqR7GElvv2z8FUzJX8a.02kYz/KISGNYidIARy8G+OIwgOoXe+sMDMw6aNRQ8yI=')
sepri.log("Auth Token : " + str(sepri.authToken))
print ("=== LOGIN SUCCES ===\n =[Sepri bot siap digunakan]=\n =TEAM FUNKZHER BOT PROTECTION=")
#===============================#
oepoll = OEPoll(sepri)
call = (sepri)
mid = sepri.getProfile().mid
Bots = [mid]
creator = ["u0e374242bee078b555d99f1fb998f1f0"]
owner = ["u0e374242bee078b555d99f1fb998f1f0"]
admin = ["u0e374242bee078b555d99f1fb998f1f0"]
staff = ["u0e374242bee078b555d99f1fb998f1f0"]
#===============================#
myProfile = {
	"displayName": "",
	"statusMessage": "",
	"pictureStatus": ""
}
protectqr = []
protectkick = []
protectjoin = []
protectinvite = []
protectcancel = []
welcome = []
scProfile = sepri.getProfile()
myProfile["displayName"] = scProfile.displayName
myProfile["statusMessage"] = scProfile.statusMessage
myProfile["pictureStatus"] = scProfile.pictureStatus

cctv = {
    "cyduk":{},
    "point":{},
    "sidermem":{}
}

with open('creator.json', 'r') as fp:
    creator = json.load(fp)
with open('owner.json', 'r') as fp:
    owner = json.load(fp)
with open('admin.json', 'r') as fp:
    admin = json.load(fp)    

Setbot1 = codecs.open("setting.json","r","utf-8")
Setmain = json.load(Setbot1)
Setbot2 = codecs.open("settings.json","r","utf-8")
settings = json.load(Setbot2)
Setbot3 = codecs.open("wait.json","r","utf-8")
wait = json.load(Setbot3)
Setbot4 = codecs.open("read.json","r","utf-8")
read = json.load(Setbot4)

mulai = time.time()

msg_dict = {}
msg_dict1 = {}

tz = pytz.timezone("Asia/Jakarta")
timeNow = datetime.now(tz=tz)

def download_page(url):
    version = (3,0)
    cur_version = sys.version_info
    if cur_version >= version:     
        import urllib,request
        try:
            headers = {}
            headers['User-Agent'] = "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.36"
            req = urllib,request.Request(url, headers = headers)
            resp = urllib,request.urlopen(req)
            respData = str(resp.read())
            return respData
        except Exception as e:
            print(str(e))
    else:                        
        import urllib2
        try:
            headers = {}
            headers['User-Agent'] = "Mozilla/5.0 (X11; Linux i686) AppleWebKit/537.17 (KHTML, like Gecko) Chrome/24.0.1312.27 Safari/537.17"
            req = urllib2.Request(url, headers = headers)
            response = urllib2.urlopen(req)
            page = response.read()
            return page
        except:
            return"Page Not found"
            
def cTime_to_datetime(unixtime):
    return datetime.fromtimestamp(int(str(unixtime)[:len(str(unixtime))-3]))
    
def dt_to_str(dt):
    return dt.strftime('%H:%M:%S')

def delete_log():
    ndt = datetime.now()
    for data in msg_dict:
        if (datetime.utcnow() - cTime_to_datetime(msg_dict[data]["createdTime"])) > datetime.timedelta(1):
            del msg_dict[msg_id]

def atend():
    print("Saving")
    with open("Log_data.json","w",encoding='utf8') as f:
        json.dump(msg_dict, f, ensure_ascii=False, indent=4,separators=(',', ': '))
    print("BYE")

def _images_get_all_items(page):
    items = []
    while True:
        item, end_content = _images_get_next_item(page)
        if item == "no_links":
            break
        else:
            items.append(item)      
            time.sleep(0.1)        
            page = page[end_content:]
    return items
    
def backupData():
    try:
        backup1 = Setmain
        f = codecs.open('setting.json','w','utf-8')
        json.dump(backup1, f, sort_keys=True, indent=4, ensure_ascii=False)
        backup2 = settings
        f = codecs.open('settings.json','w','utf-8')
        json.dump(backup2, f, sort_keys=True, indent=4, ensure_ascii=False)
        backup3 = wait
        f = codecs.open('wait.json','w','utf-8')
        json.dump(backup3, f, sort_keys=True, indent=4, ensure_ascii=False)
        backup4 = read
        f = codecs.open('read.json','w','utf-8')
        json.dump(backup4, f, sort_keys=True, indent=4, ensure_ascii=False)        
        return True
    except Exception as error:
        logError(error)
        return False     

def restartBot():
    backupData()
    python = sys.executable
    os.execl(python, python, *sys.argv)

def waktu(secs):
    mins, secs = divmod(secs,60)
    hours, mins = divmod(mins,60)
    days, hours = divmod(hours, 24)
    return '%02d Hari %02d Jam %02d Menit %02d Detik' % (days, hours, mins, secs)

def runtime(secs):
    mins, secs = divmod(secs,60)
    hours, mins = divmod(mins,60)
    days, hours = divmod(hours, 24)
    return '%02d Hari %02d Jam %02d Menit %02d Detik' % (days, hours, mins, secs)

def mentionMembers(to, mid):
    try:
        arrData = ""
        textx = "Total Mention User「{}」\n\n  [ Mention ]\n1. ".format(str(len(mid)))
        arr = []
        no = 1
        num = 2
        for i in mid:
            mention = "@x\n"
            slen = str(len(textx))
            elen = str(len(textx) + len(mention) - 1)
            arrData = {'S':slen, 'E':elen, 'M':i}
            arr.append(arrData)
            textx += mention
            if no < len(mid):
                no += 1
                textx += "%i. " % (num)
                num=(num+1)
            else:
                try:
                    no = "\n┗━━[ {} ]".format(str(sepri.getGroup(to).name))
                except:
                    no = "\n┗━━[ Success ]"
        sepri.sendMessage(to, textx, {'MENTION': str('{"MENTIONEES":' + json.dumps(arr) + '}')}, 0)
    except Exception as error:
        sepri.sendMessage(to, "[ INFO ] Error :\n" + str(error))

def siderMembers(to, mid):
    try:
        arrData = ""
        textx = "Total Sider User「{}」\nHaii ".format(str(len(mid)))
        arr = []
        no = 1
        num = 2
        for i in mid:
            mention = "@x\n"
            slen = str(len(textx))
            elen = str(len(textx) + len(mention) - 1)
            arrData = {'S':slen, 'E':elen, 'M':i}
            arr.append(arrData)
            textx += mention+wait["mention"]
            if no < len(mid):
                no += 1
                textx += "%i. " % (num)
                num=(num+1)
            else:
                try:
                    no = "\n┗━━[ {} ]".format(str(sepri.getGroup(to).name))
                except:
                    no = "\n┗━━[ Success ]"
        sepri.sendMessage(to, textx, {'MENTION': str('{"MENTIONEES":' + json.dumps(arr) + '}')}, 0)
    except Exception as error:
        sepri.sendMessage(to, "[ INFO ] Error :\n" + str(error))

def welcomeMembers(to, mid):
    try:
        arrData = ""
        textx = "Total Member Masuk「{}」\nHaii  ".format(str(len(mid)))
        arr = []
        no = 1
        num = 2
        for i in mid:
            ginfo = sepri.getGroup(to)
            mention = "@x\n"
            slen = str(len(textx))
            elen = str(len(textx) + len(mention) - 1)
            arrData = {'S':slen, 'E':elen, 'M':i}
            arr.append(arrData)
            textx += mention+wait["welcome"]+"\nDi group "+str(ginfo.name)
            if no < len(mid):
                no += 1
                textx += "%i " % (num)
                num=(num+1)
            else:
                try:
                    no = "\n┗━━[ {} ]".format(str(sepri.getGroup(to).name))
                except:
                    no = "\n┗━━[ Success ]"
        sepri.sendMessage(to, textx, {'MENTION': str('{"MENTIONEES":' + json.dumps(arr) + '}')}, 0)
    except Exception as error:
        sepri.sendMessage(to, "[ INFO ] Error :\n" + str(error))
        
def leaveMembers(to, mid):
    try:
        arrData = ""
        textx = "Total Member baper「{}」\nByee  ".format(str(len(mid)))
        arr = []
        no = 1
        num = 2
        for i in mid:
            ginfo = sepri.getGroup(to)
            mention = "@x\n"
            slen = str(len(textx))
            elen = str(len(textx) + len(mention) - 1)
            arrData = {'S':slen, 'E':elen, 'M':i}
            arr.append(arrData)
            textx += mention+wait["leave"]+"\nDari group "+str(ginfo.name)
            if no < len(mid):
                no += 1
                textx += "%i " % (num)
                num=(num+1)
            else:
                try:
                    no = "\n┗━━[ {} ]".format(str(sepri.getGroup(to).name))
                except:
                    no = "\n┗━━[ Success ]"
        sepri.sendMessage(to, textx, {'MENTION': str('{"MENTIONEES":' + json.dumps(arr) + '}')}, 0)
    except Exception as error:
        sepri.sendMessage(to, "[ INFO ] Error :\n" + str(error))        

def sendMention(to, mid, firstmessage):
    try:
        arrData = ""
        text = "%s " %(str(firstmessage))
        arr = []
        mention = "@x \n"
        slen = str(len(text))
        elen = str(len(text) + len(mention) - 1)
        arrData = {'S':slen, 'E':elen, 'M':mid}
        arr.append(arrData)
        today = datetime.today()
        future = datetime(2018,3,1)
        hari = (str(future - today))
        comma = hari.find(",")
        hari = hari[:comma]
        teman = sepri.getAllContactIds()
        gid = sepri.getGroupIdsJoined()
        tz = pytz.timezone("Asia/Jakarta")
        timeNow = datetime.now(tz=tz)
        eltime = time.time() - mulai
        bot = runtime(eltime)
        text += mention+"◐ Jam : "+datetime.strftime(timeNow,'%H:%M:%S')+" Wib\n=  Group : "+str(len(gid))+"\n=  Teman : "+str(len(teman))+"\n=  Expired : In "+hari+"\n=  Version : Python3\n=  Tanggal : "+datetime.strftime(timeNow,'%Y-%m-%d')+"\n=  Runtime : \n • "+bot
        sepri.sendMessage(to, text, {'MENTION': str('{"MENTIONEES":' + json.dumps(arr) + '}')}, 0)
    except Exception as error:
        sepri.sendMessage(to, "[ INFO ] Error :\n" + str(error))

def command(text):
    pesan = text.lower()
    if pesan.startswith(Setmain["keyCommand"]):
        cmd = pesan.replace(Setmain["keyCommand"],"")
    else:
        cmd = "command"
    return cmd

def help():
    key = Setmain["keyCommand"]
    key = key.title()
    helpMessage = "╔════════════╗" + "\n" + \
                  "      command " + "\n" + \
                  "╚════════════╝" + "\n" + \
                  "╔════════════╗" + "\n" + \
                  "     ◄]·✪·Menu·✪·[►" + "\n" + \
                  "╠════════════╝" + "\n" + \
                  "╠❂➣ " + key + "Help\n" + \
                  "╠❂➣ " + key + "Help bot\n" + \
                  "╠❂➣ " + key + "Meme\n" + \
                  "╠❂➣ " + key + "Me\n" + \
                  "╠❂➣ " + key + "Mymid\n" + \
                  "╠❂➣ " + key + "Mid「@」\n" + \
                  "╠❂➣ " + key + "Info 「@」\n" + \
                  "╠❂➣ " + key + "Kick1 「@」\n" + \
                  "╠❂➣ " + key + "Mybot\n" + \
                  "╠❂➣ " + key + "Status\n" + \
                  "╠❂➣ " + key + "About\n" + \
                  "╠❂➣ " + key + "Restart\n" + \
                  "╠❂➣ " + key + "Runtime\n" + \
                  "╠❂➣ " + key + "Creator\n" + \
                  "╠❂➣ " + key + "Respon\n" + \
                  "╠❂➣ " + key + "Responcall on/off\n" + \
                  "╠❂➣ " + key + "Setstartcall:\n" + \
                  "╠❂➣ " + key + "Setendcall:\n" + \
                  "╠❂➣ " + key + "Speed/Sp\n" + \
                  "╠❂➣ " + key + "Sprespon\n" + \
                  "╠❂➣ " + key + "Tagall/sepi\n" + \
                  "╠❂➣ " + key + "Ginfo\n" + \
                  "╠❂➣ " + key + "Open\n" + \
                  "╠❂➣ " + key + "Close\n" + \
                  "╠❂➣ " + key + "Url grup\n" + \
                  "╠❂➣ " + key + "Reject\n" + \
                  "╠❂➣ " + key + "Gruplist\n" + \
                  "╠❂➣ " + key + "Infogrup「angka」\n" + \
                  "╠❂➣ " + key + "Infomem「angka」\n" + \
                  "╠❂➣ " + key + "Lurking「on/off」\n" + \
                  "╠❂➣ " + key + "Lurkers\n" + \
                  "╠❂➣ " + key + "Sider「on/off」\n" + \
                  "╠❂➣ " + key + "Updatefoto\n" + \
                  "╠❂➣ " + key + "Updategrup\n" + \
                  "╠❂➣ " + key + "Updatebot\n" + \
                  "╠❂➣ " + key + "Broadcast:「Text」\n" + \
                  "╠❂➣ " + key + "Setkey「New Key」\n" + \
                  "╠❂➣ " + key + "Mykey\n" + \
                  "╠❂➣ " + key + "Resetkey\n" + \
                  "╠❂➣ " + key + "Ytmp3:「Judul Lagu」\n" + \
                  "╠❂➣ " + key + "Ytmp4:「Judul Video\n" + \
                  "╠❂➣ " + key + "Meme@Nama@Teks@Teks\n" + \
                  "╠❂➣ " + key + "1cak\n" + \
                  "╠❂➣ " + key + "Profilesmule:「ID Smule」\n" + \
                  "╠❂➣ " + key + "Randomnumber:「Nmor-Nmor」\n" + \
                  "╠❂➣ " + key + "Gimage:「Keyword」\n" + \
                  "╠❂➣ " + key + "Img food: \n" + \
                  "╠❂➣ " + key + "Cekig:「ID IG」\n" + \
                  "╠❂➣ " + key + "Profileig:「Nama IG」\n" + \
                  "╠❂➣ " + key + "Cekdate:「tgl-bln-thn」\n" + \
                  "╠❂➣ " + key + "Spamtag:「jumlahnya」\n" + \
                  "╠❂➣ " + key + "Spamtag「@」\n" + \
                  "╠❂➣ " + key + "Spamcall:「jumlahnya」\n" + \
                  "╠❂➣ " + key + "Spamcall\n" + \
                  "╠❂➣ " + key + "Notag「on/off」\n" + \
                  "╠❂➣ " + key + "Allpro「on/off」\n" + \
                  "╠❂➣ " + key + "Protecturl「on/off」\n" + \
                  "╠❂➣ " + key + "Protectjoin「on/off」\n" + \
                  "╠❂➣ " + key + "Protectkick「on/off」\n" + \
                  "╠❂➣ " + key + "Protectcancel「on/off」\n" + \
                  "╠❂➣ " + key + "Protectinvite「on/off」\n" + \
                  "╠❂➣ " + key + "Unsend「on/off」\n" + \
                  "╠❂➣ " + key + "Jointicket「on/off」\n" + \
                  "╠❂➣ " + key + "Sticker「on/off」\n" + \
                  "╠❂➣ " + key + "Respon「on/off」\n" + \
                  "╠❂➣ " + key + "Respongift「on/off」\n" + \
                  "╠❂➣ " + key + "Contact「on/off」\n" + \
                  "╠❂➣ " + key + "Autojoin「on/off」\n" + \
                  "╠❂➣ " + key + "Autoadd「on/off」\n" + \
                  "╠❂➣ " + key + "Welcome「on/off」\n" + \
                  "╠❂➣ " + key + "Autoleave「on/off」\n" + \
                  "╠❂➣ " + key + "Admin:on\n" + \
                  "╠❂➣ " + key + "Admin:delete\n" + \
                  "╠❂➣ " + key + "Staff:on\n" + \
                  "╠❂➣ " + key + "Staff:delete\n" + \
                  "╠❂➣ " + key + "Bot:on\n" + \
                  "╠❂➣ " + key + "Bot:delete\n" + \
                  "╠❂➣ " + key + "Adminadd「@」\n" + \
                  "╠❂➣ " + key + "Admindell「@」\n" + \
                  "╠❂➣ " + key + "Staffadd「@」\n" + \
                  "╠❂➣ " + key + "Staffdell「@」\n" + \
                  "╠❂➣ " + key + "Botadd「@」\n" + \
                  "╠❂➣ " + key + "Botdell「@」\n" + \
                  "╠❂➣ " + key + "Refresh\n" + \
                  "╠❂➣ " + key + "Listbot\n" + \
                  "╠❂➣ " + key + "Listadmin\n" + \
                  "╠❂➣ " + key + "Listprotect\n" + \
                  "╠════════════╗" + "\n" + \
                  "      FUNKZHER BOT PROTECTION " + "\n" + \
                  "╠════════════╝" + "\n" + \
                  "╠════════════╗" + "\n" + \
                  "◄]·✪line.me/ti/p/~sepriche✪·[►" + "\n" + \
                  "╚════════════╝"
    return helpMessage

def helpbot():
    key = Setmain["keyCommand"]
    key = key.title()
    helpMessage1 = "╔════════════╗" + "\n" + \
                  "     ™❍✯͜͡ˢᵉᵖʳⁱChe✯͜͡❂➣  " + "\n" + \
                  "╚════════════╝" + "\n" + \
                  "╔════════════╗" + "\n" + \
                  "     ✪·BOT·✪" + "\n" + \
                  "╠════════════╝" + "\n" + \
                  "╠❂➣ " + key + "Mytoken\n" + \
                  "╠❂➣ " + key + "Cek sider\n" + \
                  "╠❂➣ " + key + "Cek spam\n" + \
                  "╠❂➣ " + key + "Cek pesan\n" + \
                  "╠❂➣ " + key + "Cek respon\n" + \
                  "╠❂➣ " + key + "Cek welcome\n" + \
                  "╠❂➣ " + key + "Cek leave\n" + \
                  "╠❂➣ " + key + "Set sider:「Text」\n" + \
                  "╠❂➣ " + key + "Set spam:「Text」\n" + \
                  "╠❂➣ " + key + "Set pesan:「Text」\n" + \
                  "╠❂➣ " + key + "Set respon:「Text」\n" + \
                  "╠❂➣ " + key + "Set welcome:「Text」\n" + \
                  "╠❂➣ " + key + "Set leave:「Text」\n" + \
                  "╠❂➣ " + key + "Myname:「Nama」\n" + \
                  "╠❂➣ " + key + "Gift:「Mid korban」「Jumlah」\n" + \
                  "╠❂➣ " + key + "Spam:「Mid korban」「Jumlah」\n" + \
				  "╠❂➣ " + key + "Spamtag:「jumlahnya」\n" + \
                  "╠❂➣ " + key + "Spamtag「@」\n" + \
                  "╠❂➣ " + key + "Spamcall:「jumlahnya」\n" + \
                  "╠❂➣ " + key + "Spamcall\n" + \
                  "╠❂➣ " + key + "Autoblock on/off\n" + \
				  "╠❂➣ " + key + "Updatefoto\n" + \
                  "╠❂➣ " + key + "Updategrup\n" + \
                  "╠❂➣ " + key + "Updatebot\n" + \
                  "╠❂➣ " + key + "Broadcast:「Text」\n" + \
                  "╠❂➣ " + key + "Setkey「New Key」\n" + \
                  "╠❂➣ " + key + "Mykey\n" + \
                  "╠❂➣ " + key + "Resetkey\n" + \
				  "╠❂➣ " + key + "Self「on/off」\n" + \
                  "╠❂➣ " + key + "Rchat\n" + \
				  "╠❂➣ " + key + "Leave:「Namagrup」\n" + \
                  "╠❂➣ " + key + "Blc\n" + \
                  "╠❂➣ " + key + "Ban:on\n" + \
                  "╠❂➣ " + key + "Unban:on\n" + \
                  "╠❂➣ " + key + "Ban「@」\n" + \
                  "╠❂➣ " + key + "Unban「@」\n" + \
                  "╠❂➣ " + key + "Talkban「@」\n" + \
                  "╠❂➣ " + key + "Untalkban「@」\n" + \
                  "╠❂➣ " + key + "Talkban:on\n" + \
                  "╠❂➣ " + key + "Untalkban:on\n" + \
                  "╠❂➣ " + key + "Banlist\n" + \
                  "╠❂➣ " + key + "Talkbanlist\n" + \
                  "╠❂➣ " + key + "Clearban\n" + \
                  "╠❂➣ " + key + "Refresh\n" + \
                  "╠════════════╗" + "\n" + \
                  "      FUNKZHER BOT PROTECTION " + "\n" + \
                  "╠════════════╝" + "\n" + \
                  "╠════════════╗" + "\n" + \
                  "◄]·✪line.me/ti/p/~sepriche" + "\n" + \
                  "╚════════════╝"
    return helpMessage1
    
def infomeme():
    helpMessage2 = """
╔════════════╗
       MEME
╚════════════╝
╔════════════╗
    ✪·List Meme·✪
╠════════════╝
╠❂➣ Buzz
╠❂➣ Spongebob
╠❂➣ Patrick
╠❂➣ Doge
╠❂➣ Joker
╠❂➣ Xzibit
╠❂➣ You_tried
╠❂➣ cb
╠❂➣ blb
╠❂➣ wonka
╠❂➣ keanu
╠❂➣ cryingfloor
╠❂➣ disastergirl
╠❂➣ facepalm
╠❂➣ fwp
╠❂➣ grumpycat
╠❂➣ captain
╠❂➣ mmm
╠❂➣ rollsafe
╠❂➣ sad-obama
╠❂➣ sad-clinton
╠❂➣ aag
╠❂➣ sarcasticbear
╠❂➣ sk
╠❂➣ sparta
╠❂➣ sad
╠❂➣ contoh:
╠❂➣ Meme@buzz@lu tau?@gatau
╠════════════╗
      FUNKZHER BOT PROTECTION
╠════════════╝
╠════════════╗
◄]·✪line.me/ti/p/~sepriche
╚════════════╝
"""
    return helpMessage2

def bot(op):
    global time
    global ast
    global groupParam
    try:
        if op.type == 0:
            return
        
        if op.type == 11:
            if op.param1 in protectqr:
                try:
                    if sepri.getGroup(op.param1).preventedJoinByTicket == False:
                        if op.param2 not in Bots and op.param2 not in owner and op.param2 not in admin and op.param2 not in staff:
                            sepri.reissueGroupTicket(op.param1)
                            X = sepri.getGroup(op.param1)
                            X.preventedJoinByTicket = True
                            sepri.updateGroup(X)
                            sepri.sendMessage(op.param1, None, contentMetadata={'mid': op.param2}, contentType=13)
                except:
                    pass
        if op.type == 13:
            if mid in op.param3:
                if wait["autoLeave"] == True:
                    if op.param2 not in Bots and op.param2 not in owner and op.param2 not in admin and op.param2 not in staff:
                        sepri.acceptGroupInvitation(op.param1)
                        ginfo = sepri.getGroup(op.param1)
                        sepri.sendMessage(op.param1,"Maaf, autoleave sedang on\n Group " +str(ginfo.name))
                        sepri.leaveGroup(op.param1)
                    else:
                        sepri.acceptGroupInvitation(op.param1)
                        ginfo = sepri.getGroup(op.param1)
                        sepri.sendMessage(op.param1,"Hai " + str(ginfo.name))
        if op.type == 13:
            if mid in op.param3:
                if wait["autoJoin"] == True:
                    if op.param2 not in Bots and op.param2 not in owner and op.param2 not in admin and op.param2 not in staff:
                        sepri.acceptGroupInvitation(op.param1)
                        ginfo = sepri.getGroup(op.param1)
                        sepri.sendMessage(op.param1,"Haii, ")
                    else:
                        sepri.acceptGroupInvitation(op.param1)
                        ginfo = sepri.getGroup(op.param1)
                        sepri.sendMessage(op.param1,"Haii, ")
        if op.type == 13:
            if op.param1 in protectinvite:
                if op.param2 not in Bots and op.param2 not in owner and op.param2 not in admin and op.param2 not in staff:
                    try:
                        group = sepri.getGroup(op.param1)
                        gMembMids = [contact.mid for contact in group.invitee]
                        for _mid in gMembMids:
                            sepri.cancelGroupInvitation(op.param1,[_mid])
                    except:
                        pass
        if op.type == 5:
            print ("[ 5 ] NOTIFIED AUTO BLOCK CONTACT")
            if wait["autoBlock"] == True:
              if op.param2 not in Bots and op.param2 not in owner and op.param2 not in admin and op.param2 not in staff:
                sepri.blockContact(op.param1)
                sepri.sendMessage(op.param1, "sorry autoblock gw aktif")
        if op.type == 15:
            if op.param1 in welcome:
                if op.param2 in Bots:
                    pass
                ginfo = sepri.getGroup(op.param1)
                contact = sepri.getContact(op.param2).picturePath
                image = 'http://dl.profile.line.naver.jp'+contact
                leaveMembers(op.param1, [op.param2])
                sepri.sendImageWithURL(op.param1, image)
        if op.type == 17:
            if op.param2 in wait["blacklist"]:
                random.choice(ABC).kickoutFromGroup(op.param1,[op.param2])
            else:
                pass
        if op.type == 17:
            if op.param1 in welcome:
                if op.param2 in Bots:
                    pass
                ginfo = sepri.getGroup(op.param1)
                contact = sepri.getContact(op.param2)
                image = "http://dl.profile.line-cdn.net/" + contact.pictureStatus
                welcomeMembers(op.param1, [op.param2])
                sepri.sendImageWithURL(op.param1, image)
        if op.type == 17:
            if op.param1 in protectjoin:
                if op.param2 not in Bots and op.param2 not in owner and op.param2 not in admin and op.param2 not in staff:
                    wait["blacklist"][op.param2] = True
                    try:
                        if op.param3 not in wait["blacklist"]:
                        	sepri.kickoutFromGroup(op.param1,[op.param2])
                    except:
                        pass
                return

        if op.type == 0:
            return
        if op.type == 5:
            if wait["autoAdd"] == True:
                if op.param2 not in Bots and op.param2 not in owner and op.param2 not in admin and op.param2 not in staff:
                    if (wait["message"] in [" "," ","\n",None]):
                        pass
                    else:
                        sepri.sendMessage(op.param1, wait["message"])
#===============================#
        if op.type == 19:
            if op.param1 in protectkick:
                if op.param2 not in Bots and op.param2 not in owner and op.param2 not in admin and op.param2 not in staff:
                    wait["blacklist"][op.param2] = True
                    sepri.kickoutFromGroup(op.param1,[op.param2])
                else:
                    pass
        if op.type == 32:
            if op.param1 in protectcancel:
              if op.param3 in Bots:    
                if op.param2 not in Bots and op.param2 not in owner and op.param2 not in admin and op.param2 not in staff:
                    wait["blacklist"][op.param2] = True
                    try:
                        if op.param3 not in wait["blacklist"]:
                            sepri.findAndAddContactsByMid(op.param1,[op.param3])
                            sepri.kickoutFromGroup(op.param1,[op.param2])
                            sepri.inviteIntoGroup(op.param1,[op.param3])
                    except:
                        try:
                            if op.param3 not in wait["blacklist"]:
                                sepri.findAndAddContactsByMid(op.param1,[op.param3])
                                sepri.kickoutFromGroup(op.param1,[op.param2])
                                sepri.inviteIntoGroup(op.param1,[op.param3])
                        except:
                            pass
                return

        if op.type == 19:
            if admin in op.param3:
                if op.param2 in Bots:
                    pass
                if op.param2 in owner:
                    pass
                if op.param2 in admin:
                    pass
                if op.param2 in staff:
                    pass
                else:
                    wait["blacklist"][op.param2] = True
                    try:
                        sepri.findAndAddContactsByMid(op.param1,admin)
                        sepri.inviteIntoGroup(op.param1,admin)
                        sepri.kickoutFromGroup(op.param1,[op.param2])
                    except:
                        pass

                return

            if staff in op.param3:
                if op.param2 in Bots:
                    pass
                if op.param2 in owner:
                    pass
                if op.param2 in admin:
                    pass
                if op.param2 in staff:
                    pass
                else:
                    wait["blacklist"][op.param2] = True
                    try:
                        sepri.findAndAddContactsByMid(op.param1,staff)
                        sepri.inviteIntoGroup(op.param1,staff)
                        sepri.kickoutFromGroup(op.param1,[op.param2])
                    except:
                        pass
                return

        if op.type == 55:
            try:
                if op.param1 in Setmain["SCreadPoint"]:
                   if op.param2 in Setmain["SCreadMember"][op.param1]:
                       pass
                   else:
                       Setmain["SCreadMember"][op.param1][op.param2] = True
                else:
                   pass
            except:
                pass

        if op.type == 55:
            if op.param2 in wait["blacklist"]:
                sepri.kickoutFromGroup(op.param1,[op.param2])
            else:
                pass

            if cctv['cyduk'][op.param1]==True:
                if op.param1 in cctv['point']:
                    Name = sepri.getContact(op.param2).displayName
                    if Name in cctv['sidermem'][op.param1]:
                        pass
                    else:
                        cctv['sidermem'][op.param1] += "\n~ " + Name
                        siderMembers(op.param1, [op.param2])
                        contact = sepri.getContact(op.param2)
                        image = "http://dl.profile.line-cdn.net/" + contact.pictureStatus
                        sepri.sendImageWithURL(op.param1, image)                        

        if op.type == 65:
            if wait["unsend"] == True:
                try:
                    at = op.param1
                    msg_id = op.param2
                    if msg_id in msg_dict:
                        if msg_dict[msg_id]["from"]:
                           if msg_dict[msg_id]["text"] == 'Gambarnya dibawah':
                                ginfo = sepri.getGroup(at)
                                Sepriche = sepri.getContact(msg_dict[msg_id]["from"])
                                zx = ""
                                zxc = ""
                                zx2 = []
                                xpesan =  "「 Gambar Dihapus 」\n• Pengirim : "
                                ret_ = "• Nama Grup : {}".format(str(ginfo.name))
                                ret_ += "\n• Waktu Ngirim : {}".format(dt_to_str(cTime_to_datetime(msg_dict[msg_id]["createdTime"])))
                                ry = str(sepri.displayName)
                                pesan = ''
                                pesan2 = pesan+"@x \n"
                                xlen = str(len(zxc)+len(xpesan))
                                xlen2 = str(len(zxc)+len(pesan2)+len(xpesan)-1)
                                zx = {'S':xlen, 'E':xlen2, 'M':sepri.mid}
                                zx2.append(zx)
                                zxc += pesan2
                                text = xpesan + zxc + ret_ + ""
                                sepri.sendMessage(at, text, contentMetadata={'MENTION':str('{"MENTIONEES":'+json.dumps(zx2).replace(' ','')+'}')}, contentType=0)
                                sepri.sendImage(at, msg_dict[msg_id]["data"])
                           else:
                                ginfo = sepri.getGroup(at)
                                Sepriche = sepri.getContact(msg_dict[msg_id]["from"])
                                ret_ =  "✯͜͡❂➣ 「 Pesan Dihapus 」\n"
                                ret_ += "✯͜͡❂➣  Pengirim : {}".format(str(sepri.displayName))
                                ret_ += "\n✯͜͡❂➣ Nama Grup : {}".format(str(ginfo.name))
                                ret_ += "\n✯͜͡❂➣ Waktu Ngirim : {}".format(dt_to_str(cTime_to_datetime(msg_dict[msg_id]["createdTime"])))
                                ret_ += "\n✯͜͡❂➣ Pesannya : {}".format(str(msg_dict[msg_id]["text"]))
                                sepri.sendMessage(at, str(ret_))
                        del msg_dict[msg_id]
                except Exception as e:
                    print(e)

        if op.type == 65:
            if wait["unsend"] == True:
                try:
                    at = op.param1
                    msg_id = op.param2
                    if msg_id in msg_dict1:
                        if msg_dict1[msg_id]["from"]:
                                ginfo = sepri.getGroup(at)
                                Sepriche = sepri.getContact(msg_dict1[msg_id]["from"])
                                ret_ =  "「 Sticker Dihapus 」\n"
                                ret_ += "• Pengirim : {}".format(str(sepri.displayName))
                                ret_ += "\n• Nama Grup : {}".format(str(ginfo.name))
                                ret_ += "\n• Waktu Ngirim : {}".format(dt_to_str(cTime_to_datetime(msg_dict1[msg_id]["createdTime"])))
                                ret_ += "{}".format(str(msg_dict1[msg_id]["text"]))
                                sepri.sendMessage(at, str(ret_))
                                sepri.sendImage(at, msg_dict1[msg_id]["data"])
                        del msg_dict1[msg_id]
                except Exception as e:
                    print(e)

        if op.type == 25 or op.type == 26:
           if wait["selfbot"] == True:
               msg = op.message
               if msg._from not in Bots:
                 if wait["talkban"] == True:
                   if msg._from in wait["Talkblacklist"]:
                      try:
                          sepri.kickoutFromGroup(msg.to, [msg._from])
                      except:
                          pass
               if 'MENTION' in msg.contentMetadata.keys() != None:
                 if wait["detectMention"] == True:
                   contact = sepri.getContact(msg._from)
                   image = "http://dl.profile.line-cdn.net/" + contact.pictureStatus
                   name = re.findall(r'@(\w+)', msg.text)
                   mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                   mentionees = mention['MENTIONEES']
                   for mention in mentionees:
                        if mention ['M'] in Bots:
                           sepri.sendMessage(msg.to, wait["Respontag"])
                           sepri.sendImageWithURL(msg.to,image)
                           sepri.sendMessage(msg.to, None, contentMetadata={"STKID":"94734116","STKPKGID":"4981191","STKVER":"1"}, contentType=7)
                           break
               if 'MENTION' in msg.contentMetadata.keys() != None:
                 if wait["Mentiongift"] == True:
                   name = re.findall(r'@(\w+)', msg.text)
                   mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                   mentionees = mention['MENTIONEES']
                   for mention in mentionees:
                        if mention ['M'] in Bots:
                           idth = ["a0768339-c2d3-4189-9653-2909e9bb6f58","ec4a14ea-7437-407b-aee7-96b1cbbc1b4b","f35bd31f-5ec7-4b2f-b659-92adf5e3d151","ba1d5150-3b5f-4768-9197-01a3f971aa34","2b4ccc45-7309-47fe-a006-1a1edb846ddb","168d03c3-dbc2-456f-b982-3d6f85f52af2","d4f09a5f-29df-48ac-bca6-a204121ea165","517174f2-1545-43b9-a28f-5777154045a6","762ecc71-7f71-4900-91c9-4b3f213d8b26","2df50b22-112d-4f21-b856-f88df2193f9e"]
                           plihth = random.choice(idth)
                           jenis = ["5","6","7","8"]
                           plihjenis = random.choice(jenis)
                           sepri.sendMessage(msg.to, " ✯͜͡❂➣sukses send gift\ncek pm😛.")
                           sepri.sendMessage(msg._from, None, contentMetadata={"PRDID":plihth,"PRDTYPE":"THEME","MSGTPL":plihjenis}, contentType=9)
                           break                       
               if 'MENTION' in msg.contentMetadata.keys() != None:
                 if wait["Mentionkick"] == True:
                   name = re.findall(r'@(\w+)', msg.text)
                   mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                   mentionees = mention['MENTIONEES']
                   for mention in mentionees:
                        if mention ['M'] in Bots:
                           sepri.sendMessage(msg.to, "oit...")
                           sepri.kickoutFromGroup(msg.to, [msg._from])
                           break
               if msg.contentType == 7:
                 if wait["sticker"] == True:
                    msg.contentType = 0
                    sepri.sendMessage(msg.to,"「Cek ID Sticker」\n=  STKID : " + msg.contentMetadata["STKID"] + "\n✯͜͡❂➣  STKPKGID : " + msg.contentMetadata["STKPKGID"] + "\n✯͜͡❂➣  STKVER : " + msg.contentMetadata["STKVER"]+ "\n\n「Link Sticker」" + "\nline://shop/detail/" + msg.contentMetadata["STKPKGID"])
               if msg.contentType == 13:
                 if wait["contact"] == True:
                    msg.contentType = 0
                    sepri.sendMessage(msg.to,msg.contentMetadata["mid"])
                    if 'displayName' in msg.contentMetadata:
                        contact = sepri.getContact(msg.contentMetadata["mid"])
                        path = sepri.getContact(msg.contentMetadata["mid"]).picturePath
                        image = 'http://dl.profile.line.naver.jp'+path
                        sepri.sendMessage(msg.to,"✯͜͡❂➣  Nama : " + msg.contentMetadata["displayName"] + "\n✯͜͡❂➣  MID : " + msg.contentMetadata["mid"] + "\n✯͜͡❂➣  Status : " + contact.statusMessage + "\n✯͜͡❂➣  Picture URL : http://dl.profile.line-cdn.net/" + contact.pictureStatus)
                        sepri.sendImageWithURL(msg.to, image)

        if op.type == 25 or op.type == 26:
            msg = op.message
            text = msg.text
            msg_id = msg.id
            receiver = msg.to
            sender = msg._from
            if msg.contentType == 0:
                msg_dict[msg.id] = {"text":msg.text,"from":msg._from,"createdTime":msg.createdTime}
                
            if msg.contentType == 1:
                    path = sepri.downloadObjectMsg(msg_id)
                    msg_dict[msg.id] = {"text":'Gambarnya dibawah',"data":path,"from":msg._from,"createdTime":msg.createdTime}
            if msg.contentType == 7:
                   stk_id = msg.contentMetadata["STKID"]
                   stk_ver = msg.contentMetadata["STKVER"]
                   pkg_id = msg.contentMetadata["STKPKGID"]
                   ret_ = "\n\n「 Sticker Info 」"
                   ret_ += "\n• Sticker ID : {}".format(stk_id)
                   ret_ += "\n• Sticker Version : {}".format(stk_ver)
                   ret_ += "\n• Sticker Package : {}".format(pkg_id)
                   ret_ += "\n• Sticker Url : line://shop/detail/{}".format(pkg_id)
                   query = int(stk_id)
                   if type(query) == int:
                            data = 'https://stickershop.line-scdn.net/stickershop/v1/sticker/'+str(query)+'/ANDROID/sticker.png'
                            path = sepri.downloadFileURL(data)
                            msg_dict1[msg.id] = {"text":str(ret_),"data":path,"from":msg._from,"createdTime":msg.createdTime}
                                                      
                            
            if msg.toType == 0 or msg.toType == 2:
               if msg.toType == 0:
                    to = receiver
               elif msg.toType == 2:
                    to = receiver
               if msg.contentType == 7:
                 if wait["sticker"] == True:
                    msg.contentType = 0
                    sepri.sendMessage(msg.to,"Cek ID Sticker\n\nSTKID : " + msg.contentMetadata["STKID"] + "\nSTKPKGID : " + msg.contentMetadata["STKPKGID"] + "\nSTKVER : " + msg.contentMetadata["STKVER"]+ "\n\n「Link Sticker」" + "\nline://shop/detail/" + msg.contentMetadata["STKPKGID"])
               if msg.contentType == 13:
                 if wait["contact"] == True:
                    msg.contentType = 0
                    sepri.sendMessage(msg.to,msg.contentMetadata["mid"])
                    if 'displayName' in msg.contentMetadata:
                        contact = sepri.getContact(msg.contentMetadata["mid"])
                        path = sepri.getContact(msg.contentMetadata["mid"]).picturePath
                        image = 'http://dl.profile.line.naver.jp'+path
                        sepri.sendMessage(msg.to,"Nama : " + msg.contentMetadata["displayName"] + "\nMID : " + msg.contentMetadata["mid"] + "\nStatus Msg : " + contact.statusMessage + "\nPicture URL : http://dl.profile.line-cdn.net/" + contact.pictureStatus)
                        sepri.sendImageWithURL(msg.to, image)

               if msg.contentType == 13:
                 if msg._from in admin:
                  if wait["addbots"] == True:
                    if msg.contentMetadata["mid"] in Bots:
                        sepri.sendMessage(msg.to,"Contact itu sudah jadi anggota bot")
                        wait["addbots"] = True
                    else:
                        Bots.append(msg.contentMetadata["mid"])
                        wait["addbots"] = True
                        sepri.sendMessage(msg.to,"Berhasil menambahkan ke anggota bot")
                 if wait["dellbots"] == True:
                    if msg.contentMetadata["mid"] in Bots:
                        Bots.remove(msg.contentMetadata["mid"])
                        sepri.sendMessage(msg.to,"Berhasil menghapus dari anggota bot")
                    else:
                        wait["dellbots"] = True
                        sepri.sendMessage(msg.to,"Contact itu bukan anggota sepri BOT")
#=======================#
                 if msg._from in admin:
                  if wait["addstaff"] == True:
                    if msg.contentMetadata["mid"] in staff:
                        sepri.sendMessage(msg.to,"Contact itu sudah jadi staff")
                        wait["addstaff"] = True
                    else:
                        staff.append(msg.contentMetadata["mid"])
                        wait["addstaff"] = True
                        sepri.sendMessage(msg.to,"Berhasil menambahkan ke staff")
                 if wait["dellstaff"] == True:
                    if msg.contentMetadata["mid"] in staff:
                        staff.remove(msg.contentMetadata["mid"])
                        sepri.sendMessage(msg.to,"Berhasil menghapus dari staff")
                        wait["dellstaff"] = True
                    else:
                        wait["dellstaff"] = True
                        sepri.sendMessage(msg.to,"Contact itu bukan staff")
#=======================#
                 if msg._from in admin:
                  if wait["addadmin"] == True:
                    if msg.contentMetadata["mid"] in admin:
                        sepri.sendMessage(msg.to,"Contact itu sudah jadi admin")
                        wait["addadmin"] = True
                    else:
                        admin.append(msg.contentMetadata["mid"])
                        wait["addadmin"] = True
                        sepri.sendMessage(msg.to,"Berhasil menambahkan ke admin")
                 if wait["delladmin"] == True:
                    if msg.contentMetadata["mid"] in admin:
                        admin.remove(msg.contentMetadata["mid"])
                        sepri.sendMessage(msg.to,"Berhasil menghapus dari admin")
                    else:
                        wait["delladmin"] = True
                        sepri.sendMessage(msg.to,"Contact itu jago desah")
#===========ADD BLACKLIST============#
                 if msg._from in admin:
                  if wait["wblacklist"] == True:
                    if msg.contentMetadata["mid"] in wait["blacklist"]:
                        sepri.sendMessage(msg.to,"Contact itu sudah ada di blacklist")
                        wait["wblacklist"] = True
                    else:
                        wait["blacklist"][msg.contentMetadata["mid"]] = True
                        wait["wblacklist"] = True
                        sepri.sendMessage(msg.to,"Berhasil menambahkan ke blacklist user")
                  if wait["dblacklist"] == True:
                    if msg.contentMetadata["mid"] in wait["blacklist"]:
                        del wait["blacklist"][msg.contentMetadata["mid"]]
                        sepri.sendMessage(msg.to,"Berhasil menghapus dari blacklist user")
                    else:
                        wait["dblacklist"] = True
                        sepri.sendMessage(msg.to,"Contact itu tidak ada di blacklist")
#===========TALKBAN============#
                 if msg._from in admin:
                  if wait["Talkwblacklist"] == True:
                    if msg.contentMetadata["mid"] in wait["Talkblacklist"]:
                        sepri.sendMessage(msg.to,"Contact itu sudah ada di Talkban")
                        wait["Talkwblacklist"] = True
                    else:
                        wait["Talkblacklist"][msg.contentMetadata["mid"]] = True
                        wait["Talkwblacklist"] = True
                        sepri.sendMessage(msg.to,"Berhasil menambahkan ke Talkban user")
                  if wait["Talkdblacklist"] == True:
                    if msg.contentMetadata["mid"] in wait["Talkblacklist"]:
                        del wait["Talkblacklist"][msg.contentMetadata["mid"]]
                        sepri.sendMessage(msg.to,"Berhasil menghapus dari Talkban user")
                    else:
                        wait["Talkdblacklist"] = True
                        sepri.sendMessage(msg.to,"Contact itu tidak ada di Talkban")
#===========UPDATE FOTO============#
               if msg.contentType == 1:
                 if msg._from in admin:
                    if Setmain["Addimage"] == True:
                        msgid = msg.id
                        fotoo = "https://obs.line-apps.com/talk/m/download.nhn?oid="+msgid
                        headers = sepri.Talk.Headers
                        r = requests.get(fotoo, headers=headers, stream=True)
                        if r.status_code == 200:
                            path = os.path.join(os.path.dirname(__file__), 'dataPhotos/%s.jpg' % Setmain["Img"])
                            with open(path, 'wb') as fp:
                                shutil.copyfileobj(r.raw, fp)
                            sepri.sendMessage(msg.to, "Berhasil menambahkan gambar")
                        Setmain["Img"] = {}
                        Setmain["Addimage"] = False

               if msg.toType == 2:
                 if msg._from in admin:
                   if settings["groupPicture"] == True:
                     path = sepri.downloadObjectMsg(msg_id)
                     settings["groupPicture"] = False
                     sepri.updateGroupPicture(msg.to, path)
                     sepri.sendMessage(msg.to, "Berhasil mengubah foto group")

               if msg.contentType == 1:
                   if msg._from in admin:
                       if mid in Setmain["SCfoto"]:
                            path = sepri.downloadObjectMsg(msg_id)
                            del Setmain["SCfoto"][mid]
                            sepri.updateProfilePicture(path)
                            sepri.sendMessage(msg.to,"Foto berhasil dirubah")

               if msg.contentType == 0:
                    if Setmain["autoRead"] == True:
                        sepri.sendChatChecked(msg.to, msg_id)
                    if text is None:
                        return
                    else:
                        cmd = command(text)
                        if cmd == "help":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                               helpMessage = help()
                               sepri.sendMessage(msg.to, str(helpMessage))
                                                                                       
                        if cmd == "self on":
                            if msg._from in admin:
                                wait["selfbot"] = True
                                sepri.sendMessage(msg.to, "✯͜͡❂➣ Selfbot diaktifkan")
                                
                        elif cmd == "self off":
                            if msg._from in admin:
                                wait["selfbot"] = False
                                sepri.sendMessage(msg.to, "✯͜͡❂➣ Selfbot dinonaktifkan")
                                            
                        elif cmd == "help bot":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                               helpMessage1 = helpbot()
                               sepri.sendMessage(msg.to, str(helpMessage1))
                               
                        elif cmd == "meme":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                               helpMessage2 = infomeme()
                               sepri.sendMessage(msg.to, str(helpMessage2))

                        if cmd == "unsend on":
                            if msg._from in admin:
                                wait["unsend"] = True
                                sepri.sendMessage(msg.to, "✯͜͡❂➣ Deteksi Unsend Diaktifkan")
                                
                        if cmd == "unsend off":
                            if msg._from in admin:
                                wait["unsend"] = False
                                sepri.sendMessage(msg.to, "✯͜͡❂➣ Deteksi Unsend Dinonaktifkan")                                

                        elif cmd == "status":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                tz = pytz.timezone("Asia/Jakarta")
                                timeNow = datetime.now(tz=tz)
                                md = "  ┏━\n┃┃ ✯ ♠️ S T A T U S ♠️✯┃┣━\n"
                                if wait["unsend"] == True: md+="┃┃☣ [ℹ️] Unsend「ON」\n"
                                else: md+="┃┃☣ [⭕️] Unsend「OFF」\n"                                
                                if wait["sticker"] == True: md+="┃┃☣ [ℹ️] Sticker「ON」\n"
                                else: md+="┃┃☣ [⭕️] Sticker「OFF」\n"
                                if wait["contact"] == True: md+="┃┃☣ [ℹ️] Contact「ON」\n"
                                else: md+="┃┃☣ [⭕️] Contact「OFF」\n"
                                if wait["talkban"] == True: md+="┃┃☣ [ℹ️] Talkban「ON」\n"
                                else: md+="┃┃☣ [⭕️] Mode NIKUNG「OFF」\n"
                                if wait["Mentionkick"] == True: md+="┃┃☣ [ℹ️] Notag「ON」\n"
                                else: md+="┃┃☣ [⭕️] Mode SANGE「OFF」\n"
                                if wait["detectMention"] == True: md+="┃┃☣ [ℹ️] Respon「ON」\n"
                                else: md+="┃┃☣ [⭕️] Respon「OFF」\n"
                                if wait["Mentiongift"] == True: md+="┃┃☣ [ℹ️] Respongift「ON」\n"
                                else: md+="┃┃☣ [⭕️] Respongift「OFF」\n"                                
                                if wait["autoJoin"] == True: md+="┃┃☣ [ℹ️] Autojoin「ON」\n"
                                else: md+="┃┃☣ [⭕️] Autojoin「OFF」\n"
                                if settings["autoJoinTicket"] == True: md+="┃┃☣ [ℹ️] Jointicket「ON」\n"
                                else: md+="┃┃☣ [⭕️] Jointicket「OFF」\n"                                
                                if wait["autoAdd"] == True: md+="┃┃☣ [ℹ️] Autoadd「ON」\n"
                                else: md+="┃┃☣ [⭕️] Autoadd「OFF」\n"
                                if msg.to in welcome: md+="┃┃☣ [ℹ️] Welcome「ON」\n"
                                else: md+="┃┃☣ [⭕️] Welcome「OFF」\n"
                                if wait["autoLeave"] == True: md+="┃┃☣ [ℹ️] Autoleave「ON」\n"
                                else: md+="┃┃☣ [⭕️] Autoleave「OFF」\n"
                                if msg.to in protectqr: md+="┃┃☣ [ℹ️] Protecturl「ON」\n"
                                else: md+="┃┃☣ [⭕️] Protecturl「OFF」\n"
                                if msg.to in protectjoin: md+="┃┃☣ [ℹ️] Protectjoin「ON」\n"
                                else: md+="┃┃☣ [⭕️] Protectjoin「OFF」\n"
                                if msg.to in protectkick: md+="┃┃☣ [ℹ️] Protectkick「ON」\n"
                                else: md+="┃┃☣ [⭕️] Protectkick「OFF」\n"
                                if msg.to in protectcancel: md+="┃┃☣ [ℹ️] Protectcancel「ON」\n"
                                else: md+="┃┃☣ [⭕️] Protectcancel「OFF」\n"
                                if msg.to in protectinvite: md+="┃┃☣ [ℹ️] Protectinvite「ON」\n"
                                else: md+="┃┃☣ [⭕️] Protectinvite「OFF」\n"                                                
                                sepri.sendMessage(msg.to, md+"┃┣━━━━━━━━━━━━━━━\n┃┃❧ Tanggal : "+ datetime.strftime(timeNow,'%Y-%m-%d')+"\n┃┃❧ Jam [ "+ datetime.strftime(timeNow,'%H:%M:%S')+" ]\n  ┗━━━━━━━━━━━━━━━")

                        elif cmd == "baper" or text.lower() == 'baper':
                            sepri.sendImageWithURL(msg.to,"puskun aja dul") 
                        elif cmd == "pm" or text.lower() == 'pm':
                            sepri.sendMessage(msg.to, "Udah gak jaman main pm mending vc lansung😄😄")
                        elif cmd == "kojom" or text.lower() == 'mojok':
                            sepri.sendMessage(msg.to, "Hadehh penjahat kelamin kerjanya kojom terus😁😁😁")
                        elif cmd == "sue" or text.lower() == 'suek':
                            sepri.sendMessage(msg.to, "sue ora jamu,. jamu ora sue")
                        elif cmd == "dudul" or text.lower() == 'dodol':
                            sepri.sendMessage(msg.to, "iya,  kayaknya kamu memang dudul wkwkkkk")
                        elif cmd == "asem" or text.lower() == 'sem':
                            sepri.sendMessage(msg.to, "biar asem, tapi banyak tikungan..😄😄😄")
                        elif cmd == "nah" or text.lower() == 'nah':
                            sepri.sendMessage(msg.to, "kenapa kk,, atit ya")
                        elif cmd == "bot" or text.lower() == 'botak':
                            sepri.sendMessage(msg.to, "apa dul")
                        elif cmd == "bah" or text.lower() == 'bahh':
                            sepri.sendMessage(msg.to, "horas bah.., habis beras makan gabah")
                        elif cmd == "naik" or text.lower() == 'naik':
                            sepri.sendMessage(msg.to, "Gak mau naik kk maunya di naikin ")
                        elif cmd == "assalamualaikum" or text.lower() == 'asalamualaikum':
                            sepri.sendMessage(msg.to, "waalaikumsalam kaka")
                        elif cmd == "sepri" or text.lower() == 'cepi':
                            sepri.sendImageWithURL(msg.to,"https://1.bp.blogspot.com/-vdKxC2_KfsQ/W_ZhTOYrh8I/AAAAAAAAAQQ/F9uzi2fSWtkS7JLacRbNo94-oKksIUERgCLcBGAs/s1600/IMG_20180716_233657.JPG") 
                        elif cmd == "funkzher" or text.lower() == 'funkzher':
                            sepri.sendImageWithURL(msg.to,"https://4.bp.blogspot.com/-ep5ISQIVk6g/W_ZiRS6k7AI/AAAAAAAAAQY/rKMINF8byiw0zbC0IH5j7sSgUDXU70zUQCLcBGAs/s1600/PicsArt_11-04-09.02.36.jpg") 
                          
                        elif cmd == "creator" or text.lower() == 'creator':
                            if msg._from in admin:
                                sepri.sendMessage(msg.to,"Creator Bot") 
                                ma = ""
                                for i in creator:
                                    ma = sepri.getContact(i)
                                    sepri.sendMessage(msg.to, None, contentMetadata={'mid': i}, contentType=13)

                        elif cmd == "me" or text.lower() == 'me':
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                               msg.contentType = 13
                               msg.contentMetadata = {'mid': msg._from}
                               sepri.sendMessage(msg.to,"􀌂􀄲􏿿")
                               sepri.sendContact(to, mid)

                        elif text.lower() == "mymid":
                            if msg._from in admin:
                               sepri.sendMessage(msg.to, msg._from)

                        elif ("Mid " in msg.text):
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                               key = eval(msg.contentMetadata["MENTION"])
                               key1 = key["MENTIONEES"][0]["M"]
                               mi = sepri.getContact(key1)
                               sepri.sendMessage(msg.to, "Nama : "+str(mi.displayName)+"\nMID : " +key1)
                               sepri.sendMessage(msg.to, None, contentMetadata={'mid': key1}, contentType=13)

                        elif ("Info " in msg.text):
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                               key = eval(msg.contentMetadata["MENTION"])
                               key1 = key["MENTIONEES"][0]["M"]
                               mi = sepri.getContact(key1)
                               sepri.sendMessage(msg.to, "❧ Nama : "+str(mi.displayName)+"\n=  Mid : " +key1+"\n=  Status : "+str(mi.statusMessage))
                               sepri.sendMessage(msg.to, None, contentMetadata={'mid': key1}, contentType=13)
                               if "videoProfile='{" in str(sepri.getContact(key1)):
                                   sepri.sendVideoWithURL(msg.to, 'http://dl.profile.line.naver.jp'+str(mi.picturePath)+'/vp.small')
                               else:
                                   sepri.sendImageWithURL(msg.to, 'http://dl.profile.line.naver.jp'+str(mi.picturePath))

                        elif cmd == "mybot":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                               msg.contentType = 13
                               msg.contentMetadata = {'mid': mid}
                               sepri.sendMessage(msg)

                        elif text.lower() == "rchat":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                               try:
                                   sepri.removeAllMessages(op.param2)
                                   sepri.sendMessage(msg.to,"✯͜͡❂➣ Chat dibersihkan...")
                               except:
                                   pass

                        elif cmd.startswith("broadcast: "):
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                               sep = text.split(" ")
                               pesan = text.replace(sep[0] + " ","")
                               saya = sepri.getGroupIdsJoined()
                               for group in saya:
                                   sepri.sendMessage(group,"=======[BROADCAST]=======\n\n"+pesan+"\n\nFunkzher")

                        elif text.lower() == "mykey":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                               sepri.sendMessage(msg.to, "「Mykey」\nSetkey bot mu「 " + str(Setmain["keyCommand"]) + " 」")
                               
                        elif cmd.startswith("setkey "):
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                               sep = text.split(" ")
                               key = text.replace(sep[0] + " ","")
                               if key in [""," ","\n",None]:
                                   sepri.sendMessage(msg.to, "Gagal mengganti key")
                               else:
                                   Setmain["keyCommand"] = str(key).lower()
                                   sepri.sendMessage(msg.to, "「Setkey」\nSetkey diganti jadi「{}」".format(str(key).lower()))

                        elif text.lower() == "resetkey":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                               Setmain["keyCommand"] = ""
                               sepri.sendMessage(msg.to, "「Setkey」\nSetkey mu kembali ke awal")

                        elif cmd == "restart":
                          if wait["selfbot"] == True:
                            if msg._from in creator:
                               sepri.sendMessage(msg.to, "✯͜͡❂➣ Restart Sukses")
                               Setmain["restartPoint"] = msg.to
                               restartBot()
                            
                        elif cmd == "runtime":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                               eltime = time.time() - mulai
                               bot = "Aktif " +waktu(eltime)
                               sepri.sendMessage(msg.to,bot)
                            
                        elif cmd == "ginfo":
                          if msg._from in admin:
                            try:
                                G = sepri.getGroup(msg.to)
                                if G.invitee is None:
                                    gPending = "0"
                                else:
                                    gPending = str(len(G.invitee))
                                if G.preventedJoinByTicket == True:
                                    gQr = "Tertutup"
                                    gTicket = "Tidak ada"
                                else:
                                    gQr = "Terbuka"
                                    gTicket = "https://line.me/R/ti/g/{}".format(str(sepri.reissueGroupTicket(G.id)))
                                timeCreated = []
                                timeCreated.append(time.strftime("%d-%m-%Y [ %H:%M:%S ]", time.localtime(int(G.createdTime) / 1000)))
                                sepri.sendMessage(msg.to, "❧ BOT Grup Info\n\n ❧ Nama Group : {}".format(G.name)+ "\n=  ID Group : {}".format(G.id)+ "\n=  Pembuat : {}".format(G.creator.displayName)+ "\n=  Waktu Dibuat : {}".format(str(timeCreated))+ "\n=  Jumlah Member : {}".format(str(len(G.members)))+ "\n=  Jumlah Pending : {}".format(gPending)+ "\n=  Group Qr : {}".format(gQr)+ "\n=  Group Ticket : {}".format(gTicket))
                                sepri.sendMessage(msg.to, None, contentMetadata={'mid': G.creator.mid}, contentType=13)
                                sepri.sendImageWithURL(msg.to, 'http://dl.profile.line-cdn.net/'+G.pictureStatus)
                            except Exception as e:
                                sepri.sendMessage(msg.to, str(e))

                        elif cmd.startswith("infogrup "):
                          if msg._from in admin:
                            separate = text.split(" ")
                            number = text.replace(separate[0] + " ","")
                            groups = sepri.getGroupIdsJoined()
                            ret_ = ""
                            try:
                                group = groups[int(number)-1]
                                G = sepri.getGroup(group)
                                try:
                                    gCreator = G.creator.displayName
                                except:
                                    gCreator = "Tidak ditemukan"
                                if G.invitee is None:
                                    gPending = "0"
                                else:
                                    gPending = str(len(G.invitee))
                                if G.preventedJoinByTicket == True:
                                    gQr = "Tertutup"
                                    gTicket = "Tidak ada"
                                else:
                                    gQr = "Terbuka"
                                    gTicket = "https://line.me/R/ti/g/{}".format(str(sepri.reissueGroupTicket(G.id)))
                                timeCreated = []
                                timeCreated.append(time.strftime("%d-%m-%Y [ %H:%M:%S ]", time.localtime(int(G.createdTime) / 1000)))
                                ret_ += "✯͜͡❂➣  BOT Grup Info\n"
                                ret_ += "\n✯͜͡❂➣  Name : {}".format(G.name)
                                ret_ += "\n✯͜͡❂➣  ID : {}".format(G.id)
                                ret_ += "\n✯͜͡❂➣  Creator : {}".format(gCreator)
                                ret_ += "\n✯͜͡❂➣  Created Time : {}".format(str(timeCreated))
                                ret_ += "\n✯͜͡❂➣  Member : {}".format(str(len(G.members)))
                                ret_ += "\n✯͜͡❂➣  Pending : {}".format(gPending)
                                ret_ += "\n✯͜͡❂➣  Qr : {}".format(gQr)
                                ret_ += "\n✯͜͡❂➣  Ticket : {}".format(gTicket)
                                ret_ += ""
                                sepri.sendMessage(to, str(ret_))
                            except:
                                pass

                        elif cmd.startswith("infomem "):
                          if msg._from in admin:
                            separate = msg.text.split(" ")
                            number = msg.text.replace(separate[0] + " ","")
                            groups = sepri.getGroupIdsJoined()
                            ret_ = ""
                            try:
                                group = groups[int(number)-1]
                                G = sepri.getGroup(group)
                                no = 0
                                ret_ = ""
                                for mem in G.members:
                                    no += 1
                                    ret_ += "\n " "✯͜͡❂➣  "+ str(no) + ". " + mem.displayName
                                sepri.sendMessage(to,"✯͜͡❂➣  Group Name : [ " + str(G.name) + " ]\n\n   [ List Member ]\n" + ret_ + "\n\n「Total %i Members」" % len(G.members))
                            except: 
                                pass

                        elif cmd.startswith("leave: "):
                          if msg._from in admin:
                            separate = msg.text.split(" ")
                            number = msg.text.replace(separate[0] + " ","")
                            groups = sepri.getGroupIdsJoined()
                            group = groups[int(number)-1]
                            for i in group:
                                ginfo = sepri.getGroup(i)
                                if ginfo == group:
                                    ki.leaveGroup(i)
                                    sepri.sendMessage(msg.to,"Berhasil keluar di grup " +str(ginfo.name))

                        elif cmd == "friendlist":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                               ma = ""
                               a = 0
                               gid = sepri.getAllContactIds()
                               for i in gid:
                                   G = sepri.getContact(i)
                                   a = a + 1
                                   end = "\n"
                                   ma += "┃┃ " + str(a) + ". " +G.displayName+ "\n"
                               sepri.sendMessage(msg.to,"┏━━[ FRIEND LIST ]\n┃┃\n"+ma+"┃┃\n┗━━[ Total「"+str(len(gid))+"」Friends ]")

                        elif cmd == "gruplist":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                               ma = ""
                               a = 0
                               gid = sepri.getGroupIdsJoined()
                               for i in gid:
                                   G = sepri.getGroup(i)
                                   a = a + 1
                                   end = "\n"
                                   ma += "┃┃ " + str(a) + ". " +G.name+ "\n"
                               sepri.sendMessage(msg.to,"┏━━[ GROUP LIST ]\n┃┃\n"+ma+"┃┃\n┗━━[ Total「"+str(len(gid))+"」Groups ]")

                        elif cmd == "gruplist1":
                            if msg._from in admin:
                               ma = ""
                               a = 0
                               gid = ki.getGroupIdsJoined()
                               for i in gid:
                                   G = ki.getGroup(i)
                                   a = a + 1
                                   end = "\n"
                                   ma += "┃┃ " + str(a) + ". " +G.name+ "\n"
                               ki.sendMessage(msg.to,"┏━━[ GROUP LIST ]\n┃┃\n"+ma+"┃┃\n┗━━[ Total「"+str(len(gid))+"」Groups ]")


                        elif cmd == "open":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                if msg.toType == 2:
                                   X = ki.getGroup(msg.to)
                                   X.preventedJoinByTicket = False
                                   ki.updateGroup(X)
                                   ki.sendMessage(msg.to, "Url Opened")

                        elif cmd == "close":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                if msg.toType == 2:
                                   X = ki.getGroup(msg.to)
                                   X.preventedJoinByTicket = True
                                   ki.updateGroup(X)
                                   ki.sendMessage(msg.to, "Url Closed")

                        elif cmd == "url grup":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                if msg.toType == 2:
                                   x = ki.getGroup(msg.to)
                                   if x.preventedJoinByTicket == True:
                                      x.preventedJoinByTicket = False
                                      ki.updateGroup(x)
                                   gurl = ki.reissueGroupTicket(msg.to)
                                   ki.sendMessage(msg.to, "Nama : "+str(x.name)+ "\nUrl grup : http://line.me/R/ti/g/"+gurl)

                        elif cmd == "invitelist" or cmd == "listinvite":
                          if msg._from in admin:
                            groups = sepri.getGroupIdsInvited()
                            ret_ = "====「 Invitation List 」"
                            no = 1
                            for gid in groups:
                                group = sepri.getGroup(gid)
                                ret_ += "\n│•{}. {} | {}".format(str(no), str(group.name), str(len(group.members)))
                                no = (no+1)
                            ret_ += "\n│Total {} Pending".format(str(len(groups)))
                            ret_ += "\n├───「 Usage 」───"
                            ret_ += "\n├Accept 「Nomor」"
                            ret_ += "\n├Reject 「Nomor」"
                            ret_ += "\n====「 Funkzher Bot 」"
                            sepri.sendMessage(msg.to, str(ret_))

                        elif cmd == "reject":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                              ginvited = sepri.getGroupIdsInvited()
                              if ginvited != [] and ginvited != None:
                                  for gid in ginvited:
                                      time.sleep(3)
                                      sepri.rejectGroupInvitation(gid)
                                  sepri.sendMessage(msg.to, "♪ᶠᵇᵏ Succes Reject {} Group Invite".format(str(len(ginvited))))
                              else:
                                  sepri.sendMessage(msg.to, "♪ᶠᵇᵏno thing")

#===========BOT UPDATE============#
                        elif cmd == "updategrup":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                              if msg.toType == 2:
                                settings["groupPicture"] = True
                                sepri.sendMessage(msg.to,"Kirim fotonya.....")

                        elif cmd == "updatebot":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                settings["changePicture"] = True
                                ki.sendMessage(msg.to,"Kirim fotonya.....")
                                
                        elif cmd == "updatefoto":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                Setmain["SCfoto"][mid] = True
                                sepri.sendMessage(msg.to,"Kirim fotonya.....")

                        elif cmd.startswith("myname: "):
                          if msg._from in admin:
                            separate = msg.text.split(" ")
                            string = msg.text.replace(separate[0] + " ","")
                            if len(string) <= 10000000000:
                                profile = sepri.getProfile()
                                profile.displayName = string
                                sepri.updateProfile(profile)
                                sepri.sendMessage(msg.to,"Nama diganti jadi " + string + "")

#===========BOT UPDATE============#
                        elif cmd == "tagall" or text.lower() == 'sepi':
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                               group = sepri.getGroup(msg.to)
                               nama = [contact.mid for contact in group.members]
                               nm1, nm2, nm3, nm4,nm5,nm6,nm7, jml = [], [], [], [],[], [], [], len(nama)
                               if jml <= 20:
                                   mentionMembers(msg.to, nama)
                               if jml > 20 and jml < 40:
                                   for i in range (0, 19):
                                       nm1 += [nama[i]]
                                   mentionMembers(msg.to, nm1)
                                   for j in range (20, len(nama)-1):
                                       nm2 += [nama[j]]
                                   mentionMembers(msg.to, nm2)
                               if jml > 40 and jml < 60:
                                   for i in range (0, 19):
                                       nm1 += [nama[i]]
                                   mentionMembers(msg.to, nm1)
                                   for j in range (20, 39):
                                       nm2 += [nama[j]]
                                   mentionMembers(msg.to, nm2)
                                   for k in range (40, len(nama)-1):
                                       nm3 += [nama[k]]
                                   mentionMembers(msg.to, nm3)
                               if jml > 60 and jml < 80:
                                   for i in range (0, 19):
                                       nm1 += [nama[i]]
                                   mentionMembers(msg.to, nm1)
                                   for j in range (20, 39):
                                       nm2 += [nama[j]]
                                   mentionMembers(msg.to, nm2)
                                   for k in range (40, 59):
                                       nm3 += [nama[k]]
                                   mentionMembers(msg.to, nm3)
                                   for l in range (60, len(nama)-1):
                                       nm4 += [nama[l]]
                                   mentionMembers(msg.to, nm4)
                               if jml > 80 and jml < 100:
                                   for i in range (0, 19):
                                       nm1 += [nama[i]]
                                   mentionMembers(msg.to, nm1)
                                   for j in range (20, 39):
                                       nm2 += [nama[j]]
                                   mentionMembers(msg.to, nm2)
                                   for k in range (40, 59):
                                       nm3 += [nama[k]]
                                   mentionMembers(msg.to, nm3)
                                   for l in range (60, 79):
                                       nm4 += [nama[l]]
                                   mentionMembers(msg.to, nm4)
                                   for m in range (80, len(nama)-1):
                                       nm5 += [nama[m]]
                                   mentionMembers(msg.to, nm5)
                               if jml > 100 and jml < 120:
                                   for i in range (0, 19):
                                       nm1 += [nama[i]]
                                   mentionMembers(msg.to, nm1)
                                   for j in range (20, 39):
                                       nm2 += [nama[j]]
                                   mentionMembers(msg.to, nm2)
                                   for k in range (40, 59):
                                       nm3 += [nama[k]]
                                   mentionMembers(msg.to, nm3)
                                   for l in range (60, 79):
                                       nm4 += [nama[l]]
                                   mentionMembers(msg.to, nm4)
                                   for m in range (80, 99):
                                       nm5 += [nama[m]]
                                   mentionMembers(msg.to, nm5)
                                   for n in range (100, len(nama)-1):
                                       nm6 += [nama[n]]
                                   mentionMembers(msg.to, nm6)
                               if jml > 120 and jml < 140:
                                   for i in range (0, 19):
                                       nm1 += [nama[i]]
                                   mentionMembers(msg.to, nm1)
                                   for j in range (20, 39):
                                       nm2 += [nama[j]]
                                   mentionMembers(msg.to, nm2)
                                   for k in range (40, 59):
                                       nm3 += [nama[k]]
                                   mentionMembers(msg.to, nm3)
                                   for l in range (60, 79):
                                       nm4 += [nama[l]]
                                   mentionMembers(msg.to, nm4)
                                   for m in range (80, 99):
                                       nm5 += [nama[m]]
                                   mentionMembers(msg.to, nm5)
                                   for n in range (100, 119):
                                       nm6 += [nama[n]]
                                   mentionMembers(msg.to, nm6)
                                   for o in range (120, len(nama)-1):
                                       nm7 += [nama[o]]
                                   mentionMembers(msg.to, nm7)
                               if jml > 140 and jml < 160:
                                   for i in range (0, 19):
                                       nm1 += [nama[i]]
                                   mentionMembers(msg.to, nm1)
                                   for j in range (20, 39):
                                       nm2 += [nama[j]]
                                   mentionMembers(msg.to, nm2)
                                   for k in range (40, 59):
                                       nm3 += [nama[k]]
                                   mentionMembers(msg.to, nm3)
                                   for l in range (60, 79):
                                       nm4 += [nama[l]]
                                   mentionMembers(msg.to, nm4)
                                   for m in range (80, 99):
                                       nm5 += [nama[m]]
                                   mentionMembers(msg.to, nm5)
                                   for n in range (100, 119):
                                       nm6 += [nama[n]]
                                   mentionMembers(msg.to, nm6)
                                   for o in range (120, 139):
                                       nm7 += [nama[o]]
                                   mentionMembers(msg.to, nm7)
                                   for p in range (140, len(nama)-1):
                                       nm8 += [nama[p]]
                                   mentionMembers(msg.to, nm8)

                        elif cmd == "listbot":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                ma = ""
                                a = 0
                                for m_id in Bots:
                                    a = a + 1
                                    end = '\n'
                                    ma += str(a) + ". " +sepri.getContact(m_id).displayName + "\n"
                                sepri.sendMessage(msg.to,"✯͜͡❂➣  BOT\n\n"+ma+"\nTotal「%s」BOT" %(str(len(Bots))))

                        elif cmd == "listadmin":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                ma = ""
                                mb = ""
                                mc = ""
                                a = 0
                                b = 0
                                c = 0
                                for m_id in owner:
                                    a = a + 1
                                    end = '\n'
                                    ma += str(a) + ". " +sepri.getContact(m_id).displayName + "\n"
                                for m_id in admin:
                                    b = b + 1
                                    end = '\n'
                                    mb += str(b) + ". " +sepri.getContact(m_id).displayName + "\n"
                                for m_id in staff:
                                    c = c + 1
                                    end = '\n'
                                    mc += str(c) + ". " +sepri.getContact(m_id).displayName + "\n"
                                sepri.sendMessage(msg.to,"✯͜͡❂➣  Admin ❍✯͜͡ˢᵉᵖʳⁱBOT\n\n✯͜͡❂➣ Creator BOT:\n"+ma+"\n✯͜͡❂➣ Admin:\n"+mb+"\n✯͜͡❂➣ Staff:\n"+mc+"\n✯͜͡❂➣ Total「%s」" %(str(len(owner)+len(admin)+len(staff))))

                        elif cmd == "listprotect":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                ma = ""
                                mb = ""
                                mc = ""
                                md = ""
                                me = ""
                                a = 0
                                b = 0
                                c = 0
                                d = 0
                                e = 0
                                gid = protectqr
                                for group in gid:
                                    a = a + 1
                                    end = '\n'
                                    ma += str(a) + ". " +sepri.getGroup(group).name + "\n"
                                gid = protectkick
                                for group in gid:
                                    b = b + 1
                                    end = '\n'
                                    mb += str(b) + ". " +sepri.getGroup(group).name + "\n"
                                gid = protectjoin
                                for group in gid:
                                    d = d + 1
                                    end = '\n'
                                    md += str(d) + ". " +sepri.getGroup(group).name + "\n"
                                gid = protectcancel
                                for group in gid:
                                    c = c + 1
                                    end = '\n'
                                    mc += str(c) + ". " +sepri.getGroup(group).name + "\n"
                                gid = protectinvite
                                for group in gid:
                                    e = e + 1
                                    end = '\n'
                                    me += str(e) + ". " +sepri.getGroup(group).name + "\n"                                    
                                sepri.sendMessage(msg.to,"✯͜͡❂➣  ❍✯͜͡ˢᵉᵖʳⁱBOT Protection\n\n✯͜͡❂➣  PROTECT URL :\n"+ma+"\n✯͜͡❂➣  PROTECT KICK :\n"+mb+"\n✯͜͡❂➣  PROTECT JOIN :\n"+md+"\n✯͜͡❂➣  PROTECT CANCEL:\n"+mc+"\n✯͜͡❂➣  PROTECT INVITE :\n"+me+"\nTotal「%s」Protect yang aktif" %(str(len(protectqr)+len(protectkick)+len(protectjoin)+len(protectcancel)+len(protectinvite))))

                        elif cmd == "respon":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                ki.sendMessage(msg.to,responsename1)

                        elif cmd == "assist join":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                try:
                                    anggota = [Amid]
                                    sepri.inviteIntoGroup(msg.to, anggota)
                                    ki.acceptGroupInvitation(msg.to)
                                except:
                                    pass
                                
    
                        elif cmd == "masuk1":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                G = sepri.getGroup(msg.to)
                                ginfo = sepri.getGroup(msg.to)
                                G.preventedJoinByTicket = False
                                sepri.updateGroup(G)
                                invsend = 0
                                Ticket = sepri.reissueGroupTicket(msg.to)
                                ki.acceptGroupInvitationByTicket(msg.to,Ticket)
                                G = gg.getGroup(msg.to)
                                G.preventedJoinByTicket = True
                                ki.updateGroup(G)

                        elif cmd == "..byeme..":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                G = sepri.getGroup(msg.to)
                                ki.sendMessage(msg.to, "Bye bye group "+str(G.name))
                                ki.leaveGroup(msg.to)
                                

                        elif cmd.startswith("leave "):
                            if msg._from in admin:
                                proses = text.split(" ")
                                ng = text.replace(proses[0] + " ","")
                                gid = sepri.getGroupIdsJoined()
                                for i in gid:
                                    h = sepri.getGroup(i).name
                                    if h == ng:
                                        ki.sendMessage(i, "Silahkan admin invite atau masukan kembali")
                                        ki.leaveGroup(i)
                                        sepri.sendMessage(to,"Berhasil keluar dari grup " +h)

                        elif cmd == "assist1":
                            if msg._from in admin:
                                G = sepri.getGroup(msg.to)
                                ginfo = sepri.getGroup(msg.to)
                                G.preventedJoinByTicket = False
                                sepri.updateGroup(G)
                                invsend = 0
                                Ticket = sepri.reissueGroupTicket(msg.to)
                                ki.acceptGroupInvitationByTicket(msg.to,Ticket)
                                G = ki.getGroup(msg.to)
                                G.preventedJoinByTicket = True
                                ki.updateGroup(G)


                        elif cmd == "sprespon":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                get_profile_time_start = time.time()
                                get_profile = sepri.getProfile()
                                get_profile_time = time.time() - get_profile_time_start
                                get_group_time_start = time.time()
                                get_group = sepri.getGroupIdsJoined()
                                get_group_time = time.time() - get_group_time_start
                                get_contact_time_start = time.time()
                                get_contact = sepri.getContact(mid)
                                get_contact_time = time.time() - get_contact_time_start
                                sepri.sendMessage(msg.to, " ❧ BOT Speed respon\n\n - Get Profile\n   %.10f\n - Get Contact\n   %.10f\n - Get Group\n   %.10f" % (get_profile_time/3,get_contact_time/3,get_group_time/3))

                        elif cmd == "speed" or cmd == "sp":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                               start = time.time()
                               sepri.sendMessage(msg.to, "™❍✯͜͡speed...✯͜͡❂➣")
                               elapsed_time = time.time() - start
                               sepri.sendMessage(msg.to, "{} detik".format(str(elapsed_time)))

                        elif cmd == "lurking on":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                 tz = pytz.timezone("Asia/Jakarta")
                                 timeNow = datetime.now(tz=tz)
                                 Setmain['SCreadPoint'][msg.to] = msg_id
                                 Setmain['SCreadMember'][msg.to] = {}
                                 sepri.sendMessage(msg.to, "Lurking berhasil diaktifkan\n\nTanggal : "+ datetime.strftime(timeNow,'%Y-%m-%d')+"\nJam [ "+ datetime.strftime(timeNow,'%H:%M:%S')+" ]")
                            
                        elif cmd == "lurking off":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                 tz = pytz.timezone("Asia/Jakarta")
                                 timeNow = datetime.now(tz=tz)
                                 del Setmain['SCreadPoint'][msg.to]
                                 del Setmain['SCreadMember'][msg.to]
                                 sepri.sendMessage(msg.to, "Lurking berhasil dinoaktifkan\n\nTanggal : "+ datetime.strftime(timeNow,'%Y-%m-%d')+"\nJam [ "+ datetime.strftime(timeNow,'%H:%M:%S')+" ]")
                            
                        elif cmd == "lurkers":
                          if msg._from in admin:
                            if msg.to in Setmain['SCreadPoint']:
                                if Setmain['SCreadMember'][msg.to] != {}:
                                    sche = []
                                    for x in Setmain['SCreadMember'][msg.to]:
                                        sche.append(x)
                                    try:
                                        arrData = ""
                                        textx = "  [ Result {} member ]    \n\n  [ Lurkers ]\n1. ".format(str(len(sche)))
                                        arr = []
                                        no = 1
                                        b = 1
                                        for i in sche:
                                            b = b + 1
                                            end = "\n"
                                            mention = "@x\n"
                                            slen = str(len(textx))
                                            elen = str(len(textx) + len(mention) - 1)
                                            arrData = {'S':slen, 'E':elen, 'M':i}
                                            arr.append(arrData)
                                            tz = pytz.timezone("Asia/Jakarta")
                                            timeNow = datetime.now(tz=tz)
                                            textx += mention
                                            if no < len(sche):
                                                no += 1
                                                textx += str(b) + ". "
                                            else:
                                                try:
                                                    no = "[ {} ]".format(str(sepri.getGroup(msg.to).name))
                                                except:
                                                    no = "  "
                                        msg.to = msg.to
                                        msg.text = textx+"\nTanggal : "+ datetime.strftime(timeNow,'%Y-%m-%d')+"\nJam [ "+ datetime.strftime(timeNow,'%H:%M:%S')+" ]"
                                        msg.contentMetadata = {'MENTION': str('{"MENTIONEES":' + json.dumps(arr) + '}')}
                                        msg.contentType = 0
                                        sepri.sendMessage(msg)
                                    except:
                                        pass
                                    try:
                                        del Setmain['SCreadPoint'][msg.to]
                                        del Setmain['SCreadMember'][msg.to]
                                    except:
                                        pass
                                    Setmain['SCreadPoint'][msg.to] = msg.id
                                    Setmain['SCreadMember'][msg.to] = {}
                                else:
                                    sepri.sendMessage(msg.to, "User kosong...")
                            else:
                                sepri.sendMessage(msg.to, "Ketik lurking on dulu")

                        elif cmd == "autoblock on":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                wait["autoBlock"] = True
                                sepri.sendMessage(msg.to, "Successfully activated")
                        elif cmd == "autoblock off":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                wait["autoBlock"] = False
                                sepri.sendMessage(msg.to, "Disable successfully")
                                
                        elif cmd == "sider on":
                          if wait["selfbot"] == True:
                           if msg._from in admin:
                              try:
                                  tz = pytz.timezone("Asia/Jakarta")
                                  timeNow = datetime.now(tz=tz)
                                  sepri.sendMessage(msg.to, "✯͜͡❂➣Cek sider diaktifkan\n\nTanggal : "+ datetime.strftime(timeNow,'%Y-%m-%d')+"\nJam [ "+ datetime.strftime(timeNow,'%H:%M:%S')+" ]")
                                  sepri.sendMessage(msg.to, None, contentMetadata={"STKID":"11789035","STKPKGID":"1291001","STKVER":"1"}, contentType=7)
                                  del cctv['point'][msg.to]
                                  del cctv['sidermem'][msg.to]
                                  del cctv['cyduk'][msg.to]
                              except:
                                  pass
                              cctv['point'][msg.to] = msg.id
                              cctv['sidermem'][msg.to] = ""
                              cctv['cyduk'][msg.to]=True

                        elif cmd == "sider off":
                          if wait["selfbot"] == True:
                           if msg._from in admin:
                              if msg.to in cctv['point']:
                                  tz = pytz.timezone("Asia/Jakarta")
                                  timeNow = datetime.now(tz=tz)
                                  cctv['cyduk'][msg.to]=False
                                  sepri.sendMessage(msg.to, "✯͜͡❂➣Cek sider dinonaktifkan\n\nTanggal : "+ datetime.strftime(timeNow,'%Y-%m-%d')+"\nJam [ "+ datetime.strftime(timeNow,'%H:%M:%S')+" ]")
                                  sepri.sendMessage(msg.to, None, contentMetadata={"STKID":"15439592","STKPKGID":"1398071","STKVER":"1"}, contentType=7)
                              else:
                                  sepri.sendMessage(msg.to, "Sudak tidak aktif")
        
                        elif cmd.startswith("img food: "):
                          if msg._from in admin:
                                query = msg.text.replace("img food: ","")
                                r = requests.get("https://cryptic-ridge-9197.herokuapp.com/api/imagesearch/" + query + "?offset=1")
                                data=r.text
                                data=json.loads(r.text)
                                if data != []:
                                    for food in data:
                                        sepri.sendImageWithURL(msg.to, str(food["url"]))
                                        
                        elif cmd.startswith("profilesmule: "):
                          if msg._from in admin:    
                            try:
                                separate = msg.text.split(" ")
                                smule = msg.text.replace(separate[0] + " ","")
                                links = ("https://smule.com/"+smule)
                                ss = ("http://api2.ntcorp.us/screenshot/shot?url={}".format(urllib.parse.quote(links)))
                                sepri.sendMessage(msg.to, "Sedang Mencari...")
                                time.sleep(2)
                                sepri.sendMessage(msg.to, "ID Smule : "+smule+"\nLink : "+links)
                                sepri.sendImageWithURL(msg.to, ss)
                            except Exception as error:
                                pass                                
                            	
                            	
                        elif cmd.startswith("meme"):
                          if msg._from in admin:    
                            txt = msg.text.split("@")
                            image = ("http://memegen.link/"+txt[1].replace(" ","_")+"/"+txt[2].replace(" ","_")+"/"+txt[3].replace(" ","_")+".jpg?watermark=none")
                            sepri.sendImageWithURL(msg.to, image)
          

                        elif cmd.startswith("ytmp4: "):
                          if msg._from in admin:
                            try:
                                sep = msg.text.split(" ")
                                textToSearch = msg.text.replace(sep[0] + " ","")
                                query = urllib.parse.quote(textToSearch)
                                search_url="https://www.youtube.com/results?search_query="
                                mozhdr = {'User-Agent': 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-GB; rv:1.9.0.3) Gecko/2008092417 Firefox/3.0.3'}
                                sb_url = search_url + query
                                sb_get = requests.get(sb_url, headers = mozhdr)
                                soupeddata = BeautifulSoup(sb_get.content, "html.parser")
                                yt_links = soupeddata.find_all("a", class_ = "yt-uix-tile-link")
                                x = (yt_links[1])
                                yt_href =  x.get("href")
                                yt_href = yt_href.replace("watch?v=", "")
                                qx = "https://youtu.be" + str(yt_href)
                                vid = pafy.new(qx)
                                stream = vid.streams
                                best = vid.getbest()
                                best.resolution, best.extension
                                for s in stream:
                                    me = best.url
                                    hasil = ""
                                    title = "Judul [ " + vid.title + " ]"
                                    author = '\n\n❧ Author : ' + str(vid.author)
                                    durasi = '\n❧ Duration : ' + str(vid.duration)
                                    suka = '\n❧ Likes : ' + str(vid.likes)
                                    rating = '\n❧ Rating : ' + str(vid.rating)
                                    deskripsi = '\n❧ Deskripsi : ' + str(vid.description)
                                sepri.sendVideoWithURL(msg.to, me)
                                sepri.sendMessage(msg.to,title+ author+ durasi+ suka+ rating+ deskripsi)
                            except Exception as e:
                                sepri.sendMessage(msg.to,str(e))

                        elif cmd.startswith("ytmp3: "):
                          if msg._from in admin:
                            try:
                                sep = msg.text.split(" ")
                                textToSearch = msg.text.replace(sep[0] + " ","")
                                query = urllib.parse.quote(textToSearch)
                                search_url="https://www.youtube.com/results?search_query="
                                mozhdr = {'User-Agent': 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-GB; rv:1.9.0.3) Gecko/2008092417 Firefox/3.0.3'}
                                sb_url = search_url + query
                                sb_get = requests.get(sb_url, headers = mozhdr)
                                soupeddata = BeautifulSoup(sb_get.content, "html.parser")
                                yt_links = soupeddata.find_all("a", class_ = "yt-uix-tile-link")
                                x = (yt_links[1])
                                yt_href =  x.get("href")
                                yt_href = yt_href.replace("watch?v=", "")
                                qx = "https://youtu.be" + str(yt_href)
                                vid = pafy.new(qx)
                                stream = vid.streams
                                bestaudio = vid.getbestaudio()
                                bestaudio.bitrate
                                best = vid.getbest()
                                best.resolution, best.extension
                                for s in stream:
                                    shi = bestaudio.url
                                    me = best.url
                                    vin = s.url
                                    hasil = ""
                                    title = "Judul [ " + vid.title + " ]"
                                    author = '\n\n❧ Author : ' + str(vid.author)
                                    durasi = '\n❧ Duration : ' + str(vid.duration)
                                    suka = '\n❧ Likes : ' + str(vid.likes)
                                    rating = '\n❧ Rating : ' + str(vid.rating)
                                    deskripsi = '\n❧ Deskripsi : ' + str(vid.description)
                                sepri.sendImageWithURL(msg.to, me)
                                sepri.sendAudioWithURL(msg.to, shi)
                                sepri.sendMessage(msg.to,title+ author+ durasi+ suka+ rating+ deskripsi)
                            except Exception as e:
                                sepri.sendMessage(msg.to,str(e))
                                    
                        elif cmd.startswith("profileig: "):
                          if msg._from in admin:
                            try:
                                sep = msg.text.split(" ")
                                instagram = msg.text.replace(sep[0] + " ","")
                                html = requests.get('https://www.instagram.com/' + instagram + '/?')
                                soup = BeautifulSoup(html.text, 'html.parser')
                                data = soup.find_all('meta', attrs={'property':'og:description'})
                                text = data[0].get('content').split()
                                data1 = soup.find_all('meta', attrs={'property':'og:image'})
                                text1 = data1[0].get('content').split()
                                AR = text1[0].replace("s150x150/","")
                                user = "Name: " + text[-2] + "\n"
                                user1 = "Username: " + text[-1] + "\n"
                                followers = "Followers: " + text[0] + "\n"
                                following = "Following: " + text[2] + "\n"
                                post = "Post: " + text[4] + "\n"
                                link = "Link: " + "https://www.instagram.com/" + instagram
                                detail = "========INSTAGRAM INFO ========\n"
                                details = "\n========INSTAGRAM INFO ========"
                                sepri.sendMessage(msg.to, detail + user + user1 + followers + following + post + link + details)
                                sepri.sendImageWithURL(msg.to, AR)
                            except Exception as njer:
                                sepri.sendMessage(msg.to, str(njer))
                                
                        elif cmd.startswith("cekig:"):
                            if msg._from in admin:
                                try:
                                    sep = text.split(" ")
                                    search = text.replace(sep[0] + " ","")
                                    r = requests.get("https://farzain.xyz/api/ig_profile.php?apikey=arTdnVbJkW1EuzDNQrIxQDvHARIDcQ&id={}".format(search))
                                    data = r.text
                                    data = json.loads(data)
                                    if data != []:
                                        ret_ = "┏━━[ Profile Instagram ]"
                                        ret_ += "\n┃┃ Nama : {}".format(str(data["info"]["full_name"]))
                                        ret_ += "\n┃┃ Username : {}".format(str(data["info"]["username"]))
                                        ret_ += "\n┃┃ Bio : {}".format(str(data["info"]["bio"]))
                                        ret_ += "\n┃┃ URL Bio : {}".format(str(data["info"]["url_bio"]))
                                        ret_ += "\n┃┃ Pengikut : {}".format(str(data["count"]["followers"]))
                                        ret_ += "\n┃┃ Diikuti : {}".format(str(data["count"]["followers"]))
                                        ret_ += "\n┃┃ Total Post : {}".format(str(data["count"]["post"]))
                                        ret_ += "\n┗━━[ https://www.instagram.com/{} ]".format(search)
                                        path = data["info"]["profile_pict"]
                                        sepri.sendMessage(to, str(ret_))
                                        sepri.sendImageWithURL(to, str(path))
                                except Exception as e:
                                    sepri.sendMessage(msg.to, str(e))                                  

                        elif cmd.startswith("cekdate: "):
                          if msg._from in admin:
                            sep = msg.text.split(" ")
                            tanggal = msg.text.replace(sep[0] + " ","")
                            r=requests.get('https://script.google.com/macros/exec?service=AKfycbw7gKzP-WYV2F5mc9RaR7yE3Ve1yN91ARs91hp_jHSE02dSv9w&nama=ervan&tanggal='+tanggal)
                            data=r.text
                            data=json.loads(data)
                            lahir = data["data"]["lahir"]
                            usia = data["data"]["usia"]
                            ultah = data["data"]["ultah"]
                            zodiak = data["data"]["zodiak"]
                            sepri.sendMessage(msg.to,"=  I N F O R M A S I = \n\n"+"=  Date Of Birth : "+lahir+"\n=  Age : "+usia+"\n=  Ultah : "+ultah+"\n=  Zodiak : "+zodiak)

                        elif cmd.startswith("spamtag: "):
                          if wait["selfbot"] == True:
                           if msg._from in admin:
                                proses = text.split(":")
                                strnum = text.replace(proses[0] + ":","")
                                num =  int(strnum)
                                Setmain["SClimit"] = num
                                sepri.sendMessage(msg.to,"Total Spamtag Diubah Menjadi " +strnum)

                        elif cmd.startswith("spamcall: "):
                          if wait["selfbot"] == True:
                           if msg._from in admin:
                                proses = text.split(":")
                                strnum = text.replace(proses[0] + ":","")
                                num =  int(strnum)
                                wait["limit"] = num
                                sepri.sendMessage(msg.to,"Total Spamcall Diubah Menjadi " +strnum)

                        elif cmd.startswith("spamtag "):
                          if wait["selfbot"] == True:
                           if msg._from in admin:
                                if 'MENTION' in msg.contentMetadata.keys()!=None:
                                    key = eval(msg.contentMetadata["MENTION"])
                                    key1 = key["MENTIONEES"][0]["M"]
                                    zx = ""
                                    zxc = " "
                                    zx2 = []
                                    pesan2 = "@a"" "
                                    xlen = str(len(zxc))
                                    xlen2 = str(len(zxc)+len(pesan2)-1)
                                    zx = {'S':xlen, 'E':xlen2, 'M':key1}
                                    zx2.append(zx)
                                    zxc += pesan2
                                    msg.contentType = 0
                                    msg.text = zxc
                                    lol = {'MENTION':str('{"MENTIONEES":'+json.dumps(zx2).replace(' ','')+'}')}
                                    msg.contentMetadata = lol
                                    jmlh = int(Setmain["SClimit"])
                                    if jmlh <= 1000:
                                        for x in range(jmlh):
                                            try:
                                                sepri.sendMessage(msg)
                                            except Exception as e:
                                                sepri.sendMessage(msg.to,str(e))
                                    else:
                                        sepri.sendMessage(msg.to,"Jumlah melebihi 1000")
                                        
                        elif cmd == "spamcall":
                          if wait["selfbot"] == True:
                           if msg._from in admin:
                             if msg.toType == 2:
                                group = sepri.getGroup(to)
                                members = [mem.mid for mem in group.members]
                                jmlh = int(wait["limit"])
                                sepri.sendMessage(msg.to, "Berhasil mengundang {} undangan Call Grup".format(str(wait["limit"])))
                                if jmlh <= 1000:
                                  for x in range(jmlh):
                                     try:
                                        call.acquireGroupCallRoute(to)
                                        call.inviteIntoGroupCall(to, contactIds=members)
                                     except Exception as e:
                                        sepri.sendMessage(msg.to,str(e))
                                else:
                                    sepri.sendMessage(msg.to,"Jumlah melebihi batas")

                        elif 'Gift: ' in msg.text:
                          if wait["selfbot"] == True:
                           if msg._from in admin:
                              korban = msg.text.replace('Gift: ','')
                              korban2 = korban.split()
                              midd = korban2[0]
                              jumlah = int(korban2[1])
                              if jumlah <= 1000:
                                  for var in range(0,jumlah):
                                      sepri.sendMessage(midd, None, contentMetadata={'PRDID': 'a0768339-c2d3-4189-9653-2909e9bb6f58', 'PRDTYPE': 'THEME', 'MSGTPL': '5'}, contentType=9)
                                      ki.sendMessage(midd, None, contentMetadata={'PRDID': 'a0768339-c2d3-4189-9653-2909e9bb6f58', 'PRDTYPE': 'THEME', 'MSGTPL': '6'}, contentType=9)

                        elif 'Spam: ' in msg.text:
                          if wait["selfbot"] == True:
                           if msg._from in admin:
                              korban = msg.text.replace('Spam: ','')
                              korban2 = korban.split()
                              midd = korban2[0]
                              jumlah = int(korban2[1])
                              if jumlah <= 1000:
                                  for var in range(0,jumlah):
                                      sepri.sendMessage(midd, str(Setmain["SCmessage1"]))

                                  
                        elif 'Mytoken' in msg.text:
                          if wait["selfbot"] == True:
                           if msg._from in creator:
                               sepri.sendMessage(msg.to,"ini tokenku\n"+sepri.authToken)
#==============================================================================# 

                        elif 'Welcome ' in msg.text:
                           if msg._from in admin:
                              spl = msg.text.replace('Welcome ','')
                              if spl == 'on':
                                  if msg.to in welcome:
                                       msgs = "✯͜͡❂➣ Welcome Msg sudah aktif"
                                  else:
                                       welcome.append(msg.to)
                                       ginfo = sepri.getGroup(msg.to)
                                       msgs = "Welcome Msg diaktifkan\nDi Group : " +str(ginfo.name)
                                  sepri.sendMessage(msg.to, "「Diaktifkan」\n" + msgs)
                              elif spl == 'off':
                                    if msg.to in welcome:
                                         welcome.remove(msg.to)
                                         ginfo = sepri.getGroup(msg.to)
                                         msgs = "Welcome Msg dinonaktifkan\nDi Group : " +str(ginfo.name)
                                    else:
                                         msgs = "✯͜͡❂➣ Welcome Msg sudah tidak aktif"
                                    sepri.sendMessage(msg.to, "「Dinonaktifkan」\n" + msgs)
                                    
#===========Protection============#                                    

                        elif 'Protecturl ' in msg.text:
                           if msg._from in admin:
                              spl = msg.text.replace('Protecturl ','')
                              if spl == 'on':
                                  if msg.to in protectqr:
                                       msgs = "✯͜͡❂➣ Protect url sudah aktif"
                                  else:
                                       protectqr.append(msg.to)
                                       ginfo = sepri.getGroup(msg.to)
                                       msgs = "✯͜͡❂➣ Protect url diaktifkan\nDi Group : " +str(ginfo.name)
                                  sepri.sendMessage(msg.to, "「Diaktifkan」\n" + msgs)
                              elif spl == 'off':
                                    if msg.to in protectqr:
                                         protectqr.remove(msg.to)
                                         ginfo = sepri.getGroup(msg.to)
                                         msgs = "Protect url dinonaktifkan\nDi Group : " +str(ginfo.name)
                                    else:
                                         msgs = "✯͜͡❂➣ Protect url sudah tidak aktif"
                                    sepri.sendMessage(msg.to, "「Dinonaktifkan」\n" + msgs)

                        elif 'Protectkick ' in msg.text:
                           if msg._from in admin:
                              spl = msg.text.replace('Protectkick ','')
                              if spl == 'on':
                                  if msg.to in protectkick:
                                       msgs = "✯͜͡❂➣ Protect kick sudah aktif"
                                  else:
                                       protectkick.append(msg.to)
                                       ginfo = sepri.getGroup(msg.to)
                                       msgs = "✯͜͡❂➣ Protect kick diaktifkan\nDi Group : " +str(ginfo.name)
                                  sepri.sendMessage(msg.to, "「Diaktifkan」\n" + msgs)
                              elif spl == 'off':
                                    if msg.to in protectkick:
                                         protectkick.remove(msg.to)
                                         ginfo = sepri.getGroup(msg.to)
                                         msgs = "✯͜͡❂➣Protect kick dinonaktifkan\nDi Group : " +str(ginfo.name)
                                    else:
                                         msgs = "✯͜͡❂➣Protect kick sudah tidak aktif"
                                    sepri.sendMessage(msg.to, "「Dinonaktifkan」\n" + msgs)

                        elif 'Protectjoin ' in msg.text:
                           if msg._from in admin:
                              spl = msg.text.replace('Protectjoin ','')
                              if spl == 'on':
                                  if msg.to in protectjoin:
                                       msgs = "✯͜͡❂➣ Protect join sudah aktif"
                                  else:
                                       protectjoin.append(msg.to)
                                       ginfo = sepri.getGroup(msg.to)
                                       msgs = "✯͜͡❂➣ Protect join diaktifkan\nDi Group : " +str(ginfo.name)
                                  sepri.sendMessage(msg.to, "「Diaktifkan」\n" + msgs)
                              elif spl == 'off':
                                    if msg.to in protectjoin:
                                         protectjoin.remove(msg.to)
                                         ginfo = sepri.getGroup(msg.to)
                                         msgs = "✯͜͡❂➣ Protect join dinonaktifkan\nDi Group : " +str(ginfo.name)
                                    else:
                                         msgs = "✯͜͡❂➣ Protect join sudah tidak aktif"
                                    sepri.sendMessage(msg.to, "「Dinonaktifkan」\n" + msgs)

                        elif 'Protectcancel ' in msg.text:
                           if msg._from in admin:
                              spl = msg.text.replace('Protectcancel ','')
                              if spl == 'on':
                                  if msg.to in protectcancel:
                                       msgs = "✯͜͡❂➣ Protect cancel sudah aktif"
                                  else:
                                       protectcancel.append(msg.to)
                                       ginfo = sepri.getGroup(msg.to)
                                       msgs = "✯͜͡❂➣ Protect cancel diaktifkan\nDi Group : " +str(ginfo.name)
                                  sepri.sendMessage(msg.to, "「Diaktifkan」\n" + msgs)
                              elif spl == 'off':
                                    if msg.to in protectcancel:
                                         protectcancel.remove(msg.to)
                                         ginfo = sepri.getGroup(msg.to)
                                         msgs = "✯͜͡❂➣Protect cancel dinonaktifkan\nDi Group : " +str(ginfo.name)
                                    else:
                                         msgs = "✯͜͡❂➣Protect cancel sudah tidak aktif"
                                    sepri.sendMessage(msg.to, "「Dinonaktifkan」\n" + msgs)
                                    
                        elif 'Protectinvite ' in msg.text:
                           if msg._from in admin:
                              spl = msg.text.replace('Protectinvite ','')
                              if spl == 'on':
                                  if msg.to in protectinvite:
                                       msgs = "✯͜͡❂➣ Protect invite sudah aktif"
                                  else:
                                       protectinvite.append(msg.to)
                                       ginfo = sepri.getGroup(msg.to)
                                       msgs = "✯͜͡❂➣ Protect invite diaktifkan\nDi Group : " +str(ginfo.name)
                                  sepri.sendMessage(msg.to, "「Diaktifkan」\n" + msgs)
                              elif spl == 'off':
                                    if msg.to in protectinvite:
                                         protectinvite.remove(msg.to)
                                         ginfo = sepri.getGroup(msg.to)
                                         msgs = "✯͜͡❂➣Protect invite dinonaktifkan\nDi Group : " +str(ginfo.name)
                                    else:
                                         msgs = "✯͜͡❂➣Protect invite sudah tidak aktif"
                                    sepri.sendMessage(msg.to, "「Dinonaktifkan」\n" + msgs)                                                                      

                        elif 'Allpro ' in msg.text:
                           if msg._from in admin:
                              spl = msg.text.replace('Allpro ','')
                              if spl == 'on':
                                  if msg.to in protectqr:
                                       msgs = ""
                                  else:
                                       protectqr.append(msg.to)
                                  if msg.to in protectkick:
                                      msgs = ""
                                  else:
                                      protectkick.append(msg.to)
                                  if msg.to in protectinvite:
                                      msgs = ""
                                  else:
                                      protectinvite.append(msg.to)                                      
                                  if msg.to in protectjoin:
                                      msgs = ""
                                  else:
                                      protectjoin.append(msg.to)
                                  if msg.to in protectcancel:
                                      ginfo = sepri.getGroup(msg.to)
                                      msgs = "Semua protect sudah on\nDi Group : " +str(ginfo.name)
                                  else:
                                      protectcancel.append(msg.to)
                                      ginfo = sepri.getGroup(msg.to)
                                      msgs = "Berhasil mengaktifkan semua protect\nDi Group : " +str(ginfo.name)
                                  sepri.sendMessage(msg.to, "「Diaktifkan」\n" + msgs)
                              elif spl == 'off':
                                    if msg.to in protectqr:
                                         protectqr.remove(msg.to)
                                    else:
                                         msgs = ""
                                    if msg.to in protectkick:
                                         protectkick.remove(msg.to)
                                    else:
                                         msgs = ""
                                    if msg.to in protectinvite:
                                         protectinvite.remove(msg.to)
                                    else:
                                         msgs = ""                                         
                                    if msg.to in protectjoin:
                                         protectjoin.remove(msg.to)
                                    else:
                                         msgs = ""
                                    if msg.to in protectcancel:
                                         protectcancel.remove(msg.to)
                                         ginfo = sepri.getGroup(msg.to)
                                         msgs = "Berhasil menonaktifkan semua protect\nDi Group : " +str(ginfo.name)
                                    else:
                                         ginfo = sepri.getGroup(msg.to)
                                         msgs = "Semua protect sudah off\nDi Group : " +str(ginfo.name)
                                    sepri.sendMessage(msg.to, "「Dinonaktifkan」\n" + msgs)

#===========KICKOUT============#

                        elif ("Kick1 " in msg.text):
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                               key = eval(msg.contentMetadata["MENTION"])
                               key["MENTIONEES"][0]["M"]
                               targets = []
                               for x in key["MENTIONEES"]:
                                    targets.append(x["M"])
                               for target in targets:
                                   if target not in Bots:
                                       try:
                                           random.choice(ABC).kickoutFromGroup(msg.to, [target])
                                       except:
                                           pass

#===========ADMIN ADD============#
                        elif ("Adminadd " in msg.text):
                          if wait["selfbot"] == True:
                            if msg._from in creator:
                               key = eval(msg.contentMetadata["MENTION"])
                               key["MENTIONEES"][0]["M"]
                               targets = []
                               for x in key["MENTIONEES"]:
                                    targets.append(x["M"])
                               for target in targets:
                                       try:
                                           admin[target] = True
                                           f=codecs.open('admin.json','w','utf-8')
                                           json.dump(admin, f, sort_keys=True, indent=4,ensure_ascii=False)                                            
                                           sepri.sendMessage(msg.to,"Berhasil menambahkan admin")
                                       except:
                                           pass

                        elif ("Staffadd " in msg.text):
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                               key = eval(msg.contentMetadata["MENTION"])
                               key["MENTIONEES"][0]["M"]
                               targets = []
                               for x in key["MENTIONEES"]:
                                    targets.append(x["M"])
                               for target in targets:
                                       try:
                                           staff.append(target)
                                           sepri.sendMessage(msg.to,"Berhasil menambahkan staff")
                                       except:
                                           pass

                        elif ("Botadd " in msg.text):
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                               key = eval(msg.contentMetadata["MENTION"])
                               key["MENTIONEES"][0]["M"]
                               targets = []
                               for x in key["MENTIONEES"]:
                                    targets.append(x["M"])
                               for target in targets:
                                       try:
                                           Bots.append(target)
                                           sepri.sendMessage(msg.to,"Berhasil menambahkan bot")
                                       except:
                                           pass

                        elif ("Admindell " in msg.text):
                            if msg._from in creator:
                               key = eval(msg.contentMetadata["MENTION"])
                               key["MENTIONEES"][0]["M"]
                               targets = []
                               for x in key["MENTIONEES"]:
                                    targets.append(x["M"])
                               for target in targets:
                                       try:
                                           del admin[target]
                                           f=codecs.open('admin.json','w','utf-8')
                                           json.dump(admin, f, sort_keys=True, indent=4,ensure_ascii=False)                                            
                                           sepri.sendMessage(msg.to,"Berhasil menghapus admin")
                                       except:
                                           pass

                        elif ("Staffdell " in msg.text):
                            if msg._from in admin:
                               key = eval(msg.contentMetadata["MENTION"])
                               key["MENTIONEES"][0]["M"]
                               targets = []
                               for x in key["MENTIONEES"]:
                                    targets.append(x["M"])
                               for target in targets:
                                   if target not in admin:
                                       try:
                                           staff.remove(target)
                                           sepri.sendMessage(msg.to,"Berhasil menghapus admin")
                                       except:
                                           pass

                        elif ("Botdell " in msg.text):
                            if msg._from in admin:
                               key = eval(msg.contentMetadata["MENTION"])
                               key["MENTIONEES"][0]["M"]
                               targets = []
                               for x in key["MENTIONEES"]:
                                    targets.append(x["M"])
                               for target in targets:
                                   if target not in admin:
                                       try:
                                           Bots.remove(target)
                                           sepri.sendMessage(msg.to,"Berhasil menghapus admin")
                                       except:
                                           pass

                        elif cmd == "admin:on" or text.lower() == 'admin:on':
                            if msg._from in admin:
                                wait["addadmin"] = True
                                sepri.sendMessage(msg.to,"Kirim kontaknya...")

                        elif cmd == "admin:delete" or text.lower() == 'admin:delete':
                            if msg._from in admin:
                                wait["delladmin"] = True
                                sepri.sendMessage(msg.to,"Kirim kontaknya...")

                        elif cmd == "staff:on" or text.lower() == 'staff:on':
                            if msg._from in admin:
                                wait["addstaff"] = True
                                sepri.sendMessage(msg.to,"Kirim kontaknya...")

                        elif cmd == "staff:delete" or text.lower() == 'staff:delete':
                            if msg._from in admin:
                                wait["dellstaff"] = True
                                sepri.sendMessage(msg.to,"Kirim kontaknya...")

                        elif cmd == "bot:on" or text.lower() == 'bot:on':
                            if msg._from in admin:
                                wait["addbots"] = True
                                sepri.sendMessage(msg.to,"Kirim kontaknya...")

                        elif cmd == "bot:delete" or text.lower() == 'bot:delete':
                            if msg._from in admin:
                                wait["dellbots"] = True
                                sepri.sendMessage(msg.to,"Kirim kontaknya...")

                        elif cmd == "refresh" or text.lower() == 'refresh':
                            if msg._from in admin:
                                wait["addadmin"] = False
                                wait["delladmin"] = False
                                wait["addstaff"] = False
                                wait["dellstaff"] = False
                                wait["addbots"] = False
                                wait["dellbots"] = False
                                wait["wblacklist"] = False
                                wait["dblacklist"] = False
                                wait["Talkwblacklist"] = False
                                wait["Talkdblacklist"] = False
                                sepri.sendMessage(msg.to,"Berhasil di Refresh...")

                        elif cmd == "contact admin" or text.lower() == 'contact admin':
                                ma = ""
                                for i in admin:
                                    ma = ki.getContact(i)
                                    ki.sendMessage(msg.to, None, contentMetadata={'mid': i}, contentType=13)

                        elif cmd == "contact staff" or text.lower() == 'contact staff':
                                ma = ""
                                for i in staff:
                                    ma = ki.getContact(i)
                                    ki.sendMessage(msg.to, None, contentMetadata={'mid': i}, contentType=13)

                        elif cmd == "contact bot" or text.lower() == 'contact bot':
                                ma = ""
                                for i in Bots:
                                    ma = ki.getContact(i)
                                    ki.sendMessage(msg.to, None, contentMetadata={'mid': i}, contentType=13)

#===========COMMAND ON OFF============#
                        elif cmd == "notag on" or text.lower() == 'notag on':
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                wait["Mentionkick"] = True
                                sepri.sendMessage(msg.to,"Notag diaktifkan")

                        elif cmd == "notag off" or text.lower() == 'notag off':
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                wait["Mentionkick"] = False
                                sepri.sendMessage(msg.to,"Notag dinonaktifkan")

                        elif cmd == "contact on" or text.lower() == 'contact on':
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                wait["contact"] = True
                                sepri.sendMessage(msg.to,"Deteksi contact diaktifkan")

                        elif cmd == "contact off" or text.lower() == 'contact off':
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                wait["contact"] = False
                                sepri.sendMessage(msg.to,"Deteksi contact dinonaktifkan")

                        elif cmd == "respon on" or text.lower() == 'respon on':
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                wait["detectMention"] = True
                                sepri.sendMessage(msg.to,"✯͜͡❂➣ Auto respon diaktifkan")

                        elif cmd == "respon off" or text.lower() == 'respon off':
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                wait["detectMention"] = False
                                sepri.sendMessage(msg.to,"✯͜͡❂➣ Auto respon dinonaktifkan")
                                
                        elif cmd == "respongift on" or text.lower() == 'respongift on':
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                wait["Mentiongift"] = True
                                sepri.sendMessage(msg.to,"✯͜͡❂➣ Auto respon gift diaktifkan")

                        elif cmd == "respongift off" or text.lower() == 'respongift off':
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                wait["Mentiongift"] = False
                                sepri.sendMessage(msg.to,"✯͜͡❂➣ Auto respon gift dinonaktifkan")                                

                        elif cmd == "autojoin on" or text.lower() == 'autojoin on':
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                wait["autoJoin"] = True
                                sepri.sendMessage(msg.to,"✯͜͡❂➣ Autojoin diaktifkan")

                        elif cmd == "autojoin off" or text.lower() == 'autojoin off':
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                wait["autoJoin"] = False
                                sepri.sendMessage(msg.to,"✯͜͡❂➣ Autojoin dinonaktifkan")

                        elif cmd == "autoleave on" or text.lower() == 'autoleave on':
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                wait["autoLeave"] = True
                                sepri.sendMessage(msg.to,"✯͜͡❂➣ Auto Leave Diaktifkan")

                        elif cmd == "autoleave off" or text.lower() == 'autoleave off':
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                wait["autoLeave"] = False
                                sepri.sendMessage(msg.to,"✯͜͡❂➣ Auto Leave Dimatikan")

                        elif cmd == "autoadd on" or text.lower() == 'autoadd on':
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                wait["autoAdd"] = True
                                sepri.sendMessage(msg.to,"✯͜͡❂➣ Auto Add Diaktifkan")

                        elif cmd == "autoadd off" or text.lower() == 'autoadd off':
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                wait["autoAdd"] = False
                                sepri.sendMessage(msg.to,"✯͜͡❂➣ Auto Add Dimatikan")

                        elif cmd == "sticker on" or text.lower() == 'sticker on':
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                wait["sticker"] = True
                                sepri.sendMessage(msg.to,"✯͜͡❂➣ Detect Sticker Diaktifkan")

                        elif cmd == "sticker off" or text.lower() == 'sticker off':
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                wait["sticker"] = False
                                sepri.sendMessage(msg.to,"✯͜͡❂➣ Detect Sticker Dimatikan")

                        elif cmd == "jointicket on" or text.lower() == 'jointicket on':
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                settings["autoJoinTicket"] = True
                                sepri.sendMessage(msg.to,"✯͜͡❂➣ Auto Join Ticket Diaktifkan")

                        elif cmd == "jointicket off" or text.lower() == 'jointicket off':
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                settings["autoJoinTicket"] = False
                                sepri.sendMessage(msg.to,"✯͜͡❂➣ Auto Join Ticket Dimatikan")

#===========COMMAND BLACKLIST============#
                        elif ("Talkban " in msg.text):
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                               key = eval(msg.contentMetadata["MENTION"])
                               key["MENTIONEES"][0]["M"]
                               targets = []
                               for x in key["MENTIONEES"]:
                                    targets.append(x["M"])
                               for target in targets:
                                       try:
                                           wait["Talkblacklist"][target] = True
                                           sepri.sendMessage(msg.to,"Berhasil menambahkan blacklist")
                                       except:
                                           pass

                        elif ("Untalkban " in msg.text):
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                               key = eval(msg.contentMetadata["MENTION"])
                               key["MENTIONEES"][0]["M"]
                               targets = []
                               for x in key["MENTIONEES"]:
                                    targets.append(x["M"])
                               for target in targets:
                                       try:
                                           del wait["Talkblacklist"][target]
                                           sepri.sendMessage(msg.to,"Berhasil menghapus blacklist")
                                       except:
                                           pass

                        elif cmd == "talkban:on" or text.lower() == 'talkban:on':
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                wait["Talkwblacklist"] = True
                                sepri.sendMessage(msg.to,"Kirim kontaknya...")

                        elif cmd == "untalkban:on" or text.lower() == 'untalkban:on':
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                wait["Talkdblacklist"] = True
                                sepri.sendMessage(msg.to,"Kirim kontaknya...")

                        elif ("Ban " in msg.text):
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                               key = eval(msg.contentMetadata["MENTION"])
                               key["MENTIONEES"][0]["M"]
                               targets = []
                               for x in key["MENTIONEES"]:
                                    targets.append(x["M"])
                               for target in targets:
                                       try:
                                           wait["blacklist"][target] = True
                                           sepri.sendMessage(msg.to,"Berhasil menambahkan blacklist")
                                       except:
                                           pass

                        elif ("Unban " in msg.text):
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                               key = eval(msg.contentMetadata["MENTION"])
                               key["MENTIONEES"][0]["M"]
                               targets = []
                               for x in key["MENTIONEES"]:
                                    targets.append(x["M"])
                               for target in targets:
                                       try:
                                           del wait["blacklist"][target]
                                           sepri.sendMessage(msg.to,"Berhasil menghapus blacklist")
                                       except:
                                           pass

                        elif cmd == "ban:on" or text.lower() == 'ban:on':
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                wait["wblacklist"] = True
                                sepri.sendMessage(msg.to,"Kirim kontaknya...")

                        elif cmd == "unban:on" or text.lower() == 'unban:on':
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                wait["dblacklist"] = True
                                sepri.sendMessage(msg.to,"Kirim kontaknya...")

                        elif cmd == "banlist" or text.lower() == 'banlist':
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                              if wait["blacklist"] == {}:
                                sepri.sendMessage(msg.to,"Tidak ada blacklist")
                              else:
                                ma = ""
                                a = 0
                                for m_id in wait["blacklist"]:
                                    a = a + 1
                                    end = '\n'
                                    ma += str(a) + ". " +sepri.getContact(m_id).displayName + "\n"
                                sepri.sendMessage(msg.to,"✯͜͡❂➣  Blacklist User\n\n"+ma+"\nTotal「%s」Blacklist User" %(str(len(wait["blacklist"]))))

                        elif cmd == "talkbanlist" or text.lower() == 'talkbanlist':
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                              if wait["Talkblacklist"] == {}:
                                sepri.sendMessage(msg.to,"Tidak ada Talkban user")
                              else:
                                ma = ""
                                a = 0
                                for m_id in wait["Talkblacklist"]:
                                    a = a + 1
                                    end = '\n'
                                    ma += str(a) + ". " +sepri.getContact(m_id).displayName + "\n"
                                sepri.sendMessage(msg.to,"✯͜͡❂➣  Talkban User\n\n"+ma+"\nTotal「%s」Talkban User" %(str(len(wait["Talkblacklist"]))))

                        elif cmd == "blc" or text.lower() == 'blc':
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                              if wait["blacklist"] == {}:
                                    sepri.sendMessage(msg.to,"Tidak ada blacklist")
                              else:
                                    ma = ""
                                    for i in wait["blacklist"]:
                                        ma = sepri.getContact(i)
                                        sepri.sendMessage(msg.to, None, contentMetadata={'mid': i}, contentType=13)

                        elif cmd == "clearban" or text.lower() == 'clearban':
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                              wait["blacklist"] = {}
                              ragets = sepri.getContacts(wait["blacklist"])
                              mc = "���%i」User Blacklist" % len(ragets)
                              sepri.sendMessage(msg.to,"✯͜͡❂➣ Sukses membersihkan " +mc)
#===========COMMAND SET============#
                        elif 'Set pesan: ' in msg.text:
                           if msg._from in admin:
                              spl = msg.text.replace('Set pesan: ','')
                              if spl in [""," ","\n",None]:
                                  sepri.sendMessage(msg.to, "Gagal mengganti Pesan Message")
                              else:
                                  wait["message"] = spl
                                  sepri.sendMessage(msg.to, "「Pesan Msg」\nPesan Message diganti jadi :\n\n「{}」".format(str(spl)))

                        elif 'Set welcome: ' in msg.text:
                           if msg._from in admin:
                              spl = msg.text.replace('Set welcome: ','')
                              if spl in [""," ","\n",None]:
                                  sepri.sendMessage(msg.to, "Gagal mengganti Welcome Message")
                              else:
                                  wait["welcome"] = spl
                                  sepri.sendMessage(msg.to, "「Welcome Msg」\nWelcome Message diganti jadi :\n\n「{}」".format(str(spl)))
                                  
                        elif 'Set leave: ' in msg.text:
                           if msg._from in admin:
                              spl = msg.text.replace('Set leave: ','')
                              if spl in [""," ","\n",None]:
                                  sepri.sendMessage(msg.to, "Gagal mengganti Leave Message")
                              else:
                                  wait["leave"] = spl
                                  sepri.sendMessage(msg.to, "「Leave Msg」\nLeave Message diganti jadi :\n\n「{}」".format(str(spl)))                                    

                        elif 'Set respon: ' in msg.text:
                           if msg._from in admin:
                              spl = msg.text.replace('Set respon: ','')
                              if spl in [""," ","\n",None]:
                                  sepri.sendMessage(msg.to, "Gagal mengganti Respon Message")
                              else:
                                  wait["Respontag"] = spl
                                  sepri.sendMessage(msg.to, "「Respon Msg」\nRespon Message diganti jadi :\n\n「{}」".format(str(spl)))

                        elif 'Set spam: ' in msg.text:
                           if msg._from in admin:
                              spl = msg.text.replace('Set spam: ','')
                              if spl in [""," ","\n",None]:
                                  sepri.sendMessage(msg.to, "Gagal mengganti Spam")
                              else:
                                  Setmain["SCmessage1"] = spl
                                  sepri.sendMessage(msg.to, "「Spam Msg」\nSpam Message diganti jadi :\n\n「{}」".format(str(spl)))

                        elif 'Set sider: ' in msg.text:
                           if msg._from in admin:
                              spl = msg.text.replace('Set sider: ','')
                              if spl in [""," ","\n",None]:
                                  sepri.sendMessage(msg.to, "Gagal mengganti Sider Message")
                              else:
                                  wait["mention"] = spl
                                  sepri.sendMessage(msg.to, "「Sider Msg」\nSider Message diganti jadi :\n\n「{}」".format(str(spl)))

                        elif text.lower() == "cek pesan":
                            if msg._from in admin:
                               sepri.sendMessage(msg.to, "「Pesan Msg」\nPesan Message lu :\n\n「 " + str(wait["message"]) + " 」")

                        elif text.lower() == "cek welcome":
                            if msg._from in admin:
                               sepri.sendMessage(msg.to, "「Welcome Msg」\nWelcome Message lu :\n\n「 " + str(wait["welcome"]) + " 」")
                               
                        elif text.lower() == "cek leave":
                            if msg._from in admin:
                               sepri.sendMessage(msg.to, "「Leave Msg」\nLeave Message lu :\n\n「 " + str(wait["leave"]) + " 」")                                 

                        elif text.lower() == "cek respon":
                            if msg._from in admin:
                               sepri.sendMessage(msg.to, "「Respon Msg」\nRespon Message lu :\n\n「 " + str(wait["Respontag"]) + " 」")

                        elif text.lower() == "cek spam":
                            if msg._from in admin:
                               sepri.sendMessage(msg.to, "「Spam Msg」\nSpam Message lu :\n\n「 " + str(Setmain["SCmessage1"]) + " 」")

                        elif text.lower() == "cek sider":
                            if msg._from in admin:
                               sepri.sendMessage(msg.to, "「Sider Msg」\nSider Message lu :\n\n「 " + str(wait["mention"]) + " 」")

#===========JOIN TICKET============#
                        elif "/ti/g/" in msg.text.lower():
                          if wait["selfbot"] == True:
                              if settings["autoJoinTicket"] == True:
                                 link_re = re.compile('(?:line\:\/|line\.me\/R)\/ti\/g\/([a-zA-Z0-9_-]+)?')
                                 links = link_re.findall(text)
                                 n_links = []
                                 for l in links:
                                     if l not in n_links:
                                        n_links.append(l)
                                 for ticket_id in n_links:
                                     group = sepri.findGroupByTicket(ticket_id)
                                     sepri.acceptGroupInvitationByTicket(group.id,ticket_id)
                                     sepri.sendMessage(msg.to, "sukses masuk group: %s" % str(group.name))

    except Exception as error:
        print (error)

while True:
    try:
        ops = oepoll.singleTrace(count=50)
        if ops is not None:
            for op in ops:
                oepoll.setRevision(op.revision)
                thread = threading.Thread(target=bot, args=(op,))
                thread.start()
    except Exception as e:
        print(e)
