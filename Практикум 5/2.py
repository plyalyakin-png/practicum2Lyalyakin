xc = float(input("xc = "))
yc = float(input("yc = "))
r = float(input("r = "))
x = float(input("x = "))
y = float(input("y = "))
distance= (x - xc)**2 + (y - yc)**2
r_square = r**2
if distance < r_square:
    print("Точка внутри окружности")
elif distance == r_square:
    print("Точка на окружности")
else:
    print("Точка вне окружности")
