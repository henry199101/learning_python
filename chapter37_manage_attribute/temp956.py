class Person:
	def __init__(self, name):
		self._name = name

	def __getattr__(self, attr):
		if attr == 'name':
			print('fetch...')
			return self._name
		else:
			raise AttributeError(attr)

	def __setattr__(self, attr, value):
		if attr == 'name':
			print('change...')
			attr = '_name'
		self.__dict__[attr] = value

	def __delattr__(self, attr):
		if attr == 'name':
			print('remove...')
			attr = '_name'
		del self.__dict__[attr]

bob = Person('Bob Smith')
print(bob.name)
bob.name = 'Robert Smith'
print(bob.name)
del bob.name

print('-'*20)
sue = Person('Sue Jones')
print(sue.name)
#print(Person.name.__doc__)