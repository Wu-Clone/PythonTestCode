from dataclasses import dataclass

@dataclass
class Point:
    x: int
    y: int

point = Point(1, 2)
print(point)
print(point.x)
print(point.y)

point2 = Point(1, 2)
print(point2)
print(point2 == point)