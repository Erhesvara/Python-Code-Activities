# Review Exercise
# 1. Print the result of the calculation 3 ** .125 as a fixed-point number with three decimal places.
# 2. Print the number 150000 as currency with the thousands grouped with commas. Currency should be display with two
#    decimal places.
# 3. Print the result of 2 / 10 as a percentage with no decimal places. The output should look like 20%

# 1.
num1 = 3 ** .125
print(f"The calculation of 3 raised to .125 is: {num1:.3f}")

# 2.
num2 = 150000
print(f"The currency num2 grouped with commas is: {num2:,.2f}")

# 3.
num3 = 2 / 10
print(f"the result of 2 divided by 10 as a percentage with no decimal places is {num3:.0%}")
