import models as model
import urllib2 as urlib

def write_html(html_store):
	
	url=html_store.url
	print "Dumping:"+url
	html_store.html_dump=urlib.urlopen(url).read()
	html_store.save()

for html_store in model.html_data.objects: write_html(html_store)
