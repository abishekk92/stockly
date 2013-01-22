import urllib2 as urlib
from BeautifulSoup import BeautifulSoup


base_url="http://in.finance.yahoo.com/q/hp?s=INFY.BO"
html_page=urlib.urlopen(base_url)
print html_page.read()
