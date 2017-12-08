class Callback:
	def __init__(self, color):
		self.color = color
	def __call__(self):
		print('turn', self.color)

cb1 = Callback('blue')		
cb2 = Callback('green')

B1 = Button(command=cb1)
B2 = Button(command=cb2)