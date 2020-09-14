import urllib.request
import random
username = 'lum-customer-hl_9fb27fc7-zone-static'
password = '34v1aa74qrty'
port = 22225
def stealth_requests(a):
    session_id = random.random()
    super_proxy_url = ('http://%s-session-%s:%s@zproxy.lum-superproxy.io:%d' %
        (username, session_id, password, port))
    proxy_handler = urllib.request.ProxyHandler({
        'http': super_proxy_url,
        'https': super_proxy_url,
    })
    opener = urllib.request.build_opener(proxy_handler)
    treasure= opener.open(a).read()
    print(treasure)
    return treasure
