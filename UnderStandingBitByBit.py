# Python backends are often paired with databases like PostgreSQL, MySQL, or SQLite, and 
# can handle tasks like serving APIs, interacting with databases, and processing data. 
# Python's extensive libraries and support for various protocols and technologies make it a 
# strong choice for backend development.


# Run Button --------------------------------------------------------
Shift + F10 to Run 

# print statement ---------------------------------------------------
print("Amit") # Here the print is case Sensitive.
                      # "" This is called Strings.
                      # In python we dont need semicolon(;).

print(25) # This is an Integer.

# Print Multiple lines with single print statement ------------------
print("Hello world!\nThis is a new line.") # Multiple lines.
                                           # gaps between lines would not effect. 

# Concatenation (Combine diffrent Strings) -----------------------------
print("Hello world!" + " This is a new line.") # U can add space inside Strings.
print("Hello world!" + " " + "This is a new line.") # Adding Space Between with Strings.

# Python is Sensitive -----------------------------------------------
1) Case Sensitive # P p.
2) Space Sensitive # In the beggingin of lines there should not be any expty sapces.
3) 

# input() function ----------------------------------------------------
input("what is your name?") # U can give input to the Computer.

# Storing and Using the input -----------------------------------------
userName = input("what is your name? ") # Here U dont need to use var to delcaire a variable.
print("Hello " + userName + "!") # Adding exclamation mark(!) with strings and concatination.

# You can write this in one line.
print("Hello " + input("what is your name?") + "!") 

# Variables ----------------------------------------------------------
name = "Amit"
print(name)

# Parameter and Argument ---------------------------------------------
something = 123 # Parameter = Argument
                # Data = Value of the Data
                # Variable = Value of the Variable

# Print number as value of a variable.
age = 24
print(age)

# age Using as input.
age = input("What is your age")
print(int(age)) # Converting the age String into intiger.

# Using Strings and Concatination to give a Sentance.
age = input("What is your age ")
age = int(age)
print("You are " + str(age) + " years old.")

# Numbers inside Strings("") are not treated as Numbers they are treated as Strings.
print("1234" + "4567") # This will print 12344567
print(1234 + 4567) # This is how you can calculate Numbers.
                   # 5801
                   # Numbers are Called Integers.

*** # Applicable varible names -----------------------------------------
1) myvar = "Amit"
2) myVar = "Amit"
3) my_var = "Amit"
4) my123 = "Amit"
5) my1name = "Amit" 

# Use Small Letters for Varialbes in the beggining.

# Letters and Numbers as Value of a Variable.
name = "Anjela" # You need Strings for letters to have value of a variable.
age = 24 # You dont need Strings for Numbers.

# Camel Casing --------------------------------------------------------
myName # The first letter is Small and the next word first letter is Capital.

# Changing variables values -------------------------------------------
a = "3"
b = "8"
c = a
a = b
b = c
print(a, b)

# Can not use as varible ------------------------------------------------
1) my name # we cant use space in beteewn.
        # we can use underscore my_name
2) 20name # we cant use numbers in the beggining of the variable.
       # we can use numbers in the end of the variable name20
3) my-var # we cant use dash(-) as variables.
4) 123 # we cant use nubmers as variables.
5) print, input # we cant use print or input as variable coz they are functions.
7) NameError #when your variable name does not match to each other.

# NameError ----------------------------------------------------------
name = "Amit"
print(Name) # This is a NameError 

# TypeError ----------------------------------------------------------
# The len() function in Python is used to get the length of sequences like strings, 
# lists, tuples, and dictionaries, but not integers.

# In Python, you can't directly concatenate a string with an integer. You need to 
# convert the integer length to a string before concatenating it with other strings.
# The Return Value of len Function is an Integer or Number and You need to convert it 
# into String to Concatinate with Other Strings.

# The input function value is also stored as strings.

# This will Create a TypeError.
length = len(12345) # This will Create a TypeError.        
print("Your Number is " + length + " Charecters long.") # This will Create a TypeError.

# Converting the Number(12345) Integer into String.
length = len(str(12345))
print(length)

# Converting the len(5) integer into String.
length = len("Hello")
print("Hello is " + str(length) + " Characters long.")

# In this The value is taken as String, So this will not give any Error.
number = input("Type your data ")
length = len(number)
print(length)

# Converting the Integer length into String to Concatinate with Strings. 
number = input("Type your Phone Number here: ")
length = len(str(number)) # This gives the length of the number.
print("Your phone Number is " + str(length) + " characters long.")

# ValueError -------------------------------------------------------------
1) print(int("abc")) # We can't Convert abc into Number.
                     # This will Create a ValueError.
2) height = input("Enter your height in m: ") # The input() function in Python returns 
                                              # data as a string by default. 
   height = float(input("Enter your height in m: ")) # so you'll need to convert these 
   # inputs into floating number or integer to perform arithmetic operations.

# To check if the user input is a digit(integer)
if not user_input.isdigit(): 

# Indentation error ------------------------------------------------------
# 4 spaces or one tab at the beggining of a codeblock is important to make it work. 
# the space at the beginning of a line
# Indentation errors are common in languages like Python, where proper indentation is 
# crucial for defining blocks of code.
# Indentation is so inportant for python if else code blocks.. Look out for them.

# IndexError or TracebackError--------------------------------------------
# IndexError: Raised when you try to access an index that is out of range.
# When you try to access an item that is not in the range of the List, 
# you will get an IndexError.
friends = ["Amit", "Parag", "Harsha", "Aparna", "Princy", "Zarin"]

