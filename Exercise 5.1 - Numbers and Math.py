# Review Exercise
# 1. Write a program that creates two variables, num1 and num2. both num1 and num2 should be assigned the integer
#    literal 25000000, one written with underscores and one without. print num1 and num2 on two seperate lines.
# 2. Write a program that assigns the floating point literal 175000.0 to the variable num using E notation and then
#    prints num in the interactive window.
# 3. In IDLE's interactive window, try to find the smallest exponent N for which 2e<N>, where <N> is replaced with
#    your number, returns inf.

# 1.
num1 = 25000000
num2 = 25_000_000
print(num1)
print(num2)

# 2.
num3 = 175e3
print(num3)

# 3.
num4 = 2e800
num5 = -2e999
print(num4)
print(num5)