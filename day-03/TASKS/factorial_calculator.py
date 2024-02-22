# Write the code ↓ to read the user's input for a non-negative integer.
num = int(input("Please, enter a non-negative integer: "))
# Be cautious when reading input of various data types.

# Write the code ↓ to calculate the factorial of the user-defined integer using a loop.


if num >= 0:
    factorial_result = 1
else:
        print("Please enter a valid integer :)")
        quit()

for i in range(1, num + 1):
    factorial_result *= i

# Write the code ↓ to display the factorial result.
print(f"The factorial of {num} is: {factorial_result}")
# Select and employ a string concatenation method based on your personal preference and comfort level.



