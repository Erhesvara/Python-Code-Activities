# Review Exercise
# 1. Write a program that asks the user to input a number and then displays that number rounded to two decimal places.
#    When run, your program should look like this:
#    Enter a number: 5.432
#    5.432 rounded to 2 decimal places is 5.43
# 2. Write a program that asks the user to input a number and then displays the absolute value of that number.
#    When run, your program should look like this:
#    Enter a number: -10
#    The absolute Value of -10 is 10.0
# 3. Write a program that asks the user to input two numbers by using input() twice, then displays whether the
#    difference between those two number is an integer. When run, your program should look like this:
#    Enter a number: 1.5
#    Enter another number: .5
#    The difference between 1.5 and .5 is an integer? True!
#    If the user inputs two number whose difference is not integral, then the output should look like this:
#    The difference between 1.5 and 1.0 is an integer? False!

# 1.
num1 = float(input("Enter a number: "))
print(f"{num1} rounded to 2 decimal places is {round(num1,2)}")

# 2.
num2 = float(input("Enter a number: "))
print(f"The Absolute value of {num2} is {abs(num2)}")

# 3.
num3 = float(input("Enter a number: "))
num4 = float(input("Enter another number: "))
print(f"The difference between {num3} and {num4} is an integer? {(num3 - num4).is_integer()}")
