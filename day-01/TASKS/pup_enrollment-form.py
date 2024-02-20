print(f"PUP Enrollment Form\n")

# Write the code ↓ to read user's input.
name = input("Enter your full name: ")

# Be cautious when reading input of various data types.
age = int(input("Enter your age: "))

# Write the code ↓ to display the user's personal information.
gwa = float(input("Enter your previous general weighted average: "))

# Select and employ a string concatenation method based on your personal preference and comfort level.
member = input("Are you a member of AWS Cloud Club? (yes/no): ").lower() == "yes"

print(f"\n\nYour Enrollment Form:\nName: {name}\nAge: {age}\nGWA: {gwa}\nAwstraunot: {member}")



