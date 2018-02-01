from adder import adder

class addrepr(adder):
	def __repr__(self):
		return 'addrepr(%s)' % self.data
