import math
import turtle
x1, y1, r1 = map(float, input().split())
x2, y2, r2 = map(float, input().split())
t = turtle.Turtle()
t.speed(5)
t.penup()
t.goto(x1, y1-r1); t.pendown(); t.circle(r1)
t.penup()
t.goto(x2, y2-r2); t.pendown(); t.circle(r2)
d = math.sqrt((x1-x2)**2 + (y1-y2)**2)
centre_rast = r1 + r2
diff_rast = abs(r1 - r2)
if d > centre_rast:
    result = "Окружности лежат одна вне другой, не касаясь"
elif d == centre_rast:
    result = "Окружности имеют внешнее касание"
elif d > diff_rast:
    result = "Окружности пересекаются"
elif d ==diff_rast:
    result = "Окружности имеют внутреннее касание"
else:
    result = "Одна окружность лежит внутри другой, не касаясь"
print(result)