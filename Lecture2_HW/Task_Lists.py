# Task 1: Create a new list with numbers between 100 and 200 that can be devided by 3.
my_list = [x for x in range(100, 300) if x%3 == 0]
print(my_list)
# Task 2: Given a list [13, 59, 56, 13, 84, 58, 43, 4, 74, 8, 32, 100, 92, 50, 29, 24, 61, 39, 99, 45]. Find the maximum and minumum numbers in this list.

my_list1 = [13, 59, 56, 13, 84, 58, 43, 4, 74, 8, 32, 100, 92, 50, 29, 24, 61, 39, 99, 45]
print(max(my_list1))
print(min(my_list1))

# Task 3: Given a list [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]. Reverse this list in place without creation a new list. Print the result to the console.
my_list2 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
my_list2.reverse()
print(my_list2)

# Task 4: Given a list with duplicates [1, 2, 3, 4, 3, 1, 5, 2, 6]. 
# You need to create a new list with all the duplicate elements removed.
# The order of the elements should be preserved. For example, if the input list is [1, 2, 2, 3, 4, 1, 5],result will be [1, 2, 3, 4, 5].
my_list_with_dupl = [1, 2, 3, 4, 3, 1, 5, 2, 6]
my_list_without_duplicates = []
[my_list_without_duplicates.append(x) for x in my_list_with_dupl if x not in my_list_without_duplicates]
print(my_list_without_duplicates)

# Task 5: Using list comprehension create a list that contains numbers from 10 to 1 in descending order.
numbers = [x for x in reversed(range(1, 10))]
print(numbers)

# Task 6: Given a list [13, 59, 56, 13, 84, 58, 43, 4, 74, 8, 32, 100, 92, 50, 29, 24, 61, 39, 99, 45]. 
# You need to sort it in ascending order using any sorting algorithm. Do not user built-in "sort" or "sorted" method.
my_list3 = [13, 59, 56, 13, 84, 58, 43, 4, 74, 8, 32, 100, 92, 50, 29, 24, 61, 39, 99, 45]
for i in range(len(my_list3)):
    for j in range(i+1, len(my_list3)):
        if my_list3[i] > my_list3[j]:
            my_list3[i], my_list3[j] = my_list3[j], my_list3[i]
print(my_list3)
                   
