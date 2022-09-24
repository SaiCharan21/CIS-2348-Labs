x1 = int(input())
y1 = int(input())
z1 = int(input())
x2 = int(input())
y2 = int(input())
z2 = int(input())

boolean = False

for valX in range(-10, 11):
    for valY in range(-10, 11):
        if (x2 * valX + y2 * valY == z2) and (x1 * valX + y1 * valY == z1):
            boolean = True
            print(valX, valY)

if not boolean:
    print("No solution")
