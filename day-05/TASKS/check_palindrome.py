# Write the code ↓ to prompt the user to enter a word.
word = input("Please, enter a word/s to check: ")
# Be cautious when reading input of various data types.







# Write the code ↓ to check if the entered word is a palindrome.
is_palindrome = word.lower() == word.lower()[::-1]
# Utilize string functions to compare the original word with its reverse.






# Write the code ↓ to display whether the entered word is a palindrome or not.
word = "The word '{}' is {}.".format(word, 'a palindrome' if is_palindrome else 'not a palindrome')
print(word)
# Select and employ a string concatenation method based on your personal preference and comfort level.