no_of_friends = len(friends) # 50 -> 49
print(friends[no_of_friends - 1]) # This is how you can solve this error.
                                  # By giving -1 you can counter the 0.

# 2) Look for -> Rock, Paper, Scissors Excercise  

*** # Errors --------------------------------------------------------------
1) NameError
2) TypeError
3) ValueError 
4) IndentationError
5) IndexError or TracebackError

# Error Handling # try-except blocks ----------------------------------------
# try, except, finally, and else (Exception Handling) -----------------------
# These are used for handling exceptions and errors that might occur during 
# the execution of your code.
try:
    result = 10 / 0
except ZeroDivisionError:
    print("Cannot divide by zero")
finally:
    print("This will always execute")

# IndexError and ValueError Handling ----------------------------------------
# Not perfect may need modification if extent to broad project.
# 1) IndexError or TracebackError
# 2) ValueError
rockPaperScissors = ["Rock", "Paper", "Scissors"]

try:
    myChoice = int(input("What is your choice? "
                         "\nType 0 for Rock, 1 for Paper, or 2 for Scissors: "))
    myChoice = rockPaperScissors[myChoice]
    print(f"You chose: {myChoice}")
except IndexError:
    print("Invalid choice! Please enter 0, 1, or 2.")
except ValueError:
    print("Invalid input! Please enter a number (0, 1, or 2).")

*** # keywords and constructs ------------------------------------------------
1) while Loop #  as long as a given condition is True
2) if, elif, else: # conditional execution 
3) break # statement 
4) continue # statement 
5) pass # statement
6) range() # function 
7) enumerate() # function
8) zip() # function
9) max() # function
10) sum() # function
9) else with Loops # unless the loop is terminated.
10) try, except, finally, and else # (Exception Handling)

# while Loop -----------------------------------------------------------------
# repeatedly executes a block of code as long as a given condition is True.
count = 0
while count < 5:
    print(count)
    count += 1

# Output: 1, 2, 3, 4

# if, elif, else: conditional execution --------------------------------------
# These are used for conditional execution, allowing you to execute certain 
# blocks of code based on specific conditions.
x = 10

if x > 10:
    print("x is greater than 10")
elif x == 10:
    print("x is equal to 10")
else:
    print("x is less than 10")

# break statement -----------------------------------------------------------
# The break statement is used to exit a loop prematurely, before it has 
# iterated over all items.
for i in range(10):
    if i == 5:
        break
    print(i)

# Output:
# 0
# 1
# 2
# 3
# 4

# continue statement -------------------------------------------------------
# The continue statement skips the rest of the code inside the loop for 
# the current iteration and jumps to the next iteration of the loop.
for i in range(5):
    if i == 2:
        continue
    print(i)

# Output: 
# 0
# 1
# 3
# 4

# pass statement ------------------------------------------------------------
# The pass statement is a placeholder. It does nothing and is often used when 
# a statement is required syntactically but you don’t want to execute any code.
for i in range(5):
    if i == 2:
        pass  # Do nothing
    else:
        print(i)

# Output: 
# 0
# 1
# 3
# 4

# range() function ---------------------------------------------------------
for i in range(1, 11):
    print(i)

# Output 1, 2, 3, 4, 5, 6, 7, 8, 9, 10

# range step by 2 
for i in range(2, 10, 2):
    print(i)

# Output 2, 4, 6, 8

# enumerate() function ------------------------------------------------------
# The enumerate() function adds a counter to an iterable and returns it as 
# an enumerate object, which can then be used in a for loop.
fruits = ["apple", "banana", "cherry"]
for index, fruit in enumerate(fruits):
    print(index, fruit)

# Output: 
# 0 apple
# 1 banana
# 2 cherry

# zip() function ------------------------------------------------------------
# The zip() function combines two or more iterables (like lists) into tuples, 
# pairing the elements of the iterables.
names = ["Amit", "Bala", "Chitra"]
ages = [25, 30, 22]

for name, age in zip(names, ages):
    print(f"{name} is {age} years old")

# Output:
# Amit is 25 years old
# Bala is 30 years old
# Chitra is 22 years old

# max() function -------------------------------------------------------------
student_scores = [150, 142, 185, 120, 171, 184, 149, 24, 59, 68, 199, 78, 65, 89, 86, 55, 91, 64, 89]
print(max(student_scores))

# sum() function -------------------------------------------------------------
student_scores = [150, 142, 185, 120, 171, 184, 149, 24, 59, 68, 199, 78, 65, 89, 86, 55, 91, 64, 89]
print(sum(student_scores))

# else with Loops ------------------------------------------------------------
# The else clause in a for or while loop is executed after the loop finishes 
# its iterations, unless the loop is terminated by a break statement.
for i in range(5):
    print(i)
else:
    print("Loop finished without break")

# try, except, finally, and else (Exception Handling) -----------------------
# These are used for handling exceptions and errors that might occur during 
# the execution of your code.
try:
    result = 10 / 0
except ZeroDivisionError:
    print("Cannot divide by zero")
finally:
    print("This will always execute")

# Functions -----------------------------------------------------------------
1) print() # Prints Out the Data.
2) input() # Data Input from the User. 
3) len() # Length of a Value.
4) type() # To Check the Data Type. 
5) str() # Converting Integer into String.
6) float() # Converting Strings into Floating Number.
7) .lower() # Converts upper case input or value of a variable into lower case.
8) round(bmi, 2) # The round() function in Python is used to round a floating-point 
                 # number to a specified number of decimal places.
