# -*- coding: utf-8 -*-
import LINETCR
from LINETCR.lib.curve.ttypes import *
from datetime import datetime
import time, random, sys, ast, re, os, io, json, subprocess, threading, string, codecs, requests, ctypes, urllib, urllib2, urllib3, wikipedia, tempfile
import unicodedata
from bs4 import BeautifulSoup
from urllib import urlopen
from io import StringIO
from threading import Thread
from gtts import gTTS
from googletrans import Translator
cl = LINETCR.LINE()
cl.login(qr=True)
cl.loginResult()
print "1"

#ki = LINETCR.LINE()
#ki.login(token="EnkJAUGe4a84SgvF7BRd.CTtSh9UpBjSFeVe3j2lXxq.rs83YHPpVOLtWhiRyKqu9h32gVgul1faOZDkwQ2xUaE=")
#ki.loginResult()
print "2"

#kk = LINETCR.LINE()
#kk.login(token="EnLSplSXUp7lMvwHDdp6.iPBRaR1RMNZ6JK83Lr8Y1G.M1VrcyOG9MsIpw4emIr4W2whNgzZS00rJC6ZdfHEPXM=")
#kk.loginResult()
print "3"

#kc = LINETCR.LINE()
#kc.login(token="Enyw0hpu28uFSBNJbuS8.JML4H1XdaTwzS9RX/sR/ka.+b+dlD62CXTvZFtAVe9l61eHZN8PnD964c1M4b/qazk=")
#kc.loginResult()
print "4"

#ke = LINETCR.LINE()
#ke.login(token="EnN5T5DTmqKL8hrLnBz5.C14lfzxM4FuxU2yIGWHg5q.fU6wm2WgP9tkY9P+cc0VcHT776fj1bV5eGx8AqD8mx4=")
#ke.loginResult()
print "5"

#ko = LINETCR.LINE()
#ko.login(token="EnCbS4DvCw4gutjwKCN6.8TpVl4F/azavSAKKabg6bG.gX+q3Abo7KTmuTdO03WCNZ3OsJS97uiznrA594WYGz8=")
#ko.loginResult()
print "6"

#ks = LINETCR.LINE()
#ks.login(token="EncPqjrNm9sugaFNqVYf.LrkxplhqaEVpA3t5C4bSJW.v6vfhk0I6lCD02c6IVuHFVBriAhI7JyDfbnGo3NXLRA=")
#ks.loginResult()
print "7"
#xl = LINETCR.LINE()
#xl.login(token="Eng3hevUKg2R21GitTt8.zIYFy2Kc4BnB2ZbU6OWXsa.3wSAQ5Ey6BaVAtepQaSnT1BX0hpa2EfrCs98yVSttvQ=")
#xl.loginResult()
print "8"

#lx = LINETCR.LINE()
#lx.login(token="Eny8YDkGxZkZg1G4vPu0.b8Fj7vmq9zZ3sLz9FZk34a.gVnGmz7a8muAhJglPPFIU7Rh7wtOaDPZmuTpnBCe20E=")
#lx.loginResult()
print "9"

#ww = LINETCR.LINE()
#ww.login(token="En2OGuByPM6EUyb0SMc6.FAuHybZ7rLb5ENH4DM4onG.0qAOCbqXxsJeJLmvEXgaZCR+ojRbCd+UiYne0RYk2RE=")
#ww.loginResult()
print "10"

#pw = LINETCR.LINE()
#pw.login(token="En8jSnkFifsuZ1SPE1if.F+uO1UpBrBXbmqKjbMEGJW.FhVFk6QpUIRnxF8icrkUh2Pf8R+qtkQ61XWsqeLmrzY=")
#pw.loginResult()
print "11"

#ku = LINETCR.LINE()
#ku.login(token="EnXGQPwxmKEppCrWEMO1.kF2FXVi4PyP6crs9fN0a0q.1TLJx/ujFO4Mr46QyW8ZYr3ytMlmixDrfMorFryHaGE=")
#ku.loginResult()
print "12"

#mj = LINETCR.LINE()
#mj.login(token="En7KnCQk1lx91KnGvZT1.kF2FXVi4PyP6crs9fN0a0q.kLN+fmfFOQDihYEhDdpx4Sk4/mYsbeqVJaGtShX8nUU=")
#mj.loginResult()

#k2 = LINETCR.LINE()
#k2.login(token="EnSrcUrGy1UlRHYdHuj9.VWtBSximFtqX1daFa0VL6q.njvNRNcuNzgEbj/PmSxHm2JVc/VBY5qrIzuCYfrmZ2o=")
#k2.loginResult()

#k3 = LINETCR.LINE()
#k3.login(token="EnZvoE9qEzOin790lPf1.ZySAgXWuzXIRX2B8heRO4q.m7QZSKUHSCM6ghAjgdDsJXEAXKZcV2D5EYC0xW5c5/8=")
#k3.loginResult()

#k4 = LINETCR.LINE()
#k4.login(token="EnN1UkEiI7z6bXqSjfSe.f1+n/j5bgp7TlKCoIXIIhG.aCtWDRVvRwBkInN9cpdcCTLBiXHMPV4G7kD2zgy/UoI=")
#k4.loginResult()
# client_id = ''
# client_secret = ''
# access_token = ''
# client = ImgurClient(client_id, client_secret, access_token)
print "BOT TRISAN SUKSES LOGIN"
reload(sys)
sys.setdefaultencoding('utf-8')
album = None
image_path = 'tmp/tmp.jpg'
helpMessage ="""╔═════════════
║𖤓≛≛≛≛≛≛≛≛≛≛≛≛≛≛𖤓
║✰ɞȏṭ קяȏṭєċṭ✰
║𖤓≛≛≛≛≛≛≛≛≛≛≛≛≛≛𖤓
║𖤓Mྂeྂnྂuྂ fྂoྂrྂ  Pྂuྂbྂlྂiྂcྂ𖤓
║╔════════════
║╠⚫️⭐️Gcreator ► Pembuat Grup
║╠⚫️⭐️Ownerlist
║╠⚫⭐ ️Ginfo ►info Grup
║╠⚫️⭐️Ourl ► open QR (New Protect QR)
║╠⚫️⭐️Creator
║╠⚫️⭐️Apakah ► Kerang Ajaib
║╠⚫️⭐️Rate ►  %.
║╠⚫️⭐️San = Cek Sider
║╠⚫️⭐️
║╚════════════
"""
KAC=[cl,ki,kk,kc,ko,ks,ke,lx,xl,ww,pw,ku]
Bots=[cl,ki,kk,kc,ko,ks,ke,lx,xl,ww,pw,ku]
mid = cl.getProfile().mid
Amid = ki.getProfile().mid
Bmid = kk.getProfile().mid
Cmid = kc.getProfile().mid
Gmid = ko.getProfile().mid
Dmid = ks.getProfile().mid
Hmid = ke.getProfile().mid
Lmid = lx.getProfile().mid
Xmid = xl.getProfile().mid
Wmid = ww.getProfile().mid
Pmid = pw.getProfile().mid
Kmid = ku.getProfile().mid

Bots=[mid,Amid,Bmid,Cmid,Gmid,Dmid,Hmid,Lmid,Xmid,Wmid,Pmid,Kmid]
induk=[mid,Amid,Bmid]
xbots=[mid,Cmid,Dmid,Dmid]
admin=["ue5c53b616f883dcb82526ad2b3c66f15","u72d4ec1fdb8f6c9b1f12f1372762f15d","uba553877e995e2bd476d1d78469dc8d2","u1b9ab645520fa5ae9d734f6e6b9b56ba"]
creator=["uba553877e995e2bd476d1d78469dc8d2","u1b9ab645520fa5ae9d734f6e6b9b56ba"]
owner=["uba553877e995e2bd476d1d78469dc8d2"]
wait = {
    'contact':False,
    'autoJoin':True,
    'autoCancel':{"on":True,"members":1},
    'leaveRoom':False,
    'timeline':True,
    'autoAdd':True,
    'message':"Open PP,Curhat Pc Creator: line://ti/p/~mtrisan Karna Saya hanya BOT Buatan BosTrisan",
    "lang":"JP",
    "comment":"Creator : line://ti/p/~mtrisan",
    "commentOn":True,
    "commentBlack":{},
    "wblack":False,
    "dblack":False,
    "clock":False,
    "cName":"¹Xplyer ا ",
    "blacklist":{},
    "wblacklist":False,
    "dblacklist":False,
    "ProtectQR":False,
    "protectionOn":False,
    "Protectguest":True,
    "Protectcancel":True,
    "atjointicket":True,
    }

wait2 = {
    'readPoint':{},
    'readMember':{},
    'setTime':{},
    'ProtectQR':{},
    'ROM':{}
    }

mimic = {
    "copy":True,
    "copy2":True,
    "status":True,
    "target":{}
    }

setTime = {}
setTime = wait2['setTime']

res = {
    'num':{},
    'us':{},
    'au':{},
}
fastbinary = None
mulai = time.time()
contact = cl.getProfile()
mybackup = cl.getProfile()
mybackup.displayName = contact.displayName
mybackup.statusMessage = contact.statusMessage
mybackup.pictureStatus = contact.pictureStatus

contact = cl.getProfile()
backup = cl.getProfile()
backup.displayName = contact.displayName
backup.statusMessage = contact.statusMessage
backup.pictureStatus = contact.pictureStatus

def Cmd(string, commands):
    tex = [""]
    for texX in tex:
        for command in command:
            if string ==texX + command:
                return True
    return False

def something():
    data = other_something()
    # do something to data
    return data
def other_something():
    other_data = "msg"
    return other_data

def download_page(url):
    version = (3,0)
    cur_version = sys.version_info
    if cur_version >= version:     #If the Current Version of Python is 3.0 or above
        import urllib,request    #urllib library for Extracting web pages
        try:
            headers = {}
            headers['User-Agent'] = "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.36"
            req = urllib,request.Request(url, headers = headers)
            resp = urllib,request.urlopen(req)
            respData = str(resp.read())
            return respData
        except Exception as e:
            print(str(e))
    else:                        #If the Current Version of Python is 2.x
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
            time.sleep(0.01)        #Timer could be used to slow down the request for image downloads
            page = page[end_content:]
    return items

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
     image = client.upload_from_path(image_path, config=config, anon=False)
     print("Done")
     print()

     return image

def restart_program():
    python = sys.executable
    os.execl(python, python,  sys.argv)

def waktu(secs):
    mins, secs = divmod(secs,60)
    hours, mins = divmod(mins,60)
    return '||(%02d Jam)•(%02d Menit)•(%02d Detik)||' % (hours, mins, secs)

def sendMessage(to, text, contentMetadata={}, contentType=0):
    mes = Message()
    mes.to, mes.from_ = to, profile.mid
    mes.text = text
    mes.contentType, mes.contentMetadata = contentType, contentMetadata
    if to not in messageReq:
        messageReq[to] = -1

def mention(to,nama):
    aa = ""
    bb = ""
    strt = int(12)
    akh = int(12)
    nm = nama
    print nm
    for mm in nm:
        akh = akh + 2
        aa += """{"S":"""+json.dumps(str(strt))+""","E":"""+json.dumps(str(akh))+""","M":"""+json.dumps(mm)+"},"""
        strt = strt + 6
        akh = akh + 4
        bb += "◈ @c \n"
    aa = (aa[:int(len(aa)-1)])
    msg = Message()
    msg.to = to
    msg.text = "「Mention」\n"+bb
    msg.contentMetadata = {'MENTION':'{"MENTIONEES":['+aa+']}','EMTVER':'4'}
    print msg
    try:
         cl.sendMessage(msg)
    except Exception as error:
        print error 

def RECEIVE_MESSAGE(op):
    msg = op.message
    try:
        if msg.contentType == 0:
            try:
                if msg.to in wait['readPoint']:
                    if msg.from_ in wait["ROM"][msg.to]:
                        del wait["ROM"][msg.to][msg.from_]
                else:
                    pass
            except:
                pass
        else:
            pass
    except KeyboardInterrupt:
           sys.exit(0)
    except Exception as error:
        print error
        print ("\n\nRECEIVE_MESSAGE\n\n")
        return

