# Python Day 2 - PM - Functions and Modules

# Formatting Variables
format_output = "\033[47m\033[30m"
format_reset = "\033[0m"

# Formatted Message - Signify Start of Output
print(f"{format_output}---START---{format_reset}")

# ! Functions:
# * As discussed, functions are blocks of code that can be reused throughout our program
# * Exactly the same as we have seen with JavaScript but with different syntax.

# * Basic Example (Greeting Function):

def greeting():
    print("Hello World!")

# * We now have our function, but in order for it to run we need to call it

greeting()

# ! Parameters and Arguments:
# ? What are arguments and parameters and how do they differ?

# ! Parameter(s) - Defined with the function, placeholder for data passed to the function
# ! Argument(s) - Passed to the function when calling it, fulfilling the parameter(s)

# * Parameters are defined in the parentheses following our function name
# * Lets look at an example function that defines 'name' as our parameter

def greet_by_name(name):
    print(f"Hello {name}!")

# * If we call this function without passing an argument we get an error

# greet_by_name()

# * We supply the data to our argument in the parentheses of our function call

greet_by_name("John")

# * Our 'greet_by_name' example used 1 parameter, lets look at how we can work with multiple
# * If we define an 'add' function with parameters of 'a' and 'b':

def add(a,b):
    print(a + b)

# * Our params are seperated by commas and we can work with 'a' and 'b' in our function
# * In this example our function will print the sum of the numbers passed as our args

add(3,2)

# ! Default Arguments:
# * Another concept we have seen before in JS, we can set default arguments with functions

def greet_user(message = "Hello", name = "User"):
    print(f"{message} {name}!")

# * Here we have created a 'greet_user' function with defualt args set for our params

greet_user()

# * With no arguments passed, our default arguments are supplied to the function

greet_user("Good Afternoon")

# * By defualt our single argument will be supplied to our first parameter
# * Meaning if we just supply a name to our function we get 'name User'

greet_user("Dave")

# * To get around this we can use a 'keyword argument' and reference the parameter
# * When calling the function we can reference the parameter name and supply a value

greet_user(name = "Dave")

# ! *args - Arbitary Arguments:
# * *args allow a function to take any number of arguments

# * For example lets say we wanted to write a function that calculates the...
# * ...sum of the numbers passed to it, no matter how many numbers are passed

# * When defining our params a pass an asterisk(star) '*' followed by our param name
# * In this case 'nums'
# * Our function then prints the result of the sum function with 'nums' as the arg

def add_numbers(*nums):
    print(sum(nums))

# * Now when we call our function we can pass as many numbers as we like

add_numbers(1,2,3,4,5)

# ? Think about JavaScript functions, if I wanted to do something with the result...
# ? ...of our function other than print it to the console, what would we need to do?

# ! Return Statement
# * To return a value from a function we need to use 'return'
# * This is no different to what we have seen with JavaScript

def multiply(a,b):
    return a * b

print(multiply(5,4))

# * We can also store the result in a variable and print the variable
ten_times_ten = multiply(10,10)

print(ten_times_ten)

# ! Modules
# * As discussed earlier, modules in Python can be used to compartmentalise our code
# * We can create modules of our own but to introduce the concept we will look at...
# * ...an example of a module built-in to Python

# ! 'random' module:
# * To import a module we use the 'import' keyword followed by the module name

import random

# * We can also rename a module on import and provide it a different reference

# import random as r

# * For demo purposes we will stick with 'random'
# * Now we have imported the module we have access to its functions such as random()
# * 'random.random()' will provide us with a random float between 0-1

print(random.random())

# * Similar to 'math.random()' in JS
# * However, if we want to generate an integer between a range it is much simpler
# * We can use 'random.randint(a,b)' and pass the range as the argument

random_num = random.randint(1,100)
print(random_num)


# Python - Day 2 (PM) – Function and Module Tasks:

# 1: Write functions that meet the following criteria in order to familiarise yourself with how they work:

# - A function that uses input to obtain a user's name and returns a string greeting them by their name.
# - A function with parameters of 'name' and 'age' that returns a string containing the 'name' and 'age' supplied to it as arguments. Set a default argument of 'unknown' for 'age'.
# - A function that uses input to obtain a user’s name and age and checks whether or not the user is over the age of 18. If the user is over the age of 18, return a string containing their name advising that their sign-up has been successful. If a user is under the age of 18, return a string containing their name and age advising that they are unable to register due to their age.

# 2: Create your own custom module containing the functions from Task 1:

# - Create a file named 'my_functions.py'.
# - Import your file as a module into a 'main.py' file.
# - Use all 3 of the created functions from the module in your 'main.py' file.

# https://www.programiz.com/python-programming/modules

# 3: Familiarise yourself with Scope in Python:

# https://www.programiz.com/python-programming/global-local-nonlocal-variables


# Stretch Task: 

# Guess the Number V2: Write a function called 'guess_the_number' that starts the game when called. 

# Use the random module to generate a random number between 1 and 100. Each turn the user should guess a number, feedback to the user whether their guess is too high, too low or correct. The game should continue until the user guesses the correct number. 

# https://www.w3schools.com/python/module_random.asp

# ! Custom Module Import
import my_module

print(my_module.task_one("Dave"))
print(my_module.task_two("Dave"))
print(my_module.task_two("Dave", 18))
print(my_module.task_three())

# ! Guess the number game
def guess_the_number():
    number_to_guess = random.randint(1,100)
    print(number_to_guess) # This is not needed only here for demo
    print("Welcome to Guess The Number")
    print("I'm thinking of a number between 1 and 100.")
    print("Can you guess what it is?")
    while True:
        guess = int(input("Enter your guess: "))
        if guess < number_to_guess:
            print("Too low! Try again")
        elif guess > number_to_guess:
            print("Too high! Try again")
        else:
            print(f"Well done! You guessed {guess} correctly!")
            break


guess_the_number()




















# Formatted Message - Signify Start of Output
print(f"{format_output}---END---{format_reset}")