####################
# If Else
####################

if True:
    print("This is true!")

if False:
    print("This is false")


a = 1
b = 2

if a > 2:
    print("A is bigger!")
else:
    print("A is smaller!")


if a > 2:
    print("A is bigger!")
elif a == 1:
    print("A is 1!!")
else:
    print("A is smaller!")


def isTrue():
    return True


if isTrue():
    print("True!!")


if "True!":
    print("Strings are true?")

if "False":
    print("how about the word false?")

if 1:
    print("Numbers are true???")

if 0:
    print("Is zero true?")
else:
    print("Zero isn't true?? But it's a number!!")

if [1, 3]:
    print("Arrays are true?")

if []:
    print("Arrays are true?")
else:
    print("But not if they're empty!")


# num = input("Guess a number!")
# if int(num) > 3:
#     print("Hey that's bigger (or equal to) 3!!!")
# else:
#     print("Hey that's smaller than 3!")


# Logical Operators
if True and True:
    print("True and True is true?")

if True and False:
    print("True and False is true?")

if True or False:
    print("True or False is true?")


if not 1 > 2:
    print("One is greater than 2????")
