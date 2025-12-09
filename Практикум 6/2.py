input_size = input().strip()
A, B = map(int, input_size.split('x'))
input_size2 = input().strip()
C, D, E= map(int, input_size2.split('x'))
hole_sorted = sorted([A, B])
brick_sorted = sorted([C, D, E])
if brick_sorted[0] <= hole_sorted[0] and brick_sorted[1] <= hole_sorted[1]:
    print("да")
else:
    print("нет")