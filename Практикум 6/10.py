import turtle
print("Введите координаты первого прямоугольника (x1 y1 x2 y2):")
x1_1, y1_1, x2_1, y2_1 = map(float, input().split())
print("Введите координаты второго прямоугольника (x1 y1 x2 y2):")
x1_2, y1_2, x2_2, y2_2 = map(float, input().split())
t = turtle.Turtle()
t.speed(5)
t.penup()
t.goto(x1_1, y1_1)
t.pendown()
t.color("blue")
for i in range(2):
    t.forward(x2_1 - x1_1)
    t.right(90)
    t.forward(y1_1 - y2_1)
    t.right(90)
t.penup()
t.goto(x1_2, y1_2)
t.pendown()
t.color("red")
for i in range(2):
    t.forward(x2_2 - x1_2)
    t.right(90)
    t.forward(y1_2 - y2_2)
    t.right(90)
if (x1_1 <= x1_2 and x2_1 >= x2_2 and y1_1 >= y1_2 and y2_1 <= y2_2) or \
        (x1_2 <= x1_1 and x2_2 >= x2_1 and y1_2 >= y1_1 and y2_2 <= y2_1):
    result = "Один прямоугольник лежит внутри другого, не касаясь"
elif x2_1 < x1_2 or x2_2 < x1_1 or y2_1 > y1_2 or y2_2 > y1_1:
    result = "Прямоугольники лежат вне друг друга, не касаясь"
elif (x2_1 == x1_2 or x2_2 == x1_1 or
      y1_1 == y2_2 or y1_2 == y2_1):
    result = "Прямоугольники имеют касание"
else:
    result = "Прямоугольники имеют пересечение"
print(result)