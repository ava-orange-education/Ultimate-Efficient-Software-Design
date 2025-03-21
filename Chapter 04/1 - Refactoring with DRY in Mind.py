# Duplicated code (calculates area of a rectangle)
def calculate_area_1(width, height):
  return width * height

def calculate_area_2(length, breadth):  # Same logic with different variable names
  return length * breadth

# Refactored DRY code (using a function)
def calculate_area(width, height):
  return width * height

# Usage
area_of_rectangle = calculate_area(5, 10)
area_of_square = calculate_area(4, 4)
