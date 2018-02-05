class Life:
	def __init__(self, name='unknow'):
		print('Hello', name)
		self.name = name
	def __del__(self):
		print('Goodbye', self.name)
