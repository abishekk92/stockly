from mongoengine import *

connect('test-db')

class Foo(Document):
	bar=FloatField()


foo=Foo()
foo.bar=1.0
foo.save()
inst=Foo.objects[0]
print type(inst.bar)
