# Create a function called greeting that takes a string argument
# and return hello string

def greeting(name):
    return "Hello " + name


# Test of greeting
print(greeting("Ben"))


# Declare a list of numbers from 1-9, iterate through the list and print each number
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]

for number in numbers:
    print(number)


# Write the names of the boolean operators
# and
# or

if 'a' == 'b' and 'b' == 'c':
    print(True)


# create a list of 5 numbers starting with 0
# create a tuple with the same information
# change the value of the last index of the tuple

num_list = [0, 1, 2, 3, 4]
num_tuple = (0, 1, 2, 3, 4)

# num_tuple[4] = 6  does not work, tuples are immutable
