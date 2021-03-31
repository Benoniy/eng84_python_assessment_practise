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


# Create a dictionary with two key value pairs
# first pair - "name": "james"
# second pair - "age": 21
# print the value of each of the keys

dict_example = {"name": "James",
                "age": 21}

print(dict_example["name"], dict_example["age"])


# Create a class called Isobel, initialize it
# It should take two arguments
# create an object of that class


class Isobel:
    def __init__(self, mood, sleepy):
        self.mood = mood
        self.sleepy = sleepy


isobel = Isobel("yes", False)
print(isobel.mood)
print(isobel.sleepy)

# create another Isobel object and print the attributes
student = Isobel("happy", True)
print(student.mood)
print(student.sleepy)


# Declare a set with values from 1-4

num_set = {"1", "2", "3", "4"}
# The differance between sets and other collections are that they are unordered
print(num_set)
print(num_set)

# Add something to the set
num_set.add("10")
print(num_set)


# task 8 - Create a method that takes one string argument
# The arg should be a name
# If the name equals Dunni return true else false

def is_dunni(name):
    if name.lower() == "dunni":
        return True
    return False


print(is_dunni("Dunni"))


# task 8 - Create a class called Human with one method called breathe
# breathe should return "breathing"
# create a second class Student that inherits from human
# create an object of student and call the inherited breathe method

class Human:
    def breathe(self):
        return "breathing"


class Student(Human):
    pass


student1 = Student()
print(student1.breathe())
