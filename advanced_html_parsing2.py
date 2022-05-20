# -*- coding: utf-8 -*-
"""
Created on Sat Apr 23 17:29:22 2022

@author: N1OVU
"""

from urllib.request import urlopen
from bs4 import BeautifulSoup


html = urlopen('http://www.pythonscraping.com/pages/page3.html')
bs = BeautifulSoup(html, 'html.parser')

for child in bs.find('table',{'id': 'giftList'}).children:
    print(child)

for sibling in bs.find('table', {'id':'giftList'}).tr.next_siblings:
    print(sibling)
    
