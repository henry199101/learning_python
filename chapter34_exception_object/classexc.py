class General(Exception): pass
class Specific1(General): pass
class Specific2(General): pass

def raise0():
	X = General()
	raise X

def raise1():
	X = Specific1()
	raise X

def raise2():
	X = Specific2()
	raise X

for func in (raise0, raise1, raise2):
	try:
		func()
	except General:
		import sys
		print('caught:', sys.exc_info()[0])