class empty:
	def __getattr__(self, attrname):
		if attrname == "age":
			return 40
		else:
			raise AttributeError

X = empty()
print(X.age)
print(X.name)