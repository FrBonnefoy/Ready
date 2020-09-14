import os
import re
import time
from ast import literal_eval
from bs4 import BeautifulSoup as soup
chrome_driver = os.getcwd() +"/chromedriver"
from selenium import webdriver

def reouvrir():
	global browser
	try:
		browser = webdriver.Chrome()
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


import time



def more():
	browser.find_element_by_css_selector("button.btn.btn-secondary.hidden-xs-down").click()

listy=['https://www.abcsalles.com/location-de-salle-2_alsace_r.html', 'https://www.abcsalles.com/location-de-salle-2_aquitaine_r.html', 'https://www.abcsalles.com/location-de-salle-2_auvergne_r.html', 'https://www.abcsalles.com/location-de-salle-2_basse-normandie_r.html', 'https://www.abcsalles.com/location-de-salle-2_bourgogne_r.html', 'https://www.abcsalles.com/location-de-salle-2_bretagne_r.html', 'https://www.abcsalles.com/location-de-salle-2_centre_r.html', 'https://www.abcsalles.com/location-de-salle-2_champagne-ardenne_r.html', 'https://www.abcsalles.com/location-de-salle-2_corse_r.html', 'https://www.abcsalles.com/location-de-salle-2_franche-comte_r.html', 'https://www.abcsalles.com/location-de-salle-2_guadeloupe_r.html', 'https://www.abcsalles.com/location-de-salle-2_guyane_r.html', 'https://www.abcsalles.com/location-de-salle-2_haute-normandie_r.html', 'https://www.abcsalles.com/location-de-salle-2_ile-de-france_r.html', 'https://www.abcsalles.com/location-de-salle-2_la-reunion_r.html', 'https://www.abcsalles.com/location-de-salle-2_languedoc-roussillon_r.html', 'https://www.abcsalles.com/location-de-salle-2_limousin_r.html', 'https://www.abcsalles.com/location-de-salle-2_lorraine_r.html', 'https://www.abcsalles.com/location-de-salle-2_martinique_r.html', 'https://www.abcsalles.com/location-de-salle-2_mayotte_r.html', 'https://www.abcsalles.com/location-de-salle-2_midi-pyrenees_r.html', 'https://www.abcsalles.com/location-de-salle-2_monaco_r.html', 'https://www.abcsalles.com/location-de-salle-2_nord-pas-de-calais_r.html', 'https://www.abcsalles.com/location-de-salle-2_pays-de-la-loire_r.html', 'https://www.abcsalles.com/location-de-salle-2_picardie_r.html', 'https://www.abcsalles.com/location-de-salle-2_poitou-charentes_r.html', 'https://www.abcsalles.com/location-de-salle-2_paca_r.html', 'https://www.abcsalles.com/location-de-salle-2_rhone-alpes_r.html']

def get_urls():
	indiv_urls=[]
	outhandle=open('dicturls.txt','w')
	outhandle2=open('texturls.txt','w')
	for url in listy:
		change(url)
		time.sleep(1)
		while True:
			try:
				more()
				time.sleep(1)
			except:
				break
		data()
		element=sopa.findAll('a',href=True)
		for a in element:
			indiv_urls.append(a['href'])

	indiv_urls=list(filter(lambda x: '/lieu/' in x,indiv_urls))
	indiv_urls = list(dict.fromkeys(indiv_urls))
	indiv_urls=list(map(lambda x: 'https://www.abcsalles.com'+x,indiv_urls))
	print(indiv_urls,file=outhandle)
	for z in indiv_urls:
		print(z,file=outhandle2)
		print('\n',file=outhandle2)

def ouvrir():
	global browser
	browser = webdriver.Chrome()

def sopa(x):
	sopa=soup(x,'html.parser')
	return sopa



from selenium.webdriver.chrome.options import Options
chrome_options = Options()
user_agent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.79 Safari/537.36'
chrome_options.add_argument('user-agent={0}'.format(user_agent))
chrome_options.add_argument("--window-size=1024x720")
chrome_options.add_argument('--headless')
chrome_options.add_argument('start-maximized')

chrome_options.add_argument('disable-infobars')

def ouvrir_stealth():
	global browser
	browser = webdriver.Chrome(options=chrome_options)
