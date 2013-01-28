from mongoengine import *

connect('stockly')

class Url(Document):
	urls=URLField()

class Index(Document):
	indexes=ListField(DictField(field=MapField(field=StringField())))

class Html_dump(Document):
	url =URLField()
	html_dump=StringField()


