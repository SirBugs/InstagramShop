#!/usr/bin/python
# -*- coding: utf-8 -*-

# ( -- IMPORTS -- ) #
import requests
import time
import string
import random

# ( -- LOGO * INFO -- ) #
bugs = '''
>>> ================================================================ <<<
>>>    ____  ___ _   _ ____ _____  _        ____  _   _  ___  ____   <<<
>>>   / __ \|_ _| \ | / ___|_   _|/ \      / ___|| | | |/ _ \|  _ \  <<<
>>>  / / _` || ||  \| \___ \ | | / _ \ ____\___ \| |_| | | | | |_) | <<<
>>> | | (_| || || |\  |___) || |/ ___ \_____|__) |  _  | |_| |  __/  <<<
>>>  \ \__,_|___|_| \_|____/ |_/_/   \_\   |____/|_| |_|\___/|_|     <<<
>>>   \____/                                                         <<<
>>> ================================================================ <<<
>>> [DEV] : SIRBUGS (Fares Walid)                                    <<<
>>> [GitHub] : https://www.github.com/sirbugs			     <<<
>>> [Version] : 1.2.V                                                <<<
>>> ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++ <<<
'''
#################################
# ( -- PROGRAMMED BY @BUGS -- ) #
#################################

													#//Login and Cookies Defs\\#
												# /\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\ #
# //X IG APP ID
def random_app_id():
	return ''.join(random.choice(string.digits) for _ in range(15))
# //Insta AJAX
def random_AJAX():
	return ''.join(random.choice(string.digits + string.ascii_lowercase) for _ in range(12))

token = requests.get('https://www.instagram.com/accounts/login/?source=auth_switcher').content.split('csrf_token":"')[1].split('"')[0]

# //Login Def.
def log(u, p):
	global r ;global acc_id;global validation
	data = 'username='+u+'&password='+p+'&queryParams=%7B%22source%22%3A%22auth_switcher%22%7D&optIntoOneTap=false'
	headers = {
		'Origin':'https://www.instagram.com',
		'X-Instagram-AJAX':random_AJAX(),
		'Content-Type':'application/x-www-form-urlencoded',
		'Accept':'*/*',
		'X-Requested-With':'XMLHttpRequest',
		'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.157 Safari/537.36',
		'X-CSRFToken':token,
		'X-IG-App-ID':random_app_id(),
		'Referer':'https://www.instagram.com/accounts/login/?source=auth_switcher',
		'Cookie':'ig_cb=1; rur=FRC; mid=XOSRsAALAAERbKhySt9i8hXiCJUJ; csrftoken='+token
	}
	r = requests.post('https://www.instagram.com/accounts/login/ajax/', data=data, headers=headers)
	src = r.content
	# //print src
	if 'authenticated": true' in src:
		print '[$] Logged In Successfully ['+u+':'+p+'].'
		acc_id = src.split('"userId": "')[1].split('"')[0]
		validation = 'TRUE'
	else:
		print '[$] Login Failed ['+u+':'+p+'].'
		validation = 'FALSE'
		pass
	# //INVALID SRC: {"authenticated": false, "user": false, "status": "ok"} / {"authenticated": false, "user": true, "status": "ok"}
	# //VALID SRC: {"authenticated": true, "user": true, "userId": "8285032951", "oneTapPrompt": false, "reactivated": true, "status": "ok"}

# //Cookies Making Def.
def cookiesmaker():
	global shbid;global shbts;global rur;global csrftoken;global ds_user_id;global sessionid;
	#//print r.headers
	cookies = r.headers['Set-Cookie']

	# //shbid = cookies.split('shbid=')[1].split(';')[0]
	# //shbts = cookies.split('shbts=')[1].split(';')[0]
	rur = cookies.split('rur=')[1].split(';')[0]
	csrftoken = cookies.split('csrftoken=')[1].split(';')[0]
	ds_user_id = cookies.split('ds_user_id=')[1].split(';')[0]
	sessionid = cookies.split('sessionid=')[1].split(';')[0]
	#// a = cookies.split('')[1].split('')[0]
	f = requests.get('https://ipapi.co/');f = f.content; ip = f.split('class="key">IP Address</td><td class="ipval" data-clipboard-text="')[1].split('"')[0]
	global cookie
	cookie = 'ig_cb=1; mid=XOSRsAALAAERbKhySt9i8hXiCJUJ; shbid=7309; shbts=1561068037.9766755; ds_user_id='+acc_id+'; sessionid='+sessionid+'; rur='+rur+'; csrftoken='+csrftoken+'; urlgen="{\"'+ip+'\": 16276}:1hTTb8:JUuqGp1eePAuguP9kub11kToZlk"'
	#// print cookie
	global headers
	headers = {
		'Origin':'https://www.instagram.com',
		'X-Instagram-AJAX':random_AJAX(),
		'Content-Type':'application/x-www-form-urlencoded',
		'Accept':'*/*',
		'X-Requested-With':'XMLHttpRequest',
		'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.157 Safari/537.36',
		'X-CSRFToken':csrftoken,
		'X-IG-App-ID':random_app_id(),
		'Cookie':cookie
	}

