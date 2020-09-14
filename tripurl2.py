import ready as ry
import time
import random

ry.change('https://www.tripadvisor.fr/Hotels-g187070-France-Hotels.html')
ry.data()
scrape=ry.sopa.findAll('a',{'class':'linkText'})
with open('tripurl2.txt','a') as f:
    for a in scrape:
        print('https://www.tripadvisor.fr'+a['href'],file=f)
element=ry.browser.find_element_by_css_selector("a.nav.next.ui_button.primary.cx_brand_refresh_phase2")
element.click()
while True:
    time.sleep(random.uniform(2,4))
    ry.browser.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    ry.data()
    element=ry.browser.find_element_by_css_selector("a.nav.next.ui_button.primary.cx_brand_refresh_phase2")
    scrape=ry.sopa.findAll('a',{'class':'city'})
    with open('tripurl2.txt','a') as f:
        for a in scrape:
            print('https://www.tripadvisor.fr'+a['href'],file=f)
    element.click()
