from mongoengine import *

connect('stockly')

class Urls(Document):
	url=URLField()

class Index(Document):
	indexes=ListField(DictField(field=MapField(field=StringField())))

class Html_dump(Document):
	url = ReferenceField(Urls)
	html_dump=DynamicField()


