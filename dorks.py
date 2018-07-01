import requests
from bs4 import BeautifulSoup
import time
import random
import os

def draw():
	os.system('cls' if os.name == 'nt' else 'clear')
	print("""
             ,----------------,              ,---------,
        ,-----------------------,          ,"        ,"|
      ,"                      ,"|        ,"        ,"  |
     +-----------------------+  |      ,"        ,"    |
     |  .-----------------.  |  |     +---------+      |
     |  |                 |  |  |     | -==----'|      |
     |  |                 |  |  |     |         |      |
     |  |     Dorks.py    |  |  |/----|`---=    |      |
     |  |                 |  |  |   ,/|==== ooo |      ;
     |  |                 |  |  |  // |(((( [33]|    ,"
     |  `-----------------'  |," .;'| |((((     |  ,"
     +-----------------------+  ;;  | |         |,"
        /_)______________(_/  //'   | +---------+
   ___________________________/___  `,
  /  oooooooooooooooo  .o.  oooo /,   \,"-----------
 / ==ooooooooooooooo==.o.  ooo= //   ,`\--{)B     ,"
/_==__==========__==_ooo__ooo=_/'   /___________,"
`-----------------------------'


""")

def proxies():
	file = input("Your proxies list: ")
	proxies = []
	with open(file, "r") as p:
		proxies = [line.strip() for line in p]
	proxy = random.choice(proxies)
	start = 0
	end = proxy.index(":")
	st = proxy[start:end]
	e = proxy[end+1:]
	global proxie
	proxie = {"http":"{}:{}".format(st, e)}

def user_agents():
	file = input("Your user_agents list: ")
	ua = []
	with open(file, "r") as txt:
		ua = [line.strip() for line in txt]
	user = random.choice(ua)
	global header
	header = {"User-Agent":"{}".format(user)}

def dorks():
	link = input("Dorks: ")
	try:
		pages = int(input("Number of pages you want: "))
	except ValueError:
		print("It's not a number.")
		print("Number of pages set to 10 by default.")
		pages = 0
	try:
		sec = int(input("Seconds you want to wait between requests (5 secs recommanded to avoid being suspended by Google): "))
	except:
		print("It's not a number.")
		print("Seconds set to 5 by default")
	proxies()
	user_agents()
	i = 0

	while i < pages:
		page = 0
		url = "https://www.google.com/search?&q={}&start={}".format(link, page)
		r = requests.get(url, headers=header, proxies=proxie)
		soup = BeautifulSoup(r.text, "html.parser")
		for cite in soup.find_all('cite'):
			link = 0
			if link <= 10:
				print(cite.text)
				print("------------------")
				time.sleep(sec)
				link += 1
			else:
				time.sleep(sec)
				print(url)
				continue
			page += 10
		i += 1
draw()
dorks()