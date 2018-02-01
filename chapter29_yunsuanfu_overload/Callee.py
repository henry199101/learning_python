class Callee:
	def __call__(self, *pargs, **kargs):
		print('Called:', pargs, kargs)
