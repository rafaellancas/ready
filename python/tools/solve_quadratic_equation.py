import math

while True:
    try:
        a = float(input("Insert the number for a:"))
        b = float(input("Inser the number for b:"))
        c = float(input("Insert the number for c:"))

        print("Your equation is {}x² + {}x + {} = 0".format(int(a),int(b),int(c)))

        dis = ((b**2)-4*a*c)

        if dis == 0:
            z = (-b)/(2*a)
            print("The solution is {}.".format(z))
        if dis < 0:
            print("The equation has complex roots.")
        if dis > 0:
            z = ((-b)-math.sqrt(dis))/(2*a)
            y = ((-b)+math.sqrt(dis))/(2*a)
            print("The solutions are {} and {}.".format(z,y))

    except ValueError:
        print("Invalid number!")