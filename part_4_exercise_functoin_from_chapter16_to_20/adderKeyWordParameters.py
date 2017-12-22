def adder2(**args):
	argskeys = list(args.keys())
	sum = args[argskeys[0]]
	for key in argskeys[1:]:
		sum += args[key]
	return sum

print(adder2(good=1))
print(adder2(good=1, bad=2))
print(adder2(good=1, bad=2, ugly=3))
# print(adder2(good=1, bad=2, ugly=3, 4))