import models as model
from BeautifulSoup import BeautifulSoup
from dateutil.parser import parse
import re
import logging 

logging.basicConfig(filename='parser.log')
def to_date(date_string):
	
	return parse(date_string)

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
	try:
		page=BeautifulSoup(html_store.html_dump)
		table=page.find('table','yfnc_datamodoutline1')
		price_rows=table.findAllNext('tr')
		for price_row in price_rows[2:-4]:
			index=model.Index()
			try:
				indices=[index.date,index.open_price,index.day_high,index.day_low,index.close_price,index.volume,index.adj_close]=[cast(re.sub(',','',field.string)) for field in price_row.findChildren('td','yfnc_tabledata1')]
				html_store.indexes.append(index)
			except:
				logging.warning('Skipping %s',field.string)
		html_store.save()
		logging.info('%s is parsed and dumped',html_store.url)
	except:
		logging.exception("Document is empty or doesn't have valid HMTL")
for html_store in model.html_data.objects: extract_attributes(html_store)

