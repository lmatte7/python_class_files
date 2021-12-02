# To create a class use the "class" keyword
class Rectangle: 
  width = 4
  height = 5
 
# To create an "instance" of a class use the same format as calling a function
# rect = Rectangle()

# To access a variable in a class use a "." 
# print(rect.width)
# print(rect.height)

# To make classes more useful you can use a special function that lets you 
# assign its variables in the program. 
# self is a way to reference the class itself 
# class Rectangle: 

#   def __init__(self, width, height): 
#     self.width = width
#     self.height = height


# rect = Rectangle(5, 9)

# print(rect.width)
# print(rect.height)

# Each time a class is created it creates an "instance" of the class. 
# There can be as many as needed in a program
# rect2 = Rectangle(89, 33)

# print(rect2.width)
# print(rect2.height)

# Classes can have functions that belong to them as well
# This lets you use the variables in a class in a 
# reliable way
# class Rectangle: 

#   def __init__(self, width, height): 
#     self.width = width
#     self.height = height

#   def area(self): 
#     return self.width * self.height



# rect = Rectangle(5, 9)
# print(rect.area())

# rect.height = 15
# print(rect.area())

# area()

# We can create a function that takes a rectangle, but there isn't a way
# to ensure anyone reading the program knows we want a rectangle class
# def calc_area(rectangle):
#   return rectangle.width * rectangle.height

# a = calc_area(rect)
# print(a)