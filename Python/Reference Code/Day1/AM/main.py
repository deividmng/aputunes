# Python Day 1 - AM - Introduction

# Formatting Variables
format_output = "\033[47m\033[30m"
format_reset = "\033[0m"

# Formatted Message - Signify Start of Output
print(f"{format_output}---START---{format_reset}")

# ! 'print()' - Is the equivalent to console.log in JavaScript
# * This will print the string "Hello World" to the console

print("Hello World")

# ? How do we run the file to see our output? 
# ! We have 2 options
# * Press the play button in the top right of our VS Code workspace
#  or
# * Open our terminal in the CORRECT DIRECTORY and run: "python filename.py"

# ! Similar to console.log(), print() will evaluate the argument and print the result
# * For Example: We can complete mathematical operations

print(2+2)

# * We can also seperate arguments with a comma

print("The answer to 2+2 is:", 2+2)

# ? What happens if we try to add quote marks to a string in our print function? 
# * For example if you wanted to write "My name is "name""

# print("My name is "Christian"")

# * Notice we encounter an error - Python tries to help but isn't correct
# ! In order to write "illegal" characters we need to use an "escape character"
# * Backslash + Quote '\"' allows us to escape our string and use our quote marks

print("My name is \"Christian\"")

# ? Thinking back to JavaScript do we remember what a variable is?
# * Aside from syntax there is no difference - Just a label / box for our data

# ! Python Varaiables are delcared without a keyword - no 'let'/'const' equivalent

greeting = "Good Morning!"

# * Meaning we can now access our string by referencing our variable

print(greeting)

# ? How do you think we would assign a new value to the variable? 

greeting = "Good Afternoon!"
print(greeting)

# ? As there is no keyword you may be wondering how we declare constants? 
# ! In Python constants are declared by a practice and are not a seperate type of variable
# * To indicate a constant we would declare a variable in capital letters

NAME = "Christian"
print(NAME)

# ! NOTE the value can still be reassigned
# * However the rule is if the variable is capitalised DO NOT reassign value

NAME = "New Value (EXAMPLE ONLY: Never update a capitalised variable - CONSTANT)"
print(NAME)

# ! snake_case - Previously when working with JavaScript we have used camelCase
# ! to differentiate between the languages we will be using snake_case instead
# * Seperate variables with more than 1 word in their name with underscore
# * This follows python convention and also helps you not confuse PY with JS

multi_word_variable = "snake_case"
print(multi_word_variable)

# ! We will introduce Python specific data types later this week
# * For now lets look at ones we are familiar with

# * String - Series of characters contained in quote marks - single '' or double ""
string = "Characters between quote marks"

# * Integer - A whole number
integer = 5

# * Float - Decimal place number
float = 1.5

# * Boolean - True or False
# ! Must start with a capital T or F
boolean = True

# ! By using 'type()' we can check the data type

print(type(string))
print(type(integer))
print(type(float))
print(type(boolean))

# ! fSTRING - Think of Template Literals/Strings in JavaScript
# * By passing 'f' before our string we are able to inject variable values
# * Simply wrap the variable in curlys '{}' and the value will take its place

day = "Monday"
print(f"Today is {day}")



# Python - Day 1 (AM) - Tasks:

# 1: Create a variable "name" and assign a string containing your first name as its value, then print the variable to the console.

# 2: Update the value of your "name" variable to contain your full name. Create 2 more variables named "age" and "city" and assign them your age as a number and your city of residence as a string. Finally, print an f{string} to the console of a sentence containing the name, age and city information. eg: "My name is Dave, I'm 25 and live in London"

# 3: Research the 'input()' function and utilise it to store a users name in a "user_name" variable.

# 4: Utilise 'input()' to obtain a users age and city, then print an f{string} containing the user data, similar to Task 2.

# Stretch Tasks: 

# 1: Use input to obtain 2 numbers from a user, once obtained add the 2 numbers provided together and print the result to the console. 

# (TIP: Think about data types and type conversion...)

# 2: Research Python's built in methods and string methods. Experiment with them to familiarise yourself with what Python can do natively.

# Built-In Methods (Functions): 
# https://www.programiz.com/python-programming/methods/built-in

# String Methods (Functions): 
# https://www.programiz.com/python-programming/methods/string

# ! Task 1: 
task_name = "Christian"
print(task_name)

# ! Task 2: 
task_age, task_city = 32, "Manchester"
print(f"My name is {task_name}, I am {task_age} years old and live in {task_city}.")

# ! Task 3:
# user_name = input("What is your name? ")
# print(user_name)

# ! Task 4:
# user_age = input("How old are you? ")
# user_city = input("What city do you live in? ")
# print(f"The users name is {user_name}, they are {user_age} years old and live in {user_city}.")

# ! Task 5: 
num1 = int(input("Number 1: "))
num2 = int(input("Number 2: "))
result = num1 + num2
print(f"{num1} + {num2} = {result}")




















# Formatted Message - Signify End of Output
print(f"{format_output}---END---{format_reset}")