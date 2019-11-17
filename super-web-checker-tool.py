#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Nov 17 14:44:16 2019

@author: javicarmona
"""
import requests
from bs4 import BeautifulSoup
from requests.exceptions import HTTPError

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
