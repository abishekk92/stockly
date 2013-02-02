
def cast(item):
	try:
		return int(item)
	except:
		pass
	try:
		return float(item)
	except:
		return item
foo=["string","1","1.5"]
bar=[cast(item) for item in foo]
for item in bar: print item,type(item)
