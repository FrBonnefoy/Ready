import random
import time

from selenium import webdriver
from selenium.webdriver.common.proxy import ProxyType, Proxy

username = 'lum-customer-hl_9fb27fc7-zone-static'
password = '34v1aa74qrty'
port = 22225
listy=[]
def stealth_browser():
    global browser


    session_id = random.random()
    super_proxy_url = ('http://%s-session-%s:%s@zproxy.luminati.io:%d' %
                       (username, session_id, password, port))

    proxy = Proxy({
        'proxyType': ProxyType.MANUAL,
        'httpProxy': super_proxy_url,
        'ftpProxy': super_proxy_url,
        'sslProxy': super_proxy_url,
        'noProxy': ''  # set this value as desired
    })

    print(proxy)
    listy.append(proxy)
    fhandle=open('savy.txt','a')
    print(proxy,file=fhandle)
    fhandle.close()
    # driver = webdriver.Chrome(executable_path="./bin/geckodriver", proxy=proxy)

    options = webdriver.ChromeOptions()
    options.add_argument('--proxy-server=%s' % proxy)

    browser = webdriver.Chrome(options=options

        # options=options
    )
