L = [1,2,3]

I = iter(L)

while True:
	try:
		X = next(I)
	except StopIteration:
		break
	print(X ** 2, end=' ')
