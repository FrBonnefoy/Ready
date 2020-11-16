from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup as soup

def help():

    print( ''' open_session() : Ouvre une nouvelle séance de chrome avec une nouvelle adresse IP
               close_session() : Fermer la session avant de reouvrir une nouvelle avec une nouvelle adresse IP (économise des ressources)
               change(x) : Aller sur le site x avec une séance ouvert de chrome. Ex: change('https://www.google.com/') pour aller à Google.
               data(): Lire le code html tel comme il est présenté dans le navigateur virtuel.
               scroll(): Aller à la fin de la page.
               screnshoot(x): Sauvegarder une capture d'écran du navigateur avec l'image x. Ex: screenshot('test.png')
               screen(): Sauvegarder une capture d'écran du navigateur sous le nom 'browser.png'
               find(x,y): Trouver tous les éléments avec les identifiants html x et y. Ex: identifiant= h2 class="mb0" -> x='h2' ; y={'class':'mb0'}
               printext(x): Imprimer le texte trouvé sur la console 
            ''')

def open_session():
    global browser
    PROXY = "127.0.0.1:24000"
    chrome_options = Options()
    chrome_options.add_argument('--no-sandbox')
    chrome_options.add_argument("--headless")
    chrome_options.add_argument('--disable-dev-shm-usage')
    chrome_options.add_argument('--proxy-server=%s' % PROXY)
    chrome_options.add_argument("--window-size=1920x1080")
    chrome_options.add_argument('start-maximized')
    chrome_options.add_argument('disable-infobars')
    browser = webdriver.Chrome(options=chrome_options)

def screenshot(x):
    browser.save_screenshot(x)

def screen():
	browser.save_screenshot('browser.png')

def close_session():
    browser.close()

def data():
	global content
	content=browser.page_source
	global sopa
	sopa=soup(content,'html.parser')

def scroll():
	height=0
	height2=1
	while height!=height2:
		height= browser.execute_script("return $(document).height()")
		browser.execute_script("window.scrollTo(0, document.body.scrollHeight);")
		time.sleep(2)
		height2 = browser.execute_script("return $(document).height()")
	browser.save_screenshot("endscroll.png")

def change(x):
	browser.get(x)

class find(x,y=None):
    def __init__(self):
        self.x = x
        self.y = y if y is not None else x
    def now(self):
        return sopa.findAll(x,y)

def printext(x):
    for a in x:
        print(a.text)
