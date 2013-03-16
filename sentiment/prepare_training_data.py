from BeautifulSoup import BeautifulSoup
import urllib2 as urlib
import re
test_data=open('dataset/unclean_test.data','w')
for url in open('articles.txt','r').readlines():
	html_document=BeautifulSoup(urlib.urlopen(url).read())
	for script in html_document.findAll('script'): script.extract()
	for elem in html_document(text=re.compile(r'(I|i)nfosys')): 
		try:
			test_data.write(elem+"\n")
		except:
			pass

	
