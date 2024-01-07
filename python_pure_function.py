# not a pure function 

""" my_list = [1, 2, 3]

def add_to_list(item):
    return my_list.append(item)

add_to_list(4)
add_to_list(5)
print(my_list)
 """
# pure function

my_list = [1, 2, 3]

def add_to_list(lst, item):
    nl = lst.copy()
    nl.append(item)
    return nl

new_list = add_to_list(my_list, 4)

print(my_list)
print(new_list)