def bot(op):
    try:
        if op.type == 0:
            return
        if op.type == 5:
            if wait["autoAdd"] == True:
                cl.findAndAddContactsByMid(op.param1)
                if (wait["message"] in [""," ","\n",None]):
                    pass
                else:
                    cl.sendText(op.param1,str(wait["message"]))

         #------Open QR Kick start------#
        if op.type == 10:
           if wait["ProtectQR"] == True:
               if op.param2 not in Bots:
                   G = cl.getGroup(op.param1)
                   G = ki.getGroup(op.param1)
                   G.preventJoinByTicket = True
                   ka.kickoutFromGroup(op.param1,[op.param2])
                   cl.updateGroup(G)
        #------Open QR Kick finish-----#

        #------Invite User Kick start------#
        if op.type == 13:
           if wait["Protectguest"] == True:
            if op.param2 not in Bots:
              group = cl.getGroup(op.param1)
              gMembMids = [contact.mid for contact in group.invitee]
              random.choice(KAC).cancelGroupInvitation(op.param1, gMembMids)
              random.choice(KAC).kickoutFromGroup(op.param1,[op.param2])
        #------Invite User Kick Finish------#

        elif op.type == OpType.NOTIFIED_INVITE_INTO_GROUP:
                try:
                    group_id=op.param1
                    client.acceptGroupInvitation(group_id)
                except Exception as e:
                    client.log("[NOTIFIED_INVITE_INTO_GROUP] ERROR : " + str(e))
                else:
                    pass

        if op.type == 17:
            if op.param2 not in Bots:
                joinblacklist = op.param2.replace("�1�7�1�7",',')
                joinblacklistX = joinblacklist.split(",")
                matched_list = []
                for tag in wait["blacklist"]:
                    matched_list+=filter(lambda str: str == tag, joinblacklistX)
                if matched_list == []:
                    pass
                else:
                    random.choice(KAC).kickoutFromGroup(op.param1,[op.param2])
        if op.type == 17:
            if op.param2 not in Bots:
                joinblacklist = op.param2.replace("·",',')
                joinblacklistX = joinblacklist.split(",")
                matched_list = []
                for tag in wait["blacklist"]:
                    matched_list+=filter(lambda str: str == tag, joinblacklistX)
                if matched_list == []:
                    pass
                else:
                    random.choice(KAC).kickoutFromGroup(op.param1,[op.param2])

        if op.type == 55:
          try:
            if op.param1 in wait2['readPoint']:
              Name = cl.getContact(op.param2).displayName
              if Name in wait2['readMember'][op.param1]:
                 pass
              else:
                wait2['readMember'][op.param1] += "\n[•]" + Name
                wait2['ROM'][op.param1][op.param2] = "[•]" + Name
            else:
              cl.sendText
          except:
             pass

        if op.type == 13:
                if op.param3 in mid:
                    if op.param2 in Amid:
                        G = ki.getGroup(op.param1)
                        G.preventJoinByTicket = False
                        ki.updateGroup(G)
                        Ticket = ki.reissueGroupTicket(op.param1)
                        cl.acceptGroupInvitationByTicket(op.param1,Ticket)
                        G.preventJoinByTicket = True
                        ki.updateGroup(G)
                        Ticket = ki.reissueGroupTicket(op.param1)

                if op.param3 in Amid:
                    if op.param2 in Bmid:
                        X = kk.getGroup(op.param1)
                        X.preventJoinByTicket = False
                        kk.updateGroup(X)
                        Ti = kk.reissueGroupTicket(op.param1)
                        ki.acceptGroupInvitationByTicket(op.param1,Ti)
                        X.preventJoinByTicket = True
                        kk.updateGroup(X)
                        Ti = kk.reissueGroupTicket(op.param1)

                if op.param3 in Bmid:
                    if op.param2 in Cmid:
                        X = kc.getGroup(op.param1)
                        X.preventJoinByTicket = False
                        kc.updateGroup(X)
                        Ti = kc.reissueGroupTicket(op.param1)
                        kk.acceptGroupInvitationByTicket(op.param1,Ti)
                        X.preventJoinByTicket = True
                        kc.updateGroup(X)
                        Ti = kc.reissueGroupTicket(op.param1)
                        
                if op.param3 in Cmid:
                    if op.param2 in Gmid:
                        X = ko.getGroup(op.param1)
                        X.preventJoinByTicket = False
                        ko.updateGroup(X)
                        Ti = ko.reissueGroupTicket(op.param1)
                        kc.acceptGroupInvitationByTicket(op.param1,Ti)
                        X.preventJoinByTicket = True
                        ko.updateGroup(X)
                        Ti = ko.reissueGroupTicket(op.param1)
                        
                if op.param3 in Gmid:
                    if op.param2 in Dmid:
                        X = ks.getGroup(op.param1)
                        X.preventJoinByTicket = False
                        ks.updateGroup(X)
                        Ti = ks.reissueGroupTicket(op.param1)
                        ko.acceptGroupInvitationByTicket(op.param1,Ti)
                        X.preventJoinByTicket = True
                        ks.updateGroup(X)
                        Ti = ks.reissueGroupTicket(op.param1)
                        
                if op.param3 in Dmid:
                    if op.param2 in Hmid:
                        X = ke.getGroup(op.param1)
                        X.preventJoinByTicket = False
                        ke.updateGroup(X)
                        Ti = ke.reissueGroupTicket(op.param1)
                        ks.acceptGroupInvitationByTicket(op.param1,Ti)
                        X.preventJoinByTicket = True
                        ks.updateGroup(X)
                        Ti = ke.reissueGroupTicket(op.param1)
                        
                if op.param3 in Hmid:
                    if op.param2 in Kmid:
                        X = ku.getGroup(op.param1)
                        X.preventJoinByTicket = False
                        ku.updateGroup(X)
                        Ti = ku.reissueGroupTicket(op.param1)
                        ke.acceptGroupInvitationByTicket(op.param1,Ti)
                        X.preventJoinByTicket = True
                        ku.updateGroup(X)
                        Ti = ku.reissueGroupTicket(op.param1)
                        
                if op.param3 in Kmid:
                    if op.param2 in Xmid:
                        X = xl.getGroup(op.param1)
                        X.preventJoinByTicket = False
                        xl.updateGroup(X)
                        Ti = xl.reissueGroupTicket(op.param1)
                        ku.acceptGroupInvitationByTicket(op.param1,Ti)
                        X.preventJoinByTicket = True
                        ku.updateGroup(X)
                        Ti = xl.reissueGroupTicket(op.param1)
                        
                if op.param3 in Xmid:
                    if op.param2 in Lmid:
                        X = lx.getGroup(op.param1)
                        X.preventJoinByTicket = False
                        lx.updateGroup(X)
                        Ti = lx.reissueGroupTicket(op.param1)
                        xl.acceptGroupInvitationByTicket(op.param1,Ti)
                        X.preventJoinByTicket = True
                        lx.updateGroup(X)
                        Ti = lx.reissueGroupTicket(op.param1)
                
                if op.param3 in Lmid:
                    if op.param2 in Wmid:
                        X = ww.getGroup(op.param1)
                        X.preventJoinByTicket = False
                        lx.updateGroup(X)
                        Ti = ww.reissueGroupTicket(op.param1)
                        lx.acceptGroupInvitationByTicket(op.param1,Ti)
                        X.preventJoinByTicket = True
                        lx.updateGroup(X)
                        Ti = ww.reissueGroupTicket(op.param1)
                
                if op.param3 in Wmid:
                    if op.param2 in Pmid:
                        X = pw.getGroup(op.param1)
                        X.preventJoinByTicket = False
                        pw.updateGroup(X)
                        Ti = pw.reissueGroupTicket(op.param1)
                        ww.acceptGroupInvitationByTicket(op.param1,Ti)
                        X.preventJoinByTicket = True
                        lx.updateGroup(X)
                        Ti = pw.reissueGroupTicket(op.param1)
                
        if op.type == 32:
            if not op.param2 in Bots and admin:
                if wait["protectionOn"] == True: 
                    try:
                        klist=[cl,ki,kk,kc,ko,ks,ke,lx,xl,ww,pw,ku]
                        kicker = random.choice(klist) 
                        G = kicker.getGroup(op.param1)
                        kicker.kickoutFromGroup(op.param1,[op.param2])
                        kicker.inviteIntoGroup(op.param1, [op.param3])
                    except Exception, e:
                       print e

        if op.type == 13:
            print op.param1
            print op.param2
            print op.param3
            if mid in op.param3:
                G = cl.getGroup(op.param1)
                if wait["autoJoin"] == True:
                    if wait["autoCancel"]["on"] == True:
                        if len(G.members) <= wait["autoCancel"]["members"]:
                            cl.rejectGroupInvitation(op.param1)
                        else:
                            cl.acceptGroupInvitation(op.param1)
                    else:
                        cl.acceptGroupInvitation(op.param1)
                elif wait["autoCancel"]["on"] == True:
                    if len(G.members) <= wait["autoCancel"]["members"]:
                        cl.rejectGroupInvitation(op.param1)
            else:
                Inviter = op.param3.replace("^^",',')
                InviterX = Inviter.split(",")
                matched_list = []
                for tag in wait["blacklist"]:
                    matched_list+=filter(lambda str: str == tag, InviterX)
                if matched_list == []:
                    pass
                else:
                    cl.cancelGroupInvitation(op.param1, matched_list)

        if op.type == 11:
            if op.param2 not in Bots:
                G = cl.getGroup(op.param1)
                G.preventJoinByTicket = True
                invsend = 0
                Ticket = cl.reissueGroupTicket(op.param1)
                ku.acceptGroupInvitationByTicket(op.param1, Ticket)
                ku.kickoutFromGroup(op.param1,[op.param2])
                ku.leaveGroup(op.param1)
                cl.updateGroup(G)
                x = Message(to=op.param1, from_=None, text=None, contentType=13)
                x.contentMetadata={'mid':op.param2}
                ki.sendMessage(x)
                wait["blacklist"][op.param2] = True
                print "kicker"

                        #------SEPERTI SIRI------#
        if op.type == 19:
            if op.param2 not in Bots:
                G = cl.getGroup(op.param1)
                G.preventJoinByTicket = False
                cl.updateGroup(G)
                Ticket = cl.reissueGroupTicket(op.param1)
                pw.acceptGroupInvitationByTicket(op.param1,Ticket)
                time.sleep(0.0)
                pw.kickoutFromGroup(op.param1,[op.param2])
                c = Message(to=op.param1, from_=None, text=None, contentType=13)
                c.contentMetadata={'mid':op.param2}
                pw.sendMetadata={'mid':op.param2}
                pw.leaveGroup(op.param1)
                G.preventJoinByTicket = True
                cl.updateGroup(G)
                wait["blacklist"][op.param2] = True
                print "kicker"

        #if op.type == 32:
                #lf op.param2 not in admin and Bots
                    #random.choice(KAC).kickoutFromGroup(op.param1,[op.param2])
        if op.type == 19: #Member Ke Kick
            if op.param2 not in Bots:
                random.choice(KAC).kickoutFromGroup(op.param1,[op.param2])
                random.choice(KAC).inviteIntoGroup(op.param1,[op.param3])

        if op.type == 19:
           if op.param2 in induk: 
                random.choice(KAC).kickoutFromGroup(op.param1,[op.param2])
                random.choice(xbots).inviteIntoGroup(op.param1,[op.param3])

        if op.type == 19:
           if op.param2 in Bots:
                G = cl.getGroup(msg.to)
                ginfo = cl.getGroup(msg.to)
                G.preventJoinByTicket = False
                cl.updateGroup(G)
                invsend = 0
                Ticket = cl.reissueGroupTicket(msg.to)
                ki.acceptGroupInvitationByTicket(msg.to,Ticket)
                time.sleep(0.0)
                ki.acceptGroupInvitationByTicket(msg.to,Ticket)
                time.sleep(0.0)
                kk.acceptGroupInvitationByTicket(msg.to,Ticket)
                time.sleep(0.0)
                kc.acceptGroupInvitationByTicket(msg.to,Ticket)
                time.sleep(0.0)
                ko.acceptGroupInvitationByTicket(msg.to,Ticket)
                time.sleep(0.01)
                ks.acceptGroupInvitationByTicket(msg.to,Ticket)
                time.sleep(0.0)
                ke.acceptGroupInvitationByTicket(msg.to,Ticket)
                time.sleep(0.0)
                lx.acceptGroupInvitationByTicket(msg.to,Ticket)
                time.sleep(0.0)
                xl.acceptGroupInvitationByTicket(msg.to,Ticket)
                time.sleep(0.0)
                ww.acceptGroupInvitationByTicket(msg.to,Ticket)
                time.sleep(0.0)
                pw.acceptGroupInvitationByTicket(msg.to,Ticket)
                time.sleep(0.0)
                ku.acceptGroupInvitationByTicket(msg.to,Ticket)
                time.sleep(0.0)
                G = cl.getGroup(msg.to)
                ginfo = cl.getGroup(msg.to)
                G.preventJoinByTicket = True
                ki.updateGroup(G)
                G.preventJoinByTicket(G)
                random.choice(KAC).updateGroup(G)

        if op.type == 19: 
          if op.param3 in admin: #Kalo Admin ke Kick
            if op.param2 in Bots:
              pass
            if op.param2 in owner:
              pass
            else:
                random.choice(KAC).kickoutFromGroup(op.param1,[op.param2])
                random.choice(xbots).inviteIntoGroup(op.param1,[op.param3])

        if op.type == 19:
            if op.param3 in Amid: #Akun Utama Ke Kick
                G = random.choice(KAC).getGroup(op.param1)
                random.choice(KAC).kickoutFromGroup(op.param1,[op.param2])
                G.preventJoinByTicket = False
                random.choice(KAC).updateGroup(G)
                Ticket = random.choice(KAC).reissueGroupTicket(op.param1)
                ki.acceptGroupInvitationByTicket(op.param1,Ticket)
                time.sleep(0.0)
                G.preventJoinByTicket = True
                random.choice(KAC).updateGroup(G)
                ki.updateGroup(G)
                wait["blacklist"][op.param2] = True

        if op.type == 19:
            if op.param3 in mid: #Akun Utama Ke Kick
                G = random.choice(KAC).getGroup(op.param1)
                random.choice(KAC).kickoutFromGroup(op.param1,[op.param2])
                G.preventJoinByTicket = False
                random.choice(KAC).updateGroup(G)
                Ticket = random.choice(KAC).reissueGroupTicket(op.param1)
                cl.acceptGroupInvitationByTicket(op.param1,Ticket)
                time.sleep(0.0)
                G.preventJoinByTicket = True
                random.choice(KAC).updateGroup(G)
                cl.updateGroup(G)
                wait["blacklist"][op.param2] = True

        if op.type == 19:
            if op.param3 in Bmid: #Akun Utama Ke Kick
                G = random.choice(KAC).getGroup(op.param1)
                random.choice(KAC).kickoutFromGroup(op.param1,[op.param2])
                G.preventJoinByTicket = False
                random.choice(KAC).updateGroup(G)
                Ticket = random.choice(KAC).reissueGroupTicket(op.param1)
                kk.acceptGroupInvitationByTicket(op.param1,Ticket)
                time.sleep(0.0)
                G.preventJoinByTicket = True
                random.choice(KAC).updateGroup(G)
                kk.updateGroup(G)
                wait["blacklist"][op.param2] = True

        if op.type == 19:
            if op.param3 in Cmid: #Akun Utama Ke Kick
                G = random.choice(KAC).getGroup(op.param1)
                random.choice(KAC).kickoutFromGroup(op.param1,[op.param2])
                G.preventJoinByTicket = False
                random.choice(KAC).updateGroup(G)
                Ticket = random.choice(KAC).reissueGroupTicket(op.param1)
                kc.acceptGroupInvitationByTicket(op.param1,Ticket)
                time.sleep(0.0)
                G.preventJoinByTicket = True
                random.choice(KAC).updateGroup(G)
                kc.updateGroup(G)
                wait["blacklist"][op.param2] = True

        if op.type == 19:
            if op.param3 in Gmid: #Akun Utama Ke Kick
                G = random.choice(KAC).getGroup(op.param1)
                random.choice(KAC).kickoutFromGroup(op.param1,[op.param2])
                G.preventJoinByTicket = False
                random.choice(KAC).updateGroup(G)
                Ticket = random.choice(KAC).reissueGroupTicket(op.param1)
                ko.acceptGroupInvitationByTicket(op.param1,Ticket)
                time.sleep(0.0)
                G.preventJoinByTicket = True
                random.choice(KAC).updateGroup(G)
                ko.updateGroup(G)
                wait["blacklist"][op.param2] = True

        if op.type == 19:
            if op.param3 in Dmid: #Akun Utama Ke Kick
                G = random.choice(KAC).getGroup(op.param1)
                random.choice(KAC).kickoutFromGroup(op.param1,[op.param2])
                G.preventJoinByTicket = False
                random.choice(KAC).updateGroup(G)
                Ticket = random.choice(KAC).reissueGroupTicket(op.param1)
                ks.acceptGroupInvitationByTicket(op.param1,Ticket)
                time.sleep(0.0)
                G.preventJoinByTicket = True
                random.choice(KAC).updateGroup(G)
                ks.updateGroup(G)
                wait["blacklist"][op.param2] = True

        if op.type == 19:
            if op.param3 in Hmid: #Akun Utama Ke Kick
                G = random.choice(KAC).getGroup(op.param1)
                random.choice(KAC).kickoutFromGroup(op.param1,[op.param2])
                G.preventJoinByTicket = False
                random.choice(KAC).updateGroup(G)
                Ticket = random.choice(KAC).reissueGroupTicket(op.param1)
                ke.acceptGroupInvitationByTicket(op.param1,Ticket)
                time.sleep(0.0)
                G.preventJoinByTicket = True
                random.choice(KAC).updateGroup(G)
                ke.updateGroup(G)
                wait["blacklist"][op.param2] = True

                if op.param3 in Amid:
                   if op.param2 in mid:
                    G = cl.getGroup(op.param1)
                    G.preventJoinByTicket = False
                    cl.updateGroup(G)
                    Ticket = cl.reissueGroupTicket(op.param1)
                    cl.acceptGroupInvitationByTicket(op.param1,Ticket)
                    time.sleep(0.0)
                    ki.acceptGroupInvitationByTicket(op.param1,Ticket)
                    time.sleep(0.0)
                    kk.acceptGroupInvitationByTicket(op.param1,Ticket)
                    time.sleep(0.0)
                    kc.acceptGroupInvitationByTicket(op.param1,Ticket)
                    time.sleep(0.0)
                    ko.acceptGroupInvitationByTicket(op.param1,Ticket)
                    time.sleep(0.0)
                    ks.acceptGroupInvitationByTicket(op.param1,Ticket)
                    time.sleep(0.0)
                    ke.acceptGroupInvitationByTicket(op.param1,Ticket)
                    time.sleep(0.0)
                    lx.acceptGroupInvitationByTicket(op.param1,Ticket)
                    time.sleep(0.0)
                    xl.acceptGroupInvitationByTicket(op.param1,Ticket)
                    time.sleep(0.0)
                    ww.acceptGroupInvitationByTicket(op.param1,Ticket)
                    time.sleep(0.0)
                    pw.acceptGroupInvitationByTicket(op.param1,Ticket)
                    time.sleep(0.0)
                    ku.acceptGroupInvitationByTicket(op.param1,Ticket)
                    time.sleep(0.0)
                    G.preventJoinByTicket = True
                    cl.updateGroup(G)
                else:
                    G = cl.getGroup(op.param1)
                    cl.kickoutFromGroup(op.param1,[op.param2])
                    G.preventJoinByTicket = False
                    cl.updateGroup(G)
                    Ticket = cl.reissueGroupTicket(op.param1)
                    cl.acceptGroupInvitationByTicket(op.param1,Ticket)
                    time.sleep(0.0)
                    ki.acceptGroupInvitationByTicket(op.param1,Ticket)
                    time.sleep(0.0)
                    kk.acceptGroupInvitationByTicket(op.param1,Ticket)
                    time.sleep(0.0)
                    kc.acceptGroupInvitationByTicket(op.param1,Ticket)
                    time.sleep(0.0)
                    ko.acceptGroupInvitationByTicket(op.param1,Ticket)
                    time.sleep(0.0)
                    ks.acceptGroupInvitationByTicket(op.param1,Ticket)
                    time.sleep(0.0)
                    ke.acceptGroupInvitationByTicket(op.param1,Ticket)
                    time.sleep(0.0)
                    lx.acceptGroupInvitationByTicket(op.param1,Ticket)
                    time.sleep(0.0)
                    xl.acceptGroupInvitationByTicket(op.param1,Ticket)
                    time.sleep(0.0)
                    ww.acceptGroupInvitationByTicket(op.param1,Ticket)
                    time.sleep(0.0)
                    pw.acceptGroupInvitationByTicket(op.param1,Ticket)
                    time.sleep(0.0)
                    ku.acceptGroupInvitationByTicket(op.param1,Ticket)
                    time.sleep(0.0)
                    G.preventJoinByTicket = True
                    ki.updateGroup(G)
                    cl.updateGroup(G)
                    wait["blacklist"][op.param2] = True

                if op.param3 in Bmid:
                   if op.param2 in Amid:
                    G = ki.getGroup(op.param1)
                    G.preventJoinByTicket = False
                    ki.updateGroup(G)
                    Ticket = ki.reissueGroupTicket(op.param1)
                    cl.acceptGroupInvitationByTicket(op.param1,Ticket)
                    time.sleep(0.0)
                    ki.acceptGroupInvitationByTicket(op.param1,Ticket)
                    time.sleep(0.0)
                    kk.acceptGroupInvitationByTicket(op.param1,Ticket)
                    time.sleep(0.0)
                    kc.acceptGroupInvitationByTicket(op.param1,Ticket)
                    time.sleep(0.0)
                    ko.acceptGroupInvitationByTicket(op.param1,Ticket)
                    time.sleep(0.0)
                    ks.acceptGroupInvitationByTicket(op.param1,Ticket)
                    time.sleep(0.0)
                    ke.acceptGroupInvitationByTicket(op.param1,Ticket)
                    time.sleep(0.0)
                    lx.acceptGroupInvitationByTicket(op.param1,Ticket)
                    time.sleep(0.0)
                    xl.acceptGroupInvitationByTicket(op.param1,Ticket)
                    time.sleep(0.0)
                    ww.acceptGroupInvitationByTicket(op.param1,Ticket)
                    time.sleep(0.0)
                    pw.acceptGroupInvitationByTicket(op.param1,Ticket)
                    time.sleep(0.0)
                    ku.acceptGroupInvitationByTicket(op.param1,Ticket)
                    time.sleep(0.0)
                    G.preventJoinByTicket = True
                    ki.updateGroup(G)
                else:
                    G = ki.getGroup(op.param1)
                    ki.kickoutFromGroup(op.param1,[op.param2])
                    G.preventJoinByTicket = False
                    ki.updateGroup(G)
                    Ticket = ki.reissueGroupTicket(op.param1)
                    cl.acceptGroupInvitationByTicket(op.param1,Ticket)
                    time.sleep(0.0)
                    ki.acceptGroupInvitationByTicket(op.param1,Ticket)
                    time.sleep(0.0)
                    kk.acceptGroupInvitationByTicket(op.param1,Ticket)
                    time.sleep(0.0)
                    kc.acceptGroupInvitationByTicket(op.param1,Ticket)
                    time.sleep(0.0)
                    ko.acceptGroupInvitationByTicket(op.param1,Ticket)
                    time.sleep(0.0)
                    ks.acceptGroupInvitationByTicket(op.param1,Ticket)
                    time.sleep(0.0)
                    ke.acceptGroupInvitationByTicket(op.param1,Ticket)
                    time.sleep(0.0)
                    lx.acceptGroupInvitationByTicket(op.param1,Ticket)
                    time.sleep(0.0)
                    xl.acceptGroupInvitationByTicket(op.param1,Ticket)
                    time.sleep(0.0)
                    ww.acceptGroupInvitationByTicket(op.param1,Ticket)
                    time.sleep(0.0)
                    pw.acceptGroupInvitationByTicket(op.param1,Ticket)
                    time.sleep(0.0)
                    ku.acceptGroupInvitationByTicket(op.param1,Ticket)
                    time.sleep(0.0)
                    G.preventJoinByTicket = True
                    ki.updateGroup(G)
                    kk.updateGroup(G)
                    wait["blacklist"][op.param2] = True

                if op.param3 in Cmid:
                   if op.param2 in Bmid:
                    G = kk.getGroup(op.param1)
                    G.preventJoinByTicket = False
                    kk.updateGroup(G)
                    Ticket = kk.reissueGroupTicket(op.param1)
                    cl.acceptGroupInvitationByTicket(op.param1,Ticket)
                    time.sleep(0.0)
                    ki.acceptGroupInvitationByTicket(op.param1,Ticket)
                    time.sleep(0.0)
                    kk.acceptGroupInvitationByTicket(op.param1,Ticket)
                    time.sleep(0.0)
                    kc.acceptGroupInvitationByTicket(op.param1,Ticket)
                    time.sleep(0.0)
                    ko.acceptGroupInvitationByTicket(op.param1,Ticket)
                    time.sleep(0.0)
                    ks.acceptGroupInvitationByTicket(op.param1,Ticket)
                    time.sleep(0.0)
                    ke.acceptGroupInvitationByTicket(op.param1,Ticket)
                    time.sleep(0.0)
                    lx.acceptGroupInvitationByTicket(op.param1,Ticket)
                    time.sleep(0.0)
                    xl.acceptGroupInvitationByTicket(op.param1,Ticket)
                    time.sleep(0.0)
                    ww.acceptGroupInvitationByTicket(op.param1,Ticket)
                    time.sleep(0.0)
                    pw.acceptGroupInvitationByTicket(op.param1,Ticket)
                    time.sleep(0.0)
                    ku.acceptGroupInvitationByTicket(op.param1,Ticket)
                    time.sleep(0.0)
                    G.preventJoinByTicket = True
                    kk.updateGroup(G)
                else:
                    G = kk.getGroup(op.param1)
                    kk.kickoutFromGroup(op.param1,[op.param2])
                    G.preventJoinByTicket = False
                    kk.updateGroup(G)
                    Ticket = kk.reissueGroupTicket(op.param1)
                    cl.acceptGroupInvitationByTicket(op.param1,Ticket)
                    time.sleep(0.0)
                    ki.acceptGroupInvitationByTicket(op.param1,Ticket)
                    time.sleep(0.0)
                    kk.acceptGroupInvitationByTicket(op.param1,Ticket)
                    time.sleep(0.0)
                    kc.acceptGroupInvitationByTicket(op.param1,Ticket)
                    time.sleep(0.0)
                    ko.acceptGroupInvitationByTicket(op.param1,Ticket)
                    time.sleep(0.0)
                    ks.acceptGroupInvitationByTicket(op.param1,Ticket)
                    time.sleep(0.0)
                    ke.acceptGroupInvitationByTicket(op.param1,Ticket)
                    time.sleep(0.0)
                    lx.acceptGroupInvitationByTicket(op.param1,Ticket)
                    time.sleep(0.0)
                    xl.acceptGroupInvitationByTicket(op.param1,Ticket)
                    time.sleep(0.0)
                    ww.acceptGroupInvitationByTicket(op.param1,Ticket)
                    time.sleep(0.0)
                    pw.acceptGroupInvitationByTicket(op.param1,Ticket)
                    time.sleep(0.0)
                    ku.acceptGroupInvitationByTicket(op.param1,Ticket)
                    time.sleep(0.0)
                    kk.updateGroup(G)
                    kc.updateGroup(G)
                    wait["blacklist"][op.param2] = True

                if op.param3 in Gmid:
                   if op.param2 in Cmid:
                    G = kc.getGroup(op.param1)
                    G.preventJoinByTicket = False
                    kc.updateGroup(G)
                    Ticket = kc.reissueGroupTicket(op.param1)
                    cl.acceptGroupInvitationByTicket(op.param1,Ticket)
                    time.sleep(0.0)
                    ki.acceptGroupInvitationByTicket(op.param1,Ticket)
                    time.sleep(0.0)
                    kk.acceptGroupInvitationByTicket(op.param1,Ticket)
                    time.sleep(0.0)
                    kc.acceptGroupInvitationByTicket(op.param1,Ticket)
                    time.sleep(0.0)
                    ko.acceptGroupInvitationByTicket(op.param1,Ticket)
                    time.sleep(0.0)
                    ks.acceptGroupInvitationByTicket(op.param1,Ticket)
                    time.sleep(0.0)
                    ke.acceptGroupInvitationByTicket(op.param1,Ticket)
                    time.sleep(0.0)
                    lx.acceptGroupInvitationByTicket(op.param1,Ticket)
                    time.sleep(0.0)
                    xl.acceptGroupInvitationByTicket(op.param1,Ticket)
                    time.sleep(0.0)
                    ww.acceptGroupInvitationByTicket(op.param1,Ticket)
                    time.sleep(0.0)
                    pw.acceptGroupInvitationByTicket(op.param1,Ticket)
                    time.sleep(0.0)
                    ku.acceptGroupInvitationByTicket(op.param1,Ticket)
                    time.sleep(0.0)
                    G.preventJoinByTicket = True
                    kc.updateGroup(G)
                else:
                    G = kc.getGroup(op.param1)
                    kc.kickoutFromGroup(op.param1,[op.param2])
                    G.preventJoinByTicket = False
                    kc.updateGroup(G)
                    Ticket = cl.reissueGroupTicket(op.param1)
                    cl.acceptGroupInvitationByTicket(op.param1,Ticket)
                    time.sleep(0.0)
                    ki.acceptGroupInvitationByTicket(op.param1,Ticket)
                    time.sleep(0.0)
                    kk.acceptGroupInvitationByTicket(op.param1,Ticket)
                    time.sleep(0.0)
                    kc.acceptGroupInvitationByTicket(op.param1,Ticket)
                    time.sleep(0.0)
                    ko.acceptGroupInvitationByTicket(op.param1,Ticket)
                    time.sleep(0.0)
                    ks.acceptGroupInvitationByTicket(op.param1,Ticket)
                    time.sleep(0.0)
                    ke.acceptGroupInvitationByTicket(op.param1,Ticket)
                    time.sleep(0.0)
                    lx.acceptGroupInvitationByTicket(op.param1,Ticket)
                    time.sleep(0.0)
                    xl.acceptGroupInvitationByTicket(op.param1,Ticket)
                    time.sleep(0.0)
                    ww.acceptGroupInvitationByTicket(op.param1,Ticket)
                    time.sleep(0.0)
                    pw.acceptGroupInvitationByTicket(op.param1,Ticket)
                    time.sleep(0.0)
                    ku.acceptGroupInvitationByTicket(op.param1,Ticket)
                    time.sleep(0.0)
                    kc.updateGroup(G)
                    ko.updateGroup(G)
                    wait["blacklist"][op.param2] = True

                if op.param3 in Dmid:
                   if op.param2 in Gmid:
                    G = ko.getGroup(op.param1)
                    G.preventJoinByTicket = False
                    ko.updateGroup(G)
                    Ticket = ko.reissueGroupTicket(op.param1)
                    cl.acceptGroupInvitationByTicket(op.param1,Ticket)
                    time.sleep(0.0)
                    ki.acceptGroupInvitationByTicket(op.param1,Ticket)
                    time.sleep(0.0)
                    kk.acceptGroupInvitationByTicket(op.param1,Ticket)
                    time.sleep(0.0)
                    kc.acceptGroupInvitationByTicket(op.param1,Ticket)
                    time.sleep(0.0)
                    ko.acceptGroupInvitationByTicket(op.param1,Ticket)
                    time.sleep(0.0)
                    ks.acceptGroupInvitationByTicket(op.param1,Ticket)
                    time.sleep(0.0)
                    ke.acceptGroupInvitationByTicket(op.param1,Ticket)
                    time.sleep(0.0)
                    lx.acceptGroupInvitationByTicket(op.param1,Ticket)
                    time.sleep(0.0)
                    xl.acceptGroupInvitationByTicket(op.param1,Ticket)
                    time.sleep(0.0)
                    ww.acceptGroupInvitationByTicket(op.param1,Ticket)
                    time.sleep(0.0)
                    pw.acceptGroupInvitationByTicket(op.param1,Ticket)
                    time.sleep(0.0)
                    ku.acceptGroupInvitationByTicket(op.param1,Ticket)
                    time.sleep(0.0)
                    G.preventJoinByTicket = True
                    ko.updateGroup(G)
                else:
                    G = ko.getGroup(op.param1)
                    ko.kickoutFromGroup(op.param1,[op.param2])
                    G.preventJoinByTicket = False
                    ko.updateGroup(G)
                    Ticket = ko.reissueGroupTicket(op.param1)
                    cl.acceptGroupInvitationByTicket(op.param1,Ticket)
                    time.sleep(0.0)
                    ki.acceptGroupInvitationByTicket(op.param1,Ticket)
                    time.sleep(0.0)
                    kk.acceptGroupInvitationByTicket(op.param1,Ticket)
                    time.sleep(0.0)
                    kc.acceptGroupInvitationByTicket(op.param1,Ticket)
                    time.sleep(0.0)
                    ko.acceptGroupInvitationByTicket(op.param1,Ticket)
                    time.sleep(0.0)
                    ks.acceptGroupInvitationByTicket(op.param1,Ticket)
                    time.sleep(0.0)
                    ke.acceptGroupInvitationByTicket(op.param1,Ticket)
                    time.sleep(0.0)
                    lx.acceptGroupInvitationByTicket(op.param1,Ticket)
                    time.sleep(0.0)
                    xl.acceptGroupInvitationByTicket(op.param1,Ticket)
                    time.sleep(0.0)
                    ww.acceptGroupInvitationByTicket(op.param1,Ticket)
                    time.sleep(0.0)
                    pw.acceptGroupInvitationByTicket(op.param1,Ticket)
                    time.sleep(0.0)
                    ku.acceptGroupInvitationByTicket(op.param1,Ticket)
                    time.sleep(0.0)
                    ko.updateGroup(G)
                    ks.updateGroup(G)
                    wait["blacklist"][op.param2] = True

                if op.param3 in Hmid:
                   if op.param2 in Dmid:
                    G = ks.getGroup(op.param1)
                    G.preventJoinByTicket = False
                    ks.updateGroup(G)
                    Ticket = ks.reissueGroupTicket(op.param1)
                    cl.acceptGroupInvitationByTicket(op.param1,Ticket)
                    time.sleep(0.0)
                    ki.acceptGroupInvitationByTicket(op.param1,Ticket)
                    time.sleep(0.0)
                    kk.acceptGroupInvitationByTicket(op.param1,Ticket)
                    time.sleep(0.0)
                    kc.acceptGroupInvitationByTicket(op.param1,Ticket)
                    time.sleep(0.0)
                    ko.acceptGroupInvitationByTicket(op.param1,Ticket)
                    time.sleep(0.0)
                    ks.acceptGroupInvitationByTicket(op.param1,Ticket)
                    time.sleep(0.0)
                    ke.acceptGroupInvitationByTicket(op.param1,Ticket)
                    time.sleep(0.0)
                    lx.acceptGroupInvitationByTicket(op.param1,Ticket)
                    time.sleep(0.0)
                    xl.acceptGroupInvitationByTicket(op.param1,Ticket)
                    time.sleep(0.0)
                    ww.acceptGroupInvitationByTicket(op.param1,Ticket)
                    time.sleep(0.0)
                    pw.acceptGroupInvitationByTicket(op.param1,Ticket)
                    time.sleep(0.0)
                    ku.acceptGroupInvitationByTicket(op.param1,Ticket)
                    time.sleep(0.0)
                    G.preventJoinByTicket = True
                    ko.updateGroup(G)
                else:
                    G = ks.getGroup(op.param1)
                    ks.kickoutFromGroup(op.param1,[op.param2])
                    G.preventJoinByTicket = False
                    ks.updateGroup(G)
                    Ticket = ks.reissueGroupTicket(op.param1)
                    cl.acceptGroupInvitationByTicket(op.param1,Ticket)
                    time.sleep(0.0)
                    ki.acceptGroupInvitationByTicket(op.param1,Ticket)
                    time.sleep(0.0)
                    kk.acceptGroupInvitationByTicket(op.param1,Ticket)
                    time.sleep(0.0)
                    kc.acceptGroupInvitationByTicket(op.param1,Ticket)
                    time.sleep(0.0)
                    ko.acceptGroupInvitationByTicket(op.param1,Ticket)
                    time.sleep(0.0)
                    ks.acceptGroupInvitationByTicket(op.param1,Ticket)
                    time.sleep(0.0)
                    ke.acceptGroupInvitationByTicket(op.param1,Ticket)
                    time.sleep(0.0)
                    lx.acceptGroupInvitationByTicket(op.param1,Ticket)
                    time.sleep(0.0)
                    xl.acceptGroupInvitationByTicket(op.param1,Ticket)
                    time.sleep(0.0)
                    ww.acceptGroupInvitationByTicket(op.param1,Ticket)
                    time.sleep(0.0)
                    pw.acceptGroupInvitationByTicket(op.param1,Ticket)
                    time.sleep(0.0)
                    ku.acceptGroupInvitationByTicket(op.param1,Ticket)
                    time.sleep(0.0)
                    ks.updateGroup(G)
                    ke.updateGroup(G)
                    wait["blacklist"][op.param2] = True

                if op.param3 in Kmid:
                   if op.param2 in Hmid:
                    G = ke.getGroup(op.param1)
                    G.preventJoinByTicket = False
                    ke.updateGroup(G)
                    Ticket = ke.reissueGroupTicket(op.param1)
                    cl.acceptGroupInvitationByTicket(op.param1,Ticket)
                    time.sleep(0.0)
                    ki.acceptGroupInvitationByTicket(op.param1,Ticket)
                    time.sleep(0.0)
                    kk.acceptGroupInvitationByTicket(op.param1,Ticket)
                    time.sleep(0.0)
                    kc.acceptGroupInvitationByTicket(op.param1,Ticket)
                    time.sleep(0.0)
                    ko.acceptGroupInvitationByTicket(op.param1,Ticket)
                    time.sleep(0.0)
                    ks.acceptGroupInvitationByTicket(op.param1,Ticket)
                    time.sleep(0.0)
                    ke.acceptGroupInvitationByTicket(op.param1,Ticket)
                    time.sleep(0.0)
                    lx.acceptGroupInvitationByTicket(op.param1,Ticket)
                    time.sleep(0.0)
                    xl.acceptGroupInvitationByTicket(op.param1,Ticket)
                    time.sleep(0.0)
                    ww.acceptGroupInvitationByTicket(op.param1,Ticket)
                    time.sleep(0.0)
                    pw.acceptGroupInvitationByTicket(op.param1,Ticket)
                    time.sleep(0.0)
                    ku.acceptGroupInvitationByTicket(op.param1,Ticket)
                    time.sleep(0.0)
                    G.preventJoinByTicket = True
                    ke.updateGroup(G)
                else:
                    G = ke.getGroup(op.param1)
                    ke.kickoutFromGroup(op.param1,[op.param2])
                    G.preventJoinByTicket = False
                    ke.updateGroup(G)
                    Ticket = ke.reissueGroupTicket(op.param1)
                    cl.acceptGroupInvitationByTicket(op.param1,Ticket)
                    time.sleep(0.0)
                    ki.acceptGroupInvitationByTicket(op.param1,Ticket)
                    time.sleep(0.0)
                    kk.acceptGroupInvitationByTicket(op.param1,Ticket)
                    time.sleep(0.0)
                    kc.acceptGroupInvitationByTicket(op.param1,Ticket)
                    time.sleep(0.0)
                    ko.acceptGroupInvitationByTicket(op.param1,Ticket)
                    time.sleep(0.0)
                    ks.acceptGroupInvitationByTicket(op.param1,Ticket)
                    time.sleep(0.0)
                    ke.acceptGroupInvitationByTicket(op.param1,Ticket)
                    time.sleep(0.0)
                    lx.acceptGroupInvitationByTicket(op.param1,Ticket)
                    time.sleep(0.0)
                    xl.acceptGroupInvitationByTicket(op.param1,Ticket)
                    time.sleep(0.0)
                    ww.acceptGroupInvitationByTicket(op.param1,Ticket)
                    time.sleep(0.0)
                    pw.acceptGroupInvitationByTicket(op.param1,Ticket)
                    time.sleep(0.0)
                    ku.acceptGroupInvitationByTicket(op.param1,Ticket)
                    time.sleep(0.0)
                    ke.updateGroup(G)
                    ku.updateGroup(G)
                    wait["blacklist"][op.param2] = True
                    
                if op.param3 in Hmid:
                   if op.param2 in Lmid:
                    G = lx.getGroup(op.param1)
                    G.preventJoinByTicket = False
                    lx.updateGroup(G)
                    Ticket = lx.reissueGroupTicket(op.param1)
                    cl.acceptGroupInvitationByTicket(op.param1,Ticket)
                    time.sleep(0.01)
                    ki.acceptGroupInvitationByTicket(op.param1,Ticket)
                    time.sleep(0.01)
                    kk.acceptGroupInvitationByTicket(op.param1,Ticket)
                    time.sleep(0.01)
                    kc.acceptGroupInvitationByTicket(op.param1,Ticket)
                    time.sleep(0.01)
                    ko.acceptGroupInvitationByTicket(op.param1,Ticket)
                    time.sleep(0.01)
                    ks.acceptGroupInvitationByTicket(op.param1,Ticket)
                    time.sleep(0.01)
                    ke.acceptGroupInvitationByTicket(op.param1,Ticket)
                    time.sleep(0.01)
                    lx.acceptGroupInvitationByTicket(op.param1,Ticket)
                    time.sleep(0.01)
                    xl.acceptGroupInvitationByTicket(op.param1,Ticket)
                    time.sleep(0.01)
                    ww.acceptGroupInvitationByTicket(op.param1,Ticket)
                    time.sleep(0.01)
                    pw.acceptGroupInvitationByTicket(op.param1,Ticket)
                    time.sleep(0.01)
                    ku.acceptGroupInvitationByTicket(op.param1,Ticket)
                    time.sleep(0.01)
                    G.preventJoinByTicket = True
                    lx.updateGroup(G)
                else:
                    G = lx.getGroup(op.param1)
                    lx.kickoutFromGroup(op.param1,[op.param2])
                    TickickoutFromGroup(op.param1,[op.param2])
                    G.preventJoinByTicket = False
                    lx.updateGroup(G)
                    Ticket = lx.reissueGroupTicket(op.param1)
                    cl.acceptGroupInvitationByTicket(op.param1,Ticket)
                    time.sleep(0.01)
                    ki.acceptGroupInvitationByTicket(op.param1,Ticket)
                    time.sleep(0.01)
                    kk.acceptGroupInvitationByTicket(op.param1,Ticket)
                    time.sleep(0.01)
                    kc.acceptGroupInvitationByTicket(op.param1,Ticket)
                    time.sleep(0.01)
                    ko.acceptGroupInvitationByTicket(op.param1,Ticket)
                    time.sleep(0.01)
                    ks.acceptGroupInvitationByTicket(op.param1,Ticket)
                    time.sleep(0.01)
                    ke.acceptGroupInvitationByTicket(op.param1,Ticket)
                    time.sleep(0.01)
                    lx.acceptGroupInvitationByTicket(op.param1,Ticket)
                    time.sleep(0.01)
                    xl.acceptGroupInvitationByTicket(op.param1,Ticket)
                    time.sleep(0.01)
                    ww.acceptGroupInvitationByTicket(op.param1,Ticket)
                    time.sleep(0.01)
                    pw.acceptGroupInvitationByTicket(op.param1,Ticket)
                    time.sleep(0.01)
                    ku.acceptGroupInvitationByTicket(op.param1,Ticket)
                    time.sleep(0.01)
                    lx.updateGroup(G)
                    wait["blacklist"][op.param2] = True
                    
                if op.param3 in Lmid:
                   if op.param2 in Xmid:
                    G = xl.getGroup(op.param1)
                    G.preventJoinByTicket = False
                    xl.updateGroup(G)
                    Ticket = xl.reissueGroupTicket(op.param1)
                    cl.acceptGroupInvitationByTicket(op.param1,Ticket)
                    time.sleep(0.01)
                    ki.acceptGroupInvitationByTicket(op.param1,Ticket)
                    time.sleep(0.01)
                    kk.acceptGroupInvitationByTicket(op.param1,Ticket)
                    time.sleep(0.01)
                    kc.acceptGroupInvitationByTicket(op.param1,Ticket)
                    time.sleep(0.01)
                    ko.acceptGroupInvitationByTicket(op.param1,Ticket)
                    time.sleep(0.01)
                    ks.acceptGroupInvitationByTicket(op.param1,Ticket)
                    time.sleep(0.01)
                    ke.acceptGroupInvitationByTicket(op.param1,Ticket)
                    time.sleep(0.01)
                    lx.acceptGroupInvitationByTicket(op.param1,Ticket)
                    time.sleep(0.01)
                    xl.acceptGroupInvitationByTicket(op.param1,Ticket)
                    time.sleep(0.01)
                    ww.acceptGroupInvitationByTicket(op.param1,Ticket)
                    time.sleep(0.01)
                    pw.acceptGroupInvitationByTicket(op.param1,Ticket)
                    time.sleep(0.01)
                    ku.acceptGroupInvitationByTicket(op.param1,Ticket)
                    time.sleep(0.01)
                    G.preventJoinByTicket = True
                    xl.updateGroup(G)
                else:
                    G = xl.getGroup(op.param1)
                    xl.kickoutFromGroup(op.param1,[op.param2])
                    G.preventJoinByTicket = False
                    xl.updateGroup(G)
                    Ticket = xl.reissueGroupTicket(op.param1)
                    cl.acceptGroupInvitationByTicket(op.param1,Ticket)
                    time.sleep(0.01)
                    ki.acceptGroupInvitationByTicket(op.param1,Ticket)
                    time.sleep(0.01)
                    kk.acceptGroupInvitationByTicket(op.param1,Ticket)
                    time.sleep(0.01)
                    kc.acceptGroupInvitationByTicket(op.param1,Ticket)
                    time.sleep(0.01)
                    ko.acceptGroupInvitationByTicket(op.param1,Ticket)
                    time.sleep(0.01)
                    ks.acceptGroupInvitationByTicket(op.param1,Ticket)
                    time.sleep(0.01)
                    ke.acceptGroupInvitationByTicket(op.param1,Ticket)
                    time.sleep(0.01)
                    lx.acceptGroupInvitationByTicket(op.param1,Ticket)
                    time.sleep(0.01)
                    xl.acceptGroupInvitationByTicket(op.param1,Ticket)
                    time.sleep(0.01)
                    ww.acceptGroupInvitationByTicket(op.param1,Ticket)
                    time.sleep(0.01)
                    pw.acceptGroupInvitationByTicket(op.param1,Ticket)
                    time.sleep(0.01)
                    ku.acceptGroupInvitationByTicket(op.param1,Ticket)
                    time.sleep(0.01)
                    xl.updateGroup(G)
                    wait["blacklist"][op.param2] = True

        if op.type == 13:
            if mid in op.param3:
                G = cl.getGroup(op.param1)
                if wait["autoJoin"] == True:
                    if wait["autoCancel"]["on"] == True:
                        if len(G.members) <= wait["autoCancel"]["members"]:
                            cl.rejectGroupInvitation(op.param1)
                        else:
                            cl.acceptGroupInvitation(op.param1)
                    else:
                        cl.acceptGroupInvitation(op.param1)
                elif wait["autoCancel"]["on"] == True:
                    if len(G.members) <= wait["autoCancel"]["members"]:
                        cl.rejectGroupInvitation(op.param1)
            else:
                Inviter = op.param3.replace("",',')
                InviterX = Inviter.split(",")
                matched_list = []
                for tag in wait["blacklist"]:
                    matched_list+=filter(lambda str: str == tag, InviterX)
                if matched_list == []:
                    pass
                else:
                    cl.cancelGroupInvitation(op.param1, matched_list)

        if op.type == 22:
            if wait["leaveRoom"] == True:
                cl.leaveRoom(op.param1)
        if op.type == 24:
            if wait["leaveRoom"] == True:
                cl.leaveRoom(op.param1)
        if op.type == 26:
            msg = op.message
            if msg.toType == 0:
                msg.to = msg.from_
                if msg.from_ == admin:
                    if "join:" in msg.text:
                        list_ = msg.text.split(":")
                        try:
                            cl.acceptGroupInvitationByTicket(list_[1],list_[2])
                            X = cl.getGroup(list_[1])
                            X.preventJoinByTicket = True
                            cl.updateGroup(X)
                        except:
                            cl.sendText(msg.to,"error")
            if msg.toType == 1:
                if wait["leaveRoom"] == True:
                    cl.leaveRoom(msg.to)
            if msg.contentType == 16:
                url = msg.contentMetadata("line://home/post?userMid="+mid+"&postId="+"new_post")
                cl.like(url[25:58], url[66:], likeType=1001)
        if op.type == 26:
            msg = op.message
            if msg.contentType == 13:
               if wait["wblack"] == True:
                    if msg.contentMetadata["mid"] in wait["commentBlack"]:
                        cl.sendText(msg.to,"already")
                        wait["wblack"] = False
                    else:
                        wait["commentBlack"][msg.contentMetadata["mid"]] = True
                        wait["wblack"] = False
                        cl.sendText(msg.to,"decided not to comment")

               elif wait["dblack"] == True:
                   if msg.contentMetadata["mid"] in wait["commentBlack"]:
                        del wait["commentBlack"][msg.contentMetadata["mid"]]
                        cl.sendText(msg.to,"deleted")
                        wait["dblack"] = False

                   else:
                        wait["dblack"] = False
                        cl.sendText(msg.to,"It is not in the black list")
                        ki.sendText(msg.to,"It is not in the black list")
               elif wait["wblacklist"] == True:
                   if msg.contentMetadata["mid"] in wait["blacklist"]:
                        cl.sendText(msg.to,"already")
                        ki.sendText(msg.to,"already")
                        wait["wblacklist"] = False
                   else:
                        wait["blacklist"][msg.contentMetadata["mid"]] = True
                        wait["wblacklist"] = False
                        cl.sendText(msg.to,"aded")

               elif wait["dblacklist"] == True:
                   if msg.contentMetadata["mid"] in wait["blacklist"]:
                        del wait["blacklist"][msg.contentMetadata["mid"]]
                        cl.sendText(msg.to,"deleted")
                        wait["dblacklist"] = False

                   else:
                        wait["dblacklist"] = False
                        cl.sendText(msg.to,"It is not in the black list")
        if op.type == 26:
            msg = op.message
            if msg.contentType == 13:
               if wait["winvite"] == True:
                     if msg.from_ in admin:
                         _name = msg.contentMetadata["displayName"]
                         invite = msg.contentMetadata["mid"]
                         groups = cl.getGroup(msg.to)
                         pending = groups.invitee
                         targets = []
                         for s in groups.members:
                             if _name in s.displayName:
                                 cl.sendText(msg.to,"-> " + _name + " was here")
                                 break
                             elif invite in wait["blacklist"]:
                                 ki.sendText(msg.to,"Sorry, " + _name + " On Blacklist")
                                 ki.sendText(msg.to,"Call my owner to use command !, \n➡Unban: " + invite)
                                 break                             
                             else:
                                 targets.append(invite)
                         if targets == []:
                             pass
                         else:
                             for target in targets:
                                 try:
                                     ki.findAndAddContactsByMid(target)
                                     ki.inviteIntoGroup(msg.to,[target])
                                     ki.sendText(msg.to,"Done Invite : \n➡" + _name)
                                     wait["winvite"] = False
                                     break
                                 except:
                                     try:
                                         ki.findAndAddContactsByMid(invite)
                                         ki.inviteIntoGroup(op.param1,[invite])
                                         wait["winvite"] = False
                                     except:
                                         ki.sendText(msg.to,"Negative, Error detected")
                                         wait["winvite"] = False
                                         break
            elif "Invite:" in msg.text:
              if msg.from_ in admin:
                midd = msg.text.replace("Invite:"," ")
                cl.findAndAddContactsByMid(midd)
                cl.inviteIntoGroup(msg.to,[midd])

            elif msg.contentType == 16:
                if wait["timeline"] == True:
                    msg.contentType = 0
                    if wait["lang"] == "JP":
                        msg.text = "post URL\n" + msg.contentMetadata["postEndUrl"]
                    else:
                        msg.text = "URLâ†’\n" + msg.contentMetadata["postEndUrl"]
                    cl.sendText(msg.to,msg.text)
            elif msg.text is None:
                return
            elif msg.text in ["Key","help","Help"]:
                if wait["lang"] == "JP":
                    cl.sendText(msg.to,helpMessage)
                else:
                    cl.sendText(msg.to,helpt)
            elif ("Gn " in msg.text):
                if msg.toType == 2:
                    X = cl.getGroup(msg.to)
                    X.name = msg.text.replace("Gn ","")
                    cl.updateGroup(X)
                else:
                    cl.sendText(msg.to,"It can't be used besides the group.")
            elif "Kick " in msg.text:
                midd = msg.text.replace("Kick ","")
                cl.kickoutFromGroup(msg.to,[midd])
            elif "Invite " in msg.text:
                midd = msg.text.replace("Invite ","")
                cl.findAndAddContactsByMid(midd)
                cl.inviteIntoGroup(msg.to,[midd])
            elif "Rom invite " in msg.text:
                midd = msg.text.replace("Nami invite ","")
                ki.findAndAddContactsByMid(midd)
                ki.inviteIntoGroup(msg.to,[midd])
            elif "Rom2 invite " in msg.text:
                midd = msg.text.replace("Zoro invite ","")
                kk.findAndAddContactsByMid(midd)
                kk.inviteIntoGroup(msg.to,[midd])
            elif "Rom3 invite " in msg.text:
                midd = msg.text.replace("Trisan invite ","")
                kc.findAndAddContactsByMid(midd)
                kc.inviteIntoGroup(msg.to,[midd])
            elif msg.text in ["Me"]:
                msg.contentType = 13
                msg.contentMetadata = {'mid': msg.from_}
                cl.sendMessage(msg)
            elif msg.text in ["Gift1"]:
              if msg.from_ in admin:
                msg.contentType = 9
                msg.contentMetadata={'PRDID': '7f2a5559-46ef-4f27-9940-66b1365950c4', 
                                    'PRDTYPE': 'THEME',
                                    'MSGTPL': '1'}
                msg.text = None
                cl.sendMessage(msg)
            elif msg.text in ["Gift2"]:
              if msg.from_ in admin:
                msg.contentType = 9
                msg.contentMetadata={'PRDID': '291e428d-e003-4d89-b8b2-a3e720fa11e0',
                                    'PRDTYPE': 'THEME',
                                    'MSGTPL': '2'}
                msg.text = None
                ki.sendMessage(msg)
            elif msg.text in ["Gift3"]:
                msg.contentType = 9
                msg.contentMetadata={'PRDID': 'f35e14c2-2bac-4a93-b1d2-75e279806e98',
                                    'PRDTYPE':'THEME', 
                                    'MSGTPL': '3'}
                msg.text = None
                kk.sendMessage(msg)
            elif msg.text in ["Gift4"]:
              if msg.from_ in admin:
                msg.contentType = 9
                msg.contentMetadata={'PRDID': '39d46a33-94e3-45ef-8023-6c94bdd7f7aa',
                                    'PRDTYPE':'THEME', 
                                    'MSGTPL': '4'}
                msg.text = None
                kc.sendMessage(msg)
            elif msg.text in ["Gift all"]:
              if msg.from_ in admin:
                msg.contentType = 9
                msg.contentMetadata={'PRDID': 'aa66ca83-3b95-48f5-9e35-55cc48e0e923',
                                    'PRDTYPE': 'THEME',
                                    'MSGTPL': '12'}
                msg.text = None
                cl.sendMessage(msg)
                ki.sendMessage(msg)
                kk.sendMessage(msg)
                kc.sendMessage(msg)
                ko.sendMessage(msg)
                ks.sendMessage(msg)
                ke.sendMessage(msg)
                ku.sendMessage(msg)

            elif msg.text.lower() == 'Allbio:':
              if msg.from_ in owner:
                string = msg.text.lower().replace("Allbio: ","")
                if len(string.decode('utf-8')) <= 500:
                    profile = ki.getProfile()
                    profile.statusMessage = string
                    ki.updateProfile(profile)
                if len(string.decode('utf-8')) <= 500:
                    profile = kk.getProfile()
                    profile.statusMessage = string
                    kk.updateProfile(profile)
                if len(string.decode('utf-8')) <= 500:
                    profile = kc.getProfile()
                    profile.statusMessage = string
                    kc.updateProfile(profile)
                if len(string.decode('utf-8')) <= 500:
                    profile = cl.getProfile()
                    profile.statusMessage = string
                    cl.updateProfile(profile)
                if len(string.decode('utf-8')) <= 500:
                    profile = ks.getProfile()
                    profile.statusMessage = string
                    ks.updateProfile(profile)
                if len(string.decode('utf-8')) <= 500:
                    profile = kt.getProfile()
                    profile.statusMessage = string
                    ko.updateProfile(profile)
                    cl.sendText(msg.to,"successfully turn it into: " + string + "")

            elif msg.text in ["cancel","Cancel"]:
                if msg.toType == 2:
                    X = cl.getGroup(msg.to)
                    if X.invitee is not None:
                        gInviMids = [contact.mid for contact in X.invitee]
                        cl.cancelGroupInvitation(msg.to, gInviMids)
                    else:
                        if wait["lang"] == "JP":
                            cl.sendText(msg.to,"No one is inviting")
                        else:
                            cl.sendText(msg.to,"Sorry, nobody absent")
                else:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Can not be used outside the group")
                    else:
                        cl.sendText(msg.to,"Not for use less than group")
            elif msg.text in ["Cancel2","cancel2"]:
                if msg.toType == 2:
                    G = kk.getGroup(msg.to)
                    if G.invitee is not None:
                        gInviMids = [contact.mid for contact in G.invitee]
                        kk.cancelGroupInvitation(msg.to, gInviMids)
                    else:
                        if wait["lang"] == "JP":
                            kk.sendText(msg.to,"No one is inviting")
                        else:
                            kk.sendText(msg.to,"Sorry, nobody absent")
                else:
                    if wait["lang"] == "JP":
                        kk.sendText(msg.to,"Can not be used outside the group")
                    else:
                        kk.sendText(msg.to,"Not for use less than group")
            #elif "gurl" == msg.text:
                #print cl.getGroup(msg.to)
                ##cl.sendMessage(msg)
            elif msg.text in ["Ourl","Link on"]:
                if msg.toType == 2:
                    X = cl.getGroup(msg.to)
                    X.preventJoinByTicket = False
                    cl.updateGroup(X)
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Done")
                    else:
                        cl.sendText(msg.to,"already open")
                else:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Can not be used outside the group")
                    else:
                        cl.sendText(msg.to,"Not for use less than group")
            elif msg.text in ["Curl","Link off"]:
                if msg.toType == 2:
                    X = cl.getGroup(msg.to)
                    X.preventJoinByTicket = True
                    cl.updateGroup(X)
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Done")
                    else:
                        cl.sendText(msg.to,"already close")
                else:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Can not be used outside the group")
                    else:
                        cl.sendText(msg.to,"Not for use less than group")
            elif "jointicket " in msg.text.lower():
		rplace=msg.text.lower().replace("jointicket ")
		if rplace == "on":
			wait["atjointicket"]=True
		elif rplace == "off":
			wait["atjointicket"]=False
		cl.sendText(msg.to,"Auto Join Group by Ticket is %s" % str(wait["atjointicket"]))
            elif '/ti/g/' in msg.text.lower():
		link_re = re.compile('(?:line\:\/|line\.me\/R)\/ti\/g\/([a-zA-Z0-9_-]+)?')
		links = link_re.findall(msg.text)
		n_links=[]
		for l in links:
			if l not in n_links:
				n_links.append(l)
		for ticket_id in n_links:
			if wait["atjointicket"] == True:
				group=cl.findGroupByTicket(ticket_id)
				cl.acceptGroupInvitationByTicket(group.id,ticket_id)
				cl.sendText(msg.to,"Sukses join %s" % str(group.name))
            elif msg.text == "Ginfo":
                if msg.toType == 2:
                    ginfo = cl.getGroup(msg.to)
                    try:
                        gCreator = ginfo.creator.displayName
                    except:
                        gCreator = "Error"
                    if wait["lang"] == "JP":
                        if ginfo.invitee is None:
                            sinvitee = "0"
                        else:
                            sinvitee = str(len(ginfo.invitee))
                        if ginfo.preventJoinByTicket == True:
                            u = "close"
                        else:
                            u = "open"
                        cl.sendText(msg.to,"[group name]\n" + str(ginfo.name) + "\n[gid]\n" + msg.to + "\n[group creator]\n" + gCreator + "\n[profile status]\nhttp://dl.profile.line.naver.jp/" + ginfo.pictureStatus + "\nmembers:" + str(len(ginfo.members)) + "members\npending:" + sinvitee + "people\nURL:" + u + "it is inside")
                    else:
                        cl.sendText(msg.to,"[group name]\n" + str(ginfo.name) + "\n[gid]\n" + msg.to + "\n[group creator]\n" + gCreator + "\n[profile status]\nhttp://dl.profile.line.naver.jp/" + ginfo.pictureStatus)
                else:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Can not be used outside the group")
                    else:
                        cl.sendText(msg.to,"Not for use less than group")
            elif "Mid Bot" == msg.text:
              if msg.from_ in admin:
                cl.sendText(msg.to,mid)
                ki.sendText(msg.to,Amid)
                kk.sendText(msg.to,Bmid)
                kc.sendText(msg.to,Cmid)
                ko.sendText(msg.to,Gmid)
                ks.sendText(msg.to,Dmid)
                ke.sendText(msg.to,Hmid)
                lx.sendText(msg.to,Lmid)
                xl.sendText(msg.to,Xmid)
                ku.sendText(msg.to,Kmid)
            elif "Id" == msg.text:
                cl.sendText(msg.to,msg.to)
            elif msg.text in ["You"]:
                msg.contentType = 7
                msg.text = None
                msg.contentMetadata = {
                                     "STKID": "925",
                                     "STKPKGID": "14319",
                                     "STKVER": "100" }
                ki.sendMessage(msg)
                kk.sendMessage(msg)
            elif msg.text.lower() == '200c':
                msg.contentType = 9
                msg.contentMetadata={'PRDTYPE': 'STICKER',
                                    'STKVER': '1',
                                    'MSGTPL': '5',
                                    'STKPKGID': '1319678'}
                msg.text = None
                cl.sendMessage(msg)
            elif msg.text.lower() == '250c':
                msg.contentType = 9
                msg.contentMetadata={'PRDTYPE': 'STICKER',
                                    'STKVER': '1',
                                    'MSGTPL': '5',                                                                                        'STKPKGID': '1380280'}
                msg.text = None
                cl.sendMessage(msg)
            elif msg.text.lower() == 'Njiir':
                msg.contentType = 9
                msg.contentMetadata={'PRDTYPE': 'STICKER',
                                    'STKVER': '1',
                                    'MSGTPL': '5',
                                    'STKPKGID': '1300191'}
                msg.text = None
                cl.sendMessage(msg)
            elif msg.text in ["TL:"]:
                tl_text = msg.text.replace("TL:","")
                cl.sendText(msg.to,"line://home/post?userMid="+mid+"&postId="+cl.new_post(tl_text)["result"]["post"]["postInfo"]["postId"])
            elif msg.text in ["Cnder "]:
                string = msg.text.replace("Cnder ","")
                if len(string.decode('utf-8')) <= 20:
                    profile = cl.getProfile()
                    profile.displayName = string
                    cl.updateProfile(profile)
                    cl.sendText(msg.to,"name " + string + " done")
            elif msg.text in ["Menju"]:
              if msg.from_ in admin:
                string = msg.text.replace("哦上的 ","")
                if len(string.decode('utf-8')) <= 20:
                    profile_B = k4.getProfile()
                    profile_B.displayName = string
                    k4.updateProfile(profile_B)
                    k4.sendText(msg.to,"name " + string + " done")
            elif msg.text in ["AuThenTic"]:
              if msg.from_ in admin:
                string = msg.text.replace("哦上的 ","")
                if len(string.decode('utf-8')) <= 20:
                    profile_B = k1.getProfile()
                    profile_B.displayName = string
                    k1.updateProfile(profile_B)
                    k1.sendText(msg.to,"name " + string + " done")
            elif msg.text in ["Mc "]:
                mmid = msg.text.replace("Mc ","")
                msg.contentType = 13
                msg.contentMetadata = {"mid":mmid}
                cl.sendMessage(msg)
            
            elif msg.text in ["Protect On","protect on"]:
              if msg.from_ in admin:
                if wait["protectionOn"] == True:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Protection Stranger On")
                    else:
                        cl.sendText(msg.to,"done")
                else:
                    wait["protectionOn"] = True
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Protection Stranger On")
                    else:
                        cl.sendText(msg.to,"done")
            elif msg.text in ["Protect Off","protect off"]:
              if msg.from_ in admin:
                if wait["protectionOn"] == False:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Protection Stranger Off")
                    else:
                        cl.sendText(msg.to,"done")
                else:
                    wait["protectionOn"] = False
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Protection Stranger Off")
                    else:
                        cl.sendText(msg.to,"done")

            elif msg.text in ["Guest On","guest on"]:
              if msg.from_ in admin:
                if wait["Protectguest"] == True:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"ƤƦƠƬЄƇƬ ƖƝƔƖƬƛƬƖƠƝ ƠƝ")
                    else:
                        cl.sendText(msg.to,"done")
                else:
                    wait["Protectguest"] = True
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"ƤƦƠƬЄƇƬ ƖƝƔƖƬƛƬƖƠƝ ƠƝ")
                    else:
                        cl.sendText(msg.to,"done")
            elif msg.text in ["Guest Off","guest off"]:
              if msg.from_ in admin:
                if wait["Protectguest"] == False:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"ƤƦƠƬЄƇƬ ƖƝƔƖƬƛƬƖƠƝ ƠƑƑ")
                    else:
                        cl.sendText(msg.to,"done")
                else:
                    wait["Protectguest"] = False
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"ƤƦƠƬЄƇƬ ƖƝƔƖƬƛƬƖƠƝ ƠƑƑ")
                    else:
                        cl.sendText(msg.to,"done")
            elif msg.text in ["Qr on","qr on"]:
              if msg.from_ in admin:
                if wait["ProtectQR"] == True:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Protect QR On")
                    else:
                        cl.sendText(msg.to,"done")
                else:
                    wait["ProtectQR"] = True
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Protect QR On")
                    else:
                        cl.sendText(msg.to,"done")
            elif msg.text in ["Qr off","qr off"]:
              if msg.from_ in admin:
                if wait["ProtectQR"] == False:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Protect QR Off")
                    else:
                        cl.sendText(msg.to,"done")
                else:
                    wait["ProtectQR"] = False
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Protect QR Off")
                    else:
                        cl.sendText(msg.to,"done")
            elif msg.text in ["è‡ªå‹•å‚åŠ :ã‚ªãƒ³","Join on","Auto join:on","è‡ªå‹•åƒåŠ ï¼šé–‹"]:
                if wait["autoJoin"] == True:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"already on")
                    else:
                        cl.sendText(msg.to,"done")
                else:
                    wait["autoJoin"] = True
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"already on")
                    else:
                        cl.sendText(msg.to,"done")
            elif msg.text in ["è‡ªå‹•å‚åŠ :ã‚ªãƒ•","Join off","Auto join:off","è‡ªå‹•åƒåŠ ï¼šé—œ"]:
                if wait["autoJoin"] == False:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"already off")
                    else:
                        cl.sendText(msg.to,"done")
                else:
                    wait["autoJoin"] = False
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"already off")
                    else:
                        cl.sendText(msg.to,"done")
            elif msg.text in ["Gcancel:"]:
                try:
                    strnum = msg.text.replace("Gcancel:","")
                    if strnum == "off":
                        wait["autoCancel"]["on"] = False
                        if wait["lang"] == "JP":
                            cl.sendText(msg.to,"Invitation refused turned off\nTo turn on please specify the number of people and send")
                        else:
                            cl.sendText(msg.to,"å…³äº†é‚€è¯·æ‹’ç»ã€‚è¦æ—¶å¼€è¯·æŒ‡å®šäººæ•°å‘é€")
                    else:
                        num =  int(strnum)
                        wait["autoCancel"]["on"] = True
                        if wait["lang"] == "JP":
                            cl.sendText(msg.to,strnum + "The group of people and below decided to automatically refuse invitation")
                        else:
                            cl.sendText(msg.to,strnum + "ä½¿äººä»¥ä¸‹çš„å°ç»„ç”¨è‡ªåŠ¨é‚€è¯·æ‹’ç»")
                except:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Value is wrong")
                    else:
                        cl.sendText(msg.to,"Bizarre ratings")
            elif msg.text in ["å¼·åˆ¶è‡ªå‹•é€€å‡º:ã‚ªãƒ³","Leave on","Auto leave:on","å¼·åˆ¶è‡ªå‹•é€€å‡ºï¼šé–‹"]:
                if wait["leaveRoom"] == True:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"already on")
                    else:
                        cl.sendText(msg.to,"done")
                else:
                    wait["leaveRoom"] = True
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"done")
                    else:
                        cl.sendText(msg.to,"è¦äº†å¼€ã€‚")
            elif msg.text in ["Lroom off"]:
                if wait["leaveRoom"] == False:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"already off")
                    else:
                        cl.sendText(msg.to,"done")
                else:
                    wait["leaveRoom"] = False
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"done")
                    else:
                        cl.sendText(msg.to,"already")
            elif msg.text in ["å…±æœ‰:ã‚ªãƒ³","Share on","Share on"]:
                if wait["timeline"] == True:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"already on")
                    else:
                        cl.sendText(msg.to,"done")
                else:
                    wait["timeline"] = True
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"done")
                    else:
                        cl.sendText(msg.to,"è¦äº†å¼€ã€‚")
            elif msg.text in ["å…±æœ‰:ã‚ªãƒ•","Share off","Share off"]:
                if wait["timeline"] == False:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"already off")
                    else:
                        cl.sendText(msg.to,"done")
                else:
                    wait["timeline"] = False
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"done")
                    else:
                        cl.sendText(msg.to,"è¦äº†å…³æ–­ã€‚")
            elif msg.text in ["/set"]:
                if msg.from_ in admin:
		    md = ""
		    if wait["contact"] == True: md+=" [•]Contact ➣ on\n"
		    else: md+=" [•]Contact ➣ off\n"
		    if wait["autoJoin"] == True: md+=" [•]Auto join ➣ on\n"
		    else: md +=" [•]Auto join ➣ off\n"
		    if wait["autoCancel"]["on"] == True:md+=" [•]Group cancel :" + str(wait["autoCancel"]["members"]) + "\n"
		    else: md+= " [•]Group cancel ➣ off\n"
		    if wait["leaveRoom"] == True: md+=" [•]Auto leave ➣ on\n"
		    else: md+=" [•]Auto leave ➣ off\n"
		    if wait["timeline"] == True: md+=" [•]Share ➣ on\n"
		    else:md+=" [•]Share ➣ off\n"
		    if wait["autoAdd"] == True: md+=" [•]Auto add ➣ on\n"
		    else:md+=" [•]Auto add ➣ off\n"
		    if wait["commentOn"] == True: md+=" [•]Comment ➣ on\n"
		    else:md+=" [•]Comment ➣ off\n"
		    if wait["Protectcancel"] == True: md+=" [•]Mad ➣ on\n"
		    else:md+=" [•]Mad ➣ off\n"
		    if wait["Protectguest"] == True: md+=" [•]Guest ➣ on\n"
		    else:md+=" [•]Guest ➣ off\n"
		    if wait["atjointicket"] == True: md+=" [•]Auto Join Group by Ticket ➣ on\n"
		    else:md+=" [•]Auto Join Group by Ticket ➣ off\n"
		    cl.sendText(msg.to,md)
            elif "album merit " in msg.text:
                gid = msg.text.replace("album merit ","")
                album = cl.getAlbum(gid)
                if album["result"]["items"] == []:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"There is no album")
                    else:
                        cl.sendText(msg.to,"ç›¸å†Œæ²¡åœ¨ã€‚")
                else:
                    if wait["lang"] == "JP":
                        mg = "The following is the target album"
                    else:
                        mg = "ä»¥ä¸‹æ˜¯å¯¹è±¡çš„ç›¸å†Œ"
                    for y in album["result"]["items"]:
                        if "photoCount" in y:
                            mg += str(y["title"]) + ":" + str(y["photoCount"]) + "sheet\n"
                        else:
                            mg += str(y["title"]) + ":0sheet\n"
                    cl.sendText(msg.to,mg)
            elif "album " in msg.text:
                gid = msg.text.replace("album ","")
                album = cl.getAlbum(gid)
                if album["result"]["items"] == []:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"There is no album")
                    else:
                        cl.sendText(msg.to,"ç›¸å†Œæ²¡åœ¨ã€‚")
                else:
                    if wait["lang"] == "JP":
                        mg = "The following is the target album"
                    else:
                        mg = "ä»¥ä¸‹æ˜¯å¯¹è±¡çš„ç›¸å†Œ"
                    for y in album["result"]["items"]:
                        if "photoCount" in y:
                            mg += str(y["title"]) + ":" + str(y["photoCount"]) + "sheet\n"
                        else:
                            mg += str(y["title"]) + ":0sheet\n"
            elif "album remove " in msg.text:
                gid = msg.text.replace("album remove ","")
                albums = cl.getAlbum(gid)["result"]["items"]
                i = 0
                if albums != []:
                    for album in albums:
                        cl.deleteAlbum(gid,album["id"])
                        i += 1
                if wait["lang"] == "JP":
                    cl.sendText(msg.to,str(i) + "Deleted albums")
                else:
                    cl.sendText(msg.to,str(i) + "åˆ é™¤äº†äº‹çš„ç›¸å†Œã€‚")
            elif msg.text in ["Group id","ç¾¤çµ„å…¨id"]:
                gid = cl.getGroupIdsJoined()
                h = ""
                for i in gid:
                    h += "[%s]:%s\n" % (cl.getGroup(i).name,i)
                cl.sendText(msg.to,h)
            elif msg.text in ["Group id1"]:
                gid = ki.getGroupIdsJoined()
                h = ""
                for i in gid:
                    h += "[%s]:%s\n" % (ki.getGroup(i).name,i)
                ki.sendText(msg.to,h)
            elif msg.text in ["Cancelall"]:
                gid = cl.getGroupIdsInvited()
                for i in gid:
                    cl.rejectGroupInvitation(i)
                if wait["lang"] == "JP":
                    cl.sendText(msg.to,"All invitations have been refused")
                else:
                    cl.sendText(msg.to,"æ‹’ç»äº†å…¨éƒ¨çš„é‚€è¯·ã€‚")
            elif "album removeâ†’" in msg.text:
                gid = msg.text.replace("album removeâ†’","")
                albums = cl.getAlbum(gid)["result"]["items"]
                i = 0
                if albums != []:
                    for album in albums:
                        cl.deleteAlbum(gid,album["id"])
                        i += 1
                if wait["lang"] == "JP":
                    cl.sendText(msg.to,str(i) + "Albums deleted")
                else:
                    cl.sendText(msg.to,str(i) + "åˆ é™¤äº†äº‹çš„ç›¸å†Œã€‚")
            elif msg.text in ["Add on","Auto add:on","è‡ªå‹•è¿½åŠ ï¼šé–‹"]:
                if wait["autoAdd"] == True:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"already on")
                    else:
                        cl.sendText(msg.to,"done")
                else:
                    wait["autoAdd"] = True
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"done")
                    else:
                        cl.sendText(msg.to,"è¦äº†å¼€ã€‚")
            elif msg.text in ["Add off","Auto add:off","è‡ªå‹•è¿½åŠ ï¼šé—œ"]:
                if wait["autoAdd"] == False:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"already off")
                    else:
                        cl.sendText(msg.to,"done")
                else:
                    wait["autoAdd"] = False
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"done")
                    else:
                        cl.sendText(msg.to,"è¦äº†å…³æ–­ã€‚")
            elif "Message change: " in msg.text:
                wait["message"] = msg.text.replace("Message change: ","")
                cl.sendText(msg.to,"message changed")
            elif "Message add: " in msg.text:
                wait["message"] = msg.text.replace("Message add: ","")
                if wait["lang"] == "JP":
                    cl.sendText(msg.to,"message changed")
                else:
                    cl.sendText(msg.to,"doneã€‚")
            elif msg.text in ["Message","è‡ªå‹•è¿½åŠ å•å€™èªžç¢ºèª"]:
                if wait["lang"] == "JP":
                    cl.sendText(msg.to,"message change to\n\n" + wait["message"])
                else:
                    cl.sendText(msg.to,"The automatic appending information is set as followsã€‚\n\n" + wait["message"])
            elif "Comment:" in msg.text:
                c = msg.text.replace("Comment:","")
                if c in [""," ","\n",None]:
                    cl.sendText(msg.to,"message changed")
                else:
                    wait["comment"] = c
                    cl.sendText(msg.to,"changed\n\n" + c)
            elif "Add comment:" in msg.text:
                c = msg.text.replace("Add comment:","")
                if c in [""," ","\n",None]:
                    cl.sendText(msg.to,"String that can not be changed")
                else:
                    wait["comment"] = c
                    cl.sendText(msg.to,"changed\n\n" + c)
            elif msg.text in ["ã‚³ãƒ¡ãƒ³ãƒˆ:ã‚ªãƒ³","Comment on","Comment:on","è‡ªå‹•é¦–é ç•™è¨€ï¼šé–‹"]:
                if wait["commentOn"] == True:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"done")
                    else:
                        cl.sendText(msg.to,"already on")
                else:
                    wait["commentOn"] = True
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"done")
                    else:
                        cl.sendText(msg.to,"è¦äº†å¼€ã€‚")
            elif msg.text in ["ã‚³ãƒ¡ãƒ³ãƒˆ:ã‚ªãƒ•","Comment on","Comment off","è‡ªå‹•é¦–é ç•™è¨€ï¼šé—œ"]:
                if wait["commentOn"] == False:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"done")
                    else:
                        cl.sendText(msg.to,"already off")
                else:
                    wait["commentOn"] = False
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"done")
                    else:
                        cl.sendText(msg.to,"è¦äº†å…³æ–­ã€‚")
            elif msg.text in ["Comment","ç•™è¨€ç¢ºèª"]:
                cl.sendText(msg.to,"message changed to\n\n" + str(wait["comment"]))
            elif msg.text in ["Gurl"]:
              if msg.from_ in admin:
                if msg.toType == 2:
                    x = cl.getGroup(msg.to)
                    if x.preventJoinByTicket == True:
                        x.preventJoinByTicket = False
                        cl.updateGroup(x)
                    gurl = cl.reissueGroupTicket(msg.to)
                    cl.sendText(msg.to,"line://ti/g/" + gurl)
                else:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Can't be used outside the group")
                    else:
                        cl.sendText(msg.to,"Not for use less than group")
            elif msg.text in ["Bot1 gurl"]:
                if msg.toType == 2:
                    x = cl.getGroup(msg.to)
                    if x.preventJoinByTicket == True:
                        x.preventJoinByTicket = False
                        ki.updateGroup(x)
                    gurl = ki.reissueGroupTicket(msg.to)
                    ki.sendText(msg.to,"line://ti/g/" + gurl)
                else:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Can't be used outside the group")
                    else:
                        cl.sendText(msg.to,"Not for use less than group")
            elif msg.text in ["Bot2 gurl"]:
                if msg.toType == 2:
                    x = cl.getGroup(msg.to)
                    if x.preventJoinByTicket == True:
                        x.preventJoinByTicket = False
                        kk.updateGroup(x)
                    gurl = kk.reissueGroupTicket(msg.to)
                    kk.sendText(msg.to,"line://ti/g/" + gurl)
                else:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Can't be used outside the group")
                    else:
                        cl.sendText(msg.to,"Not for use less than group")
            elif msg.text in ["Bot3 gurl"]:
                if msg.toType == 2:
                    x = cl.getGroup(msg.to)
                    if x.preventJoinByTicket == True:
                        x.preventJoinByTicket = False
                        kc.updateGroup(x)
                    gurl = kc.reissueGroupTicket(msg.to)
                    kc.sendText(msg.to,"line://ti/g/" + gurl)
                else:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Can't be used outside the group")
                    else:
                        cl.sendText(msg.to,"Not for use less than group")
            elif msg.text in ["Comment bl "]:
                wait["wblack"] = True
                cl.sendText(msg.to,"add to comment bl")
            elif msg.text in ["Comment wl "]:
                wait["dblack"] = True
                cl.sendText(msg.to,"wl to comment bl")
            elif msg.text in ["Comment bl confirm"]:
                if wait["commentBlack"] == {}:
                    cl.sendText(msg.to,"confirmed")
                else:
                    cl.sendText(msg.to,"Blacklist")
                    mc = ""
                    for mi_d in wait["commentBlack"]:
                        mc += "" +cl.getContact(mi_d).displayName + "\n"
                    cl.sendText(msg.to,mc)
            elif msg.text in ["Change clock "]:
                n = msg.text.replace("Change clock ","")
                if len(n.decode("utf-8")) > 13:
                    cl.sendText(msg.to,"changed")
                else:
                    wait["cName"] = n
                    cl.sendText(msg.to,"changed to\n\n" + n)
