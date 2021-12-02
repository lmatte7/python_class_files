# To define a function use the def keyword
# Remember that anything indented after the declaration belongs to the function
def myFunction():
  print("This is my function!")

# To use a function you "call" it by using its name
# myFunction()


# To make functions more useful you can provide arguments 
# def addFive(number):
#   result = number + 5
#   print(result)

# Arguments are included when calling a function
# addFive(5)
# addFive(2)

# You can have as many arguments as needed 
def calculate_area(width, height):
  area = width * height
  print("The area is: " + str(area))


# calculate_area(5, 3)

# Arguments can be specified by name when calling a function
# calculate_area(width=2, height=12)


# Arguments can be almost anything
# def printFunction(function):
  # print(function)

# printFunction(calculate_area)


# Arguments can also be provided a default value
# This is useful if the function is called a lot with the 
# same value
# def addPhoneNumber(number, prefix="812"):
#   print("The phone number is: " + prefix, number)


# addPhoneNumber("123-1234", "123")
# addPhoneNumber("123-1234")


# Functions can provide their result by returning values
# def calculate_area(width, height):
#   area = width * height
#   return area

# area = calculate_area(8, 9)

# print(area)


# What is the return value if we don't include a return??
# result = print("HERE!")
# print(result)

# if None:
#   print("Is None True?")


# Functions can return multiple values 
# def getPerson():
#     name = "Leona"
#     age = 35
#     country = "UK"
#     return name,age,country

# name, age, country = getPerson()
# print(name)
# print(age)
# print(country)



# Variables declared in a function can only be used in the function
# def find_average(numbers):
#   number_length = len(numbers)
#   total = 0
#   for number in numbers:
#     total += number
#   return total / number_length


# scores = [90, 78, 88, 67, 81]

# average = find_average(scores)

# print(average)
# print(total)
# print(number_length)