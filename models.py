from mongoengine import *

connect('stockly')

class Urls(Document):
	url=URLField(unique=True)

class Index(Document):
	date=DateTimeField(unique=True)
	open_price=FloatField()
	day_high=FloatField()
	day_low=FloatField()
	close_price=FloatField()
	adj_close=FloatField()
	volume=IntField()

class Html_dump(Document):
	url = ReferenceField(Urls,dbref=True)
	html_dump=DynamicField()


