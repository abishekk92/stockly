import models
total_number=3168
per_page=66
show_next=0
base_url="http://in.finance.yahoo.com/q/hp?s=INFY.BO&a=2&b=16&c=2000&d=0&e=22&f=2013&g=d&z=66&y="+str(show_next)
def write_mongo(url):
	url_store=models.Urls()
	url_store.url=url
	url_store.save()
while show_next<=total_number:
	write_mongo(base_url+str(show_next))
	show_next+=per_page



