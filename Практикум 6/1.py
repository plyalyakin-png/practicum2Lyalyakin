import math
ARENA_RADIUS = 6.5
ARENA_DIAMETER = 2 * ARENA_RADIUS
input_size = input().strip()
size = input_size.split('x')
A = float(size[0])
B = float(size[1])
diagonal = math.sqrt(A * A + B * B)
if diagonal <= ARENA_DIAMETER:
    print("да")
else:
    print("нет")