9) random.randint(0, 1) # is a function from Python’s random module that returns 
                  # a random integer between two specified values, inclusive.
10) random.random() # To generate random floating number.
11) random.uniform(0, 10) # To generate random floating point number.
13) random.choice() 
12) range() # is often used in for loops to generate a sequence of numbers.
13) enumerate() 
14) zip() 
15) sum() # mathematical operations.
          # function adds up all the elements in an iterable (like a list) 
          # and returns the total.
16) max() # mathematical operations.
          # function returns the largest element from an iterable or the 
          # largest of two or more arguments.

# print() Function ------------------------------------------------------
print("Hello world!")

# input() Function ------------------------------------------------------
print(input("What is your name? "))

# len() Function --------------------------------------------------------
# The len() function in Python is used to get the length of sequences like strings, 
# lists, tuples, and dictionaries,
print(len("Amit"))
print(len(str(12345)))
print(len(input("What is your name?")))

# type Function ---------------------------------------------------------
1) type("Hello") # This will return the data type as String.
2) type(1234) # This will return the data type as Integer.

# Doint this with variable.
data = input("Type your data: ")
print(type(data))

# The four Data Types.
print(type("Amit")) # String
print(type(12345)) # Integer
print(type(3.14159)) # Float
print(type(2 == 2)) # True or False # Boolean

# Python Primitive Data Type ---------------------------------------------
1) String # "Amit"
2) Integer # 12345
3) Float # 3.14159
4) Boolean # (2 == 2) True or False

*** # Converting Data type -----------------------------------------------
1) str() # Converting into String.
2) int() # Converting into Integer.
3) float() # Converting into Float.
4) bool() # Converting into Bool.

# Converting Integer into String.
print(str(4567)) 
# Converting String into Integer(Number).
print(int("123") + int("456"))
# Converting string into float(Number with decimal places).
print(float("1.76"))

# string -----------------------------------------------------------------
string = "Anjela" # Strings are Charecters or letters.

# integer ----------------------------------------------------------------
integer = 24 # integers are numbers.

# float ------------------------------------------------------------------
# In Python float is a built-in data type used to represent floating-point 
# numbers, which are numbers with a decimal point. 
# Float = Floating Point Number Or Numbers with Decimal places.
pi = 3.14159 # This is Float Data Type.

# Boolean ----------------------------------------------------------------
# This is Case Sensitive with a Capital "T" and Capital "F" in the begging.
True or False

1) Comparison Operators:
                        1) == # Equal to
                        2) != # Not Equal to 
                        3) > # More than
                        4) < # Less than
                        5) >= # More than Equal to  
                        6) <= # Less than Equal to 

2) Logical operators:
                   and_operation = True and False  # False # and
                   or_operation = True or False    # True # or
                   not_operation = not True        # False # not

# and operator.
a = 12
if a > 10 and a < 13:
    print("You are mine")
else:
    print("You are not mine")

# or operator.
a = 12
if a > 10 or a < 13:
    print("You are mine")
else:
    print("You are not mine")

# not operator.
a = 12
if a > 10 not a < 13:
    print("You are mine")
else:
    print("You are not mine")
    
# SubScripting ------------------------------------------------------------
# Specifically calling a part of string 
# Space and UnderScore are Countable here.
special = "Amit"[0] # The output will be A.
print(special)

print("Amit Cho"[5]) # The output is C.
                     # The empty Space is Countable Here.

print("Amit_Cho"[4]) # This will Produc _(UnderScore).
                     # The UndeScore is Countable Here.

# You can use -2 to get the 2nd Charecter from the last 
print("Amit"[-2]) # The output will be i.

# Implicit Typecasting ------------------------------------------------------
print(6 / 3) # This will give you 2.0 Which is a flaot Number .
             # Giving float number in division is default Python behavior.
