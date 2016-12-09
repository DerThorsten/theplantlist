from bs4 import BeautifulSoup
import urllib2
from subprocess import call
baseurl = 'http://www.theplantlist.org/'
f = urllib2.urlopen(baseurl + '1.1/browse/-/')
content = f.read()
soup = BeautifulSoup(content, 'html.parser')
for item in soup.find('ul', id='nametree').find_all('li'):
    fname = item.a.i.text + '.csv'
    url = item.a['href']
    call(['wget', baseurl + url + fname])


