# 1. Write a program that repeatedly asks the user to input an integer. If the user enters something other than an
#   integer, then the program should catch the ValueError and display the message "Try again."
#   Once the user enters an integer, the program should display the number back to the user and end without crashing.
# 2. Write a program that asks the user to input a string and an integer n, then display the character at index n in
#   the string.
#   Use error handling to make sure the program doesn't crash if the user integers something other than an integer or
#   if the index is out of bounds. The program should display a different message depending on which error occurs.

# 1.
while True:
    try:
        user_input = int(input("Enter an integer: "))
        print(f"Users input: {user_input}")
        break
    except ValueError:
        print("try again.")


# 2.
def display_char_index(users_int, users_str):
    """ Display characters at index n """
    try:
        print(f"The index {users_int} in your word {users_str} is {users_str[users_int]}")
    except ValueError:
        print("User must enter a integer: ")
    except IndexError:
        print("Invalid Index input.")
    except TypeError:
        print("Invalid Index Input.")


user_string = input("Enter a word: ")
user_integer = int(input("Enter a number that represent your index: "))
display_char_index(user_integer, user_string)
