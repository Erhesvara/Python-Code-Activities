# Review Exercise
# 1. Create a tuple literal named cardinal_numbers that holds the strings "first", "second", and "third", in that order.
# 2. Using index notation and print(), display the string at index 1 in cardinal_numbers.
# 3. In a single line of code, unpack the values in cardinal_numbers into three new strings named position1, position2,
#   and position3. then print each value on a separate line.
# 4. Using tuple() and a string literal, create a tuple called my_name that contains the letters of your name.
# 5. Check whether the character "x" is in my_name using the in keyword.
# 6. Create a new tuple containing all but the first letter in my_name using slice notation.

# 1.
cardinal_numbers = ("first", "second", "third ")

# 2.
print(f"the index 1 in tuple cardinal_number is {cardinal_numbers[1]}")

# 3.
position1, position2, position3 = cardinal_numbers
print(f"The first position is: {position1}")
print(f"The second position is: {position2}")
print(f"The third position is: {position3}")

# 4.
my_name = ("e", "r", "a", "l", "d")

# 5.
print(f'Is the letter x is in my name? {"x" in my_name}')

# 6.
print(f"The letters of my name not including the first letter: {my_name[1:]}")

