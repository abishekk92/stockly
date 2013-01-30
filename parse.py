import models as model
from BeautifulSoup import BeautifulSoup
def extract_attributes(html_store):
	page=BeautifulSoup(html_store.html_dump)
	table=page.find('table','yfnc_datamodoutline1')
	price_rows=table.findAllNext('tr')
	for price_row in price_rows[2:-4]:
		for field in price_row.findChildren('td','yfnc_tabledata1'): print field.string 
#for html_dump in model.Html_dump.objects: extract_attributes(html_dump)
extract_attributes(model.html_data.objects[40])
