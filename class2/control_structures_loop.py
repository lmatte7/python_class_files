####################
# While Loops
####################

i = 0
while i < 5:
    print("The variable i is currently: " + str(i))
    i += 1


i = 0
is_i_equal_to_3 = False

while not is_i_equal_to_3:
    print("The variable i is currently " + str(i) + " which is not 3")
    i += 1
    if i == 3:
        is_i_equal_to_3 = True


# j = 0
# while j < 3:
# print("j is less than 3, I'm sure it won't be soon!")

####################
# For Loops
####################

for current_number in range(5):
    print("Here is " + str(current_number) + "!")

for current_number in range(5):
    print("Here is " + str(current_number) + "!")
else:
    print("The loop has ended and current_number is: " + str(current_number))


array = [1, 2, 3]

for value in array:
    print("The current value is: " + str(value))

array = ["apple", "banana", "orange"]

for fruit in array:
    print("The current fruit is: " + str(fruit))


scores = [100, 98, 64, 75]

totalScore = 0
for score in scores:
    totalScore += score

average = totalScore / len(scores)
print("The average score is: " + str(average))


scores = {"Lucas": 84, "Hannah": 99, "Charlotte": 100}

totalScore = 0
for score in scores:
    print(score)

for score in scores:
    totalScore += scores[score]

average = totalScore / len(scores)
print("The average score is: " + str(average))


#######################
# Break and Continue
#######################


i = 0
while i < 5:
    if i != 1:
        print("The variable i is: " + str(i))
    i += 1


for i in range(5):
    if i == 1:
        continue
    print("The variable i is: " + str(i))


for i in range(5):
    if i == 3:
        break
    print("The variable i is: " + str(i))


# while True:
#     value = input("Please enter in a plus sign!")
#     if value == "+":
#         print("Thank you for your cooperation!")
#         break
