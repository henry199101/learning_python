from adder import adder

class addboth(adder):
	def __str__(self):
		return '[Value: %s]' % self.data
	def __repr__(self):
		return 'addboth(%s)' % self.data
