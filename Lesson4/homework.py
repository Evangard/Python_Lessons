# # Task: Number Guessing Game
# # Write a Python program that generates a random number between 1 and 100. Allow the user to guess the number, and provide appropriate feedback (e.g., "Too high" or "Too low") until they guess the correct number. Use a loop and conditional statements to implement the game.
# import random
# random_number = random.randrange(1, 100)
# print(random_number)
# guess_number = input("Guess the number between 1 and 100\n")
# guess_number = int(guess_number)
# if guess_number < random_number:
#     print("Too low")
# elif guess_number == random_number:
#     print("Yoohoo. You're right")
# else:
#     print("Too high")


# # Task: Character Counter
# # Write a Python program that takes a string as input from the user and counts the number of occurrences of each character in the string. Display the result in the format: "Character: Count". Use loops and conditional statements to implement this.
# # user_str = input("Enter some string:\n")
# user_str = input("Enter some text:\n")
# result = {}
# for ch in user_str:
#     if ch in result: 
#         result[ch] += 1
#     else: 
#         result[ch] = 1
# for k, v in result.items():
#     print("%r: %d" % (k, v))


# Task: Password Strength Checker
# Write a Python program that takes a password as input from the user and checks its strength. 
# Display a message indicating whether the password is weak, moderate, or strong based on the following criteria:
# Weak: Less than 8 characters long
# Moderate: 8 to 12 characters long
# Strong: More than 12 characters long
# # Use conditional statements to determine the strength.
# num = input("Enter password:\n")
# length = len(num)
# if length < 8 :
#     print("Weak: Less than 8 characters long")
# elif length > 7 and length < 13 :
#     print("Moderate: 8 to 12 characters long")
# else :
#     print("Strong: More than 12 characters long")

# Task: Number Sum
# Write a Python program that takes an integer as input from the user and calculates the sum of all numbers from 1 to that integer (inclusive). 
# Display the result. Use a loop and conditional statements to implement this.

# Task: Palindrome Checker
# Write a Python program that takes a string as input from the user and checks whether it is a palindrome. 
# A palindrome is a word, phrase, number, or other sequence of characters that reads the same forward and backward. 
# Display a message indicating whether the string is a palindrome or not. Use loops and conditional statements to implement this.

# Task: Multiplication Table
# Write a Python program that takes an integer as input from the user and prints the multiplication table for that number from 1 to 10. 
# Display the result in the format: "Number x Multiplier = Result". Use loops and conditional statements to implement this.

# Task: Vowel Counter
# Write a Python program that takes a string as input from the user and counts the number of vowels (a, e, i, o, u) in the string. 
# Display the result. Use loops and conditional statements to implement this.