# 1. Numeric Types

# int: Represents whole numbers.
age = 25  # Integer
# float: Represents decimal numbers.
height = 5.9  # Float
# complex: Represents complex numbers
z = 3 + 4j  # Complex number


# 2. String Type
# str: Represents sequences of characters
name = "Alice"  # String


# 3. Boolean Type
# bool: Represents True or False values.
is_student = True  # Boolean


# 4. Sequence Types

# list: An ordered collection of items (mutable).
fruits = ["apple", "banana", "cherry"]  # List
# tuple: An ordered collection of items (immutable).
coordinates = (10.0, 20.0)  # Tuple


# 5. Set Type
# set: An unordered collection of unique items.
unique_numbers = {1, 2, 3, 3}  # Set


# 6. Mapping Type
# dict: A collection of key-value pairs.
student = {"name": "Alice", "age": 25}  # Dictionary


# 7. None Type
# NoneType: Represents the absence of a value.
value = None  # None








# Explained in Bengali for better understanding

# Python-এ কয়েকটি Built-in Data Types আছে। এগুলোর মধ্যে সবচেয়ে সাধারণ এবং বেশি ব্যবহৃত Data Types হলো:
""" 
1. Numeric Types
int: পূর্ণসংখ্যা (Integer)
float: ভগ্নাংশ সংখ্যা (Floating point number)
complex: জটিল সংখ্যা (Complex number)
উদাহরণ:
"""
# int
num1 = 10
print(type(num1))  # Output: <class 'int'>

# float
num2 = 10.5
print(type(num2))  # Output: <class 'float'>

# complex
num3 = 3 + 4j
print(type(num3))  # Output: <class 'complex'>



""" 
2. Sequence Types
list: একটি Mutable (পরিবর্তনশীল) সংগ্রহ
tuple: একটি Immutable (অপরিবর্তনশীল) সংগ্রহ
range: একটি সংখ্যা সীমার মধ্যে সংখ্যা তৈরি করে
উদাহরণ:
"""

# list
my_list = [1, 2, 3, 4]
print(type(my_list))  # Output: <class 'list'>

# tuple
my_tuple = (1, 2, 3, 4)
print(type(my_tuple))  # Output: <class 'tuple'>

# range
my_range = range(5)
print(type(my_range))  # Output: <class 'range'>


""" 
3. Text Type
str: স্ট্রিং (পাঠ্য)
উদাহরণ:
"""

my_string = "Hello, World!"
print(type(my_string))  # Output: <class 'str'>

""" 
4. Mapping Type
dict: একটি অর্ডারড সংগ্রহ যেটি কী-মান (key-value) জোড়া হিসেবে কাজ করে
উদাহরণ:
"""

my_dict = {"name": "Alice", "age": 25}
print(type(my_dict))  # Output: <class 'dict'>

""" 
5. Set Types
set: একটি Mutable সংগ্রহ যা ডুপ্লিকেট মানগুলো সরিয়ে দেয়
frozenset: একটি Immutable সেট
উদাহরণ:
"""

# set
my_set = {1, 2, 3}
print(type(my_set))  # Output: <class 'set'>

# frozenset
my_frozenset = frozenset([1, 2, 3])
print(type(my_frozenset))  # Output: <class 'frozenset'>

""" 
6. Boolean Type
bool: সত্য (True) বা মিথ্যা (False) মান
উদাহরণ:
"""

my_bool = True
print(type(my_bool))  # Output: <class 'bool'>

""" 
7. None Type
NoneType: কিছু নেই বা অপরিবর্তনশীল মান
উদাহরণ:
"""

my_none = None
print(type(my_none))  # Output: <class 'NoneType'>

""" 
সংক্ষেপে
Python-এ এই সব Built-in Data Types-এ বিভিন্ন ধরনের তথ্য সংরক্ষণ এবং প্রক্রিয়াকরণের সুবিধা দেয়। প্রতিটি Data Type-এ বিভিন্ন কার্যকারিতা এবং বৈশিষ্ট্য রয়েছে, যা প্রোগ্রামিংয়ে কাজ করার সময় খুবই উপকারী।
 """