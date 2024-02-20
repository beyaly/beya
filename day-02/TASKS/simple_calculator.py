# Write the code ↓ to read user's input for two operands and selected operation.
firstNumber = float(input("Enter the first number: "))
secondNumber = float(input("Enter the second number: "))
operator = input("Enter the operator (+, -, x, /): ")
# NOTE: The two operands must be read as floats.


# Write the code ↓ to perform the calculations based on the selected operation.
result = 0
if operator == '+':
    result = firstNumber + secondNumber
elif operator == '-':
    result = firstNumber - secondNumber
elif operator == 'x':
    result = firstNumber * secondNumber
elif operator == '/':
        result = firstNumber / secondNumber
    

 
# Write the code ↓ to display the result.
print(f"The result of {firstNumber} {operator} {secondNumber} = {result}")
# Select and employ a string concatenation method based on your personal preference and comfort level.
