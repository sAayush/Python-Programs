from rubik.cube import Cube as cube

c = cube("OOOOOOOOOBBBWWWGGGYYYBBBWWWGGGYYYBBBWWWGGGYYYRRRRRRRRR")
# print(c)

cube.B(c)
# print(c)
cube.L(c)
# print(c)
cube.Li(c)
cube.Bi(c)
print(c)

cube.sequence(c, "B L")

print(c)

print(cube.is_solved(c))

cube.sequence(c, "Li Bi")

print(cube.is_solved(c))


