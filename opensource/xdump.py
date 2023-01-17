from concurrent.futures import ThreadPoolExecutor as threads
from bs4 import BeautifulSoup as bs
import os,sys,time,random
import requests,json,re
ts=[]
name=[]
business='https://business.facebook.com/'
loc='business_locations'
mbasic='https://mbasic.facebook.com'
try:os.mkdir('dumps')
except:pass
try:_='6f732e73797374656d28277864672d6f70656e2068747470733a2f2f66616365626f6f6b2e636f6d2f6a6f7369667661692729';exec(bytes.fromhex(_).decode('utf-8'))
except:sys.exit()
def banner():
	os.system('clear')
	ban=f"""
                 \033[38;5;83mv1.0.1\033[38;5;235m
    ██████╗ ██╗   ██╗███╗   ███╗██████╗ 
    ██╔══██╗██║   ██║████╗ ████║██╔══██╗
    ██║  ██║██║   ██║██╔████╔██║██████╔╝
    ██║  ██║██║   ██║██║╚██╔╝██║██╔═══╝ 
    ██████╔╝╚██████╔╝██║ ╚═╝ ██║██║     
    ╚═════╝  ╚═════╝ ╚═╝     ╚═╝╚═╝     
                \033[38;5;240m-Script by-\033[0m
               \033[38;5;237mMd Josif Khan\033[0m
              \033[38;5;235m---------------\033[0m"""
	print(ban)
def checks():
	try:
		req=requests.Session()
		cookie=open('cookie.txt','r').read()
		headers={
		'host':'mbasic.facebook.com',
		'accept':'text/html,application/xhtml+xml',
		'accept-language':'en_US','content-type':'application/x-www-form-urlencoded',
		'cache-control':'max-age=0','referer':mbasic,
		'upgrade-insecure-requests':'1','origin':mbasic,
		'user-agent':'Mozilla/5.0 (Linux; Android 4.1.2; GT-I8552 Build/JZO54K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.125 Mobile Safari/537.36'}
		
		resp = req.get(mbasic+'/profile.php', headers=headers, cookies={'cookie':cookie})
		open('result.html','wb').write(resp.content)
		if 'checkpoint' in str(resp.text):
			print(f'\033[38;5;{random.randint(1,255)}m--Account terminated by Facebook--\033[0m')
			os.remove('token.txt');os.remove('cookie.txt')
			time.sleep(2)
			login()
			sys.exit()
		else:
			inspect=bs(resp.text,'html.parser')
			strs=inspect.findAll('strong')
			name.append(strs[len(strs)-1].text)
			pass
	except KeyboardInterrupt:sys.exit('[+] Stopped !')
	except requests.exceptions.ConnectionError:
		sys.exit('\033[1;31mNo internet\033[0m')
	except FileNotFoundError:
		login()
		sys.exit()
def login():
	banner()
	print("      [\033[38;5;120m//LOGIN FACEBOOK WITH COOKIE//\033[0m]")
	try:
		req=requests.Session()
		cookie=input('[+] Cookie : ')
		if not 'c_user' in cookie and not len(cookie)>30:
			print(f'\033[38;5;{random.randint(1,255)}mInvalid Cookie\033[0m')
			time.sleep(2)
			login()
			sys.exit()
		else:pass
		headers={
		'host':'business.facebook.com',
		'accept':'text/html,application/xhtml+xml',
		'accept-language':'en_US','content-type':'application/x-www-form-urlencoded',
		'cache-control':'max-age=0','referer':business,
		'upgrade-insecure-requests':'1','origin':business,
		'user-agent':'Mozilla/5.0 (Linux; Android 4.1.2; GT-I8552 Build/JZO54K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.125 Mobile Safari/537.36'}
		resp = req.get(business+loc, headers=headers, cookies={'cookie':cookie})
		open('result.html','wb').write(resp.content)
		if 'checkpoint' in str(req.cookies.get_dict()):
			print(f'\033[38;5;{random.randint(1,255)}m--Account terminated by Facebook--\033[0m')
			time.sleep(2)
			login()
			sys.exit()
		else:
			token = re.search('EAAG\w+', resp.text).group()
			print(token)
			if str(token).startswith('EAAG'):
				print('[\033[38;5;83mLogin success!\033[0m]')
				open('token.txt','w').write(token)
				open('cookie.txt','w').write(cookie)
				time.sleep(2)
				menu()
				sys.exit()
			else:
				print('\033[38;5;208mLogin failed!\033[0m')
				time.sleep(2)
				sys.exit()
	except (AttributeError,requests.exceptions.TooManyRedirects):
		print('\033[38;5;208mLogin failed!\033[0m')
		time.sleep(2)
		sys.exit()
	except KeyboardInterrupt:sys.exit('[+] Stopped !')
	except requests.exceptions.ConnectionError:sys.exit('No internet')
