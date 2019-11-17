#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Nov 17 14:44:16 2019

@author: javicarmona
"""

import requests
from bs4 import BeautifulSoup
from requests.exceptions import HTTPError

#Definimos las variables que vamos a necesitar, listas donde irán las urls
#La url base no debe acabar con '/', aquí es dodne buscaremos los links. 

url_base = 'https://www.neutrogena.es' 
url_list = []
link_interno=[]
href_website = []
urlok = []
urlbad = []

#Hacemos una primera review de links, buscando links internos dentro del 
#dominio o referencias de la misma página con #
def review_links(href_website):
    for n,i in enumerate(href_website):
        if '#' in i:
            continue
        elif i[0]== '/':
            link=url_base+i
            link_interno.append(link)
        else:
            url_list.append(i)
    return url_list,link_interno


 
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
    return urlok, urlbad

#Eliminarmos los links repetidos y los ordenamos.
def eliminar_repetidos(lista):
    lista_final=[]
    for elemento in lista:
        if not elemento in lista_final:
            lista_final.append(elemento)
    lista_final.sort()
    return lista_final

#Leemos la web y guardamos en href_website los links encontrados
page = requests.get(url_base)
soup = BeautifulSoup(page.text, 'html.parser')
for href in soup.find_all('a', href=True):
    href_website.append(href['href'])

    
print('Links extraidos de:',url_base,'>>', len(href_website))
#Lanzamos los 2 procesos, limpiar links no válidos y chequear los links. 
url_list,link_interno = review_links(href_website)  

urlok, urlbad = check_ulr(url_list)
urlok, urlbad = check_ulr(link_interno)
lista_final = eliminar_repetidos(urlok)

#Resumen de resultados y listado de link inválidos. 
print('Links ok:', len(urlok))
print('Links ko:', len(urlbad))
print('Links Correctos únicos:', len(lista_final))

if len(urlbad) == 0:
    print ('Todas las URLs del site están correctas')
else:
    print ('Se han detectado', len(urlbad), 'links incorrectos dentro del site', url_base)
    print ('Links incorrectos: ')
    for link in urlbad:
        print (link)

        
        
#Fin.. por el momento