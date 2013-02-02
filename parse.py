import models as model
from BeautifulSoup import BeautifulSoup
from datetime import datetime 
import re
def to_date(date_string):
	return datetime.strptime(date_string,"%d %b %Y")

def cast(item):
	try:
		return int(item)
	except:
		pass
	try:
		return float(item)
	except:
		return to_date(item)
def extract_attributes(html_store):
	page=BeautifulSoup(html_store.html_dump)
	table=page.find('table','yfnc_datamodoutline1')
	price_rows=table.findAllNext('tr')
	for price_row in price_rows[2:-4]:
		index=model.Index()
		try:
			indices=[index.date,index.open_price,index.day_high,index.day_low,index.close_price,index.volume,index.adj_close]=[cast(re.sub(',','',field.string)) for field in price_row.findChildren('td','yfnc_tabledata1')]
			html_store.indexes=indices
			html_store.save()
		except:
			raise 
#for html_dump in model.Html_dump.objects: extract_attributes(html_dump)
extract_attributes(model.html_data.objects[48])


#to-do:Writing everything in unicode is a bad idea,do proper dynamic type conversion
