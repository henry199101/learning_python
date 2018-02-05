class Callback:
	def __init__(self, color):
		self.color = color
	def __call__(self):
		print('turn', self.color)