#-----------------------------------------------
            elif ".kickall" in msg.text:
                    try:
                        ki.kickoutFromGroup(msg.to,[msg.from_])
                    except:
                        pass
            elif "kick on" in msg.text:
                    try:
                        kk.kickoutFromGroup(msg.to,[msg.from_])
                    except:
                        pass
            elif "Kickall" in msg.text:
                    try:
                        kc.kickoutFromGroup(msg.to,[msg.from_])
                    except:
                        pass
            elif "@Trisan " in msg.text.lower():
                    try:
                        cl.sendText(msg.to,"Jangan Tag Nama Owner Klo Ga Mao Kena Kick!!")
                        ki.kickoutFromGroup(msg.to,[msg.from_])
                    except:
                        pass
            elif "@trisan " in msg.text.lower():
                    try:
                        cl.sendText(msg.to,"Jangan tang Trisan!!")
                        ki.kickoutFromGroup(msg.to,[msg.from_])
                    except:
                        pass
#===============================================
            elif msg.text.lower() == 'Bot restart':
              if msg.from_ in admin:
                    print "[Command]Like executed"
                    try:
                        cl.sendText(msg.to,"Restarting...")
                        restart_program()
                    except:
                        cl.sendText(msg.to,"Please wait")
                        restart_program()
                        pass
            elif msg.text.lower() == 'ifconfig':
              if msg.from_ in admin:
                    botKernel = subprocess.Popen(["ifconfig"], stdout=subprocess.PIPE).communicate()[0]
                    cl.sendText(msg.to, botKernel + "\n\n===SERVER INFO NetStat===")
            elif msg.text.lower() == 'system':
              if msg.from_ in admin:
                    botKernel = subprocess.Popen(["df","-h"], stdout=subprocess.PIPE).communicate()[0]
                    cl.sendText(msg.to, botKernel + "\n\n===SERVER INFO SYSTEM===")
            elif msg.text.lower() == 'kernel':
              if msg.from_ in admin:
                    botKernel = subprocess.Popen(["uname","-srvmpio"], stdout=subprocess.PIPE).communicate()[0]
                    cl.sendText(msg.to, botKernel + "\n\n===SERVER INFO KERNEL===")
            elif msg.text.lower() == 'cpu':
              if msg.from_ in admin:
                    botKernel = subprocess.Popen(["cat","/proc/cpuinfo"], stdout=subprocess.PIPE).communicate()[0]
                    cl.sendText(msg.to, botKernel + "\n\n===SERVER INFO CPU===")
