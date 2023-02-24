# Review Exercise
# 1. Write a for loop that print out the integers 2 through 10, each on a new line using range().
# 2. Write a while loop that prints our the integers 2 through 10. (Hint: you'll need to create a new integer first.)
# 3. Write a function called doubles() that takes a number as its input and doubles it. Then use doubles() in a loop to
#    double the number 2 three times, displaying each result on a separate line. Here's some sample output:
#    4
#    8
#    16

# 1.
for n in range(2, 11):
    print(n)


# 2.
num = 2
while num < 11:
    print(num)
    num = num + 1

# 3.
def doubles(interger):
    """ doubles the input """
    doubled = interger * 2
    return doubled


int_2 = 2
for n in range(3):
    int_2 = (doubles(int_2))
    print(int_2)
