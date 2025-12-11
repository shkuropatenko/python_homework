class Point():
  def __init__(self, x, y):
    self.x = x
    self.y = y

  def __eq__(self, other):
    return self.x == other.x and self.y == other.y
  def __str__(self):
    return f"({self.x}, {self.y})"
  def distance(self, other):
    return ((self.x - other.x)**2 + (self.y - other.y)**2)**0.5

class Vector(Point):
  def __str__(self):
    return f"Vector({self.x}, {self.y})"
  def __add__(self, other):
    return Vector(self.x + other.x, self.y + other.y)

p1 = Point(1, 2)
p2 = Point(1, 2)
print(p1 == p2)
print(p1.distance(p2))

v1 = Vector(1, 2)
v2 = Vector(3, 4)
print(v1 + v2)