#-----------------------------------------------
            elif msg.text.lower() == 'runtime':
              if msg.from_ in admin:
                    eltime = time.time() - mulai
                    van = "Time Selama "+waktu(eltime)
                    cl.sendText(msg.to,van)

            elif msg.text in ["Kinvite"]:
              if msg.from_ in admin:
                 wait["winvite"] = True
                 cl.sendText(msg.to,"send contact")
#----------------------------------------------
            elif "Say-id " in msg.text:
                say = msg.text.replace("Say-id ","")
                lang = 'id'
                tts = gTTS(text=say, lang=lang)
                tts.save("hasil.mp3")
                cl.sendAudio(msg.to,"hasil.mp3")
#-----------------------------------------------

            elif "/joingc: " in msg.text:
              if msg.from_ in admin:
                gid = msg.text.replace("/joingc: ","")
                if gid == "":
                  cl.sendText(msg.to,"Invalid group id")
                else:
                  try:
                    cl.findAndAddContactsByMid(msg.from_)
                    cl.inviteIntoGroup(gid,[msg.from_])
                  except:
                    cl.sendText(msg.to,"Maaf Bos Ane Tidak Ada Di Group itu")
            elif "/joingc1: " in msg.text:
              if msg.from_ in admin:
                gid = msg.text.replace("/joingc1: ","")
                if gid == "":
                  ki.sendText(msg.to,"Invalid group id")
                else:
                  try:
                    ki.findAndAddContactsByMid(msg.from_)
                    ki.inviteIntoGroup(gid,[msg.from_])
                  except:
                    ki.sendText(msg.to,"Ane Telah Pergi Dari Group Tersebut")
