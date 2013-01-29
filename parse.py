import models as model
from BeautifulSoup import BeautifulSoup

def extract_attributes(html_dump):
	'''page=BeautifulSoup(html_dump.html_dump)
	trs=page.findAll('tbody tr')
	for tr in trs: print tr'''
	print html_dump.url.url


for html_dump in model.Html_dump.objects: extract_attributes(html_dump)
