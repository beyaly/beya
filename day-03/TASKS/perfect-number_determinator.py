# Write the code ↓ to read the user's input for a positive integer.
num = int(input("Please, enter a positive integer: "))
# Be cautious when reading input of various data type
# Write the code ↓ to check if the entered integer is a Perfect Number using a loop.

if num > 0:
    is_perfect_number = False
else: 
    print("Please enter a positive integer :)")
    quit()

    for i in range(1, num):
        if num % i == 0:
            is_perfect_number += i

# Write the code ↓ to display the Perfect Number check result.
if is_perfect_number == num:
    print(f"{num} is a Perfect Number.")
else:
    print(f"{num} is not a Perfect Number.")
# NOTE : You can use if-else statement or ternary operator to display the result.


