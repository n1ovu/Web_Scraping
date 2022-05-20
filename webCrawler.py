# -*- coding: utf-8 -*-
"""
Created on Sat Apr 23 17:52:41 2022

@author: N1OVU
"""

from urllib.request import urlopen
from bs4 import BeautifulSoup
import re


html = urlopen('http://en.wikipedia.org/wiki/Kevin_Bacon')
bs = BeautifulSoup(html, 'html.parser')

the_url = '^(/wiki/)((?!:).)*$'

for link in bs.find_all('a', href=re.compile(the_url)):
    if 'href' in link.attrs:
        print(link.attrs['href'])