#-----------------------------------------------
            elif 'Dorr' in msg.text:
              if msg.from_ in admin:
                msg.contentType = 13
                msg.contentMetadata = {'mid': "u1f41296217e740650e0448b96851a3e2',"}
                ki.sendMessage(msg)
# ----------------- BAN MEMBER BY TAG 2TAG ATAU 10TAG MEMBER
            elif ("Bl " in msg.text):
              if msg.from_ in admin:
                key = eval(msg.contentMetadata["MENTION"])
                key["MENTIONEES"][0]["M"]
                targets = []
                for x in key["MENTIONEES"]:
                    targets.append(x["M"])
                for target in targets:
                   try:
                      wait["blacklist"][target] = True
                      f=codecs.open('st2__b.json','w','utf-8')
                      json.dump(wait["blacklist"], f, sort_keys=True, indent=4,ensure_ascii=False)
                      cl.sendText(msg.to,"Succes Banned ")
                   except:
                      pass        

            elif msg.text in ["Clear Bl"]:
              if msg.from_ in admin:
                wait["blacklist"] = {}
                cl.sendText(msg.to,"Blacklist Telah Dibersihkan")
#-----------------------------------------------
            elif msg.text == "San":
                cl.sendText(msg.to, "ketik (1) Untuk melihat Sider!!")
                try:
                  del wait2['readPoint'][msg.to]
                  del wait2['readMember'][msg.to]
                except:
                  pass
                now2 = datetime.now()
                wait2['readPoint'][msg.to] = msg.id
                wait2['readMember'][msg.to] = ""
                wait2['setTime'][msg.to] = datetime.strftime(now2,"%H:%M")
                wait2['ROM'][msg.to] = {}
                #print wait2
              
            elif msg.text == "1":
                    if msg.to in wait2['readPoint']:
                        if wait2["ROM"][msg.to].items() == []:
                            chiya = ""
                        else:
                            chiya = ""
                            for rom in wait2["ROM"][msg.to].items():
                                #print rom
                                chiya += rom[1] + "\n"

                        cl.sendText(msg.to, "╔═══════════════%s\n╠════════════════\n%s╠═══════════════\n║Reading point creation:\n║ [%s]\n╚════════════════\n||BOT Public||" % (wait2['readMember'][msg.to],chiya,setTime[msg.to]))
                    else:
                        cl.sendText(msg.to, "Ketik San\nBaru Ketik 1\n ♪")
