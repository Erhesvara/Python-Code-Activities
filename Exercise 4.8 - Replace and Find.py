# Review Exercise
# 1. In one line of code, display the result of trying to .find() the substring "a" in the string "AAA". the result
#    Should be -1/
# 2. Replace every occurrence of the character "s" with "x" in the string "Somebody said something to Samantha."
# 3. Write a program that accepts user input with input() and displays the result of trying to .find() a particular
#    Letter in that input.

# 1.
string = "AAA"
print(string.find("a"))

# 2.
string2 = "Somebody said something to Samantha."
string2_replaced = string2.replace("s", "x")
print(string2_replaced)
#print(string2.replace("s", "x"))

# 3.
user_input = input("Enter the letter you want to find: ")
string3 = "Try finding the letter here user "
print(string3.find(user_input))