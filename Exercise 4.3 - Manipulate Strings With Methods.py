#  Review Exercise
# 1. Write a program that converts the following strings to lowercase: "Animals", "Badger", "Honey Bee", "Honey Badger".
#    Print each lowercase string on a seperate line.
# 2. Repeat Exercise 1, but convert each string to uppercase instead of lowercase.
# 3. Write a program that removes whitespace from the following strings, then print out the string with the whitespace
#    removed:
#    String1 = "   Filet Mignon"
#    String2 = "Brisket    "
#    String3 = "   Cheese Burger   "
# 4. Write a program that prints out the result of .startswith("be") on each of the following strings:
#    String1 = "Becomes"
#    String2 = "becomes"
#    String3 = "BEAR"
#    String4 = "   bEautiful"
# 5. Using the same four strings from exercise 4, write a program that uses string method to alter each string so that
#    .startswith("be") returns True for all of them.

# 1.
print("Animals".lower())
print("Badger".lower())
print("Honey Bee".lower())
print("Honey Badger".lower())

# 2.
print("Animals".upper())
print("Badger".upper())
print("Honey Bee".upper())
print("Honey Badger".upper())

# 3.
String1 = "   Filet Mignon"
String2 = "Brisket    "
String3 = "   Cheese Burger   "

print(String1.lstrip())
print(String2.rstrip())
print(String3.strip())

# 4.
String4 = "Becomes"
String5 = "becomes"
String6 = "BEAR"
String7 = "   bEautiful"

print(String4.startswith("be"))
print(String5.startswith("be"))
print(String6.startswith("be"))
print(String7.startswith("be"))

# 5.
String4 = String4.lower()
String5 = "becomes"
String6 = String4.lower()
String7 = String7.lower()
String7 = String7.lstrip()

print(String4.startswith("be"))
print(String5.startswith("be"))
print(String6.startswith("be"))
print(String7.startswith("be"))

