from adder import adder

class addstr(adder):
	def __str__(self):
		return '[Value: %s]' % self.data
