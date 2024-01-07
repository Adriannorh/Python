""" 

string = input('Please enter your name: ') 

print(string)

name = input('What is your name? ') """

a = True 
b = True

if a and b:
    print('a and b are both True')


bill_total = 220

discount = 10
discount2 = 20

if bill_total > 100 and bill_total < 200: 
    print("your bill is greater than 100")
    bill_total = bill_total - discount
elif bill_total > 200:
    print("your bill is greater than 200")
    bill_total = bill_total - discount2
else:
    print("your bill is less than 100")

print("totall bill is: " + str(bill_total))


loyalty_customer = True
total_bill = 150

if loyalty_customer and total_bill > 100:
    #give 20% discount
    total_bill = total_bill - (float(total_bill)/ 100) * 20
elif total_bill > 100:
    #give 10% discount
    total_bill = total_bill - (float(total_bill)/ 100) * 10
else:
    #sorry no discount, 5% service charge applied.
    print('Sorry, no discount ...')

print('Total Bill: ', float(total_bill))



favorites = ['apple', 'banana', 'cherry']

for idx, items in enumerate(favorites):
    print(idx, items)


counter = 0

while counter < len(favorites):
    print("I like ", favorites[counter])
    counter += 1


for i in range(10):
    for j in range(10):
        print(0, end = ' ')
    print()

def sum_of(*args):
    sum = 0
    for i in args:
        sum += i
    return sum
print(sum_of(1,2,3,4,5,6,7,8,9,10))

def sum_off(**kwargs):
    sum = 0
    for k, v in kwargs.items():
        sum += v
    return sum
print(sum_off(coffee=1, tea=2, juice=3, water=4, milk=5, soda=10, beer=20, wine=8, whiskey=9, vodka=10))


def divide_by(a, b):
    return a / b
try:
    ans = divide_by(40, 0)
except ZeroDivisionError as e:
    print(e, 'We cannot divide by zero') 
    print(e.__class__)
except Exception as e:
    print(e, 'Something went wrong')


print(divide_by(40, 2))


file = open('test.txt', mode = "r")

data = file.readline()

print(data)

file.close()


with open('text.txt', mode = "r") as file:
    data = file.readline()
    print(data)

# write to file. remember to close the file after writing to it. and change the mode to 'w' for write.
try:
    with open('newTextFile', mode = 'a') as file:
        file.writelines(['\nThis is a new file created by Python ', '\nThis is the second line'])
except FileNotFoundError as e:
    print(e, 'tits not found motherfucker!!!') 

with open('newTextFile', mode = 'r') as file:
    Lines = file.readlines()
    print(len(Lines))
    for line in Lines:
        print(line)


tits = "big"

if ( "tits" == "big"):
    print("Arnold was here!!")
elif ("tits" == "small"):
    print("Arnold was not here")

print(tits)


def isPalindrome(str):
    startIndex = 0
    endIndex = len(str) - 1

    for x in str:
        if str[startIndex] != str[endIndex]:
            return False
    return True
print(isPalindrome('racecar'))

# create a list

big_list = [1, 2, 3, 4, 5, 6]

def count_elements(lst):
    count = 0
    for element in lst:
        count += 1
    return count

print(f"The list contains {count_elements(big_list)} elements.")


big_list.append(7)
print(f"The list contains {count_elements(big_list)} elements.")

print(len(big_list))

# reverse function
coffees = ['Espresso', 'Cappuccino', 'Latte', 'Mocha', 'Americano']

def reverse(str):
    return str[::-1]

reversed_coffees = map(reverse, coffees)
for x in reversed_coffees:
    print(x)