class ShapeFactory:
  def create_shape(self, shape_type):
    if shape_type == "circle":
      return Circle()
    elif shape_type == "rectangle":
      return Rectangle()
    else:
      raise ValueError("Invalid shape type")

class Circle:
  def draw(self):
    print("Drawing a circle")

class Rectangle:
  def draw(self):
    print("Drawing a rectangle")

# Usage
factory = ShapeFactory()
circle = factory.create_shape("circle")
circle.draw()  # Prints "Drawing a circle"
