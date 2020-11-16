from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup as soup

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

class find(x,y):
    def __init__(self):
        self.x = x
        self.y = y
    def now(self):
        return sopa.findAll(a,b)

def printext(x):
    for a in x:
        print(a.text)
