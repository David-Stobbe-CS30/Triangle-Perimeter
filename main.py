import math
def dist(p1, p2):
    return math.sqrt(((p2[0] - p1[0])**2) + ((p2[1] - p1[1])**2))


xA = int(input("Enter x-coordinate for Vertex A: "))
yA = int(input("Enter y-coordinate for Vertex A: "))
xB = int(input("Enter x-coordinate for Vertex B: "))
yB = int(input("Enter y-coordinate for Vertex B: "))
xC = int(input("Enter x-coordinate for Vertex C: "))
yC = int(input("Enter y-coordinate for Vertex C: "))

AB = dist([xA, yA], [xB, yB])
AC = dist([xA, yA], [xC, yC])
BC = dist([xB, yB], [xC, yC])
print(f"AB = {AB}")
print(f"AC = {AC}")
print(f"BC = {BC}")
print(f"Perimeter = {AB + AC + BC}")