# Control structures in python

# if statement
x = 10

# booleans
# True, False
# 1, 0

our_expression = True
our_new_expression = x > 5

if our_expression:
    print("our expression is true")

if our_new_expression:
    print("x is greater than 5")

# if else statement

if x > 5:
    print("x is greater than 5")
elif x == 5:
    print("x is less than or equal to 5")
else:
    print("x is less than 5")

# end of if block


# for loop

array = [1, 2, 3, 4, 5]
for i in range(len(array)):
    print(array[i])

while x > 0:
    print(x)
    x -= 1

# end of while loop

def function1(x=0):
    print(x)

function1(10)

class Dog():
    def __init__(self, name):
        self.name = name

    def bark(self):
        print("Woof woof")

    def walk(self):
        print("Walking")

    def roll_over(self):
        print("Rolling over")