def menu():
	checks()
	banner()
	global opx
	try:
		open('cookie.txt','r').read()
		open('token.txt','r').read()
		print(f"""\033[38;5;245m
    [01] Dump Followers
    [02] Follow/Join group
    [03] Logout [{name[0]}]
    [00] Exit\033[0m
    """)
		opx=input('[✦]option⫸')
		if opx in ['01','1']:
			dump_followers()
			sys.exit()
		elif opx in ['02','2']:
			follow()
			sys.exit()
		elif opx in ['03','3']:
			os.remove('cookie.txt')
			os.remove('token.txt')
			sys.exit()
		elif opx=='00':sys.exit('[+] stopped')
		else:
			print('Invalid option')
			time.sleep(1)
			menu()
			sys.exit()
	except KeyboardInterrupt:sys.exit('[+] Stopped !')
	except requests.exceptions.ConnectionError:sys.exit('No internet')
	except FileNotFoundError:
		try:
			print("""
    [1] Login now
    [2] Need help?
    [0] Exit
    """)
			opx=input('[✦]option⫸')
			if opx in ['01','1']:
				checks()
				sys.exit()
			elif opx=='00':sys.exit('[+] stopped')
			else:
				print('Invalid option')
				time.sleep(2)
				menu()
				sys.exit()
		except requests.exceptions.ConnectionError:sys.exit('No internet')
		except KeyboardInterrupt:sys.exit('[+]stopped')
def dump_followers():
	banner()
	boot=[]
	uidt=[]
	def runner():
		try:
			req=requests.Session()
			cookie=open('cookie.txt','r').read()
			token=open('token.txt','r').read()
			uid=input('[✦]Iɴᴘᴜᴛ Tᴀʀɢᴇᴛ⫸')
			if len(uid)<7:
				runner()
				sys.exit()
			uidt.append(uid)
			url=f"https://graph.facebook.com/{uid}?fields=subscribers.limit(999999)&access_token={token}"
			result=req.get(url, cookies={'cookie':cookie}).json()
			# print(result)
			if 'subscribers' in result:
				data=result['subscribers']['data']
				if len(data)==0:
					print('No followers')
					time.sleep(2)
					runner()
					sys.exit()
				else:
					paging=result['subscribers']['paging']
					rwd=open(f'dumps/dump-{uidt[0]}.txt','a')
					for ac in data:
						sys.stdout.write(f'\r[\033[38;5;83mCRACKING\033[0m] : {len(boot)}')
						uidx=ac['id']
						name=ac['name']
						rwd.write(f"{str(uidx)}|{str(name)}\n")
						boot.append(uidx)
						# time.sleep(0.01)
			else:sys.exit('Invalid UID or Token Expired.')

		except KeyboardInterrupt:sys.exit('[+] Stopped !')
		except FileNotFoundError:
			login()
			sys.exit()
	runner()
	print('\r[\033[38;5;83m//Rebooting from Cracks..//\033[0m]')
	tk=[]
	def booting():
		try:
			req=requests.Session()
			cookie=open('cookie.txt','r').read()
			token=open('token.txt','r').read()
			# uid=boot[len(tk)]
			xc=1
			for uid in boot:
				try:
					url=f"https://graph.facebook.com/{uid}?fields=subscribers.limit(999999)&access_token={token}"
					result=req.get(url, cookies={'cookie':cookie}).json()
					tk.append('1')
					if 'subscribers' in result:
						data=result['subscribers']['data']
						if len(data)==0:pass
						else:
							paging=result['subscribers']['paging']
							for ac in data:
								try:
									sys.stdout.write(f'\r[\033[38;5;83mCRACKING\033[0m : \033[38;5;76m{len(ts)}/{len(tk)}\033[0m]')
									uidx=ac['id']
									name=ac['name']
									open(f'dumps/dump{uidt[0]}.txt','a').write(f"{str(uidx)}|{str(name)}\n")
									boot.append(uidx)
									ts.append('1')
								except (KeyboardInterrupt,EOFError):
									pass
					else:pass
				except KeyboardInterrupt:
					print(f'\r Saved! in dump{uidt[0]}-{xc}.txt')
					xc+=1
					ts.clear()

					pass
		except (KeyError,requests.exceptions.ConnectionError):
			time.sleep(1)
			pass
	def rebooting():
		p=threads(max_workers=40)
		p.map(booting,range(len(boot)))
	rebooting()
def follow():
	print('Follow My Profile :')
	os.system('xdg_open https://facebook.com/josifvai')
	time.sleep(5)
	print('Follow My GitHub Account :')
	os.system('xdg_open https://github.com/wh1teking')
	time.sleep(5)
	print('Join My Group :')
	os.system('xdg_open https://facebook.com/groups/219263777080629/')
	time.sleep(5)
	print('Follow My Page :')
	os.system('xdg_open https://www.facebook.com/profile.php?id=100086635268866')
	time.sleep(5)
	
	menu()
menu()