#-----------------------------------------------
            elif msg.text in ["Bot out","Op bye"]:
              if msg.from_ in admin:
                gid = cl.getGroupIdsJoined()
                gid = ki.getGroupIdsJoined()
                gid = kk.getGroupIdsJoined()
                gid = kc.getGroupIdsJoined()
                gid = ks.getGroupIdsJoined()
                gid = ko.getGroupIdsjoined()
                git = ke.getGroupIdsjoined()
                for i in gid:
                  ks.leaveGroup(i)
                  kc.leaveGroup(i)
                  ki.leaveGroup(i)
                  kk.leaveGroup(i)
                  ko.leaveGroup(i)
                  ke.leaveGroup(i)
                if wait["lang"] == "JP":
                  cl.sendText(msg.to,"Sedang Ada Perbaikan R lagi iya Nanti")
                else:
                  cl.sendText(msg.to,"He declined all invitations")
#-----------------------------------------------

            elif msg.text in ["@bot out"]:
              if msg.from_ in admin:
                gid = cl.getGroupIdsJoined()
                for i in gid:
                  cl.leaveGroup(i)
                if wait["lang"] == "JP":
                  cl.sendText(msg.to,"Tidak ada Bos!!")
                else:
                  cl.sendText(msg.to,"He declined all invitations")
#-----------------------------------------------
            elif "Set member: " in msg.text:
		if msg.from_ in admin:
		    jml = msg.text.replace("Set member: ","")
		    wait["Members"] = int(jml)
		    cl.sendText(msg.to, "Jumlah minimal member telah di set : "+jml)
		else:
		    cl.sendText(msg.to, "Khusus Admin")
#-----------------------------------------------

            elif "/movechat" in msg.text.lower():
                if msg.from_ in admin:
                    try:
                        cl.removeAllMessages(op.param2)
                        ki.removeAllMessages(op.param2)
                        kk.removeAllMessages(op.param2)
                        kc.removeAllMessages(op.param2)
                        ko.removeAllMessages(op.param2)
                        ke.removeAllMessages(op.param2)
                        ks.removeAllMessages(op.param2)
                        ku.removeAllMessages(op.param2)
                        xl.removeAllMessages(op.param2)
                        lx.removeAllMessages(op.param2)
                        ww.removeAllMessages(op.param2)
                        pw.removeAllMessages(op.param2)
                        print "[Command] Remove Chat"
                        cl.sendText(msg.to,"RemoveChat Done Bos!!")
                    except Exception as error:
                        print error
                        cl.sendText(msg.to,"LineError")
#-----------------------------------------+++---

            elif msg.text in ["Tagall"]:
              if msg.from_ in admin:
                group = cl.getGroup(msg.to)
                nama = [contact.mid for contact in group.members]
                cb = ""
                cb2 = ""
                strt = int(0)
                akh = int(0)
                for md in nama:
                    akh = akh + int(5)
                    cb += """{"S":"""+json.dumps(str(strt))+""","E":"""+json.dumps(str(akh))+""","M":"""+json.dumps(md)+"},"""
                    strt = strt + int(6)
                    akh = akh + 1
                    cb2 += "@nrik\n"
                cb = (cb[:int(len(cb)-1)])
                msg.contentType = 0
                msg.text = cb2
                msg.contentMetadata ={'MENTION':'{"MENTIONEES":['+cb+']}','EMTVER':'4'}
                try:
                    ki.sendMessage(msg)
                except Exception as error:
                    print error
#-----------------------------------------------
            elif msg.text in ["Test"]:
              if msg.from_ in admin:
                G = cl.getGroup(msg.to)
                ginfo = cl.getGroup(msg.to)
                G.preventJoinByTicket = False
                cl.updateGroup(G)
                invsend = 0
                Ticket = cl.reissueGroupTicket(msg.to)
                ki.acceptGroupInvitationByTicket(msg.to,Ticket)
                time.sleep(0.0)
                kk.acceptGroupInvitationByTicket(msg.to,Ticket)
                time.sleep(0.0)
                kc.acceptGroupInvitationByTicket(msg.to,Ticket)
                time.sleep(0.0)
                ks.acceptGroupInvitationByTicket(msg.to,Ticket)
                time.sleep(0.0)
                ko.acceptGroupInvitationByTicket(msg.to,Ticket)
                time.sleep(0.0)
                ke.acceptGroupInvitationByTicket(msg.to,Ticket)
                time.sleep(0.0)
                lx.acceptGroupInvitationByTicket(msg.to,Ticket)
                time.sleep(0.0)
                xl.acceptGroupInvitationByTicket(msg.to,Ticket)
                time.sleep(0.0)
                ww.acceptGroupInvitationByTicket(msg.to,Ticket)
                time.sleep(0.0)
                pw.acceptGroupInvitationByTicket(msg.to,Ticket)
                time.sleep(0.0)
                G = cl.getGroup(msg.to)
                ginfo = cl.getGroup(msg.to)
                G.preventJoinByTicket = True
                random.choice(KAC).updateGroup(G)
                print "kicker ok"
                G.preventJoinByTicket(G)
                random.choice(KAC).updateGroup(G)

            elif msg.text in ["Der1"]:
                  X = cl.getGroup(msg.to)
                  X.preventJoinByTicket = False
                  cl.updateGroup(X)
                  invsend = 0
                  Ti = cl.reissueGroupTicket(msg.to)
                  ki.acceptGroupInvitationByTicket(msg.to,Ti)
                  G = ki.getGroup(msg.to)
                  G.preventJoinByTicket = True
                  ki.updateGroup(G)
                  Ticket = ki.reissueGroupTicket(msg.to)

            elif msg.text in ["Der2"]:
                  X = cl.getGroup(msg.to)
                  X.preventJoinByTicket = False
                  cl.updateGroup(X)
                  invsend = 0
                  Ti = cl.reissueGroupTicket(msg.to)
                  kk.acceptGroupInvitationByTicket(msg.to,Ti)
                  G = ki.getGroup(msg.to)
                  G.preventJoinByTicket = True
                  kk.updateGroup(G)
                  Ticket = kk.reissueGroupTicket(msg.to)

            elif msg.text in ["Kicker"]:
                  X = cl.getGroup(msg.to)
                  X.preventJoinByTicket = False
                  cl.updateGroup(X)
                  invsend = 0
                  Ti = cl.reissueGroupTicket(msg.to)
                  ku.acceptGroupInvitationByTicket(msg.to,Ti)
                  G = ku.getGroup(msg.to)
                  G.preventJoinByTicket = True
                  ku.updateGroup(G)
                  Ticket = ku.reissueGroupTicket(msg.to)

#-----------------------------------------------
#.acceptGroupInvitationByTicket(msg.to,Ticket)
            elif msg.text in ["Der3 join"]:
                        G = cl.getGroup(msg.to)
                        ginfo = cl.getGroup(msg.to)
                        G.preventJoinByTicket = False
                        cl.updateGroup(G)
                        invsend = 0
                        Ticket = cl.reissueGroupTicket(msg.to)
                        kc.acceptGroupInvitationByTicket(msg.to,Ticket)
                        print "Der3 join"
                        G.preventJoinByTicket = True
                        kc.updateGroup(G)
