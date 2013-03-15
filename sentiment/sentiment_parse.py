from BeautifulSoup import BeautifulSoup
import urllib2
from pattern.en import sentiment
import re
def sentiment_values(html_document):
	sentiments=[sentiment(elem) for elem in html_document(text=re.compile(r'(I|i)nfosys'))] 
	return len(sentiments),reduce(lambda x,y: (x[0]+y[0],x[1]+y[1]),sentiments)
for article in open('articles.txt','r').readlines()[0:2]:
       	html_document=BeautifulSoup(urllib2.urlopen(article).read())
	length,sentiment=sentiment_values(html_document)
	#print map(lambda x:x/length,sentiment)
	print length
	

	
