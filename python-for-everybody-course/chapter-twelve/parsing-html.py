# What is Web Scraping?
'''
* When a program or script pretends to be a browser and retrieves web pages, looks at those web pages, extracts information and then looks at more web pages
* Search engines scrape web pages - we call this "spidering the web" or "web crawling"
'''

#Why Scrape?
'''
* Pull data - particularly social data - who linkt to who?
* Get your own data back out of some system that has no "export capability"
* Moniotr a site for new information
* Spider the web to make a database for a search engine
'''

#Scraping Web Pages
'''
* There is some controversy about web page scraping and some sites are a bit snippy about it.
* Republishing copyrighted information is not allowed
* Violating terms of service is not allowed
'''

import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup

url = input('Enter - ')
html = urllib.request.urlopen(url).read()
soup = BeautifulSoup(html, 'html.parser')

#Retrieve all of the anchor tags
tags = soup('a')
for tag in tags :
    print(tag.get('href', None))


import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl

#Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter - ')
html = urllib.request.urlopen(url, context=ctx).read()
soup = BeautifulSoup(html, 'html.parser')

tags = soup('a')
for tag in tags :
    print(tag.get('href', None))