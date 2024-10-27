import math
figure = input()

if figure == "square":
    side = float(input())
    resultSquare = side * side
    print(f"{resultSquare:.3f}")
elif figure == "rectangle":
    sideA = float(input())
    sideB = float(input())
    resultRectangle = sideA * sideB
    print(f"{resultRectangle:.3f}")
elif figure == "circle":
    radius = float(input())
    resultCircle = pow(radius, 2) * math.pi
    print(f"{resultCircle:.3f}")
elif figure == "triangle":
    widthSide = float(input())
    heightSide = float(input())
    resultTriangle = (widthSide * heightSide) / 2
    print(f"{resultTriangle:.3f}")

