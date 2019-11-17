#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Nov 17 14:44:16 2019

@author: javicarmona
"""

import requests
from bs4 import BeautifulSoup
from requests.exceptions import HTTPError

import requests
from bs4 import BeautifulSoup
from requests.exceptions import HTTPError

#Definimos las variables que vamos a necesitar, listas donde irán las urls
#La url base no debe acabar con '/', aquí es dodne buscaremos los links. 

url_base = 'https://www.neutrogena.es' 
url_list = []
href_website = []
urlok = []
urlbad = []

#Hacemos una primera review de links, buscando links internos dentro del dominio o referencias de la misma página con #
#### No funciona... el # REVISAR
def review_links(url_list):
    for n,i in enumerate(url_list):
        #Si el link empieza con / son links dentro del dominio, por ello
        #debemos montar la ulr completa, incluyendo el dominio. 
        if i[0]== '/':
            url_list[n]=url_base+i
        #Los links internos con # dan error, por ello los eliminamos. 
        #if '#' in i:
        #    del url_list[n]

 
#Definimos una función que recibe una lista de urls y chequea cada una
#de ellas, las correctas van a una lista, las incorrectas a otra.           
def check_ulr(url_list):
    for url in (url_list):
        try:
            response = requests.get(url)
            # If the response was successful, no Exception will be raised
            response.raise_for_status()
        except HTTPError as http_err:
            urlbad.append(url)
        except Exception as err:
            urlbad.append(url)
        else:
            urlok.append(url)


#Leemos la web y guardamos en href_website los links encontrados
page = requests.get(url_base)
soup = BeautifulSoup(page.text, 'html.parser')
for href in soup.find_all('a', href=True):
    href_website.append(href['href'])

    
print('Links extraidos de:',url_base,'>>', len(href_website))
#Lanzamos los 2 procesos, limpiar links no válidos y chequear los links. 
review_links(href_website)  
check_ulr(href_website)

#Resumen de resultados y listado de link inválidos. 
print('Links ok:', len(urlok))
print('Links ko:', len(urlbad))
if len(urlbad) == 0:
    print ('Todas las URLs del site están correctas')
else:
    print ('Se han detectado', len(urlbad), 'links incorrectos dentro del site', url_base)
    print ('Links incorrectos: ')
    for link in urlbad:
        print (link)
        
        
#Fin.. por el momento