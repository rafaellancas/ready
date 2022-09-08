import math

x = [1,2,3]
y = [1,2,3]

z = abs(math.sqrt((math.pow((y[0]-x[0]),2)+
                    math.pow((y[1]-x[1]),2)+    
                    math.pow((y[2]-x[2]),2))))

print(z)