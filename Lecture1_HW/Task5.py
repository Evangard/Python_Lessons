# Given a string - “Hello, this is just a simple string for testing”. 
# Make this string lower-cased, reverse all the separate words and take the last word out of it. Assign this word to a variable.
text = "Hello, this is just a simple string for testing"[::-1].lower().split()
last_word = text[len(text)-1]
print(last_word)