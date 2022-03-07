product_info = {"description": "shoe", "price": 4.56, "colors": ["green", "blue", "red"]}

y = []

for key, value in product_info.items():
	y.append([key, value])

print(y)