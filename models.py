from mongoengine import *

connect('stockly')

class Index(EmbeddedDocument):
	date=DateTimeField()
	open_price=FloatField()
	day_high=FloatField()
	day_low=FloatField()
	close_price=FloatField()
	adj_close=FloatField()
	volume=IntField()
class html_data(Document):
	url = URLField()
	html_dump=DynamicField()
	indexes=ListField(EmbeddedDocumentField(Index))


