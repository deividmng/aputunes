def task_one(name):
    return f"Hello {name}"

def task_two(name, age = "Unknown"):
    return f"{name} is {age} years old"

def task_three():
    name = input("What is your name? ")
    age = int(input("How old are you? "))
    if age >= 18:
        return f"Thank you {name} as you are {age}, your sign-up has been confirmed."
    else:
        return f"Sorry {name}, as you are only {age} your sign-up cannot be processed."