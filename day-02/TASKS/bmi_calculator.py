# BMI - NUTRITIONAL STATUS GUIDE
"""
    BMI         NUTRITIONAL STATUS

BELOW 18.5         UNDERWEIGHT
18.5 - 24.9       NORMAL WEIGHT
25.0 - 29.9        OVERWEIGHT
ABOVE 30.0          OBESITY
"""
 
# Write the code ↓ to read user's height and weight.
height = float(input("Enter your height in meters: "))
weight = float(input("Enter your weight in kilograms: "))
# Be cautious when reading input of various data types.
print(f"HEIGHT: {height} - WEIGHT: {weight}")

# Write the code ↓ to perform the calculations of user's BMI and categorize its status.
bmi = weight / (height ** 2)
if bmi < 18.5:
    bmi_category = "UNDERWEIGHT"
elif 18.5 <= bmi <= 24.9:
    bmi_category = "NORMAL WEIGHT"
elif 25.0 <= bmi <= 29.9:
    bmi_category = "OVERWEIGHT"
else:
    bmi_category = "OBESITY"

# Write the code ↓ to display the user's BMI and its classification.
print(f"BMI: {bmi:.2f}")
print(f"NUTRITIONAL STATUS: {bmi_category}")

# Select and employ a string concatenation method based on your personal preference and comfort level.
# Use :.2f format specifier when printing the BMI value to display the BMI with only two decimal places.

