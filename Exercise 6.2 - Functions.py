# Review Exercise
# 1. Write a function called cube() that takes one number parameter and returns the value of that number raised to the
#   third power. Test the function by calling your cube() function on a few different numbers and displaying the result.
# 2. Write a function called greet() that takes one string parameter called name and display the text "Hello <name>!",
#    where <name> is replaced by the value of the name parameter.

# 1.
def cube(num):
    """ takes the num and raised it to third power """
    raised_num = num ** 3
    return raised_num


user_input1 = int(input("Enter a number that will be raised to third power: "))
print(cube(user_input1))

# 2.
def greet(name):
    """ greeting the name parameters with its name """
    print(f"Hello,{name}")


user_name = input("Enter your name: ")
greet(user_name)
