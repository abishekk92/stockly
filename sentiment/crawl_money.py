import urllib2 as urlib
from BeautifulSoup import BeautifulSoup

base_url="http://www.moneycontrol.com/mccode/news/searchresult.php?str=Infosys&durationType=Y&Year="
years=range(2005,2014)
link_file=open('articles.txt','w')
def crawl(url):
	html_data=BeautifulSoup(urlib.urlopen(url).read())
	for link in html_data.findAll('a','arial11_summ'): 
		try:
			link_file.write(link['href']+"\n")
		except:
			print link['href']
			pass
for year in years:
	url="%s%d" %(base_url,year)
	crawl(url)



