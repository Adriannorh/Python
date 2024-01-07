list = [1, 2, 3, 4, 5, 6, 7, 8, 9]

# create a divide and conquer function to find the index of the highest number in a list
def divide_and_conquer(lst):
    if len(lst) == 1:
        return lst[0]
    else:
        mid = len(lst) // 2
        left = lst[:mid]
        right = lst[mid:]
        return max(divide_and_conquer(left), divide_and_conquer(right))

print(divide_and_conquer(list))


list2 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]

# create a divide and conquer function to find the highest number in a list
def divide_and_conquer2(lst):
    n = len(lst)
    if n == 1:
        return lst[0]
    else:
        mid1 = n // 3
        mid2 = 2 * n // 3
        left = lst[:mid1]
        middle = lst[mid1:mid2]
        right = lst[mid2:]
        return max(divide_and_conquer(left), divide_and_conquer(middle), divide_and_conquer(right))

print(divide_and_conquer2(list2))


# Use Python's built-in max() function to find the maximum number in the list
lst = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

max_number = max(lst)

print(max_number)



z = ["alpha","bravo","charlie"]
new_z = [i[0]*2 for i in z]
print(new_z)