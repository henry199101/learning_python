L = []
for item in range(6):
	L.append(2 ** item)
X = 5

if (2 ** X) in L:
	print((2 ** X), 'was found at', L.index(2 ** X))
else:
	print(X, 'not found')
