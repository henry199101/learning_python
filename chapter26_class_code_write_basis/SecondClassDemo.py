from FirstClassDemo import FirstClass

class SecondClass(FirstClass):
	def display(self):
		print('Current value = "%s"' % self.data)