# /\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\ #

													#//Working Instagram Defs\\#
												# /\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\ #
# //Like Def
def like(item):
	global headers
	try:
		q = requests.get(item); q = q.content; item_id = q.split('instagram://media?id=')[1].split('"')[0]
		x = requests.post('https://www.instagram.com/web/likes/'+item_id+'/like/', headers=headers)
		xsrc = x.content
		# //print xsrc
		if '"status": "ok"' in xsrc:
			print '[$] Liked Photo ['+item_id+'] From ACC ['+acc_id+'].\n'
		else:
			print '[X] An Error Has Occured Please Try Again.!!\n'
			pass
	except:
		pass

# //Comment Def
def comment(item, msg):
	try:
		global headers
		q = requests.get(item); q = q.content; item_id = q.split('instagram://media?id=')[1].split('"')[0]
		
		data = 'comment_text='+msg+'&replied_to_comment_id='
		x = requests.post('https://www.instagram.com/web/comments/'+item_id+'/add/', data=data, headers=headers)
		xsrc = x.content
		# //print xsrc
		if '"status": "ok"' in xsrc:
			print '[$] Commented On ['+item_id+'] From ACC ['+acc_id+'].\n'
		else:
			print '[X] An Error Has Occured Please Try Again.!!\n'
			pass
	except:
		pass

# // Follow Def
def follow(item):
	global headers
	try:
		q = requests.get(item); q = q.content; item_id = q.split('logging_page_id":"profilePage_')[1].split('"')[0]
		
		x = requests.post('https://www.instagram.com/web/friendships/'+item_id+'/follow/', headers=headers)
		xsrc = x.content
		# //print xsrc
		if '"status": "ok"' in xsrc:
			print '[$] Followed ['+item_id+'] From ACC ['+acc_id+'].\n'
		else:
			print '[X] An Error Has Occured Please Try Again.!!\n'
			pass
	except:
		pass

# //Report Def
def report(item):
	try:
		global headers
		q = requests.get(item); q = q.content; item_id = q.split('logging_page_id":"profilePage_')[1].split('"')[0]
		
		data = 'source_name=profile&reason_id=1'
		x = requests.post('https://www.instagram.com/users/'+item_id+'/report/', data=data, headers=headers)
		# //xsrc = x.content
		print xsrc
		if '"status": "ok"' in xsrc:
			print '[$] Reported ['+item_id+'] From ACC ['+acc_id+'].\n'
		else:
			print '[X] An Error Has Occured Please Try Again.!!\n'
			pass
	except:
		pass


# /\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\ #
# \/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/ #

def start():
	ask = raw_input('[?] Choose A Tool [like:1 / comment:2 / follow:3 / report:4] : ')
	if int(ask) == 1:
		# //Like
		accs_path = raw_input('[?] Enter Your Accounts Path: ');path = open(accs_path,'r')
		item = raw_input('[?] Enter Post/Photo Link: ')
		print ''
		for i in path:
			line = i.strip()
			u, p = line.split(':')
			random_app_id();log(u,p)
			if validation == 'TRUE':
				cookiesmaker();like(item)
			else:
				pass
	elif int(ask) == 2:
		# //Comment
		accs_path = raw_input('[?] Enter Your Accounts Path: ');path = open(accs_path,'r')
		item = raw_input('[?] Enter Post/Photo Link: ')
		msg = raw_input('[?] Enter Your Comment: ')
		print ''
		for i in path:
			line = i.strip()
			u, p = line.split(':')
			random_app_id();log(u,p);
			if validation == 'TRUE':
				cookiesmaker();comment(item, msg)
			else:
				pass
	elif int(ask) == 3:
		# //Follow
		accs_path = raw_input('[?] Enter Your Accounts Path: ');path = open(accs_path,'r')
		item = raw_input('[?] Enter Account Link: ')
		print ''
		for i in path:
			line = i.strip()
			u, p = line.split(':')
			random_app_id();log(u,p);	
			if validation == 'TRUE':
				cookiesmaker();follow(item)
			else:
				pass
	elif int(ask) == 4:
		# //Report
		accs_path = raw_input('[?] Enter Your Accounts Path: ');path = open(accs_path,'r')
		item = raw_input('[?] Enter Account Link: ')
		print ''
		for i in path:
			line = i.strip()
			u, p = line.split(':')
			random_app_id();log(u,p)
			if validation == 'TRUE':
				cookiesmaker();report(item)
			else:
				pass
	else:
		print '[X] Please Select Valid Choice.'

if __name__ == '__main__':
	print bugs
	start()
