# Python Day 3 - PM - Exception Handling

# Formatting Variables
format_output = "\033[47m\033[30m"
format_reset = "\033[0m"

# Formatted Message - Signify Start of Output
print(f"{format_output}---START---{format_reset}")

# ! Built-In Exceptions:
# * Exceptions are basically errors
# * Python has some built-in error detection that we can make use of

# * Lets look at the example from the presentation
# * We want to write a function that takes 2 numbers from the user and divides...
# * ... the first number by the second number

# ! Version with no exception handling implemented:
def divide_1():
    num1 = int(input("Enter a number: "))
    num2 = int(input("Enter another number: "))
    result = num1 / num2
    print(f"The result of {num1} divided by {num2} is: {round(result)}")

# * But if we test it's robustness we can easily break it
# * Lets say someone passes a character that is not a number
# * Or if someone tries to divide by '0'

# divide_1()

# * We can handle this error with exceptions
# ! try...except Block:
# * 'try:' is followed by the code we would like to run
# * 'except:' must follow try as this is how we handle our exceptions
# * Think of the except block like a conditional
# * If there is an error, we need to do this

# ! ValueError
# * In this case the exception we're checking for is "ValueError"
# * When we encounter an invalid value we can return an error message 

# ! ZeroDivisionError:
# * When user tries to divide by zero we can handle this error and return an error message

# ! except Exception:
# * Allows us to handle any unforseen errors and return a useful error message

def divide_2():
    try:
        num1 = int(input("Enter a number: "))
        num2 = int(input("Enter another number: "))
        result = num1 / num2
        print(f"The result of {num1} divided by {num2} is: {round(result)}")
    except ValueError:
        print("Invalid input. Please enter 2 valid integers.")
    except ZeroDivisionError:
        print("Error: Division by zero is not permitted.")
    except Exception as e:
        print(f"Error: an error has occurred: {e}")
    # ! A finally block is NOT required but if added will run regardless of exceptions 
    finally:
        print("The operation has been completed.")

divide_2()















# Formatted Message - Signify Start of Output
print(f"{format_output}---END---{format_reset}")