print( 6 // 3) # To avoid floating number in division you can use Double slash.
print(2 ** 3) # 2 to the power of 3 will give you 8.

# Assignment Operator -------------------------------------------------------
score = 0
score += 1 # This will give 1.
score -= 1 # This will give -1.
score *= 1 # This will give 0.
score /= 1 # This will give 0.
print(score) # The Output will be 1.

# Giving value to variable --------------------------------------------------
bill = 3
bill = bill + bill # Oputput: 6

# Better Visualization.
# Using uncerScore as Commas for better visualization of big integer Numbers in Python.
number = 8617_6290_42 # Better Visualization.

bill += 3  # This is a shorthand of bill = bill + 3 

# f-string in Python -----------------------------------------------------------
f in Python # F-strings are a way to embed expressions inside string 
            # literals, using curly braces {}. 
print(f"Your age is {age}") # They are a convenient and efficient 
                            # way to format strings.
                            # Thye dont require to convert integer into string for 
                            # concatination.
                            # The f-string automatically handles the type conversion.
# Example of using F string.
age = 25
name = "Amit"

message = f"My name is {name} and I am {age} years old."
print(message)

# ('')Single quotation and ("")Double quotation and (\)backshash ---------------
gender = input('What\'s you\'re gender? "Boy" or a "Girl"') # using (\)backslash to
                    # escape the next symbol so don't interpert it as code. concatination.
                    # Or you can use " ''  " single coute in duble coute
# .lower() Function ------------------------------------------------------------
.lower() # Converts upper case input or value of a variable into lower case.

lower = input("Type Upper case letters to convert it into lower case: ").lower()   
print(lower)

Output: input given by the user
       
# round() function --------------------------------------------------------------
print(round(bmi, 2)) # In Python, the round() function is used to round a floating-point
                     #  number to a specified number of decimal places. It can also round 
                     # a number to the nearest integer if no decimal places are specified.
                     # 2 will give us the value of 2 decimal places. 

# random.randint(0, 1) ---------------------------------------------------------
# Pseudorandom random number generator (random number within range).
# Mersenne Twister https://en.wikipedia.org/wiki/Mersenne_Twister
# The random module in Python. https://docs.python.org/3/library/random.html
# Pseudorandom number generators.
import random
randomInt = random.randint(0, 1) # is a function from Python’s random module that returns
print(random)               # a random integer between two specified values, inclusive.

# Python API ----------------------------------------------------------------
import my_module # my_module.py
 
print(my_module.pi)

# another way to import specific data --------------------------------------
from hangman_words import word_lists 

chosen_word = random.choice(word_lists)

# random.random() -------------------------------------------------------------
# random floating number generator.
random.random() # To generate random floating number.

random_number_0_to_1 = random.random() * 10 # will give you floating number from 0 to 10
print(random_number_0_to_1)                 # but the output never will be 10

# random.uniform() ------------------------------------------------------------
# random floating point number generator.
random_float = random.uniform(1, 10) # Here the output can get to 10.
print(random_float)

# random.choice() ------------------------------------------------------------
# selects random items from the list.
friends = ["Amit", "Parag", "Harsha", "Aparna", "Princy", "Zarin"]

import random
random_Name = random.choice(friends)
print(random_Name)

# Other way to select items in the list.
friends = ["Amit", "Parag", "Harsha", "Aparna", "Princy", "Zarin"]

import random
random_index = random.randint(0, 5)
print(friends[random_index])

# How to make your own module ---------------------------------------------
1) my_module.py -> pi = 3.1415 # Create a file my_module.py and white the code inside.
2) import my_module # import the module file in your working file to use it.
3) print(my_module.pi) # use the component you want to use.

*** # Math Operators ------------------------------------------------------
# 3 + 5 [ Addition ]
# 7 - 4 [ Subtraction ]
# 3 * 2 [ Multiplication ]
# 6 / 3 [ Division ]
# 2 ** 3 [ Exponents ]
# 9 % 6 [ Modulo ] this gives you the remainder after division. Which is 3.0

# PEMDAS
# Parentheses ()
# Exponents **
# Multiplication *
# Division /
# Addition +
# Subtraction -

# PEMDAS {PEMDASLR(left to right)} 
# ()
# **    
# * OR /
# + OR -

# >   Greater than
# <   Less than
# >=  Greater than or equal to 
# <=  Less than or equal to
# === is equal to // checks for the data type
# ==  Equal to // does not check for data type (integer or string)
# !=  Not equal to
# &&  (AND) → and
# ||  (OR) → or
# !   (NOT) → not

# * /  most to the left is the one that will be prioritized.
# + -  most to the left is the one that will be prioritized.

# !== operator is a strict inequality operator in JavaScript. It checks whether 
# two values are not equal and also ensures that their types are different. It only 
# returns true if both the value and the type are not the same.

# Using PEMDAS to calculate This.
print(3 * 3 + 3 / 3 - 3)
(3 * 3) + (3 / 3) - 3
(9 + 1) - 3
10 - 3 = 7.0 # Giving float number in division is default Python behavior.

# Changing the Math operator to get 3.
print(3 * (3 + 3) / 3 - 3)
3 * (3 + 3) / 3 - 3
(3 * 6) / 3 - 3
(18 / 3) - 3
6 - 3 = 3.0 # Giving float number in division is default Python behavior.

# built-in functions used to perform basic mathematical operations
1) sum()
numbers = [1, 2, 3, 4, 5]
result = sum(numbers)
print(result)  # Output: 15

2) max()
numbers = [1, 2, 3, 4, 5]
result_with_start = sum(numbers, 10)
print(result_with_start)  # Output: 25

# List data structure ----------------------------------------------------------
# Python Data Structures https://docs.python.org/3/tutorial/datastructures.html
# The items in the list starts from the 0.
states_of_america = ["Delaware", "Pennsylvania"] # This is a list of items.
print(states_of_america[0]) # This will give you Delaware.

# Change value in the list 
# You can use -1 aswell to get the items from the opposite side.
states_of_america[1] = "Pencilvania"
print(states_of_america) # This will udpate Pennsylvania to Pencilvania.

# Add an item to the end of the list.
states_of_america.append("Angelaland")
print(states_of_america)

# Add multiple item at once in the end of the list. 
states_of_america.extend("Anjelaland", "Jack Bauer Land")
print(states_of_america)

# Multiple Nested Lists -------------------------------------------------------
fruits = ["Apple", "Banana", "Cherry", "Avocado", "Strawberries"]
vegetables = ["Spanich", "Kale", "Tomatoes", "Celery", "Potatoes"]

dirty_dozen = [fruits, vegetables]
print(dirty_dozen)

# random.choice() from list of data -------------------------------------------
# selects random items from the list.
friends = ["Amit", "Parag", "Harsha", "Aparna", "Princy", "Zarin"]

import random
random_Name = random.choice(friends)
print(random_Name)

