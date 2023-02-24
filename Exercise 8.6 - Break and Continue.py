# Review Exercise
# 1. Using break, write a program that repeatedly asks the user for some input and quits only if the user
#   enters "q" or "Q"
# 2. Using continue, write a program that loops over the number 1 to 50 and prints all numbers that are not multiples
#   of 3.

# 1.
user_input1 = input("Enter a word: ")

while user_input1 != ("q" and "Q"):
    user_input1 = input("Enter a word: ")
    if user_input1 == ("q" or "Q"):
        break


# 2.
for i in range(0, 51):
    if i % 3 == 0:
        continue
    print(i)
