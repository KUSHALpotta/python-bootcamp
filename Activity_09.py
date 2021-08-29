def cube(x):
    res = x ** (1 / 3)
    return res


import math
l=int(input("Enter the length of tromboloid"))
b=int(input("bredth"))
h=int(input("height"))

k=((l*l)+(b*b)+(h*h))

c=math.sqrt(k)
volume=((b*b*h)/(c))

print(format(volume,".3f"))

rad=((volume*3)/(4*3.14))
radius=cube(rad)

print(radius)
