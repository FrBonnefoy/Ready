import os
import re
import time
from ast import literal_eval
from bs4 import BeautifulSoup as soup
chrome_driver = os.getcwd() +"/chromedriver"
from selenium import webdriver
fhandle=open('output.txt','w')
def reouvrir():
	try:
		browser = webdriver.Chrome(executable_path=chrome_driver)
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

def xlookup(x):
	global lookup
	global tlookup
	global flookup
	flookup=literal_eval(x)

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
chrome_options.add_argument("--window-size=1920x1080")
chrome_options.add_argument('--headless')
chrome_options.add_argument('start-maximized')

chrome_options.add_argument('disable-infobars')

#browser = webdriver.Chrome(options=chrome_options,executable_path=chrome_driver)
browser = webdriver.Chrome(executable_path=chrome_driver)

list_url=['http://hotels.huazhu.com/city/shanghai', 'http://hotels.huazhu.com/city/beijing', 'http://hotels.huazhu.com/city/hangzhou', 'http://hotels.huazhu.com/city/nanjing', 'http://hotels.huazhu.com/city/xian', 'http://hotels.huazhu.com/city/chengdu', 'http://hotels.huazhu.com/city/suzhou', 'http://hotels.huazhu.com/city/qingdao', 'http://hotels.huazhu.com/city/tianjin', 'http://hotels.huazhu.com/city/zhengzhou', 'http://hotels.huazhu.com/city/jinan', 'http://hotels.huazhu.com/city/chongqing', 'http://hotels.huazhu.com/city/wuhan', 'http://hotels.huazhu.com/city/xianggang', 'http://hotels.huazhu.com/city/ningbo', 'http://hotels.huazhu.com/city/taiyuan', 'http://hotels.huazhu.com/city/shenzhen', 'http://hotels.huazhu.com/city/guangzhou', 'http://hotels.huazhu.com/city/nanchang', 'http://hotels.huazhu.com/city/wuxi', 'http://hotels.huazhu.com/city/hefei', 'http://hotels.huazhu.com/city/aershan', 'http://hotels.huazhu.com/city/anshan', 'http://hotels.huazhu.com/city/anjihuzhou', 'http://hotels.huazhu.com/city/anqing', 'http://hotels.huazhu.com/city/anxiquanzhou', 'http://hotels.huazhu.com/city/anyangshi', 'http://hotels.huazhu.com/city/ankang', 'http://hotels.huazhu.com/city/akesudiqu', 'http://hotels.huazhu.com/city/akesu', 'http://hotels.huazhu.com/city/aomen', 'http://hotels.huazhu.com/city/beijing', 'http://hotels.huazhu.com/city/baoding', 'http://hotels.huazhu.com/city/baotou', 'http://hotels.huazhu.com/city/bayanzhuoer', 'http://hotels.huazhu.com/city/benxi', 'http://hotels.huazhu.com/city/baishan', 'http://hotels.huazhu.com/city/baicheng', 'http://hotels.huazhu.com/city/binhaiyancheng', 'http://hotels.huazhu.com/city/baoyingyangzhou', 'http://hotels.huazhu.com/city/bengbu', 'http://hotels.huazhu.com/city/bozhou', 'http://hotels.huazhu.com/city/binzhou', 'http://hotels.huazhu.com/city/boxingxian', 'http://hotels.huazhu.com/city/binyangnanning', 'http://hotels.huazhu.com/city/beihai', 'http://hotels.huazhu.com/city/baise', 'http://hotels.huazhu.com/city/baoji', 'http://hotels.huazhu.com/city/baiyin', 'http://hotels.huazhu.com/city/changli', 'http://hotels.huazhu.com/city/cixianhandan', 'http://hotels.huazhu.com/city/chichengzhangjiakou', 'http://hotels.huazhu.com/city/chengde', 'http://hotels.huazhu.com/city/cangzhou', 'http://hotels.huazhu.com/city/changzhi', 'http://hotels.huazhu.com/city/chifeng', 'http://hotels.huazhu.com/city/changtutieling', 'http://hotels.huazhu.com/city/chaoyang', 'http://hotels.huazhu.com/city/changchun', 'http://hotels.huazhu.com/city/changlingxiansongyuan', 'http://hotels.huazhu.com/city/changbaishanantuxian', 'http://hotels.huazhu.com/city/changzhou', 'http://hotels.huazhu.com/city/changshu', 'http://hotels.huazhu.com/city/cixiningbo', 'http://hotels.huazhu.com/city/cangnanwenzhou', 'http://hotels.huazhu.com/city/changxing', 'http://hotels.huazhu.com/city/chuzhou', 'http://hotels.huazhu.com/city/chaohu', 'http://hotels.huazhu.com/city/chizhou', 'http://hotels.huazhu.com/city/changdaoyantai', 'http://hotels.huazhu.com/city/caoxian', 'http://hotels.huazhu.com/city/chengwuhezhe', 'http://hotels.huazhu.com/city/changgeshi', 'http://hotels.huazhu.com/city/changsha', 'http://hotels.huazhu.com/city/changshaxianchangsha', 'http://hotels.huazhu.com/city/cilizhangjiajie', 'http://hotels.huazhu.com/city/chengzhou', 'http://hotels.huazhu.com/city/chaozhou', 'http://hotels.huazhu.com/city/chengmai ', 'http://hotels.huazhu.com/city/chongqing', 'http://hotels.huazhu.com/city/chengdu', 'http://hotels.huazhu.com/city/chongzhou', 'http://hotels.huazhu.com/city/cangxiguangyuan', 'http://hotels.huazhu.com/city/changning', 'http://hotels.huazhu.com/city/chishui', 'http://hotels.huazhu.com/city/chuxiong', 'http://hotels.huazhu.com/city/changji', 'http://hotels.huazhu.com/city/damingxianhandan', 'http://hotels.huazhu.com/city/dingxingbaoding', 'http://hotels.huazhu.com/city/dachengxianlangfang', 'http://hotels.huazhu.com/city/dachanghuizuzizhixian', 'http://hotels.huazhu.com/city/datong', 'http://hotels.huazhu.com/city/dalian', 'http://hotels.huazhu.com/city/dandong', 'http://hotels.huazhu.com/city/dashiqiao', 'http://hotels.huazhu.com/city/dehuichangchun', 'http://hotels.huazhu.com/city/daanbaicheng', 'http://hotels.huazhu.com/city/dunhua', 'http://hotels.huazhu.com/city/daqing', 'http://hotels.huazhu.com/city/donghailianyungan', 'http://hotels.huazhu.com/city/dongtaiyancheng', 'http://hotels.huazhu.com/city/dafengyancheng', 'http://hotels.huazhu.com/city/danyang', 'http://hotels.huazhu.com/city/deqingxian', 'http://hotels.huazhu.com/city/dangtu(maanshan)', 'http://hotels.huazhu.com/city/dingyuanchuzhou', 'http://hotels.huazhu.com/city/dangshan', 'http://hotels.huazhu.com/city/duchangxiangjiujiang', 'http://hotels.huazhu.com/city/dongying', 'http://hotels.huazhu.com/city/dezhou', 'http://hotels.huazhu.com/city/dongmingheze', 'http://hotels.huazhu.com/city/dengfengzhengzhou', 'http://hotels.huazhu.com/city/dongguan', 'http://hotels.huazhu.com/city/dinganxian', 'http://hotels.huazhu.com/city/dujiagnyanshi', 'http://hotels.huazhu.com/city/deyang', 'http://hotels.huazhu.com/city/dazhou', 'http://hotels.huazhu.com/city/duoyunqiannan', 'http://hotels.huazhu.com/city/dali', 'http://hotels.huazhu.com/city/diqinzhou', 'http://hotels.huazhu.com/city/duilongdeqing', 'http://hotels.huazhu.com/city/dalixianweinan', 'http://hotels.huazhu.com/city/dingbianyulin', 'http://hotels.huazhu.com/city/dunhuang', 'http://hotels.huazhu.com/city/dingxi', 'http://hotels.huazhu.com/city/delingha', 'http://hotels.huazhu.com/city/dingxi', 'http://hotels.huazhu.com/city/eerduosi', 'http://hotels.huazhu.com/city/ezhou', 'http://hotels.huazhu.com/city/ems', 'http://hotels.huazhu.com/city/fupingxianbaoding', 'http://hotels.huazhu.com/city/fengningxianchengde', 'http://hotels.huazhu.com/city/fushun', 'http://hotels.huazhu.com/city/fengcheng', 'http://hotels.huazhu.com/city/fuxin', 'http://hotels.huazhu.com/city/fengxianxuzhou', 'http://hotels.huazhu.com/city/funingyancheng', 'http://hotels.huazhu.com/city/fenghuaningbo', 'http://hotels.huazhu.com/city/feidongxianhefei', 'http://hotels.huazhu.com/city/fanchangxian', 'http://hotels.huazhu.com/city/fengtaihuainan', 'http://hotels.huazhu.com/city/fengyangchuzhou', 'http://hotels.huazhu.com/city/fuyangshi', 'http://hotels.huazhu.com/city/funan', 'http://hotels.huazhu.com/city/fuzhou', 'http://hotels.huazhu.com/city/fuan', 'http://hotels.huazhu.com/city/fuding', 'http://hotels.huazhu.com/city/fuzhouou', 'http://hotels.huazhu.com/city/feixianlinyi', 'http://hotels.huazhu.com/city/fangxianshiyan', 'http://hotels.huazhu.com/city/fenghuangxiangxizhou', 'http://hotels.huazhu.com/city/foshan', 'http://hotels.huazhu.com/city/fengshunmeizhou', 'http://hotels.huazhu.com/city/fangchenggang', 'http://hotels.huazhu.com/city/fengxiangxianbaoji', 'http://hotels.huazhu.com/city/guyuanzhangjiakou', 'http://hotels.huazhu.com/city/guanlangfang', 'http://hotels.huazhu.com/city/guanyunxianlianyungang', 'http://hotels.huazhu.com/city/gaoyou', 'http://hotels.huazhu.com/city/gongqingchenjiujiang', 'http://hotels.huazhu.com/city/ganzhou', 'http://hotels.huazhu.com/city/guangraodongying', 'http://hotels.huazhu.com/city/gaomi', 'http://hotels.huazhu.com/city/guanxianliaocheng', 'http://hotels.huazhu.com/city/gushixianxinyang', 'http://hotels.huazhu.com/city/guangzhou', 'http://hotels.huazhu.com/city/guilin', 'http://hotels.huazhu.com/city/guanghan', 'http://hotels.huazhu.com/city/guangyuan', 'http://hotels.huazhu.com/city/gaoxianyibin', 'http://hotels.huazhu.com/city/guiyang', 'http://hotels.huazhu.com/city/geermu', 'http://hotels.huazhu.com/city/guyuan', 'http://hotels.huazhu.com/city/handan', 'http://hotels.huazhu.com/city/huailaixianzhangjiakou', 'http://hotels.huazhu.com/city/haixingcangzhou', 'http://hotels.huazhu.com/city/huanghuacangzhou', 'http://hotels.huazhu.com/city/hejiancangzhou', 'http://hotels.huazhu.com/city/hengshui', 'http://hotels.huazhu.com/city/houmalinfen', 'http://hotels.huazhu.com/city/huhehaote', 'http://hotels.huazhu.com/city/hulunbeier', 'http://hotels.huazhu.com/city/haichenganshan', 'http://hotels.huazhu.com/city/huludao', 'http://hotels.huazhu.com/city/hunchunyanbian', 'http://hotels.huazhu.com/city/haerbin', 'http://hotels.huazhu.com/city/heihe', 'http://hotels.huazhu.com/city/haiannantong', 'http://hotels.huazhu.com/city/haimen', 'http://hotels.huazhu.com/city/huaian', 'http://hotels.huazhu.com/city/hongzehuaian', 'http://hotels.huazhu.com/city/hangzhou', 'http://hotels.huazhu.com/city/haiyan', 'http://hotels.huazhu.com/city/haining', 'http://hotels.huazhu.com/city/huzhou', 'http://hotels.huazhu.com/city/hengdiandongyang', 'http://hotels.huazhu.com/city/hefei', 'http://hotels.huazhu.com/city/huaiyuanxianbengbu', 'http://hotels.huazhu.com/city/huainan', 'http://hotels.huazhu.com/city/hexianmaanshan', 'http://hotels.huazhu.com/city/huaibei', 'http://hotels.huazhu.com/city/huangshan', 'http://hotels.huazhu.com/city/huoshan', 'http://hotels.huazhu.com/city/htxzb', 'http://hotels.huazhu.com/city/huimingbinzhou', 'http://hotels.huazhu.com/city/heze', 'http://hotels.huazhu.com/city/hebishi', 'http://hotels.huazhu.com/city/huangshi', 'http://hotels.huazhu.com/city/huanggang', 'http://hotels.huazhu.com/city/honganhuanggang', 'http://hotels.huazhu.com/city/hengyang', 'http://hotels.huazhu.com/city/hengshan', 'http://hotels.huazhu.com/city/huaihua', 'http://hotels.huazhu.com/city/huizhouishi', 'http://hotels.huazhu.com/city/heyuan', 'http://hotels.huazhu.com/city/haikou', 'http://hotels.huazhu.com/city/hancheng', 'http://hotels.huazhu.com/city/huayin', 'http://hotels.huazhu.com/city/hanzhong', 'http://hotels.huazhu.com/city/hxmgzzzzzz', 'http://hotels.huazhu.com/city/hamishi', 'http://hotels.huazhu.com/city/hutubixianchangjizhou', 'http://hotels.huazhu.com/city/huoerguosi', 'http://hotels.huazhu.com/city/jingxianhebei', 'http://hotels.huazhu.com/city/jincheng', 'http://hotels.huazhu.com/city/jinzhong', 'http://hotels.huazhu.com/city/jiexiu', 'http://hotels.huazhu.com/city/jiaochengxianlvliang', 'http://hotels.huazhu.com/city/jinzhou', 'http://hotels.huazhu.com/city/jianchang', 'http://hotels.huazhu.com/city/jilin', 'http://hotels.huazhu.com/city/jian', 'http://hotels.huazhu.com/city/jixi', 'http://hotels.huazhu.com/city/jiamusi', 'http://hotels.huazhu.com/city/jiangyin', 'http://hotels.huazhu.com/city/jinhuhuaian', 'http://hotels.huazhu.com/city/jianhuyancheng', 'http://hotels.huazhu.com/city/jurong', 'http://hotels.huazhu.com/city/jingjiang', 'http://hotels.huazhu.com/city/jiande', 'http://hotels.huazhu.com/city/jiaxing', 'http://hotels.huazhu.com/city/jiashan', 'http://hotels.huazhu.com/city/jinhua', 'http://hotels.huazhu.com/city/jinzhaixianliuan', 'http://hotels.huazhu.com/city/jixi', 'http://hotels.huazhu.com/city/jingdezhen', 'http://hotels.huazhu.com/city/jiujiang', 'http://hotels.huazhu.com/city/jianjiangxi', 'http://hotels.huazhu.com/city/jingangshanjian', 'http://hotels.huazhu.com/city/jinan', 'http://hotels.huazhu.com/city/jiyangjinan', 'http://hotels.huazhu.com/city/jiaozhouqingdao', 'http://hotels.huazhu.com/city/jimoqingdao', 'http://hotels.huazhu.com/city/jining', 'http://hotels.huazhu.com/city/jiaxiangxianjining', 'http://hotels.huazhu.com/city/junanxianlinyi', 'http://hotels.huazhu.com/city/juyeheze', 'http://hotels.huazhu.com/city/juanchenxian', 'http://hotels.huazhu.com/city/jiaozuo', 'http://hotels.huazhu.com/city/jiyuan', 'http://hotels.huazhu.com/city/jingzhou', 'http://hotels.huazhu.com/city/jianlijingzhou', 'http://hotels.huazhu.com/city/jishou', 'http://hotels.huazhu.com/city/jiangmen', 'http://hotels.huazhu.com/city/jintangxianchengdu', 'http://hotels.huazhu.com/city/jingyanleshan', 'http://hotels.huazhu.com/city/jiayuguan', 'http://hotels.huazhu.com/city/jiuquan', 'http://hotels.huazhu.com/city/kuanchengxian', 'http://hotels.huazhu.com/city/kuandianxian', 'http://hotels.huazhu.com/city/kaiyuan', 'http://hotels.huazhu.com/city/kunshan', 'http://hotels.huazhu.com/city/kaihuaquzhou', 'http://hotels.huazhu.com/city/kaifeng', 'http://hotels.huazhu.com/city/kangdingganzizhou', 'http://hotels.huazhu.com/city/kaili', 'http://hotels.huazhu.com/city/kunming', 'http://hotels.huazhu.com/city/kelamayi', 'http://hotels.huazhu.com/city/kuerle', 'http://hotels.huazhu.com/city/kashidiqu', 'http://hotels.huazhu.com/city/kashidiqu', 'http://hotels.huazhu.com/city/leting', 'http://hotels.huazhu.com/city/lulongqinhuangdao', 'http://hotels.huazhu.com/city/linxixingtai', 'http://hotels.huazhu.com/city/langfang', 'http://hotels.huazhu.com/city/linfen', 'http://hotels.huazhu.com/city/lvliang', 'http://hotels.huazhu.com/city/lnwfdsdalian', 'http://hotels.huazhu.com/city/liaoyang', 'http://hotels.huazhu.com/city/lingyuanchaoyang', 'http://hotels.huazhu.com/city/liyang', 'http://hotels.huazhu.com/city/lianyungang', 'http://hotels.huazhu.com/city/lianshuihuaian', 'http://hotels.huazhu.com/city/linanhangzhou', 'http://hotels.huazhu.com/city/leqingshiwenzhou', 'http://hotels.huazhu.com/city/longyouquzhou', 'http://hotels.huazhu.com/city/linhai', 'http://hotels.huazhu.com/city/lishui', 'http://hotels.huazhu.com/city/laian', 'http://hotels.huazhu.com/city/linquanfuyang', 'http://hotels.huazhu.com/city/linbi', 'http://hotels.huazhu.com/city/liuan', 'http://hotels.huazhu.com/city/lixinxianbozhou', 'http://hotels.huazhu.com/city/langxi', 'http://hotels.huazhu.com/city/lianjiangxianfuzhou', 'http://hotels.huazhu.com/city/longyan', 'http://hotels.huazhu.com/city/lepingshi', 'http://hotels.huazhu.com/city/laixi', 'http://hotels.huazhu.com/city/longkouyantai', 'http://hotels.huazhu.com/city/laiyangyantai', 'http://hotels.huazhu.com/city/linquweifang', 'http://hotels.huazhu.com/city/liangshanjining', 'http://hotels.huazhu.com/city/linyi', 'http://hotels.huazhu.com/city/liaocheng', 'http://hotels.huazhu.com/city/linqnigliaocheng', 'http://hotels.huazhu.com/city/lankaokaifeng', 'http://hotels.huazhu.com/city/luoyangluoyang', 'http://hotels.huazhu.com/city/luanchuangluoyang', 'http://hotels.huazhu.com/city/luohe', 'http://hotels.huazhu.com/city/luyizhoukou', 'http://hotels.huazhu.com/city/loudi', 'http://hotels.huazhu.com/city/lufengshanwei', 'http://hotels.huazhu.com/city/liuzhou', 'http://hotels.huazhu.com/city/luzhou', 'http://hotels.huazhu.com/city/leshan', 'http://hotels.huazhu.com/city/langzhong', 'http://hotels.huazhu.com/city/liangshanyizu', 'http://hotels.huazhu.com/city/liboqiannan ', 'http://hotels.huazhu.com/city/lijiang', 'http://hotels.huazhu.com/city/lasa', 'http://hotels.huazhu.com/city/linzhi', 'http://hotels.huazhu.com/city/lanzhou', 'http://hotels.huazhu.com/city/lintaodingxi', 'http://hotels.huazhu.com/city/longnan', 'http://hotels.huazhu.com/city/manzhoulihulunbeier', 'http://hotels.huazhu.com/city/mudanjiang', 'http://hotels.huazhu.com/city/maanshan', 'http://hotels.huazhu.com/city/mingguang', 'http://hotels.huazhu.com/city/mengchengbozhou', 'http://hotels.huazhu.com/city/minhoufuzhou', 'http://hotels.huazhu.com/city/minquanshangqiu', 'http://hotels.huazhu.com/city/machenhuanggang', 'http://hotels.huazhu.com/city/meizhou', 'http://hotels.huazhu.com/city/my', 'http://hotels.huazhu.com/city/meishan', 'http://hotels.huazhu.com/city/mile', 'http://hotels.huazhu.com/city/minghehuizutuzuzizhixian', 'http://hotels.huazhu.com/city/nanhexianxingtai', 'http://hotels.huazhu.com/city/nanpicangzhou', 'http://hotels.huazhu.com/city/nanjing', 'http://hotels.huazhu.com/city/nantong', 'http://hotels.huazhu.com/city/ningbo', 'http://hotels.huazhu.com/city/ninghainingbo', 'http://hotels.huazhu.com/city/nanping', 'http://hotels.huazhu.com/city/ningde', 'http://hotels.huazhu.com/city/nanchang', 'http://hotels.huazhu.com/city/nanchangxiannanchang', 'http://hotels.huazhu.com/city/nanyangshi', 'http://hotels.huazhu.com/city/nanning', 'http://hotels.huazhu.com/city/neijiang', 'http://hotels.huazhu.com/city/nanchong', 'http://hotels.huazhu.com/city/pingshanshijiazhuang', 'http://hotels.huazhu.com/city/pingxiangxianxingtai', 'http://hotels.huazhu.com/city/pingyaojinzhong', 'http://hotels.huazhu.com/city/panjin', 'http://hotels.huazhu.com/city/peixianxuzhou', 'http://hotels.huazhu.com/city/pingyangwenzhou', 'http://hotels.huazhu.com/city/pinghujiaxing', 'http://hotels.huazhu.com/city/pujiangjinhua', 'http://hotels.huazhu.com/city/pingtanxian', 'http://hotels.huazhu.com/city/putian', 'http://hotels.huazhu.com/city/pingxiang', 'http://hotels.huazhu.com/city/poyangshangrao', 'http://hotels.huazhu.com/city/pingyinjinan', 'http://hotels.huazhu.com/city/pingduqingdao', 'http://hotels.huazhu.com/city/penglaiyantai', 'http://hotels.huazhu.com/city/pingdingshan', 'http://hotels.huazhu.com/city/puyang', 'http://hotels.huazhu.com/city/panzhihua', 'http://hotels.huazhu.com/city/pingshanyibin', 'http://hotels.huazhu.com/city/puchengweinan', 'http://hotels.huazhu.com/city/pingliankang', 'http://hotels.huazhu.com/city/pingliang', 'http://hotels.huazhu.com/city/qianan', 'http://hotels.huazhu.com/city/qinhuangdao', 'http://hotels.huazhu.com/city/qinghexingtai', 'http://hotels.huazhu.com/city/quyang', 'http://hotels.huazhu.com/city/qingxiancangzhou', 'http://hotels.huazhu.com/city/qixianjinzhong', 'http://hotels.huazhu.com/city/quwolinfen', 'http://hotels.huazhu.com/city/qixian', 'http://hotels.huazhu.com/city/qianguo', 'http://hotels.huazhu.com/city/qiananxian', 'http://hotels.huazhu.com/city/qiqihaer', 'http://hotels.huazhu.com/city/qitaihe', 'http://hotels.huazhu.com/city/qidong', 'http://hotels.huazhu.com/city/qiandaohuchunan', 'http://hotels.huazhu.com/city/quzhou', 'http://hotels.huazhu.com/city/qianshananqing', 'http://hotels.huazhu.com/city/qingyangxian', 'http://hotels.huazhu.com/city/quanzhou', 'http://hotels.huazhu.com/city/qingdao', 'http://hotels.huazhu.com/city/qixiayantai', 'http://hotels.huazhu.com/city/qinzhouweifang', 'http://hotels.huazhu.com/city/qufujining', 'http://hotels.huazhu.com/city/qihedezhou', 'http://hotels.huazhu.com/city/qingyunxiandezhou', 'http://hotels.huazhu.com/city/qianjiang', 'http://hotels.huazhu.com/city/qingyuan', 'http://hotels.huazhu.com/city/qionghai', 'http://hotels.huazhu.com/city/qianxinanbuyizumiaozuzizhhizhou', 'http://hotels.huazhu.com/city/rongchengxianbaoding', 'http://hotels.huazhu.com/city/rudongnantong', 'http://hotels.huazhu.com/city/rugao', 'http://hotels.huazhu.com/city/ruianwenzhou', 'http://hotels.huazhu.com/city/rongchengweihai', 'http://hotels.huazhu.com/city/rushanweihai', 'http://hotels.huazhu.com/city/rizhao', 'http://hotels.huazhu.com/city/renshouxian', 'http://hotels.huazhu.com/city/rikaze', 'http://hotels.huazhu.com/city/shijiazhuang', 'http://hotels.huazhu.com/city/sunpingbaoding', 'http://hotels.huazhu.com/city/suningxiancangzhou', 'http://hotels.huazhu.com/city/shuozhou', 'http://hotels.huazhu.com/city/shenyang', 'http://hotels.huazhu.com/city/suizhonghuludao', 'http://hotels.huazhu.com/city/shulan', 'http://hotels.huazhu.com/city/siping', 'http://hotels.huazhu.com/city/shuangliaojiling', 'http://hotels.huazhu.com/city/songyuan', 'http://hotels.huazhu.com/city/shuangyashan', 'http://hotels.huazhu.com/city/shanghai', 'http://hotels.huazhu.com/city/suiningxuzhou', 'http://hotels.huazhu.com/city/suzhou', 'http://hotels.huazhu.com/city/sheyangyancheng', 'http://hotels.huazhu.com/city/suqian', 'http://hotels.huazhu.com/city/shuyangsuqian', 'http://hotels.huazhu.com/city/siyangsuqian', 'http://hotels.huazhu.com/city/sihong', 'http://hotels.huazhu.com/city/shaoxing', 'http://hotels.huazhu.com/city/shengzhou', 'http://hotels.huazhu.com/city/sanmentaizhou', 'http://hotels.huazhu.com/city/shuzhoushi', 'http://hotels.huazhu.com/city/sixiansuzhou', 'http://hotels.huazhu.com/city/shouxianhuainan', 'http://hotels.huazhu.com/city/shucheng', 'http://hotels.huazhu.com/city/shexianhuangshan', 'http://hotels.huazhu.com/city/shangrao', 'http://hotels.huazhu.com/city/shanghexianjinian', 'http://hotels.huazhu.com/city/shouguangweifang', 'http://hotels.huazhu.com/city/sishuijining', 'http://hotels.huazhu.com/city/shandonglinshulinyi', 'http://hotels.huazhu.com/city/shanxianheze', 'http://hotels.huazhu.com/city/sanmenxia', 'http://hotels.huazhu.com/city/shangqiu', 'http://hotels.huazhu.com/city/shenqiuxianzhoukou', 'http://hotels.huazhu.com/city/shiyanshi', 'http://hotels.huazhu.com/city/shuizhou', 'http://hotels.huazhu.com/city/shennongjia', 'http://hotels.huazhu.com/city/shaoyang', 'http://hotels.huazhu.com/city/shaoguan', 'http://hotels.huazhu.com/city/shenzhen', 'http://hotels.huazhu.com/city/shantou', 'http://hotels.huazhu.com/city/shanweishi', 'http://hotels.huazhu.com/city/sanya', 'http://hotels.huazhu.com/city/shuangliuchengdu', 'http://hotels.huazhu.com/city/suining', 'http://hotels.huazhu.com/city/shilinyizuzizuxian', 'http://hotels.huazhu.com/city/shangluo', 'http://hotels.huazhu.com/city/sdyl', 'http://hotels.huazhu.com/city/shanshantulufan', 'http://hotels.huazhu.com/city/shihezi', 'http://hotels.huazhu.com/city/tianjin', 'http://hotels.huazhu.com/city/tangshan', 'http://hotels.huazhu.com/city/taiyuan', 'http://hotels.huazhu.com/city/tongliao', 'http://hotels.huazhu.com/city/tieling', 'http://hotels.huazhu.com/city/tonghua', 'http://hotels.huazhu.com/city/taonanshi', 'http://hotels.huazhu.com/city/taicang', 'http://hotels.huazhu.com/city/taizhou', 'http://hotels.huazhu.com/city/taixingtaizhou', 'http://hotels.huazhu.com/city/tongxiangwuzhen', 'http://hotels.huazhu.com/city/taizhou2', 'http://hotels.huazhu.com/city/tiantai', 'http://hotels.huazhu.com/city/tongling', 'http://hotels.huazhu.com/city/tianchang', 'http://hotels.huazhu.com/city/taihexian', 'http://hotels.huazhu.com/city/tengzhouzaozhuang', 'http://hotels.huazhu.com/city/taian', 'http://hotels.huazhu.com/city/tongxuxiankaifeng', 'http://hotels.huazhu.com/city/tangyinanyang', 'http://hotels.huazhu.com/city/taojiangyiyang', 'http://hotels.huazhu.com/city/taishan（jiangmen)', 'http://hotels.huazhu.com/city/tongren', 'http://hotels.huazhu.com/city/tengchongbaoshan', 'http://hotels.huazhu.com/city/tongchuan', 'http://hotels.huazhu.com/city/tianshui', 'http://hotels.huazhu.com/city/tulufan', 'http://hotels.huazhu.com/city/taipei', 'http://hotels.huazhu.com/city/weixianxingtai', 'http://hotels.huazhu.com/city/weixianzhangjiakou', 'http://hotels.huazhu.com/city/wutaixian', 'http://hotels.huazhu.com/city/wuhai', 'http://hotels.huazhu.com/city/wenniuteqi', 'http://hotels.huazhu.com/city/wulanchabu', 'http://hotels.huazhu.com/city/wulanhaote', 'http://hotels.huazhu.com/city/wuxi', 'http://hotels.huazhu.com/city/wenzhou', 'http://hotels.huazhu.com/city/wuyijinhua', 'http://hotels.huazhu.com/city/wenlingshi', 'http://hotels.huazhu.com/city/wuhu', 'http://hotels.huazhu.com/city/wuhuxian', 'http://hotels.huazhu.com/city/woyangbozhou', 'http://hotels.huazhu.com/city/wuyishan', 'http://hotels.huazhu.com/city/wuningjiujiang', 'http://hotels.huazhu.com/city/wannianxianshangrao', 'http://hotels.huazhu.com/city/wuyuanxianshangrao', 'http://hotels.huazhu.com/city/weifang', 'http://hotels.huazhu.com/city/weishanjining', 'http://hotels.huazhu.com/city/wenshangjining', 'http://hotels.huazhu.com/city/weihai', 'http://hotels.huazhu.com/city/wudibinzhou', 'http://hotels.huazhu.com/city/wuzhijiaozuo', 'http://hotels.huazhu.com/city/wuhan', 'http://hotels.huazhu.com/city/wushanchongqin', 'http://hotels.huazhu.com/city/weiyuanneijiang', 'http://hotels.huazhu.com/city/wenshan', 'http://hotels.huazhu.com/city/weinanshi', 'http://hotels.huazhu.com/city/wuwei', 'http://hotels.huazhu.com/city/wuzhong', 'http://hotels.huazhu.com/city/wulumuqi', 'http://hotels.huazhu.com/city/xinjishi', 'http://hotels.huazhu.com/city/xingtai', 'http://hotels.huazhu.com/city/xiongxianbaoding', 'http://hotels.huazhu.com/city/xinglongxian', 'http://hotels.huazhu.com/city/xinjiangyuncheng', 'http://hotels.huazhu.com/city/xinzhou', 'http://hotels.huazhu.com/city/xinganmeng', 'http://hotels.huazhu.com/city/xilinhaote', 'http://hotels.huazhu.com/city/xuzhou', 'http://hotels.huazhu.com/city/xinyi', 'http://hotels.huazhu.com/city/xuyihuaian', 'http://hotels.huazhu.com/city/xiangshuiyancheng', 'http://hotels.huazhu.com/city/xinghua', 'http://hotels.huazhu.com/city/xiangshanxianningbo', 'http://hotels.huazhu.com/city/xinchangxianshaoxing', 'http://hotels.huazhu.com/city/xianjutaizhou', 'http://hotels.huazhu.com/city/xiaoxiansuzhou', 'http://hotels.huazhu.com/city/xuancheng', 'http://hotels.huazhu.com/city/xiamen', 'http://hotels.huazhu.com/city/xianyouxian', 'http://hotels.huazhu.com/city/xiapuningde', 'http://hotels.huazhu.com/city/xinyu', 'http://hotels.huazhu.com/city/xingyang', 'http://hotels.huazhu.com/city/xinzhengzhengzhou', 'http://hotels.huazhu.com/city/xinanxianluoyang', 'http://hotels.huazhu.com/city/xinxiang', 'http://hotels.huazhu.com/city/xuchang', 'http://hotels.huazhu.com/city/xixia', 'http://hotels.huazhu.com/city/xinyang', 'http://hotels.huazhu.com/city/xihuazhoukou', 'http://hotels.huazhu.com/city/xiangyang', 'http://hotels.huazhu.com/city/xianning', 'http://hotels.huazhu.com/city/xiangtan', 'http://hotels.huazhu.com/city/xuwenzhanjiang', 'http://hotels.huazhu.com/city/xuanhandazhou', 'http://hotels.huazhu.com/city/xichang(liangshan)', 'http://hotels.huazhu.com/city/xingyi', 'http://hotels.huazhu.com/city/xishuangbanna', 'http://hotels.huazhu.com/city/xianggelila', 'http://hotels.huazhu.com/city/xian', 'http://hotels.huazhu.com/city/xianyang', 'http://hotels.huazhu.com/city/xining', 'http://hotels.huazhu.com/city/xijiguyuan', 'http://hotels.huazhu.com/city/xianggang', 'http://hotels.huazhu.com/city/yongnianhandan', 'http://hotels.huazhu.com/city/yixianbaoding', 'http://hotels.huazhu.com/city/yanshanxiancangzhou', 'http://hotels.huazhu.com/city/yongqinglangfang', 'http://hotels.huazhu.com/city/yangquan', 'http://hotels.huazhu.com/city/yuncheng', 'http://hotels.huazhu.com/city/yakeshihulunbeier', 'http://hotels.huazhu.com/city/yingkou', 'http://hotels.huazhu.com/city/yanbian', 'http://hotels.huazhu.com/city/yanjiyanbian', 'http://hotels.huazhu.com/city/yixing', 'http://hotels.huazhu.com/city/yancheng', 'http://hotels.huazhu.com/city/yangzhou', 'http://hotels.huazhu.com/city/yizheng', 'http://hotels.huazhu.com/city/yangzhong', 'http://hotels.huazhu.com/city/yuyaoningbo', 'http://hotels.huazhu.com/city/yongjia', 'http://hotels.huazhu.com/city/yiwu', 'http://hotels.huazhu.com/city/yongkang', 'http://hotels.huazhu.com/city/yuhuantaizhou', 'http://hotels.huazhu.com/city/yingshangxianfuyang', 'http://hotels.huazhu.com/city/yintan', 'http://hotels.huazhu.com/city/yichun', 'http://hotels.huazhu.com/city/yushanxianshangrao', 'http://hotels.huazhu.com/city/yiyuanzibo', 'http://hotels.huazhu.com/city/yantai', 'http://hotels.huazhu.com/city/yutaijining', 'http://hotels.huazhu.com/city/yinanlinyi', 'http://hotels.huazhu.com/city/yishuilinyi', 'http://hotels.huazhu.com/city/yangguliaocheng', 'http://hotels.huazhu.com/city/yangxinbinzhou', 'http://hotels.huazhu.com/city/yunchengheze', 'http://hotels.huazhu.com/city/yanshiluoyang', 'http://hotels.huazhu.com/city/yuanyang', 'http://hotels.huazhu.com/city/yongcheng', 'http://hotels.huazhu.com/city/yangxinhuangshi', 'http://hotels.huazhu.com/city/yichang', 'http://hotels.huazhu.com/city/yueyang', 'http://hotels.huazhu.com/city/yiyang', 'http://hotels.huazhu.com/city/yangjiang', 'http://hotels.huazhu.com/city/yangshanqingyuan', 'http://hotels.huazhu.com/city/yangshuoguilin', 'http://hotels.huazhu.com/city/youyangchongqin', 'http://hotels.huazhu.com/city/yibin', 'http://hotels.huazhu.com/city/yaan', 'http://hotels.huazhu.com/city/yanan', 'http://hotels.huazhu.com/city/yulinshanxi', 'http://hotels.huazhu.com/city/yongdengxianlanzhou', 'http://hotels.huazhu.com/city/yinchuan', 'http://hotels.huazhu.com/city/yilihasakezizhizhou', 'http://hotels.huazhu.com/city/yiningshi', 'http://hotels.huazhu.com/city/zhengding', 'http://hotels.huazhu.com/city/zhuozhou', 'http://hotels.huazhu.com/city/zhangjiakou', 'http://hotels.huazhu.com/city/zhangbeixian', 'http://hotels.huazhu.com/city/zhuoluzhangjiakou', 'http://hotels.huazhu.com/city/zhalantunhulunbeier', 'http://hotels.huazhu.com/city/zltq', 'http://hotels.huazhu.com/city/zhuanghedalian', 'http://hotels.huazhu.com/city/zhangjiagang', 'http://hotels.huazhu.com/city/zhenjiang', 'http://hotels.huazhu.com/city/zhuji', 'http://hotels.huazhu.com/city/zhoushan', 'http://hotels.huazhu.com/city/zongyangtongling', 'http://hotels.huazhu.com/city/zhangzhou', 'http://hotels.huazhu.com/city/zhangqiujinan', 'http://hotels.huazhu.com/city/zibo', 'http://hotels.huazhu.com/city/zaozhuang', 'http://hotels.huazhu.com/city/zhaoyuanyantai', 'http://hotels.huazhu.com/city/zouchengjining', 'http://hotels.huazhu.com/city/zoupingbinzhou', 'http://hotels.huazhu.com/city/zhengzhou', 'http://hotels.huazhu.com/city/zhongmuzhengzhou', 'http://hotels.huazhu.com/city/zhoukoushi', 'http://hotels.huazhu.com/city/zhumadian', 'http://hotels.huazhu.com/city/zhijiangyichang', 'http://hotels.huazhu.com/city/zhuzhou', 'http://hotels.huazhu.com/city/zhangjiajie', 'http://hotels.huazhu.com/city/zhuhai', 'http://hotels.huazhu.com/city/zhanjiang', 'http://hotels.huazhu.com/city/zhaoqing', 'http://hotels.huazhu.com/city/zhongshan', 'http://hotels.huazhu.com/city/zigong', 'http://hotels.huazhu.com/city/zunyi', 'http://hotels.huazhu.com/city/zhangye', 'http://hotels.huazhu.com/city/zhongwei']
xlookup("'h2'")
for a in list_url:
    try:
        time.sleep(1)
        change(a)
		
        print(a)
        data()
        thingy=sopa.findAll('a',{'data-page-index':lambda x: x})
        try:
            print("Pages: ",thingy[4]['data-page-index'])
            rangopag=int(thingy[4]['data-page-index'])
        except:
            print("Pages: 1")
            rangopag=3
    except:
        print(a, '    Fail')
        continue

    counter=1
    print(a,'      ',counter)
    scrape_text()
    counter2=2
    while counter2<=rangopag:
        try:
            element=browser.find_elements_by_xpath("//*[contains(text(), '下一页')]")[0]
            browser.execute_script("arguments[0].scrollIntoView();", element)
            browser.find_elements_by_xpath("//*[contains(text(), '下一页')]")[0].click()
            time.sleep(5)
            data()
            counter= counter + 1
            print(a,'      ',counter)
            scrape_text()
        except:
            pass
        counter2=counter2+1
