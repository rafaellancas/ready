list = ["a","a","v", "a", "b"]
element = "a"
y = []

if list == []:
    print("Empty List")
else:
    if element not in list:
        print("Not Found")
    else:     
        for c in (range(len(list))):
            z = list[c]
            y.append(z)
            if z == element:
                y.remove(z)
        print(y)

       

