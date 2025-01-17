# Python Day 3 - AM - Tuples, Sets, Dictionaries

# Formatting Variables
format_output = "\033[47m\033[30m"
format_reset = "\033[0m"

# Formatted Message - Signify Start of Output
print(f"{format_output}---START---{format_reset}")

# ! Tuple:
# * Think of a Tuple like a set list that cannot be changed (immutable)
# * Syntax wise just replace the square brackets with parentheses

fruits = ("Apple", "Orange", "Banana")

# * If we print the Tuple you will see it looks very similar to a list

print(fruits)

# ! Tuple: Order
# * Like a list each item is indexed
# ? With what we know about lists how would we print "Orange"?

print(fruits[1])

# ! Trying to update a Tuple:
# * The order of items in our Tuple cannot be changed, neither can the data itself
# * If we try to update our Tuple, we get an error

# fruits[1] = "Mango"

# ! Iterating over a Tuple:
# ? How do we think we would iterate over a tuple?
# * We can use a for loop

for fruit in fruits:
    print(fruit)

# * Tuples are most useful for read-only data
# * We can also store Tuples in Sets and Dictionaries

# ! Set:
# * A Set is an unordered collection of unique elements
# * Syntax wise it is similar to a Tuple but with {curly's}

days_of_week = {"Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"}

# * Access a set

print(days_of_week)

# * Notice how our order of our set is not how as we defined
# * If run our code a few more times we will see the order changes
# * This is because a set is unordered

# ! Sets wit duplicate values:
# * Sets do not allow duplicate data
# * For example lets add another "Monday" to the end of our set and print it

days_of_week = {"Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday", "Monday"}

print(days_of_week)

# * Notice that only one instance of "Monday" is included
# * This is because a set will automatically remove duplicates

# ! Set: Intersection:
# * When working with multiple sets we can find common elements
# * This is known as the intersection of the sets

weekend = {"Saturday", "Sunday"}

# * Lets look for the intersection of our examples
# * We do this by referncing one of our sets and using 'intersection()'
# * The argument we pass to this method is the set we want to compare

print(days_of_week.intersection(weekend))

# * Notice that our result is "Saturday" and "Sunday"
# * The alternate syntax for this an ampersand '&'
# * We place the '&' between the sets we want the intersection of

print(days_of_week & weekend)

# ! Set: Difference:
# * The opposite of an intersection is a difference
# * This returns us the elements NOT present in both sets
# * Using the same idea we can replace the 'intersection()' method...
# * ...with the 'difference()' method

print(days_of_week.difference(weekend))

# * Alternatively we can replace the '&' with '-'

print(days_of_week - weekend)

# ! Set: Union:
# * If we wanted to merge two sets we can use the 'union()' method
# * Or use the single bar '|' between the two sets

week = days_of_week | weekend
print(week)











# Formatted Message - Signify Start of Output
print(f"{format_output}---END---{format_reset}")