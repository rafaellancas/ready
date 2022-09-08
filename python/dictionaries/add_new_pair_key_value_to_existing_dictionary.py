dict = {"January": 45, "February": 56, "March": 67}

new_key = "January"
new_value = 67

if new_key in dict:
    print("Key already in dictionary!")
    print(dict)
else:
    dict[new_key] = new_value
    print(dict)