# 1. Write a function called roll() that uses randint() to simulate rolling a fair die by returning a random integer
#   between 1 and 6.
# 2. Write a program that simulates ten thousand rolls of a fair die and display the average number rolled.

# 1.
import random


# 1.
def roll():
    """ simulate rolling fair dice """
    random_int = random.randint(1, 6)
    return random_int


print(roll())

# 2.
total = 0

for rolled in range(10_000):
    total = total + roll()

avg_roll = total / 10_000

print(f"The average result of 10,000 rolls is {avg_roll}")