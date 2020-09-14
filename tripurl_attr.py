import ready as ry
import time
import random
from concurrent.futures import ProcessPoolExecutor
from concurrent.futures import ThreadPoolExecutor
from concurrent.futures import Future
urls=['https://www.tripadvisor.fr/Attractions-g187208-Activities-c61-Provence_Alpes_Cote_d_Azur.html', 'https://www.tripadvisor.fr/Attractions-g187208-Activities-c42-Provence_Alpes_Cote_d_Azur.html', 'https://www.tripadvisor.fr/Attractions-g187208-Activities-c47-Provence_Alpes_Cote_d_Azur.html', 'https://www.tripadvisor.fr/Attractions-g187208-Activities-c26-Provence_Alpes_Cote_d_Azur.html', 'https://www.tripadvisor.fr/Attractions-g187208-Activities-c55-Provence_Alpes_Cote_d_Azur.html', 'https://www.tripadvisor.fr/Attractions-g187208-Activities-c57-Provence_Alpes_Cote_d_Azur.html']
'''
,'https://www.tripadvisor.fr/Attractions-g187208-Activities-c36-Provence_Alpes_Cote_d_Azur.html', 'https://www.tripadvisor.fr/Attractions-g187208-Activities-c49-Provence_Alpes_Cote_d_Azur.html', 'https://www.tripadvisor.fr/Attractions-g187208-Activities-c56-Provence_Alpes_Cote_d_Azur.html', 'https://www.tripadvisor.fr/Attractions-g187208-Activities-c40-Provence_Alpes_Cote_d_Azur.html', 'https://www.tripadvisor.fr/Attractions-g187208-Activities-c59-Provence_Alpes_Cote_d_Azur.html', 'https://www.tripadvisor.fr/Attractions-g187208-Activities-c20-Provence_Alpes_Cote_d_Azur.html', 'https://www.tripadvisor.fr/Attractions-g187208-Activities-c41-Provence_Alpes_Cote_d_Azur.html', 'https://www.tripadvisor.fr/Attractions-g187208-Activities-c60-Provence_Alpes_Cote_d_Azur.html', 'https://www.tripadvisor.fr/Attractions-g187208-Activities-c58-Provence_Alpes_Cote_d_Azur.html', 'https://www.tripadvisor.fr/Attractions-g187208-Activities-c52-Provence_Alpes_Cote_d_Azur.html', 'https://www.tripadvisor.fr/Attractions-g187208-Activities-c53-Provence_Alpes_Cote_d_Azur.html', 'https://www.tripadvisor.fr/Attractions-g187208-Activities-c48-Provence_Alpes_Cote_d_Azur.html', 'https://www.tripadvisor.fr/Attractions-g187208-Activities-c62-Provence_Alpes_Cote_d_Azur.html', 'https://www.tripadvisor.fr/Attractions-g187208-Activities-c63-Provence_Alpes_Cote_d_Azur.html', 'https://www.tripadvisor.fr/Attractions-g187208-Activities-zft11306-Provence_Alpes_Cote_d_Azur.html', 'https://www.tripadvisor.fr/Attractions-g187208-Activities-zft11309-Provence_Alpes_Cote_d_Azur.html', 'https://www.tripadvisor.fr/Attractions-g187208-Activities-zft11292-Provence_Alpes_Cote_d_Azur.html', 'https://www.tripadvisor.fr/Attractions-g187208-Activities-zft11295-Provence_Alpes_Cote_d_Azur.html', 'https://www.tripadvisor.fr/Attractions-g187208-Activities-zft12169-Provence_Alpes_Cote_d_Azur.html', 'https://www.tripadvisor.fr/Attractions-g187208-Activities-zft12170-Provence_Alpes_Cote_d_Azur.html', 'https://www.tripadvisor.fr/Attractions-g187208-Activities-zft12156-Provence_Alpes_Cote_d_Azur.html', 'https://www.tripadvisor.fr/Attractions-g187208-Activities-zft11312-Provence_Alpes_Cote_d_Azur.html', 'https://www.tripadvisor.fr/Attractions-g187208-Activities-zft12159-Provence_Alpes_Cote_d_Azur.html', 'https://www.tripadvisor.fr/Attractions-g187208-Activities-zft12163-Provence_Alpes_Cote_d_Azur.html']
'''

for z in urls:

    ry.open_stealth()
    ry.change(z)
    print(z)
    #ry.browser.save_screenshot('test'+urls.index(z)+'.png')
    ry.browser.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    element=ry.browser.find_element_by_css_selector("a.ui_button.nav.next.primary")
    ry.data()
    scrape=ry.sopa.findAll('a',{'class':'_1QKQOve4'})
    time.sleep(random.uniform(0.5,1.5))
    with open('tripurl_attr.txt','a') as f:
        for a in scrape:
            print('https://www.tripadvisor.fr'+a['href'],file=f)
    element.click()
    while True:
        try:
            time.sleep(random.uniform(1,1.5))
            ry.browser.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            ry.data()
            element=ry.browser.find_element_by_css_selector("a.ui_button.nav.next.primary")
            scrape=ry.sopa.findAll('a',{'class':'_1QKQOve4'})
            with open('tripurl_attr.txt','a') as f:
                for a in scrape:
                    print('https://www.tripadvisor.fr'+a['href'],file=f)
            element.click()
        except:
            break

'''
with ProcessPoolExecutor(max_workers=5) as executor:
    future_results = {executor.submit(getter, url): url for url in (urls)}
    results=[]
    for future in concurrent.futures.as_completed(future_results):
        results.append(future.result())
'''
