import models as model
import urllib2 as urlib

def write_html_dump(url,html_store):
	html_dump=urlib.urlopen(url).read()
	html_store.html_dump[url]=html_dump

html_store=model.Html_dump()
urls=model.Url.objects()
for url in urls[0].urls:
	print "Crawling:"+url
	write_html_dump(url,html_store)
