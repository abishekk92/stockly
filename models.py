from mongoengine import *

connect('stockly')

class Url(Document):
	urls=ListFiled(URLField())

class Index(DynamicDocument):
	

