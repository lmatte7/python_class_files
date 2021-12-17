# This variable exists WAY further up
number = 8


# Many lines later...

# We're doing something unrelated down here
a = 1


numbers = [5,3,87,2]
results = []

for number in numbers:
  results.append(a + number)


print(results)

# Why is this 2?? I need this to be 8
print(number)




# Breakpoints can also only run on a condition
for number in range(100):
  results.append(number)


