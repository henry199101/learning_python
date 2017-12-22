def adder(*args):
	sum = args[0]
	for next in args[1:]:
		sum += next
	return sum

print(adder(2, 3, 4))
print(adder('spam ', 'eggs ', 'toast '))
print(adder(['a', 'b'], ['c', 'd'], ['e', 'f']))