# Review Exercise
# 1. Create a float object named weight with the value 0.2, and create a string object named animal with the value
# "newt". Then use these objects to print the following string using only string concatenation:
#  0.2 kg is the weight of the newt.
# 2. Display the same string by using .format() and empty {} placeholders.
# 3. Display the same string using an f-string.

# 1.
weight = float(0.2)
animal = "newt"
print(str(weight) + " kg is the weight of the " + animal)

# 2.
print("{} kg is the weight of the {} ".format(weight, animal))

# 3.
print(f"{weight} kg is the weight of the {animal}.")