# random.randint() from list of data -----------------------------------------
friends = ["Amit", "Parag", "Harsha", "Aparna", "Princy", "Zarin"]

import random
random_index = random.randint(0, 5)
print(friends[random_index])

# Random Head or Tail using if and else. --------------------------------------
# randint is a function from Python’s random module that generates a random 
# integer within a specified range.
import random 
number = random.randint(0, 1)
if number == 1:
    print("Heads")
else: 
    print("Tails")

# if and else statement ------------------------------------------------------
# Approval for Rollercoaster ride deppending on Height.
print("Welcome to the Rollercoaster!")
height = int(input("What is your height in cm? "))
if height >= 120:
    print("You can ride the Rollercoaster.")
else:
    print("Sorry you have to grow taller before you can ride.")

# Odd or Even Number using if and else. ---------------------------------------
number = int(input("What is the number you want to check? : "))
oddOrEven = number % 2

if oddOrEven == 0:
    print("This is an Even Number")
else:
    print("This is an Odd Number")

# if, elif and else statement ------------------------------------------------
print("Welcome to the BMI Calculator.")
weight = int(input("What is your weight in kg?: "))
height = float(input("What is your height in m?: "))

bmi = weight / (height ** 2)

bmi = round(bmi, 2)

if bmi < 18.5:
    print("Underweight")
elif bmi < 25:
    print("Normal weight")
else: 
    print("Overweight")

# Nested if / else statements ------------------------------------------------
print("Welcome to the Rollercoaster!")
height = int(input("What is your height in cm? "))

if height >= 120:
    age = int(input("What is your age? "))
    if age <= 12:
        print("Please pay $5.")
    elif age <= 18:
        print("Please pay $7")
    else:
        print("Please pay $12.")
else:
    print("Sorry you have to grow taller before you can ride.")

# Multiple if statements ----------------------------------------------------
# Nested Variable inside if else statement ----------------------------------
print("Welcome to the Rollercoaster!")
height = int(input("What is your height in cm? "))
bill = 0

if height >= 120:
    age = int(input("What is your age? "))
    if age <= 12:
        print("Child tickets are $5.")
        bill = 5
    elif age <= 18:
        print("Youth tickets are $7")
        bill = 7
    elif age >= 45 and age <= 55:
        bill = 0
    elif age > 18:
        print("Adult tickets are $12.")
        bill = 12
    wants_photo = input("Do you want to have a photo take? Type y for Yes and n for No. ")
    if wants_photo == "y":
        bill += 3
    print(f"Your final bill is ${bill}")
else:
    print("Sorry you have to grow taller before you can ride.") 

# Nested if, else statements ---------------------------------------------------
# Tresure Hunt Adventure Game --------------------------------------------------
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")
direction = input('Which way you want to go? type "left" or "right": ').lower()
if direction == "left":
    print("you have came to a lake. There is a island in the middle of the lake.")
    swimOrWait = input('Type "swim" to swim across or Type "wait" to wait for a boat: ').lower()
    if swimOrWait == "swim":
        print('You arrived at the island unharmed. There is a house with three doors. '
              'One red, one yellow and one blue.')
        chooseDoor = input('Which door you want to choose? Type "Red", '
                           '"Green" or "Yellow" to Choose a door: ').lower()
        if chooseDoor == "red":
            print("You have burned in hell by entering the Red door.")
            print("Game Over.")
        elif chooseDoor == "green":
            print("A hungry tiger waited for you to enter the green door. Tiger ate you alive, you died.")
            print("Game Over.")
        elif chooseDoor == "yellow":
            print("You have came to a Treasure Box which has all the Gold coins, "
                  "Silver, Ruby and precious jewelry.")
            print("You lived a lavish life.")
        else:
            print('You chose a door that does\'not exist. Game Over.')
    else:
        print("While waiting big anaconda came and swallowed you. You died.")
        print("Game Over.")
else:
    print("By taking right you have come to face a big Bear. The Bear ate you.")
    print("Game Over.")


# for loop --------------------------------------------------------------------
# Here giving a variable name fruit to the every item in the list with very less code.
for item in list of items:
  #Do somenting to each item

# fruit is a temporary variable name that is given to the value of each element in the 
# fruits list during each iteration of the loop.
fruits = ["Apple", "Peach", "Pear"]

for fruit in fruits: # Here fruit is a temporary variable assigned to each item in the list.
    print(fruit)
    print(fruit + "pie")
    print(fruits) # Here indentation is important, when you make the print() statement
                  # inside of for loop the fruits list will be printed multiple times.
                  # as the items in the list.
print(fruits)

# For Loop with Range ---------------------------------------------------------
# The range(1, 101) function generates numbers starting from 1 up to (but not including) 
# 101, so it generates numbers from 1 to 100. The for loop goes through each number in 
# this range.
# step by 3 # for number in range(1, 11, 3):
total = 0
for number in range(1, 101):
    total += number #  after each iteration, total becomes the sum of all numbers 
                    # up to the current number.

print(total) 

# Output:
# Sum = 100 × 101 = 5050
#           2

# for Loop with range() to compound 100 from 1 --------------------------------
addup = 0
for i in range(1, 101):
        addup += i

print(addup)

# Loop with list and if condition ---------------------------------------------
student_scores = [150, 142, 185, 120, 171, 184, 149, 24, 59, 68, 199, 78, 65, 89, 86, 55, 91, 64, 89]

