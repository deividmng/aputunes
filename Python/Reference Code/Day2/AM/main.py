# Python Day 2 - AM - Lists and Loops

# Formatting Variables
format_output = "\033[47m\033[30m"
format_reset = "\033[0m"

# Formatted Message - Signify Start of Output
print(f"{format_output}---START---{format_reset}")

# ! Lists
# * Lists in Python can be thought of like Arrays in JavaScript
# * Think of it as just a different name, the same principles apply:

# * Ordered, Indexed, Mutable, Allow Duplicates

languages = ["HTML", "CSS", "JavaScript", "Python"]

# ? How would we access an item in our list? Say we wanted to print "CSS"?

print(languages[1])

# * Remember the index starts from 0 NOT 1
# ! Negative Indexing
# * Python supports negative indexing meaning 'list[-1]' references the last item

print(languages[-1])

# ? With the last item being [-1] how would we access "HTML" using negative indexing?

print(languages[-4])

# * Think of negative indexing like counting from right to left - starting from 1

# ! Updating / Changing List Items
# * We can amend list items by referencing an index and assigning a new value
# * Lets replace "Python" with "SQL"

languages[3] = "SQL"

print(languages)

# ! List Methods
# * As we have seen with Arrays, Lists also have methods

# ! Remove an Item
# * To remove an item from a list we can use 'remove()'
# * We pass an argument of the item we wish to remove NOT the index
# * If we wanted to remove "SQL" from our list we would do so with:

languages.remove("SQL")

print(languages)

# * If the item cannot be found we receive an error

# languages.remove("SQL")

# ! Add / Append an Item
# * To add an item to the end of a list we can use 'append()'
# * We pass an argument of the item we wish to append
# * Lets add "Pyhton" back to our list

languages.append("Python")

print(languages)

# ! Familiarise yourself with the additional list methods
# * There will be an oppurtunity to experiment later on in the session

# ! Number of Items in a list
# * To find the number of items in a list in Python we have the 'len()' function
# * Think of it like the .length property in JavaScript
# * We pass the list name as an argument to the function

print(len(languages))

# ! Copy a list
# * A copy of a list can be created using the 'copy()' method

original_list = [1,2,3,4]
copied_list = original_list.copy()

print(original_list, copied_list)

# ! Loops
# * Python is no different than JavaScript or any other programming language
# * When we need to iterate over a sequence we use a loop

# ! For Loop - List
# * As mentioned earlier in the session a for loop in Python works the same as in JavaScript
# * The syntax however is more similar to a For of loop in JavaScript

# * Lets say we wanted to print our list of languages

for i in languages:
    print(i)

# ! REMEMBER 'i' is just a reference it could be anything
# * With a Python for loop we are not incrementing or checking against length
# * So our reference in this case 'i' does not hold a numeric value
# * It simply references the item in the list each iteration

for lang in languages:
    print(lang)

# ! For Loop - String
# * We can also iterate over a string

string = "Example"
for i in string:
    print(i)

# * Again our 'i' is simply a reference

for letter in string:
    print(letter)

# ! For Loop - Range
# * In Python if we wish to loop over a sequence of numbers we can use 'range()'
# * The number of iterations is defined by what we pass as an argument to the function

for i in range(5):
    print(i)

# * Remember we start our count from 0

for i in range(5):
    print(i+1)

# * With 'range()' we can also pass 2 arguments a start point and an end point
# ! NOTE: the end number of the range will not be inluded
for i in range(1,6):
    print(i)

# ! While Loop
# * We have seen these before, a loop that will repeat until a condition is met to end it
# ! Remember: No Autosave! 
# * Be mindful of infinite loops that will run forever if conditions are not met

# * Basic Example:

num = 1
while num <= 5:
    print(num)
    num += 1

# ! Break Statement:
# * A 'break' statement allows us to terminate a loop immediately regardless of the condtition

# * Lets look at an example of a loop that will run until you tell it to "Stop"
# * "while True:" will ensure a loop always begins running

while True:
    user_input = input("I will keep asking for input until you tell me to \"Stop\": ")

    if user_input.lower() == "stop":
        print(user_input)
        print("No problem I will stop.")
        break


# Python - Day 2 (AM) – Lists and Loops Tasks:

# 1: Create your own examples of the following For Loops to familiarize yourself with the syntax:

# - For Loop (List): Write a for loop that prints each item in a list
# - For Loop (String): Write a for loop that prints each character in a string
# - For Loop with Range: Write a for loop that prints numbers 1 to 10 using the range function

# 2: Create your own examples of the following While Loops to familiarize yourself with the syntax and the 'break' and 'continue' keywords:

# - Basic While Loop: Write a while loop that prints numbers from 1 to 10.
# - While Loop with Break: Implement a 'break' statement in a while loop that prints numbers from 1 to 10 and stops when it reaches 5.
# - While Loop with Continue: Research the 'continue' statement and implement it in a while loop that prints numbers from 1 to 10, but skips printing the number 5.

# https://www.programiz.com/python-programming/break-continue

# 3: Research list methods and experiment with them, putting together some example implementations:

# https://www.programiz.com/python-programming/methods/list

# Stretch Task: 

# Guess the Number: Store a number between 1 and 10 in a variable. Write a while loop that asks the user to input a guess, the game should continue until the user inputs a correct guess.









# Formatted Message - Signify End of Output
print(f"{format_output}---END---{format_reset}")