#Dictionaries:

print("Task 1: Dictionary Creation and Elements")
#Create a dictionary named my_dict that contains the following key-value pairs:
#"name" as the key and "John" as the value.
#"age" as the key and 25 as the value.
#"country" as the key and "USA" as the value.

my_dict = {"name": "John", "age": 25, "country": "USA"}
#Print the dictionary.
print(my_dict)

print("Task 2: Access Dictionary Values")
#Given the dictionary my_dict = {"name": "Alice", "age": 28, "country": "Canada"}, access and print the value associated with the key "age".
my_dict = {"name": "Alice", "age": 28, "country": "Canada"}
print(my_dict["age"])

print("Task 3: Dictionary Operations")
#Given the dictionary my_dict = {"a": 1, "b": 2, "c": 3}, perform the following operations and print the results:
my_dict = {"a": 1, "b": 2, "c": 3}

#Add a new key-value pair "d" with the value 4.
my_dict["d"] = 4
#Update the value of key "b" to 5.
my_dict["b"] = 5
#Remove the key-value pair with the key "c".
my_dict.pop("c")
print(my_dict)

print("Task 4: Dictionary Length")
#Given a dictionary my_dict = {"name": "Alice", "age": 28, "country": "Canada"}, print the number of key-value pairs in the dictionary.
my_dict = {"name": "Alice", "age": 28, "country": "Canada"}
for keys, values in my_dict.items():
    print(str(keys) + ":", str(values))

print("Task 5: Dictionary Keys and Values")
#Given the dictionary my_dict = {"a": 1, "b": 2, "c": 3}, print all the keys and values of the dictionary separately.
my_dict = {"a": 1, "b": 2, "c": 3}
print("Keys: ")
for keys in my_dict.keys():
    print(keys)
print("Values: ")
for values in my_dict.values():
    print(values)


print("Task 6: Dictionary Sorting")
#Given the dictionary my_dict = {"b": 2, "c": 1, "a": 3}, print the dictionary after sorting it based on the keys in ascending order.
my_dict = {"b": 2, "c": 1, "a": 3}
sorted_dict = dict(sorted(my_dict.items()))
print(sorted_dict)

print("Task 7: Dictionary Merging")
#Given two dictionaries dict1 = {"a": 1, "b": 2} and dict2 = {"c": 3, "d": 4}, merge them into a single dictionary named merged_dict. Print the merged dictionary.
dict1 = {"a": 1, "b": 2}
dict2 = {"c": 3, "d": 4}

merged_dict = {**dict1, **dict2}
print(merged_dict)

print("Task 8: Dictionary Nesting")
#Create a dictionary named student that contains the following information:

#"name" as the key with the value "Alice".
#"age" as the key with the value 20.
#"grades" as the key with the value [85, 92, 78].
#Print the dictionary.
student = {
    "name": "Alice",
    "age": 20,
    "grades": [85, 92, 78]
}
print(student)

print("Task 9: Dictionary Key Existence")
#Given a dictionary my_dict = {"name": "Alice", "age": 28, "country": "Canada"}, check if the key "country" exists in the dictionary. Print True if it does, and False otherwise.
my_dict = {"name": "Alice", "age": 28, "country": "Canada"}
print("country" in my_dict)
    
print("Task 10: Dictionary Conversion")
#Given a list of tuples my_list = [("a", 1), ("b", 2), ("c", 3)], convert it into a dictionary named my_dict. Print the resulting dictionary.
my_list = [("a", 1), ("b", 2), ("c", 3)]
my_dict = dict(my_list)
print(my_dict)