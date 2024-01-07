# Recursion is a function that calls itself.

# Example 1: Factorial. Looping Solution
def find_factorial_by_looping(n):
    if n<0:
        return 0
    else:
        factorial = 1
        for i in range(1,n+1):
            factorial = factorial*i
        return factorial
    
print(find_factorial_by_looping(5))

# Example 2: Factorial. Recursive Solution. Function calls itself.
def find_factorial_by_recursion(n):
    if n == 1:
        return 1
    else:
        return n * find_factorial_by_recursion(n-1)
print(find_factorial_by_recursion(5))


# Recursive function for Tower of Hanoi
def hanoi(disks, source, helper, destination):
    # Base Condition
    if (disks == 1):
        print('Disk {} moves from tower {} to tower {}.'.format(disks, source, destination))
        return

    # Recursive calls in which function calls itself
    hanoi(disks - 1, source, destination, helper)
    print('Disk {} moves from tower {} to tower {}.'.format(disks, source, destination))
    hanoi(disks - 1, helper, source, destination)

# Driver code
disks = int(input('Number of disks to be displaced: '))
'''
Tower names passed as arguments:
Source: A
Helper: B
Destination: C
'''
# Actual function call
hanoi(disks, 'A', 'B', 'C')

