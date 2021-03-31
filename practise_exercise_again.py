# Task 1 - Create a function called greetings that takes a string argument and returns it
def greetings(name):
    return name


# Testing greeting
print(greetings("Ben"))


# Task 2 - Declare a list of numbers up to 9 then iterate through it and print each entry
number_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
# Loop through and print
for n in number_list:
    print(n)


# Task 3 - Use the or operator to combine two or more conditional statements
if 5 > 6 or 1 <= 2:
    print(True)


# Task 4 - Create a list of 6 numbers starting with 0 and then create an identical tuple
# change the value of the last index of the tuple and the list
tsk4_list = [0, 1, 2, 3, 4, 5]
tsk4_tuple = (0, 1, 2, 3, 4, 5)

tsk4_list[5] = 22
# tsk4_tuple[5] = 22  Tuples are immutable
print(tsk4_list)
print(tsk4_tuple)


# Task 5 - Create a dictionary with two key value pairs
# First pair: "name": "Elon"
# Second pair: "job": "CEO"
# Third pair: "worth": "too much"
# print the key and value pairs
tsk5_dict = {"name": "James",
             "job": "CEO",
             "worth": "too much"}

for key, val in tsk5_dict.items():
    print(key + ":", val)


# Task 6 - Create a class called Ben with an init that takes two arguments,
# create an object of that class and print the values you set in the init
class Ben:
    def __init__(self, age, tired):
        self.age = age
        self.tired = tired


ben = Ben(21, True)
print(ben.age)
print(ben.tired)


# Task 7 - Declare a set with any number of values and then print it two times.
tsk7_set = {"1", "2", "3", "4", "scream"}
# The differance between sets and other collections are that they are unordered
print(tsk7_set)
print(tsk7_set)

# Remove something from the set
tsk7_set.remove("3")
print(tsk7_set)


# Task 8 - Create a method that takes one int argument
# If the int is less than 12 return true else false
def tsk8_greater(num1):
    return num1 < 12


print(tsk8_greater(4))


# Task 9 - Create a class called Lizard with one method called move which should return "walking"
# create a child class Snake that overwrites move so that it returns "slithering"
class Lizard:
    def move(self):
        return "walking"


class Snake(Lizard):
    def move(self):
        return "slithering"


liz = Lizard()
print(liz.move())
adder = Snake()
print(adder.move())


# Task 11 - Create a tuple that stores anything print its type
tsk11_tuple = (1, 20, 13, 47)

print(type(tsk11_tuple))


# Task 12 - create a function called get_percentage
# it should take 2 int arguments and returns the percentage difference between the two
def get_percentage(num1, num2):
    return str((num1 / num2) * 100) + "%"


print(get_percentage(60, 120))


# task 13 - create a function that takes 2 args as int and divide num1 by num2
# return the outcome
# if dividing by 0 throw an error

def true_divide(num1, num2):
    if num2 == 0:
        return ZeroDivisionError
    else:
        return num1 / num2


true_divide(100, 0)


# task 14 - write five odd numbers in a list and then 5 even ones in another list
# iterate through these list and combine and display them in a function


odd_numbers = [1, 3, 5, 7, 9]
even_numbers = [2, 4, 6, 8, 10]


def combine_odd_even(odd_list, even_list):
    new_list = odd_list
    count = 1
    for n in even_list:
        new_list.insert(count, n)
        count += 2

    print(new_list)


combine_odd_even(odd_numbers, even_numbers)


# task 15 - create a dictionary called shopping_list with 3 key value pairs
# "milk": 1
# "yogurt": 1.15
# "ice cream": 2.38
# create a function that takes dictionary as an argument and iterates through the values adding them to a total
# return the total cost

shopping_list = {"milk": 1,
                 "yougurt": 1.15,
                 "ice cream": 2.38}


def calc_list_value(shopping):
    total = 0
    for val in shopping.values():
        total += val
    return round(total, 2)


print("total is", calc_list_value(shopping_list))

