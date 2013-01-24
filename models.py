from mongoengine import *

connect('stockly')

class Url(Document):
	urls=ListField(URLField())

class Index(Document):
	indexes=ListField(DictField(field=MapField(field=StringField())))

class Html_dump(Document):
	html_dump=MapField(field=StringField())


