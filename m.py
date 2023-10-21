shapes = str(input())
tiles = shapes.split(" ")
square = int(tiles[0])
s_tile = int(tiles[1])
corner = int(tiles[2])

n = 0

# Square tiles

n += square * 2

# if corner tiles are greater than 2

if corner <= 1:
    s_tile = 0
    corner = 0

while corner % 2 != 0:
    corner = corner - 1

n = n + (corner * 3/2)
n = n + (s_tile * 2)


print(round(n))