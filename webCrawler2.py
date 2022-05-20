# -*- coding: utf-8 -*-
"""
Created on Sat Apr 23 18:09:06 2022

@author: N1OVU
"""

from urllib.request import urlopen
from bs4 import BeautifulSoup
import datetime
import random
import re


random.seed(datetime.datetime.now())


def getLinks(articleUrl):
    html = urlopen('http://en.wikipedia.org{}'.format(articleUrl))
    bs = BeautifulSoup(html, 'html.parser')
    the_url = '^(/wiki/)((?!:).)*$'
    return bs.find('div', {'id': 'bodyContent'}).find_all('a',
                                                          href=re.compile
                                                          (the_url))


links = getLinks('/wiki/Kevin_Bacon')
while len(links) > 0:
    newArticle = links[random.randint(0, len(links)-1)].attrs['href']
    print(newArticle)
    links = getLinks(newArticle)
