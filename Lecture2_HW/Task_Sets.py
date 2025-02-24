#Sets:

#Task 1: Set Creation and Elements
#Create a set named my_set that contains the following elements: 1, 2, 3, 4, 5. Print the set.
my_set = {1, 2, 3, 4, 5}
print(my_set)

#Task 2: Set Operations
#Given two sets set1 = {1, 2, 3, 4} and set2 = {3, 4, 5, 6}, perform the following set operations and print the results:
set1 = {1, 2, 3, 4} 
set2 = {3, 4, 5, 6}
#Union: Combine the elements from both sets without duplicates.
set3 = set1 | set2
set4 = set1.union(set2)
print(set3)
print(set4)

#Intersection: Find the common elements between the two sets.
print(set1 & set2)
print(set1.intersection(set2))

#Difference: Find the elements that are in set1 but not in set2.
print(set1 - set2)
print(set1.difference(set2))

#Task 3: Set Membership
#Given a set my_set = {1, 2, 3, 4, 5}, check if the value 3 is present in the set. Print True if it is, and False otherwise.
print(3 in my_set)

#Task 4: Set Length
#Given a set my_set = {"apple", "banana", "cherry", "durian"}, print the number of elements in the set.
my_set1 = {"apple", "banana", "cherry", "durian"}
print("Set Length: "  + str(len(my_set1)))

#Task 5: Set Addition and Removal
#Given an empty set my_set, perform the following operations and print the resulting set after each step:
my_set3 = set()

#Add the element "apple" to the set.
my_set3.add("apple")
print(my_set3)
#Add the elements "banana" and "cherry" to the set.
my_set3.add("banana")
my_set3.add("cherry")
#Remove the element "apple" from the set.
my_set3.remove("apple")
print(my_set3)

#Task 6: Set Intersection Update
#Given two sets set1 = {1, 2, 3, 4} and set2 = {3, 4, 5, 6}, use the appropriate set method to update set1 with the elements that are common between set1 and set2. Print the updated set1.
set1.intersection_update(set2)
print("Intersection: " + str(set1))

#Task 7: Set Symmetric Difference
#Given two sets set1 = {1, 2, 3, 4} and set2 = {3, 4, 5, 6}, calculate and print the symmetric difference between the two sets.
set1 = {1, 2, 3, 4}
set2 = {3, 4, 5, 6}
set1.symmetric_difference_update(set2)
print("Symmetric difference: " + str(set1))

#Task 8: Set Subset Check
#Given two sets set1 = {1, 2, 3} and set2 = {1, 2, 3, 4, 5}, check if set1 is a subset of set2. Print True if it is, and False otherwise.
set1 = {1, 2, 3}
set2 = {1, 2, 3, 4, 5}
print("Subset: " + str(set1.issubset(set2)))

#Task 9: Set FrozenSet
#Explain the concept of a frozen set in Python and discuss its characteristics and use cases.
# Frozen set is just an immutable version of a Python set object. 
# While elements of a set can be modified at any time, elements of the frozen set remain the same after creation.
#  Like normal sets, frozenset can also perform different operations like copy, difference, intersection, symmetric_difference, and union.
vowels = ('a', 'e', 'i', 'o', 'u')
my_frozen_set = frozenset(vowels)
print(my_frozen_set)

#Task 10: Set Conversion
#Given a list my_list = [1, 2, 3, 4, 5], convert it into a set named my_set. Print the resulting set.
my_list = [1, 2, 3, 4, 5]
my_set = set(my_list)
print(my_set)