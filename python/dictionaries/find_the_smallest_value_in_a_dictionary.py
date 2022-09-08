my_dict = {"a":3, "b":4, "c":2, "d":10}

y = list(my_dict.values())
x = len(y)

if x == 0:
	print("None")
else:
	print(min(y))