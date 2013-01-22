import urllib2 as urlib
from BeautifulSoup import BeautifulSoup


base_url="http://in.finance.yahoo.com/q/hp?s=INFY.BO"
html_page=urlib.urlopen(base_url)
html_document=BeautifulSoup(html_page)
for url in html_document('a',rel="next"):
	print base_url+url["href"]
