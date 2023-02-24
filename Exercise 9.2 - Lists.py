# Review Exercise
# 1. Create a list named food with two elements, "rice" and "beans"
# 2. Append the string "broccoli" to food using .append()
# 3. Add the strings "bread" and "pizza" to food using extend().
# 4. Print the first two items in the food list using print() and slice notation.
# 5. Print the last item in food using print() and index notation.
# 6. Create a list called breakfast from the string "egg, fruit, orange juice" using the string split() method.
# 7. Verify that breakfast has three items using len().
# 8. Create a new list called lengths using a list comprehension that contains the lengths of each string in the
#   breakfast list.

# 1.
food = ["rice", "beans"]

# 2.
food.append("broccoli")

# 3.
food.extend(["bread", "pizza"])

# 4.
print(f"The first two items in the food list is: {food[0:2]}")

# 5.
print(f"The last item in the food list is: {food[-1]}")

# 6.
breakfast_items = "egg, fruit, orange juice"
breakfast = breakfast_items.split(", ")
print(f"The breakfast list is: {breakfast}")

# 7.
print(len(breakfast))

# 8.
breakfast_number = [len(num) for num in breakfast]
print(breakfast_number)
