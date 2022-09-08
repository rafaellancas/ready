my_dict = {"a": 4, "b": 4, "c": 2}

#Use a set because you can't add repeated values to a set, so it's length should always be one if all the values are equal
x = len(set(my_dict.values()))

if x == 0:
	print("Empty")
elif x == 1:
	print(True)
else:
	print(False)