#-----------------------------------------------
            elif msg.text in ["★"]:
              if msg.from_ in admin:
                if msg.toType == 2:
                    ginfo = cl.getGroup(msg.to)
                    try:
                        ki.leaveGroup(msg.to)
                        time.sleep(0.0)
                        kk.leaveGroup(msg.to)
                        time.sleep(0.0)
                        ks.leaveGroup(msg.to)
                        time.sleep(0.0)
                        kc.leaveGroup(msg.to)
                        time.sleep(0.0)
                        ko.leaveGroup(msg.to)
                        time.sleep(0.0)
                        ke.leaveGroup(msg.to)
                        time.sleep(0.0)
                        lx.leaveGroup(msg.to)
                        time.sleep(0.0)
                        xl.leaveGroup(msg.to)
                        time.sleep(0.0)
                        ww.leaveGroup(msg.to)
                        time.sleep(0.0)
                        pw.leaveGroup(msg.to)
                        time.sleep(0.0)
                        ku.leaveGroup(msg.to)
                        time.sleep(0.0)
                    except:
                        pass

            elif msg.text in ["//Bye"]:
              if msg.from_ in admin:
                if msg.toType == 2:
                    ginfo = cl.getGroup(msg.to)
                    try:
                        cl.leaveGroup(msg.to,)
                        time.sleep(0.01)
                    except:
                        pass
            elif msg.text in ["@Qr"]:
              if msg.from_ in admin:
                if msg.toType == 2:
                    ginfo = ku.getGroup(msg.to)
                    try:
                        ku.leaveGroup(msg.to,)
                    except:
                        pass
#-----------------------------------------------
            elif msg.text in ["Kill"]:
              if msg.from_ in admin:
                if msg.toType == 2:
                    group = ki.getGroup(msg.to)
                    gMembMids = [contact.mid for contact in group.members]
                    matched_list = []
                    for tag in wait["blacklist"]:
                        matched_list+=filter(lambda str: str == tag, gMembMids)
                    if matched_list == []:
                        kk.sendText(msg.to,"Fuck You")
                        return
                    for jj in matched_list:
                        try:
                            klist=[ki,kk,kc]
                            kicker=random.choice(klist)
                            kicker.kickoutFromGroup(msg.to,[jj])
                            print (msg.to,[jj])
                        except:
                            pass
            elif "Room." in msg.text:
              if msg.from_ in admin:
                if msg.toType == 2:
                    print "ok"
                    _name = msg.text.replace("Room.","")
                    gs = cl.getGroup(msg.to)
                    gs = ki.getGroup(msg.to)
                    gs = kk.getGroup(msg.to)
                    gs = kc.getGroup(msg.to)
                    ki.sendText(msg.to,"Ini Room apa? ?!")
                    cl.sendText(msg.to,"Group Di Sita.")
                    k4.sendText(msg.to,"Rata Gak Rata")
                    kc.sendText(msg.to,"Kita Mampir Menghibur Kalian")
                    targets = []
                    for g in gs.members:
                        if _name in g.displayName:
                            targets.append(g.mid)
                    if targets == []:
                        ki.sendText(msg.to,"Not found.")
                    else:
                        for target in targets:
                            try:
                                klist=[ki,kk,kc,cl]
                                kicker=random.choice(klist)
                                kicker.kickoutFromGroup(msg.to,[target])
                                print (msg.to,[g.mid])
                            except:
                                ki.sendText(msg.to,"Group Disita")

            elif "Nk " in msg.text:
                  if msg.from_ in admin:
                       nk0 = msg.text.replace("Nk ","")
                       nk1 = nk0.lstrip()
                       nk2 = nk1.replace("@","")
                       nk3 = nk2.rstrip()
                       _name = nk3
                       gs = cl.getGroup(msg.to)
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
                                    klist=[cl,ki,kk,kc]
                                    kicker=random.choice(klist)
                                    kicker.kickoutFromGroup(msg.to,[target])
                                    print (msg.to,[g.mid])
                                except:
                                    kk.sendText(msg.to,"Fuck You")
            elif "Blacklist @ " in msg.text:
                _name = msg.text.replace("Blacklist @ ","")
                _kicktarget = _name.rstrip(' ')
                gs = ki2.getGroup(msg.to)
                targets = []
                for g in gs.members:
                    if _kicktarget == g.displayName:
                        targets.append(g.mid)
                        if targets == []:
                            cl.sendText(msg.to,"Not found")
                        else:
                            for target in targets:
                                try:
                                    wait["blacklist"][target] = True
                                    f=codecs.open('st2__b.json','w','utf-8')
                                    json.dump(wait["blacklist"], f, sort_keys=True, indent=4,ensure_ascii=False)
                                    k3.sendText(msg.to,"Succes ")
                                except:
                                    ki.sendText(msg.to,"error")
#-----------------------------------------------
            elif "Ban all" in msg.text:
                if msg.from_ in admin:
                    if msg.toType == 2:
                        print "[Ban]ok"
                        _name = msg.text.replace("Ban all","")
                        gs = cl.getGroup(msg.to)
                        cl.sendText(msg.to,"BL Succes💀")
                        targets = []
                        for g in gs.members:
                                if _name in g.displayName:
                                        targets.append(g.mid)
                        if targets == []:
                                cl.sendText(msg.to,"Tidak Ada Boss")
                        else:
                                for target in targets:
                                        try:
                                            wait["blacklist"][target] = True
                                            f=codecs.open('st2__b.json','w','utf-8')
                                            json.dump(wait["blacklist"], f, sort_keys=True, indent=4,ensure_ascii=False)
                                        except:
                                            cl.sendText(msg.to,"Succes")
#-----------------------------------------------
            elif "Unban all" in msg.text:
                if msg.from_ in admin:
                    if msg.toType == 2:
                        print "[Unban]ok"
                        _name = msg.text.replace("Unban all","")
                        gs = cl.getGroup(msg.to)
                        cl.sendText(msg.to,"BL Delete")
                        targets = []
                        for g in gs.members:
                                if _name in g.displayName:
                                        targets.append(g.mid)
                        if targets == []:
                                cl.sendText(msg.to,"Tidak Ada Boss Owner")
                        else:
                                for target in targets:
                                        try:
                                            del wait["blacklist"][target]
                                            f=codecs.open('st2__b.json','w','utf-8')
                                            json.dump(wait["blacklist"], f, sort_keys=True, indent=4,ensure_ascii=False)
                                        except:
                                            cl.sendText(msg.to)
#-----------------------------------------------

            elif "Mid @" in msg.text:
        	if msg.from_ in admin:
                  _name = msg.text.replace("Mid @","")
                  _nametarget = _name.rstrip(' ')
                  gs = cl.getGroup(msg.to)
                  for g in gs.members:
                      if _nametarget == g.displayName:
                          cl.sendText(msg.to, g.mid)
                      else:
                          pass
#-----------------------------------------------
            elif "Unban @" in msg.text:
                if msg.toType == 2:
                    print "[Unban]ok"
                    _name = msg.text.replace("Unban @","")
                    _nametarget = _name.rstrip('  ')
                    gs = ki.getGroup(msg.to)
                    gs = kk.getGroup(msg.to)
                    gs = kc.getGroup(msg.to)
                    targets = []
                    for g in gs.members:
                        if _nametarget == g.displayName:
                            targets.append(g.mid)
                    if targets == []:
                        ki.sendText(msg.to,"Not found ")
                    else:
                        for target in targets:
                            try:
                                del wait["blacklist"][target]
                                f=codecs.open('st2__b.json','w','utf-8')
                                json.dump(wait["blacklist"], f, sort_keys=True, indent=4,ensure_ascii=False)
                                cl.sendText(msg.to,"Succes ")
                            except:
                                ki.sendText(msg.to,"Succes ")
#-----------------------------------------------
            elif "Glist" in msg.text:
                if msg.from_ in admin:
                        gid = cl.getGroupIdsJoined()
                        h = ""
                        for i in gid:
                            h += "%s\n" % (cl.getGroup(i).name +" ? ["+str(len(cl.getGroup(i).members))+"]")
                        cl.sendText(msg.to,"-- List Groups --\n\n"+ h +"\nTotal groups =" +" ["+str(len(gid))+"]")
                        print "Glist"
#-----------------------------------------------
            elif msg.text in ["Gcreator:inv"]:
               if msg.from_ in admin:
                    ginfo = cl.getGroup(msg.to)
                    gCreator = ginfo.creator.mid
                    try:
                       cl.findAndAddContactsByMid(gCreator)
                       cl.inviteIntoGroup(msg.to,[gCreator])
                       print "success inv gCreator"
                    except:
                       pass

            elif msg.text in ["Gcreator"]:
              if msg.toType == 2:
                    msg.contentType = 13
                    ginfo = cl.getGroup(msg.to)
                    gCreator = ginfo.creator.mid
                    try:
                        msg.contentMetadata = {'mid': gCreator}
                        gCreator1 = ginfo.creator.displayName

                    except:
                        gCreator = "Error"
                    cl.sendText(msg.to, "Group Creator : " + gCreator1)
                    cl.sendMessage(msg)
#-----------------------------------------------
            elif msg.from_ in mimic["target"] and mimic["status"] == True and mimic["target"][msg.from_] == True:
        	text = msg.text
        	if text is not None:
        	    cl.sendText(msg.to,text)
        	else:
        	    if msg.contentType == 7:
        		msg.contentType = 7
        		msg.text = None
        		msg.contentMetadata = {
        				     "STKID": "6",
        				     "STKPKGID": "1",
        				     "STKVER": "100" }
        		cl.sendMessage(msg)
        	    elif msg.contentType == 13:
        		msg.contentType = 13
        		msg.contentMetadata = {'mid': msg.contentMetadata["mid"]}
        		cl.sendMessage(msg)
            elif "Mimic:" in msg.text:
        	if msg.from_ in admin:
        	    cmd = msg.text.replace("Mimic:","")
        	    if cmd == "on":
        		if mimic["status"] == False:
        		    mimic["status"] = True
        		    cl.sendText(msg.to,"Mimic on")
        		else:
        		    cl.sendText(msg.to,"Mimic already on")
        	    elif cmd == "off":
        		if mimic["status"] == True:
        		    mimic["status"] = False
        		    cl.sendText(msg.to,"Mimic off")
        		else:
        		    cl.sendText(msg.to,"Mimic already off")
        	    elif "add:" in cmd:
        		target0 = msg.text.replace("Mimic:add:","")
        		target1 = target0.lstrip()
        		target2 = target1.replace("@","")
        		target3 = target2.rstrip()
        		_name = target3
        		gInfo = cl.getGroup(msg.to)
        		targets = []
        		for a in gInfo.members:
        		    if _name == a.displayName:
        			targets.append(a.mid)
        		if targets == []:
        		    cl.sendText(msg.to,"No targets")
        		else:
        		    for target in targets:
        			try:
        			    mimic["target"][target] = True
        			    cl.sendText(msg.to,"Success added target")
        			    #cl.sendMessageWithMention(msg.to,target)
        			    break
        			except:
        			    cl.sendText(msg.to,"Failed")
        			    break
        	    elif "del:" in cmd:
        		target0 = msg.text.replace("Mimic:del:","")
        		target1 = target0.lstrip()
        		target2 = target1.replace("@","")
        		target3 = target2.rstrip()
        		_name = target3
        		gInfo = cl.getGroup(msg.to)
        		targets = []
        		for a in gInfo.members:
        		    if _name == a.displayName:
        			targets.append(a.mid)
        		if targets == []:
        		    cl.sendText(msg.to,"No targets")
        		else:
        		    for target in targets:
        			try:
        			    del mimic["target"][target]
        			    cl.sendText(msg.to,"Success deleted target")
        			    #cl.sendMessageWithMention(msg.to,target)
        			    break
        			except:
        			    cl.sendText(msg.to,"Failed!")
        			    break
        	    elif cmd == "ListTarget":
        		if mimic["target"] == {}:
        		    cl.sendText(msg.to,"No target")
                        else:
                	    lst = "<<Lit Target>>"
                	    total = len(mimic["target"])
                	    for a in mimic["target"]:
            		        if mimic["target"][a] == True:
            			    stat = "On"
            		        else:
            			    stat = "Off"
            		        lst += "\n->" + cl.getContact(mi_d).displayName + " | " + stat
                                cl.sendText(msg.to,lst + "\nTotal:" + total)
#-----------------------------------------------
            elif msg.text in ["Mad On","mad on"]:
              if msg.from_ in admin:
                 if wait["Protectcancel"] == True:
                     if wait["lang"] == "JP":
                         cl.sendText(msg.to,"Dont cancel anyone ! cause me angry!")
                     else:
                         cl.sendText(msg.to,"done")
                 else:
                    wait["Protectcancel"] = True
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Protect Cancel On")
                    else:
                        cl.sendText(msg.to,"done")
            elif msg.text in ["Mad Off","mad off"]:
              if msg.from_ in admin:
                if wait["Protectcancel"] == False:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Protect Cancel Off")
                    else:
                        cl.sendText(msg.to,"done")
                else:
                    wait["Protectcancel"] = False
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Protect Cancel Off")
                    else:
                        cl.sendText(msg.to,"done")
#-----------------------------------------------
            elif "Fuck " in msg.text:
              if msg.from_ in admin:
                key = eval(msg.contentMetadata["MENTION"])
                key["MENTIONEES"][0]["M"]
                targets = []
                for x in key["MENTIONEES"]:
                    targets.append(x["M"])
                for target in targets:
                   try:
                      cl.kickoutFromGroup(msg.to,[target])
                   except:
                      pass
            elif "Rom kick " in msg.text:
              if msg.from_ in admin:
                key = eval(msg.contentMetadata["MENTION"])
                key["MENTIONEES"][0]["M"]
                targets = []
                for x in key["MENTIONEES"]:
                    targets.append(x["M"])
                for target in targets:
                   try:
                      ki.kickoutFromGroup(msg.to,[target])
                   except:
                      pass
            elif "Rom2 kick " in msg.text:
              if msg.from_ in admin:
                key = eval(msg.contentMetadata["MENTION"])
                key["MENTIONEES"][0]["M"]
                targets = []
                for x in key["MENTIONEES"]:
                    targets.append(x["M"])
                for target in targets:
                   try:
                      kk.kickoutFromGroup(msg.to,[target])
                   except:
                      pass
            elif "Rom3 kick " in msg.text:
              if msg.from_ in admin:
                key = eval(msg.contentMetadata["MENTION"])
                key["MENTIONEES"][0]["M"]
                targets = []
                for x in key["MENTIONEES"]:
                    targets.append(x["M"])
                for target in targets:
                   try:
                      kc.kickoutFromGroup(msg.to,[target])
                   except:
                      pass
#-----------------------------------------------
            elif msg.text in ["/Respon","/pesan"]:
              if msg.from_ in admin:
                cl.sendText(msg.to,"♦Respon Di Terima♦")
                ki.sendText(msg.to,"Done♦♪")
                kk.sendText(msg.to,"Done♦♦♪")
                ko.sendText(msg.to,"Done♦♦♦♪")
                kc.sendText(msg.to,"Done♦♦♦♦♪")
                ks.sendText(msg.to,"Done♦♦♦♦♦♪")
                ke.sendText(msg.to,"Done♦♦♦♦♦♦♪")
                lx.sendText(msg.to,"Done♦♦♦♦♦♦♦♦♪")
                xl.sendText(msg.to,"♪♪♪♪DoneAll♪♪♪♪♪♪♪")
                print "/Respon"
#-----------------------------------------------
            elif msg.text in ["Creator"]:
		    msg.contentType = 13
		    msg.contentMetadata = {'mid': "uba553877e995e2bd476d1d78469dc8d2"}
		    cl.sendMessage(msg)
            elif msg.text in ["Creator1"]:
		    msg.contentType = 13
		    msg.contentMetadata = {'mid': "u1b9ab645520fa5ae9d734f6e6b9b56ba"}
		    cl.sendMessage(msg)
#-----------------------------------------------

            elif "Admin add @" in msg.text:
                if msg.from_ in creator:
                    print "[Command]Staff add executing"
                    _name = msg.text.replace("Admin add @","")
                    _nametarget = _name.rstrip('  ')
                    gs = cl.getGroup(msg.to)
                    targets = []
                    for g in gs.members:
                        if _nametarget == g.displayName:
                            targets.append(g.mid)
                    if targets == []:
                        ki.sendText(msg.to,"Contact not found")
                    else:
                        for target in targets:
                            try:
                                admin.append(target)
                                cl.sendText(msg.to,"Admin Ditambahkan")
                            except:
                                pass
                    print "[Command]Staff add executed"
                else:
                    cl.sendText(msg.to,"*\(×__=)/*")

            elif "Admin remove @" in msg.text:
                if msg.from_ in creator:
                    print "[Command]Staff remove executing"
                    _name = msg.text.replace("Admin remove @","")
                    _nametarget = _name.rstrip('  ')
                    gs = cl.getGroup(msg.to)
                    targets = []
                    for g in gs.members:
                        if _nametarget == g.displayName:
                            targets.append(g.mid)
                    if targets == []:
                        ki.sendText(msg.to,"Contact not found")
                    else:
                        for target in targets:
                            try:
                                admin.remove(target)
                                cl.sendText(msg.to,"Admin Dihapus")
                            except:
                                pass
                    print "[Command]Staff remove executed"
                else:
                    cl.sendText(msg.to,"\(x_x)//")

            elif msg.text in ["Adminlist"]:
              if msg.from_ in creator:
                if admin == []:
                    cl.sendText(msg.to,"The adminlist is empty")
                else:
                    cl.sendText(msg.to,"Tunggu...")
                    mc = ""
                    for mi_d in admin:
                        mc += "➣"+cl.getContact(mi_d).displayName + "\n"
                    cl.sendText(msg.to,mc)
                    print "[Command]Stafflist executed"
#-----------------------------------------------
            elif "Apakah " in msg.text:
                tanya = msg.text.replace("Apakah ","")
                jawab = ("Ya","Tidak")
                jawaban = random.choice(jawab)
                cl.sendText(msg.to,jawaban)
#-----------------------------------------------

            elif "Mbc " in msg.text: #NgeBC Ke semua Group yang di Join :D
              if msg.from_ in admin:
                bctxt = msg.text.replace("Mbc ","")
                a = cl.getGroupIdsJoined()
                for taf in a:
                  cl.sendText(taf, (bctxt))
