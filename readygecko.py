import os
import re
import time
from ast import literal_eval
from bs4 import BeautifulSoup as soup
gecko_driver = os.getcwd() +"/geckodriver"
from selenium import webdriver

def reouvrir():
	try:
		browser = webdriver.Firefox(executable_path=gecko_driver)
	except:
		print("Erreur\n")

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
	
browser = webdriver.Firefox(executable_path=gecko_driver)

	
