# Review Exercise
# 1. Create a String containing an integer, then convert that string into an actual integer object using int().
#    Test that your new object is a number by multiplying it by another number and displaying the result.
# 2. Repeat the previous exercise, but use a floating-point number and float()
# 3. Create a string object and an integer object, then display them side by side with a single print statement using
#    str().
# 4. Write a program that uses input() twice to get two numbers from the user, multiplies the number together, and
#    display the result. if the user enters 2 and 4, then your program should print the following text:
#    The product of 2 and 4 is 8.0

# 1.
string1 = "1"
print(int(string1) * 3)

# 2.
string2 = "2"
print(float(string2) * 3)

# 3.
string3 = "this is for the number "
num1 = 3
print(string3 + str(num1))

# 4.
user_input = int(input("Enter the first number: "))
user_input_2 = int(input("Enter the second number: "))
print("The product of " + str(user_input) + " and " + str(user_input_2) + " is " \
            + str(user_input * user_input_2))