#-----------------------------------------------

            elif "Rate " in msg.text:
                tanya = msg.text.replace("Rate ","")
                jawab = ("10% Der","20% Der","15% Der","30% Der","40% Der","50% Der","60% Der","70% Der","80% Der","90% Der","100% Der")
                jawaban = random.choice(jawab)
                cl.sendText(msg.to,jawaban)
#------------------------------------------------

            elif "Copy @" in msg.text:
                if msg.from_ in admin:
                    if msg.toType == 2:
                        _name = msg.text.replace("Copy @","")
                        _nametarget = _name.rstrip('  ')
                        gs = cl.getGroup(msg.to)
                        targets = []
                        for g in gs.members:
                            if _nametarget == g.displayName:
                                targets.append(g.mid)
                        if targets == []:
                            cl.sendText(msg.to, "Not Found...")
                        else:
                            for target in targets:
                                try:
                                    cl.cloneContactProfile(target)
                                    cl.sendText(msg.to, "Succes Copy profile")
                                except Exception as e:
                                    print e
#-----------------------------------------------

            elif msg.text in ["Backup","backup"]:
                if msg.from_ in admin:
                    try:
                       cl.updateDisplayPicture(backup.pictureStatus)
                       cl.updateProfile(backup)
                       cl.sendText(msg.to, "Telah kembali semula")
                    except Exception as e:
                       cl.sendText(msg.to, str(e))
#-----------------------------------------------
            elif msg.text in ["Sp","Speed","speed"]:
              if msg.from_ in admin:
                start = time.time()
                print ("Speed")
                elapsed_time = time.time() - start
                cl.sendText(msg.to, "%s Detik" % (elapsed_time))
#-----------BCKONTCK----------------------------
            elif "Spam @" in msg.text:
              if msg.from_ in admin:
                _name = msg.text.replace("Spam @","")
                _nametarget = _name.rstrip(' ')
                gs = cl.getGroup(msg.to)
                for g in gs.members:
                    if _nametarget == g.displayName:
                       cl.sendText(g.mid,"Ini Adalah Mugiwara")
                       cl.sendText(g.mid,"Ini Adalah Mugiwara")
                       cl.sendText(g.mid,"Ini Adalah Spam")
                       cl.sendText(g.mid,"Ini Adalah Spam")
                       cl.sendText(g.mid,"Ini Adalah Spam")
                       cl.sendText(g.mid,"Ini Adalah Spam") 
                       cl.sendText(g.mid,"Ini Adalah Spam")
                       cl.sendText(g.mid,"Ini Adalah Spam")
                       cl.sendText(g.mid,"Ini Adalah Spam")
                       cl.sendText(g.mid,"Ini Adalah Spam")
                       cl.sendText(g.mid,"Ini Adalah Spam")
                       cl.sendText(g.mid,"Ini Adalah Spam")
                       cl.sendText(g.mid,"Ini Adalah Spam")
                       cl.sendText(g.mid,"Ini Adalah Spam")
                       cl.sendText(g.mid,"Ini Adalah Spam")
                       cl.sendText(g.mid,"Ini Adalah Spam")
                       cl.sendText(g.mid,"Ini Adalah Spam")
                       cl.sendText(g.mid,"Ini Adalah Spam")
                       cl.sendText(g.mid,"Ini Adalah Spam")
                       cl.sendText(g.mid,"Ini Adalah Spam")
                       cl.sendText(g.mid,"Ini Adalah Spam")
                       cl.sendText(g.mid,"Ini Adalah Spam")
                       cl.sendText(g.mid,"Ini Adalah Spam")
                       cl.sendText(g.mid,"Ini Adalah Spam")
                       cl.sendText(g.mid,"Ini Adalah Spam")
                       cl.sendText(g.mid,"Ini Adalah Spam")
                       cl.sendText(g.mid,"Ini Adalah Spam")
                       cl.sendText(g.mid,"Ini Adalah Spam")
                       cl.sendText(g.mid,"Ini Adalah Spam")
                       cl.sendText(g.mid,"Ini Adalah Spam")
                       cl.sendText(g.mid,"Ini Adalah Spam")
                       cl.sendText(g.mid,"Ini Adalah Spam")
                       cl.sendText(g.mid,"Ini Adalah Spam")
                       cl.sendText(g.mid,"Ini Adalah Spam")
                       cl.sendText(g.mid,"Ini Adalah Mugiwara")
                       cl.sendText(g.mid,"Ini Adalah Mugiwara")
                       cl.sendText(g.mid,"Ini Adalah Mugiwara")
                       cl.sendText(g.mid,"Ini Adalah Mugiwara")
                       cl.sendText(g.mid,"Ini Adalah Spam")
                       cl.sendText(g.mid,"Ini Adalah Spam")
                       cl.sendText(g.mid,"Ini Adalah Spam")
                       cl.sendText(g.mid,"Ini Adalah Spam")
                       cl.sendText(g.mid,"Ini Adalah Spam")
                       cl.sendText(g.mid,"Ini Adalah Spam")
                       cl.sendText(g.mid,"Ini Adalah Spam")
                       cl.sendText(g.mid,"Ini Adalah Spam")
                       cl.sendText(g.mid,"Ini Adalah Spam")
                       cl.sendText(g.mid,"Ini Adalah Mugiwara")
                       cl.sendText(g.mid,"Ini Adalah Mugiwara")
                       cl.sendText(g.mid,"Ini Adalah Mugiwara")
                       cl.sendText(g.mid,"Ini Adalah Mugiwara")
                       cl.sendText(g.mid,"Ini Adalah Spam")
                       cl.sendText(g.mid,"Ini Adalah Spam")
                       cl.sendText(g.mid,"Ini Adalah Spam")
                       cl.sendText(g.mid,"Ini Adalah Spam")
                       cl.sendText(g.mid,"Ini Adalah Spam")
                       cl.sendText(g.mid,"Ini Adalah Spam")
                       cl.sendText(g.mid,"Ini Adalah Spam")
                       cl.sendText(g.mid,"Ini Adalah Spam")
                       cl.sendText(g.mid,"Ini Adalah Spam")
                       cl.sendText(g.mid,"Ini Adalah Spam")
                       cl.sendText(g.mid,"Ini Adalah Mugiwara")
                       cl.sendText(g.mid,"Ini Adalah Mugiwara")
                       cl.sendText(g.mid,"Ini Adalah Mugiwara")
                       cl.sendText(g.mid,"Ini Adalah Mugiwara")
                       cl.sendText(msg.to, "Done")
                       print " Spammed !"
#-----------BCKONTK-----------------------------
            elif "Get @" in msg.text:
                print "[Command]dp executing"
                _name = msg.text.replace("Get @","")
                _nametarget = _name.rstrip('  ')
                gs = cl.getGroup(msg.to)
                targets = []
                for g in gs.members:
                    if _nametarget == g.displayName:
                        targets.append(g.mid)
                if targets == []:
                    cl.sendText(msg.to,"Contact not found")
                else:
                    for target in targets:
                        try:
                            contact = cl.getContact(target)
                            path = "http://dl.profile.line-cdn.net/" + contact.pictureStatus
                            cl.sendImageWithURL(msg.to, path)
                        except Exception as e:
                            raise e
                print "[Command]dp executed"
#-----------------------------------------------
            elif "Music " in msg.text:
              if msg.from_ in admin:
                try:
                    songname = msg.text.lower().replace("Music ","")
                    params = {'songname': songname}
                    r = requests.get('http://ide.fdlrcn.com/workspace/yumi-apis/joox?' + urllib.urlencode(params))
                    data = r.text
                    data = json.loads(data)
                    for song in data:
                        hasil = 'This is Your Music\n'
                        hasil += 'Judul : ' + song[0]
                        hasil += '\nDurasi : ' + song[1]
                        hasil += '\nLink Download : ' + song[4]
                        cl.sendText(msg.to, hasil)
                        cl.sendText(msg.to, "Please Wait for audio...")
                        cl.sendAudioWithURL(msg.to, song[4])
                except Exception as njer:
                        cl.sendText(msg.to, str(njer))

            elif "Image " in msg.text:
                search = msg.text.replace("Image ","")
                url = 'https://www.google.com/search?espv=2&biw=1366&bih=667&tbm=isch&oq=kuc&aqs=mobile-gws-lite.0.0l5&q=' + search
                raw_html = (download_page(url))
                items = []
                items = items + (_images_get_all_items(raw_html))
                path = random.choice(items)
                print path
                try:
                    cl.sendImageWithURL(msg.to,path)
                except:
                    pass
#-----------------------------------------------
            elif "Image. " in msg.text:
                search = msg.text.replace("Image. ","")
                url = 'https://www.google.co.id/search?q=cool&source=lnms&tbm=isch&sa=X&ved=0ahUKEwj_rKTU14zYAhXLr48KHRY5CFgQ_AUICigB&biw=1100&bih=1709' + search
                raw_html = (download_page(url))
                items = []
                items = items + (_images_get_all_items(raw_html))
                path = random.choice(items)
                print path
                try:
                    cl.sendImageWithURL(msg.to,path)
                except:
                    pass
#-----------------------------------------------
            elif "Checkdate " in msg.text:
                tanggal = msg.text.replace("Checkdate ","")
                r=requests.get('https://script.google.com/macros/exec?service=AKfycbw7gKzP-WYV2F5mc9RaR7yE3Ve1yN91Tjs91hp_jHSE02dSv9w&nama=ervan&tanggal='+tanggal)
                data=r.text
                data=json.loads(data)
                lahir = data["data"]["lahir"]
                usia = data["data"]["usia"]
                ultah = data["data"]["ultah"]
                zodiak = data["data"]["zodiak"]
                cl.sendText(msg.to,"★★ I N F O R M A S I ★★\n"+"Date Of Birth : "+lahir+"\nAge : "+usia+"\nUltah : "+ultah+"\nZodiak : "+zodiak+"\n★ I N F O R M A S I ★")
            
            elif msg.text in ["Kalender","Time","Waktu"]:
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
                    if bln == str(k): bulan = bulan[k-1]
                rst = hasil + ", " + inihari.strftime('%d') + " - " + bulan + " - " + inihari.strftime('%Y') + "\nJam : [ " + inihari.strftime('%H:%M:%S') + " ]"
                cl.sendText(msg.to, rst)
#-----------------------------------------------
            elif "Getcover @" in msg.text:
                print "[Command]cover executing"
                _name = msg.text.replace("Getcover @","")    
                _nametarget = _name.rstrip('  ')
                gs = cl.getGroup(msg.to)
                targets = []
                for g in gs.members:
                    if _nametarget == g.displayName:
                        targets.append(g.mid)
                if targets == []:
                    cl.sendText(msg.to,"Contact not found")
                else:
                    for target in targets:
                        try:
                            contact = cl.getContact(target)
                            cu = cl.channel.getCover(target)         
                            path = str(cu)
                            cl.sendImageWithURL(msg.to, path)
                        except Exception as e:
                            raise e
                print "[Command]cover executed"
#------------------------------------------------------------------	
            elif "Coverurl @" in msg.text:
                print "[Command]cover executing"
                _name = msg.text.replace("Coverurl @","")    
                _nametarget = _name.rstrip('  ')
                gs = cl.getGroup(msg.to)
                targets = []
                for g in gs.members:
                    if _nametarget == g.displayName:
                        targets.append(g.mid)
                if targets == []:
                    cl.sendText(msg.to,"Contact not found")
                else:
                    for target in targets:
                        try:
                            contact = cl.getContact(target)
                            cu = cl.channel.getCover(target)          
                            path = str(cu)
                            cl.sendText(msg.to, path)
                        except Exception as e:
                            raise e
                print "[Command]cover executed"

            elif "Getgrup image" in msg.text:
                group = cl.getGroup(msg.to)
                path = "http://dl.profile.line-cdn.net/" + group.pictureStatus
                cl.sendImageWithURL(msg.to,path)
            elif "Urlgrup image" in msg.text:
                group = cl.getGroup(msg.to)
                path = "http://dl.profile.line-cdn.net/" + group.pictureStatus
                cl.sendText(msg.to,path)
#------------------------------------------------------------------
#Restart_Program
            elif msg.text in ["Bot:restart"]:
              if msg. from_ in admin:
                cl.sendText(msg.to, "Bot has been restarted")
                restart_program()
                print "@Restart"

            elif "dp @" in msg.text:            
                print "[Command]dp executing"
                _name = msg.text.replace("dp @","")
                _nametarget = _name.rstrip('  ')
                gs = cl.getGroup(msg.to)
                targets = []
                for g in gs.members:
                    if _nametarget == g.displayName:
                        targets.append(g.mid)
                if targets == []:
                    ki.sendText(msg.to,"Contact not found")
                else:
                    for target in targets:
                        try:
                            contact = cl.getContact(target)
                            path = "http://dl.profile.line-cdn.net/" + contact.pictureStatus
                            cl.sendImageWithURL(msg.to, path)
                        except:
                            pass
                print "[Command]dp executed"
#------------------------------------------------------------------
            elif msg.text in ["Ban"]:
              if msg. from_ in admin:
                wait["wblacklist"] = True
                cl.sendText(msg.to,"send contact")
            elif msg.text in ["Unban"]:
              if msg. from_ in admin:
                wait["dblacklist"] = True
                cl.sendText(msg.to,"send contact")
            elif msg.text in ["Banlist"]:   
              if msg. from_ in admin:
                if wait["blacklist"] == {}:
                    cl.sendText(msg.to,"Tidak Ada Blacklist")
                else:
                    cl.sendText(msg.to,"Daftar Banlist")
                    num=1
                    msgs="══════════List Blacklist═════════"
                    for mi_d in wait["blacklist"]:
                        msgs+="\n[%i] %s" % (num, cl.getContact(mi_d).displayName)
                        num=(num+1)
                    msgs+="\n══════════List Blacklist═════════\n\nTotal Blacklist : %i" % len(wait["blacklist"])
                    cl.sendText(msg.to, msgs)
            elif msg.text in ["Cek ban"]:
              if msg. from_ in admin:
                if msg.toType == 2:
                    group = cl.getGroup(msg.to)
                    gMembMids = [contact.mid for contact in group.members]
                    matched_list = []
                    for tag in wait["blacklist"]:
                        matched_list+=filter(lambda str: str == tag, gMembMids)
                    cocoa = ""
                    for mm in matched_list:
                        cocoa += mm + "\n"
                    cl.sendText(msg.to,cocoa + "")
            elif msg.text in ["Kill ban"]:
              if msg.from_ in admin:
                if msg.toType == 2:
                    group = cl.getGroup(msg.to)
                    gMembMids = [contact.mid for contact in group.members]
                    matched_list = []
                    for tag in wait["blacklist"]:
                        matched_list+=filter(lambda str: str == tag, gMembMids)
                    if matched_list == []:
                        cl.sendText(msg.to,"There was no blacklist user")
                        return
                    for jj in matched_list:
                        kk.kickoutFromGroup(msg.to,[jj])
                    cl.sendText(msg.to,"Blacklist emang pantas tuk di usir")
            elif msg.text in ["Clear"]:
              if msg. from_ in admin:
                if msg.toType == 2:
                    group = cl.getGroup(msg.to)
                    gMembMids = [contact.mid for contact in group.invitee]
                    for _mid in gMembMids:
                        cl.cancelGroupInvitation(msg.to,[_mid])
                    cl.sendText(msg.to,"I pretended to cancel and canceled.")
            elif "random:" in msg.text:
                if msg.toType == 2:
                    strnum = msg.text.replace("random:","")
                    source_str = 'abcdefghijklmnopqrstuvwxyz1234567890@:;./_][!&%$#)(=~^|'
                    try:
                        num = int(strnum)
                        group = cl.getGroup(msg.to)
                        for var in range(0,num):
                            name = "".join([random.choice(source_str) for x in xrange(10)])
                            time.sleep(0.01)
                            group.name = name
                            cl.updateGroup(group)
                    except:
                        cl.sendText(msg.to,"Error")	
				
            elif "albumâ†’" in msg.text:
                try:
                    albumtags = msg.text.replace("albumâ†’","")
                    gid = albumtags[:6]
                    name = albumtags.replace(albumtags[:34],"")
                    cl.createAlbum(gid,name)
                    cl.sendText(msg.to,name + "created an album")
                except:
                    cl.sendText(msg.to,"Error")
            elif "fakecâ†’" in msg.text:
                try:
                    source_str = 'abcdefghijklmnopqrstuvwxyz1234567890@:;./_][!&%$#)(=~^|'
                    name = "".join([random.choice(source_str) for x in xrange(10)])
                    anu = msg.text.replace("fakecâ†’","")
                    cl.sendText(msg.to,str(cl.channel.createAlbum(msg.to,name,anu)))
                except Exception as e:
                    try:
                        cl.sendText(msg.to,str(e))
                    except:
                        pass			
        if op.type == 59:
            print op


    except Exception as error:
        print error


def a2():
    now2 = datetime.now()
    nowT = datetime.strftime(now2,"%M")
    if nowT[14:] in ["01","10","20","30","40","50","60","70","80","90","100","00"]:
        return False
    else:
        return True

def nameUpdate():
    while True:
        try:
        #while a2():
            #pass
            if wait["clock"] == True:
                now2 = datetime.now()
                nowT = datetime.strftime(now2,"(%H:%M)")
                profile = cl.getProfile()
                profile.displayName = wait["cName"] + nowT
                cl.updateProfile(profile)

                profile2 = mj.getProfile()
                profile2.displayName = wait["cName2"]
                mj.updateProfile(profile2)

                profile3 = k1.getProfile()
                profile3.displayName = wait["cName3"]
                k1.updateProfile(profile3)
            time.sleep(800)
        except:
            pass
thread2 = threading.Thread(target=nameUpdate)
thread2.daemon = True
thread2.start()

while True:
    try:
        Ops = cl.fetchOps(cl.Poll.rev, 5)
    except EOFError:
        raise Exception("It might be wrong revision\n" + str(cl.Poll.rev))

    for Op in Ops:
        if (Op.type != OpType.END_OF_OPERATION):
            cl.Poll.rev = max(cl.Poll.rev, Op.revision)
            bot(Op)