maxScore = 0
for score in student_scores:
    if maxScore < score:
        maxScore = score

print("The maximum score is:", maxScore)

# Loop with list and max() function -------------------------------------------
student_scores = [150, 142, 185, 120, 171, 184, 149, 24, 59, 68, 199, 78, 65, 89, 86, 55, 91, 64, 89]
print(max(student_scores))

# Loop with list and sum() function -------------------------------------------
student_scores = [150, 142, 185, 120, 171, 184, 149, 24, 59, 68, 199, 78, 65, 89, 86, 55, 91, 64, 89]
print(sum(student_scores))

# FizzBuzz with loop, range, list, if, else conditions ------------------------
for eachNumber in range(1, 101):

    if eachNumber % 3 == 0 and eachNumber % 5 == 0:
        print("FizzBuzz")

    elif eachNumber % 3 == 0:
        print("Fizz")

    elif eachNumber % 5 == 0:
        print("Buzz")

    else:
        print(eachNumber)

# Code Blocks, Functions, for loop, While Loop ---------------------------------
# For loop with range and Function. --------------------------------------------
for number in range(6): # initiates jump() function 6 times.
    jump()
    
# While loop with true condition and Function ----------------------------------
number_of_hurdle = 6
while number_of_hurdle > 0: # While the condition is true initiate jump, untill it's false.
    jump()
    number_of_hurdle -= 1

# Reeborg's world while loop with if, else condition----------------------------
while not at_goal():
    if wall_in_front():
        jump()
    else: 
        move()

# While not condition with loop and function ----------------------------------
while not at_goal():
    jump()

# Another way to write this.
while at_goal() != True:
    jump()

# Infinite loop ---------------------------------------------------------------
while 5 > 3:
    jump()

# Defining Python Funciton ----------------------------------------------------
def my_function():
    print("Hello")
    print("Bye") 

my_function()

# Functions with Inputs, Arguments and Parameters -----------------------------
#Functions --------------------------------------------------------------------
def greet():
    print("Hello we wellcome you")
greet() # Calling the function

# Function with Inputs ------------------------------------------------------- 
def greet_with_name(name):
    print(f"How are you doing {name}?")

greet_with_name("Amit")

# Life in weeks Calculator ---------------------------------------------------
def life_in_weeks(your_age):
    year_left = 90 - your_age
    week_left = year_left * 52
    print(f"You have {week_left} weeks left.")

life_in_weeks(25)

# Functions with more than 1 inputs and Positional Arguments -----------------
def greet_with(name, location):
    print(f"Hello {name}, what is it like in {location}?")

greet_with("Amit", "Bardhaman")

# Keyword arguments ----------------------------------------------------------
def my_function(a, b, c):
    print(f"{a} {b} {c}")

my_function(b=3, a=1, c=2) # specifying values 



# async, await, function -----------------------------------------------------
import asyncio

async def fetch_data():
    print("Fetching data...")
    await asyncio.sleep(2)  # Simulates an async operation like a network request
    print("Data fetched")

async def main():
    await fetch_data()

asyncio.run(main())


























*** # Projects --------------------------------------------------------
# Brand Name Generator ------------------------------------------------
print("Welcome to the Band Name Generator.")
city = input("What's the name of your city?\n")
pet = input("What's your pet's name?\n")

print("Your brand name could be: " + city + " " + pet + ".")

# BMI Converter --------------------------------------------------------
print("Welcome to the BMI Converter.")
height = input("enter your height in m: ")
weight = input("enter your weight in kg: ")

bmi = float(weight) / float(height) ** 2

bmi = round(bmi, 2)
print(f"Your BMI is: {bmi}.")

# Tip Calculator -------------------------------------------------------
print("Welcome to the Tip Calculator.")
bill = float(input("What was the total bill?: $"))
tipPercent = int(input("What percentage tip would you like to give? 10 12 15: "))
people = int(input("How many people to split the bill?: "))

tipMultiplier = bill + (bill * tipPercent / 100)
# tipMultiplier = bill * (1 + tipPercent / 100)

pay = tipMultiplier / people
pay = round(pay, 2)
print(f"Each person should pay: {pay}.")

# Rollercoaster Ride Ticket ----------------------------------------------
print("Welcome to the Rollercoaster!")
height = int(input("What is your height in cm? "))

if height >= 120:
    age = int(input("What is your age? "))
    if age <= 12:
        print("Please pay $5.")
    elif age <= 18:
        print("Please pay $7")
    else:
        print("Please pay $12.")
else:
    print("Sorry you have to grow taller before you can ride.")

# BMI Calculator ----------------------------------------------------------
print("Welcome to the BMI Calculator.")
weight = int(input("What is your weight in kg?: "))
height = float(input("What is your height in m?: "))

bmi = weight / (height ** 2)

bmi = round(bmi, 2)

if bmi < 18.5:
    print("Underweight")
elif bmi < 25:
    print("Normal weight")
else: 
    print("Overweight")

# Rollercoster ride with photo take ---------------------------------------
# Free ticket for age 45 to 55.
print("Welcome to the Rollercoaster!")
height = int(input("What is your height in cm? "))
bill = 0

if height >= 120:
    age = int(input("What is your age? "))
    if age <= 12:
        print("Child tickets are $5.")
        bill = 5
    elif age <= 18:
        print("Youth tickets are $7")
        bill = 7
    elif age <= 18:
        print("Adult tickets are $12.")
        bill = 12
    elif age >= 45 and age <= 55:
        bill = 0
        print("Everything is going to be ok. Have a fun ride on us!")
    else:
        bill += 12
    wants_photo = input("Do you want to have a photo take? Type y for Yes and n for No. ")
    if wants_photo == "y":
        bill += 3
    print(f"Your final bill is ${bill}")
