# Valid variable names
a = 1
b = 2
b2 = 5
a_really_long_variable_name_thats_super_descriptive = "dog"

# Invalid variables
# a+b = 1
# lucas'sVariable = "test"
# this-variable = asdf

# CamelCase
myVariableName = "variable"
my_variable_name = "variable"

# Case Sentivie
a = 1
A = 2
print(a, A)


####################
# Variable types
####################
integerVariable = 1
stringVariable = "asdf"
floatVariable = 1.11334
booleanVariable = True
arrayVariable = [0, 2, 3, 4]
arrayVariable2 = ["one", "two", "three"]
byteVariable = 0xAA


print(type(integerVariable))
print(type(stringVariable))

# Operations depend on variable type
firstOne = 1
secondOne = "1"

# result = firstOne + secondOne

firstOne = "1"

# result = firstOne + secondOne
# print(result)


firstOne_as_integer = int(firstOne)
firstOne_as_float = float(firstOne)

print(firstOne_as_integer)
print(firstOne_as_float)

firstOne_as_boolean = bool(firstOne)
print(firstOne_as_boolean)
