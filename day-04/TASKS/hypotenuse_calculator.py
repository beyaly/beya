import math

# Write the code ↓ to read the lengths of the two shorter sides of a right-angled triangle from the user.
side_a = float(input("Please, enter the length of side A: "))
side_b = float(input("Please, enter the length of side B: "))
# Be cautious when reading input of various data types.






# Write the code ↓ to calculate the hypotenuse using the Pythagorean theorem.
hypotenuse = math.sqrt(side_a**2 + side_b**2)
# The Pythagorean theorem: c^2 = a^2 + b^2, where c is the hypotenuse.






# Write the code ↓ to display the calculated hypotenuse.
result = f"The hypotenuse of the right-angled triangle is: {hypotenuse:.2f}"
print(result)
# Select and employ a string concatenation method based on your personal preference and comfort level.






