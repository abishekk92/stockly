import models as model
import urllib2 as urlib
import pyhash

hasher=pyhash.murmur3_32()

def write_html_dump(url,html_store):
	html_dump=urlib.urlopen(url).read()
	url_hash=hasher(url)
	html_store.html_dump[str(url_hash)]=html_dump


html_store=model.Html_dump()
urls=model.Url.objects()
write_html_dump(urls[0].urls[0],html_store)

for url in urls[0].urls:
	write_html_dump(url,html_store)

html_store.save()
