lista_onepark=[]
filepark=open('urlpark.txt')
with open('urlpark.txt') as f:
    f=f.readlines()
import os.path
from os import path
if path.exists("onepark.csv"):
    pass
else:
    headers='Nom\tDescription\tAdresse Piéton\tAdresse Véhicule\tURL\n'
    fhandle=open('onepark.csv','w')
    fhandle.write(headers)
    fhandle.close()
from concurrent.futures import ProcessPoolExecutor
from concurrent.futures import ThreadPoolExecutor
from concurrent.futures import Future
import pandas as pd

    #pass
#fhandle=open('salles.csv','w')
#headers=('Nom;Adresse;Equipements;Activités;Restauration;Hébergement;Superficie;Debout;Assis;Cocktail;Conférence;Banquet;Réunion;En classe; En U\n' )
#import abcsalles as abc
#abc.ouvrir_stealth()
#from openpyxl import load_workbook
#writer = pd.ExcelWriter('abcsalles.xlsx', engine='openpyxl')
#writer.book = load_workbook('abcsalles.xlsx')
#writer.sheets = dict((ws.title, ws) for ws in writer.book.worksheets)
#reader = pd.read_excel(r'abcsalles.xlsx')


import abcsalles as abc
import re
#column_names=['Nom;Description;Adresse;URL;Horaire;Type;Superficie;Postes;Utilisation;Weekend;Services;Parking']
#try:
#    Masterdata = pd.DataFrame(columns=['Nom','URL','Adresse','Parking','Voiture','Transports','Usage','Gamme','Tarif','Equipements','Restauration','Traiteur','Espaces','Superficie','Debout','Assis','Cocktail','Conférence','Banquet','Réunion','En classe','En U'])
#except:
#    pass
import os
import random
import time
clear = lambda: os.system('clear')
#done_list=[]
from tqdm import tqdm
import requests
def onepark(url):
    time.sleep(random.uniform(1,2))
    r=requests.get(url)
    sopa=abc.sopa(r.content)
    names=sopa.findAll('h1')
    try:
        nom=re.sub(' +',' ',names[0].text.replace('\n','').replace('\t','')).strip()
    except:
        nom=''
    description=sopa.findAll('span',{'class':'park-overview__company-name'})
    try:
        desc=re.sub(' +',' ',description[0].text.replace('\n','').replace('\t','')).strip()
    except:
        desc=''
    adresses=sopa.findAll('ul',{'class':'small-icon-list m-top-30'})
    try:
        candidate=re.sub(' +',' ',adresses[0].text.replace('\n','').replace('\t','')).strip()
    except:
        candidate=''
    posauto=candidate.find('Accès véhicule')
    pospie=candidate.find('Accès piéton')
    try:
        adauto=candidate[posauto:pospieton]
    except:
        try:
            adauto=candidate[posauto:]
        except:
            adauto=''
    try:
        adpie=candidate[pospieton:]
    except:
        adpie=""

    urly=url

    varlist=[nom,description,adpie,adauto,urly]
    to_append=varlist
    s = pd.DataFrame(to_append).T
    s.to_csv('coworking.csv', mode='a', header=False,sep='\t',index=False)
    #to_append=str(nom)+'\t'+str(situation)+'\t'+str(url)+'\t'+str(adresse)+'\t'+str(espaces_net)+'\t'+str(surface_net)+'\t'+str(capacite_salle)+'\t'+str(capacite_hotel)+'\t'+str(parking)+'\t'+str(voiture)+'\t'+str(transports)+'\t'+str(ideale)+'\t'+str(gamme)+'\t'+str(montant)+'\t'+str(wea)+'\t'+str(restauration) +'\t'+ str(traiteur)+'\t'+ str(espaces) +'\t'+ varlist +'\t'+ varlist3
    #with open('abcsalles.csv','a') as fhandle:
        #fhandle.write(to_append)
    #Masterdata.to_excel("abcsalles.xlsx")
    #abc.time.sleep(1)

    #print(to_append)
    #print('\n\n')

with ProcessPoolExecutor(max_workers=10) as executor:
    future_results = {executor.submit(cowork, url): url for url in (lista_coworking)}
    results=[]
    for future in concurrent.futures.as_completed(future_results):
        results.append(future.result())
