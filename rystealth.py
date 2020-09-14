import os
import re
import time
from ast import literal_eval
from bs4 import BeautifulSoup as soup
chrome_driver = os.getcwd() +"/chromedriver"
from selenium import webdriver
fhandle=open('output.txt','w')
def reouvrir():
	global browser
	try:
		browser = webdriver.Chrome(options=chrome_options,executable_path=chrome_driver)
	except:
		print("Erreur\n")
def screen():
	browser.save_screenshot('browser.png')
def scroll():
	for a in list_url:
		change(a)
		height=0
		height2=1
		while height!=height2:
			height= browser.execute_script("return $(document).height()")
			browser.execute_script("window.scrollTo(0, document.body.scrollHeight);")
			time.sleep(2)
			height2 = browser.execute_script("return $(document).height()")
		data()
		scrape_text()



def data():
	global content
	content=browser.page_source
	global sopa
	sopa=soup(content,'html.parser')

def change(x):
	browser.get(x)

def lookup():
	global lookup
	global tlookup
	global flookup
	tlookup=input('\nElement à chercher?\n\n')
	flookup=literal_eval(tlookup)
	print('\n\n')


def lookup2():
	global lookup
	global tlookup
	global flookup
	tlookup=input('\nElement à chercher?\n\n')
	flookup=eval(tlookup)
	print('\n\n')


def scrape():
	data()
	global element
	element=sopa.findAll(flookup)
	for a in element:
		print(a)

def scrape_text():
	data()
	global element
	global list_text
	list_text=[]
	element=sopa.findAll(flookup)
	for a in element:
		x=a.text.strip().replace('\n','')
		y=re.sub(' +',' ',x)
		print(y)
		fhandle.write(y)
		fhandle.write('\n')
		list_text.append(y)

def scrape_url():
	data()
	global element
	global list_url
	list_url=[]
	element=sopa.findAll(flookup)
	for a in element:
		try:
			x=a['href']
			print(x)
			list_url.append(x)
		except:
			continue


def iscrape():
	for z in listy:
		browser.get(z)
		data()
		scrape()

def iscrape_text():
	for z in list_url:
		browser.get(z)
		data()
		scrape_text()

def pattern_text(x):
	global pattern
	pattern=input("\nPhrase à reconnaître?\n")
	result=re.search(pattern,x)
	print(result)

def pattern_text2(x):
	global pattern
	result=re.search(pattern,x)
	print(result)

def iscrape_dtext():
	iscrape_text()
	print('\n\n')
	for a in range(len(list_text)):
		if a==0:
			pattern_text(liste_text[a])
		else:
			pattern_text2(liste_text[a])

def url_split(x):
	global list_url
	list_url=[]
	list_url=x.split('\n')
	del list_url[-1]

from selenium.webdriver.chrome.options import Options
chrome_options = Options()
user_agent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.79 Safari/537.36'
chrome_options.add_argument('user-agent={0}'.format(user_agent))
chrome_options.add_argument("--window-size=1024x720")
chrome_options.add_argument('--headless')
chrome_options.add_argument('start-maximized')

chrome_options.add_argument('disable-infobars')

browser = webdriver.Chrome(options=chrome_options,executable_path=chrome_driver)
