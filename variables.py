# Variables
name = 'salman'
age = 24

a = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
b = 12345678910
""" 
print('a is of type', type(a))
print('b is of type', type(b))
"""
c = 4       # c is of type int
c = "Sally" # c is now of type string
# print(c)

x = str(3)    # x will be '3'
y = int(3)    # y will be 3
z = float(3)  # z will be 3.0
# print("Number:", x, y, z)

# Python - Variable Names
myvar = "John"
my_var = "John"
_my_var = "John"
myVar = "John"
MYVAR = "John"
myvar2 = "John"

# Python Variables - Assign Multiple Values
orange, banana, cherry = "Orange", "Banana", "Cherry"
# print(orange)
# print(banana)
# print(cherry)

# One Value to Multiple Variables
orange_x = orange_y = orange_z = "Orange"
# print(orange_x, orange_y, orange_z)

# Unpack a Collection
fruits = ["apple", "banana", "cherry"]
unpack_x, unpack_y, unpack_z = fruits
# print(unpack_x, unpack_y, unpack_z)

# Python - Global Variables
global_x = "awesome"
def myfunc():
    global_x = "fantastic"
    print("Python is " + global_x)

myfunc()

# print("Python is " + global_x)

def myfunc2():
    global global_x2
    global_x2 = "fantastic"

myfunc2()

# print("Python is " + global_x2)

global_x3 = "awesome"

def myfunc():
    global global_x3
    global_x3 = "fantastic"

myfunc()

print("Python is " + global_x3)
