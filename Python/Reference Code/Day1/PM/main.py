# Python Day 1 - PM - Conditional Statements

# Formatting Variables
format_output = "\033[47m\033[30m"
format_reset = "\033[0m"

# Formatted Message - Signify Start of Output
print(f"{format_output}---START---{format_reset}")

# ! Operators:
# * Before we look at some examples we need to be aware of operators
# * Again the concept is the same as we have seen in JavaScript
# * Most operators in Python are syntactically similar to JavaScript

# ! We have 4 main types of operator to consider:
# * Mathematical Operators - (+, -, *, / etc...)
# * Assignement Opertators - (=, +=, -= etc...)
# * Comparison Operators - (==, !=, >, <, >=, <=)
# * Logical Operators - (and, or, not, |)

# ! If Statement:
# * As we have seen previously, an If Statement executes a block of code if a condition is met

# * Example: An If Statement to check if a number is greater than 100

# ! Syntax: Very Similar to JavaScript
# * No (parentheses) around our condition
# * Colon ':' after our condition
# * Body of statement is indented rather than wrapped in {curly's}

# ! Indentation: is VERY important in Python
# * Think of it the same as {curly's} around a code block
# * It indicates that the code belongs together
num = 99

# if num > 100:
#     print(f"{num} is greater than 100")
#     print("I am also going to run")

# ! If Else Statement:
# ? If we wanted to an 'else' block to our example how would we do it?

# ! Remember indentation - 'else' should be on the same level as 'if'
# * Colon ':' after our 'else'
# * Followed by our indented 'else' block

num = 200
if num > 100:
    print(f"{num} is greater than 100")
else:
    print(f"{num} is less than 100")

# ! If Elif Else Statement:
# * Working with an 'else if' block in Python has one main difference to note
# * Rather than adding an 'else if' block the syntax is 'elif' to reduce characters

# * Example: Check if number is between 100 and 1000

# ! Remember indentation - 'elif' should be on the same level as 'if' and 'else'
# * Colon ':' after our 'elif' condition
# * Followed by our indented 'elif' block
num = 99
if num > 1000: 
    print(f"{num} is greater than 1000")
elif num > 100:
    print(f"{num} is between 100 and 1000")
else:
    print(f"{num} is less than 100")

# * Logical "and"

number = 9

if number >= 10 and number <= 20:
    print(f"{number} is between 10 and 20")
else:
    print(f"{number} is NOT between 10 and 20")

# * Logical "or"

number = 20
if number < 5 or number > 15:
    print(f"{number} is less than 5 or greater than 15")
else:
    print(f"{number} is bewtween 5 and 15")

# * Nested If Statement
number = 0

if number >= 0:
    if number == 0:
        print("The number is 0.")
    else:
        print("The number is positive.")
else:
    print("The number is negative.")


# * Match Case Statment
# grade = int(input("Enter your grade(0-100): "))
# match grade:
#     case grade if grade >= 90:
#         print("You got an A!")
#     case grade if grade >= 80:
#         print("You got a B!")
#     case grade if grade >= 70:
#         print("You got a C!")
#     case grade if grade >= 60:
#         print("You got a D!")
#     case _:
#         print("You got an F!")

# * If Else Variation
grade = int(input("Enter your grade(0-100): "))
if grade >= 90:
    print("You got an A!")
elif grade >= 80:
    print("You got a B!")
elif grade >= 70:
    print("You got a C!")
elif grade >= 60:
    print("You got a D!")
else:
    print("You got an F!")














# Formatted Message - Signify Start of Output
print(f"{format_output}---END---{format_reset}")
