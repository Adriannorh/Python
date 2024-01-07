menu = ['espresso', 'americano', 'caffelatte', 'mocha', 'cappuccino']

def find_coffee(coffee):
    if coffee[0] == 'c':
        return coffee 
    

""" map_coffee = map(find_coffee, menu)
print(map_coffee)
for x in map_coffee:
    print(x) """

filter_coffee = filter(find_coffee, menu)
print(filter_coffee)
for x in filter_coffee:
    print(x)


# Maps takes all the elements in a list and applies a function to them, returning a new list with the updated elements.
# Filters takes all the elements in a list and runs that through a function to create a new list with only the elements that return True in that function.