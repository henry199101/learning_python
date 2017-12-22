def mymap(func, *seqs):
	res = []
	for args in zip(*seqs):
		yield func(*args)

'''
def mymap(func, *seqs):
	return (func(*args) for args in zip(*seqs))
'''