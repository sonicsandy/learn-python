l=100
b=20
l=input("enter length: ")
b=input("enter breadth: ")

area = int(l) * int(b)
print("Area of a rectangle: ", area)

if area>1000:
    print("Area is too big")
else:
    print("Area is perfect")