else:
    print("Sorry you have to grow taller before you can ride.")


# Delicious Pizza Order -----------------------------------------------------
print("Welcome to Python Pizza Deliveries!")
size = input("What size pizza do you want? S, M or L: ")

bill = 0

if size == "s":
    bill += 15
    pepperoni = input("Do you want pepperoni on your pizza? Y or N: ")
    if pepperoni == "y":
        bill += 2
    extra_cheese = input("Do you want extra cheese? Y or N: ")
    if extra_cheese == "y":
        bill += 1
    print(f"Your final bill is ${bill}")
elif size == "m":
    bill += 20
    pepperoni = input("Do you want pepperoni on your pizza? Y or N: ")
    if pepperoni == "y":
        bill += 3
    extra_cheese = input("Do you want extra cheese? Y or N: ")
    if extra_cheese == "y":
        bill += 1
    print(f"Your final bill is ${bill}")
elif size == "l":
    bill += 25
    pepperoni = input("Do you want pepperoni on your pizza? Y or N: ")
    if pepperoni == "y":
        bill += 3
    extra_cheese = input("Do you want extra cheese? Y or N: ")
    if extra_cheese == "y":
        bill += 1
    print(f"Your final bill is ${bill}")
else:
       print("You have given wrong input. Please try again.")

# Delicious Pizza Order // Her way to do it ----------------------------------
print("Welcome to Python Pizza Deliveries!")
size = input("What size pizza do you want? S, M or L: ")
pepperoni = input("Do you want pepperoni on your pizza? Y or N: ")
extra_cheese = input("Do you want extra cheese? Y or N: ")
bill = 0
if size == "s":
    bill += 15
elif size == "m":
    bill += 20
elif size == "l":
    bill += 25
else:
    print("You have give wrong input. Please try again.")

if pepperoni == "y":
    if size == "s":
       bill += 2
    else:
        bill += 3
if extra_cheese == "y":
    bill += 1

print(f"Your final bill is ${bill}")

# Tresure Hunt Adventure Game --------------------------------------------------
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")
direction = input('Which way you want to go? type "left" or "right": ').lower()
if direction == "left":
    print("you have came to a lake. There is a island in the middle of the lake.")
    swimOrWait = input('Type "swim" to swim across or Type "wait" to wait for a boat: ').lower()
    if swimOrWait == "swim":
        print('You arrived at the island unharmed. There is a house with three doors. '
              'One red, one yellow and one blue.')
        chooseDoor = input('Which door you want to choose? Type "Red", '
                           '"Green" or "Yellow" to Choose a door: ').lower()
        if chooseDoor == "red":
            print("You have burned in hell by entering the Red door.")
            print("Game Over.")
        elif chooseDoor == "green":
            print("A hungry tiger waited for you to enter the green door. Tiger ate you alive, you died.")
            print("Game Over.")
        elif chooseDoor == "yellow":
            print("You have came to a Treasure Box which has all the Gold coins, "
                  "Silver, Ruby and precious jewelry.")
            print("You lived a lavish life.")
        else:
            print('You chose a door that does\'not exist. Game Over.')
    else:
        print("While waiting big anaconda came and swallowed you. You died.")
        print("Game Over.")
else:
    print("By taking right you have come to face a big Bear. The Bear ate you.")
    print("Game Over.")

# Rock, Paper, Scissors ------------------------------------------------------
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
import random
rockPaperScissors = [rock, paper, scissors]

user_input = input("What is your choice? "
                   "\nType 0 for Rock, 1 for Paper, or 2 for Scissors: ")


if not user_input.isdigit():
    print("Invalid input. Please enter a number (0, 1, or 2).")
else:
    myChoice = int(user_input)
    # if myChoice not in [0, 1, 2]:

    if myChoice >= 0 and myChoice <= 2:

        computerChoice = random.randint(0, 2)

        computerChoiceImage = rockPaperScissors[computerChoice]
        print("Computer Choice: ")
        print(computerChoiceImage)

        myChoiceImage = rockPaperScissors[myChoice]
        print("Your Choice")
        print(myChoiceImage)

        if myChoice == 0 and computerChoice == 1:
            print("You lose!")
        elif myChoice == 1 and computerChoice == 0:
            print("You win!")
        elif myChoice == 1 and computerChoice == 2:
            print("You lose!")
        elif myChoice == 2 and computerChoice == 1:
            print("You Win!")
        elif myChoice == 2 and computerChoice == 0:
            print("You lose!")
        elif myChoice == 0 and computerChoice == 2:
            print("You win!")
        elif myChoice == computerChoice:
            print("Match draw!")

    else:
        print("Choice must be 0, 1, or 2.")

# Random Password Generator ------------------------------------------------
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

# print("Welcome to the PyPassword Generator!")
nrLetters = int(input("How many letters would you like in your password? "))
nrNumbers = int(input(f"How many numbers would you like? "))
nrSymbols = int(input(f"How many symbols would you like? "))

import random

password_list = []

for char in range(nrLetters):
    password_list += random.choice(letters)
for char in range(0, nrNumbers):
    password_list += random.choice(numbers)
for char in range(1, nrSymbols + 1):
    password_list += random.choice(symbols)

