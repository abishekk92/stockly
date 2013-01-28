import models as model
import urllib2 as urlib

def write_html(url):
	
	html_store=model.Html_dump()
	html_store.url=url
	print "Dumping:"+url.url
	html_store.html_dump=urlib.urlopen(url.url).read()
	html_store.save()

for url in model.Urls.objects: write_html(url)
