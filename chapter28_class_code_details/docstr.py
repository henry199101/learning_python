"i am: docstr.__doc__"

def func(args):
	"i am: docstr.func.__doc__"

class spam:
	"i am: spam.__doc__ or docstr.spam.__doc__"
	def method(self, arg):
		"i am: spam.method.__doc__ or self.method.__doc__"
		pass