random.shuffle(password_list)

password = ''
for char in password_list:
    password += char

print(f"Your password is: {password}")

# Random password generator with ChatGPT -------------------------------------
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

# print("Welcome to the PyPassword Generator!")
nrLetters = int(input("How many letters would you like in your password?\n"))
nrNumbers = int(input(f"How many numbers would you like?\n"))
nrSymbols = int(input(f"How many symbols would you like?\n"))

import random
# Create a list to hold the password characters
password_list = []

# Add random letters
for _ in range(nrLetters):
    password_list.append(random.choice(letters))

# Add random numbers
for _ in range(nrNumbers):
    password_list.append(random.choice(numbers))

# Add random symbols
for _ in range(nrSymbols):
    password_list.append(random.choice(symbols))

# Shuffle the password list to randomize the order
random.shuffle(password_list)

# Join the list into a string to form the final password
password = ''.join(password_list)

print(f"Your password is: {password}")

# Reeborg's world Hurdle -----------------------------------------------------
def turn_right():
    turn_left()
    turn_left()
    turn_left()
def turn_around():
    turn_left()
    turn_left()
def jump():
    move()
    turn_left()
    move()
    turn_right()
    move()
    turn_right()
    move()
    turn_left()
   
for number in range(6):
    jump()

# Reeborg's world while loop with condition and function ---------------------
def turn_right():
    turn_left()
    turn_left()
    turn_left()

while front_is_clear():
    move()
while wall_in_front():
    turn_left()
    move()
    turn_right()
    move()
    turn_right()
    move()
    turn_left()
while not at_goal():
    move()


# Hangman Game Project -------------------------------------------------------
import random
import hangman_art

stages = ['''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', '''
  +---+
  |   |
      |
      |
      |
      |
=========
''']
word_list = ["aardvark", "baboon", "camel"]

lives = 6

print(hangman_art.logo)

chosen_word = random.choice(word_list)

placeholder = ""
word_length = len(chosen_word)
for position in range(word_length):
    placeholder += "_"
print("Word to guess: " + placeholder)

game_over = False
correct_letters = []

while not game_over:

    print(f"**************************** {lives}/6 LIVES LEFT****************************")
    guess = input("Guess a letter: ").lower()

    if guess in correct_letters:
        print(f"You've already guessed {guess}")
    display = ""

    for letter in chosen_word:
        if letter == guess:
            display += letter
            correct_letters.append(guess)
        elif letter in correct_letters:
            display += letter
        else:
            display += "_"

    print("Word to guess: " + display)

    if guess not in chosen_word:
        lives -= 1
        print(f"You guessed {guess} that's not in the word. You lose a life")

        if lives == 0:
            game_over = True

            print(f"***********************IT WAS {chosen_word}! YOU LOSE**********************")

    if "_" not in display:
        game_over = True
        print("****************************YOU WIN****************************")

    print(stages[lives])






















# Erorr Handling ----------------------------------------------------------

# Tresure Hunt Adventure Game --------------------------------------------
# 1) Invalid Input handling
# Errors not hadled
# 1) No Handling for Input Type Errors
# 2) No Handling for Edge Cases(empty input)
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")

# Validating the direction input with .lower()
while True:
    direction = input("Which way do you want to go? Type left or right: ").lower()
    if direction in ["left", "right"]:
        break
    else:
        print("Invalid input. Please type 'left' or 'right'.")

if direction == "left":
    print("You have come to a lake.")
    
    # Validating the swimOrWait input with .lower()
    while True:
        swimOrWait = input("Do you want to swim or wait by the lake? Type swim or wait: ").lower()
        if swimOrWait in ["swim", "wait"]:
            break
        else:
            print("Invalid input. Please type 'swim' or 'wait'.")
    
    if swimOrWait == "swim":
        print("You have crossed the lake by swimming.")
    else:
        print("While waiting, a big anaconda came and swallowed you. You died.")
else:
    print("By taking right, you have come to face a big bear. The bear ate you.")
    print("Game Over.")

# Rock, Paper, Scissors ---------------------------------------------------
# 1) IndexError handling
# 2) ValueError handling
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
import random
rockPaperScissors = [rock, paper, scissors]

user_input = input("What is your choice? "
                   "\nType 0 for Rock, 1 for Paper, or 2 for Scissors: ")


if not user_input.isdigit():
    print("Invalid input. Please enter a number (0, 1, or 2).")
else:
    myChoice = int(user_input)
    # if myChoice not in [0, 1, 2]:

    if myChoice >= 0 and myChoice <= 2:

        computerChoice = random.randint(0, 2)

        computerChoiceImage = rockPaperScissors[computerChoice]
        print("Computer Choice: ")
        print(computerChoiceImage)

        myChoiceImage = rockPaperScissors[myChoice]
        print("Your Choice")
        print(myChoiceImage)

        if myChoice == 0 and computerChoice == 1:
            print("You lose!")
        elif myChoice == 1 and computerChoice == 0:
            print("You win!")
        elif myChoice == 1 and computerChoice == 2:
            print("You lose!")
        elif myChoice == 2 and computerChoice == 1:
            print("You Win!")
        elif myChoice == 2 and computerChoice == 0:
            print("You lose!")
        elif myChoice == 0 and computerChoice == 2:
            print("You win!")
        elif myChoice == computerChoice:
            print("Match draw!")

    else:
        print("Choice must be 0, 1, or 2.")





