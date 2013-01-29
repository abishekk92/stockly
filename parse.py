import models as model
from BeautifulSoup import BeautifulSoup
def extract_attributes(html_dump):
	page=BeautifulSoup(html_dump.html_dump)
	table=page.find('table','yfnc_datamodoutline1')
	price_rows=table.findAllNext('tr')
	for price_row in price_rows[2::]:
		for field in price_row.findAllNext('td','yfnc_tabledata1'): 
			if field.string is not None: print field.string
		

#for html_dump in model.Html_dump.objects: extract_attributes(html_dump)
extract_attributes(model.Html_dump.objects[0])
