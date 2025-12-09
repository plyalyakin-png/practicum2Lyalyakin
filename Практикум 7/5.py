N = int(input())
all_cubes = []
first_cube = 1
while first_cube ** 3 <= N:
    cube = first_cube ** 3
    all_cubes.append(cube)
    first_cube += 1
print(' '.join(map(str, all_cubes)))