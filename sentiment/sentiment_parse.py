from BeautifulSoup import BeautifulSoup
import urllib2
from pattern.en import sentiment
for article in open('articles.txt','r').readlines():
       	print sentiment(BeautifulSoup(urllib2.urlopen(article).read()).find('body'))
	
