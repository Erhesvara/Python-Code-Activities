# Review Exercise
# 1. Figure out what the result will be (True or False) when evaluating the following expressions, then type them into
#   the interactive window to check your answers:
# 2. Add Parentheses where necessary so that each of the following expressions evaluates to True:

# 1.
example1 = (1 <= 1) and (1 != 1)
example2 = not (1 != 2)
example3 = ("good" != "bad") or False
example4 = ("good" != "Good") and not (1 == 1)

print(f"My answer is False, The correct answer is {example1}")
print(f"My answer is False, The correct answer is {example2}")
print(f"My answer is True, The correct answer is {example3}")
print(f"My answer is False, The correct answer is {example4}")

# 2.
example5 = False == (not True)  # False == not True
example6 = (True and False) == (True and False)  # True and False == True and False
example7 = not (True and "A" == "B")  # not True and "A" == "B"

print(example5)
print(example6)
print(example7)
