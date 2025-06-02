# Task 1: File Reading
# Write a Python program that reads the contents of a text file named "hw_data.txt" and prints them to the console.
# with open('some_data.txt', 'r') as file:
#     print(file.read())

# Task 2: File Writing
# Write a Python program that prompts the user to enter some text and saves it to a text file named "output.txt".
# user_input = input("Enter some text: ")
# with open('task2.txt', 'w') as file:
#     file.write(user_input)
# with open('task2.txt', 'r') as file:
#     print("Text from file for task2:" + file.read())

# Task 3: File Appending
# Write a Python program that prompts the user to enter a line of text and appends it to an existing text file named "hw_data.txt".
# with open('task2.txt', 'a') as file:
#     file.write(user_input)
# with open('task2.txt', 'r') as file:
#     print("Text from file for task3:" + file.read())

# Task 4: File Copying
# Write a Python program that reads the contents of a source file named "source.txt" and copies them to a destination file named "destination.txt".
# with open('task2.txt', 'r') as file1, open('task4.txt', 'w') as file2:
#     file2.writelines(file1.readlines())
# with open('task4.txt', 'r') as file:
#     print("Text from file for task4:" + file.read())


# Task 5: File Line Count
# Write a Python program that reads a text file named "hw_data.txt" and counts the number of lines in the file. Print the line count.
# with open('some_data.txt', 'r') as file:
#     count = 0
#     for line in file:
#         count=count+1
#     print(count)

# Task 6: File Word Count
# Write a Python program that reads a text file named "hw_data.txt" and counts the number of words in the file. Print the word count.
# import re
# with open('some_data.txt', 'r') as file:
#     text = re.split(r'\W+',file.read())
# count = 0
# for t in text:
#     if t != '':
#         count =count+1
# print(count)

# Task 7: File Searching
# Write a Python program that prompts the user to enter a search term and searches for occurrences of that term in a text file named "hw_data.txt". Print the line numbers where the search term is found.
# import re
# user_input = input("Enter text for searching: ")
# with open('some_data.txt', 'r') as file:
#     print(file.read().count(user_input))

# Task 8: File Line Reversal
# Write a Python program that reads the contents of a text file named "hw_data.txt" and writes the lines in reverse order to a new text file named "reversed.txt".
# with open('task2.txt', 'r') as file1, open('task8.txt', 'w') as file2:
#     file2.writelines(reversed(file1.readlines()))