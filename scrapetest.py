# -*- coding: utf-8 -*-
"""
Created on Sat Apr 23 15:10:28 2022

@author: N1OVU
"""

from urllib.request import urlopen
from bs4 import BeautifulSoup
from urllib.error import HTTPError
from urllib.error import URLError


try:
    html = urlopen('http://pythonscraping.com/pages/page1.html')
    bs = BeautifulSoup(html.read(), 'html.parser')
    print(bs.h1)
    #badcontent = bs.nonexistentTag.anotherTag
    
except AttributeError as e:
    print(e)
    print('Tag was not found!')
    
except HTTPError as e:
    print(e)
    
except URLError as e:
    print(e)
    print('The server could not be found!')
    
else:
    print('It worked!')
