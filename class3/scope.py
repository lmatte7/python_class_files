# Global scope is used when declaring a variable in the program
x = 100

# These variables can be used in functions
def cool(): 
  print(x)

cool()
# But if another variable with the same name is used in a function
# Python will use the "local" variable
def cool():
  x = 3
  print(x)

cool()
print(x)


# If you DO want to use the global variable you can 
# use the global keyword
# You should avoid this if at ALL possible
def cool():
  global x
  x = 4
  print(x)

cool()
print(x)