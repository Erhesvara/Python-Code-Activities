# Review Exercise
# 1. Write a program that prompts the user to enter a word using the input() function and compares the length of the
#   word to the number five. the program should display one of the following outputs, depending on the length of the
#   user's input:
#   "Your input is less than 5 characters long"
#   "Your input is greater than 5 characters long"
#   "Your input is 5 characters long"
# 2. Write a program that displays "I'm thinking of a number between 1 and 10. Guess which one." Then use input() to get
#   a number from the user. If the user inputs the number 3, then the program should display "you win!" for any other
#   input, the program should display "You lose".

# 1.
users_input = input("Enter a word: ")
if len(users_input) < 5:
    print("Your input is less than 5 characters long")
elif len(users_input) > 5:
    print("Your input is greater than 5 characters long")
else:
    print("Your input is 5 characters long")

# 2.
users_input2 = int(input("I'm thinking of a number between 1 and 10. Guess which one:  "))
if users_input2 == 3:
    print("You win!")
else:
    print("You lose.")
