# This program creates a method that, given a list of integers, returns the highest product between 3 of those numbers.

# Greeting fist 
def greeting(n):
    print('Hello', n,'!')

name = (input('Please write your name:    '))
greeting(name)

def pr(arr, n):
    arr.sort()
    a = {}

    max1 = arr[n-1]
    max2 = arr[n-2]
    max3 = arr[n-3]
    min1 = arr[0]
    min2 = arr[1]

    
    product1 = max1*max2*max3
    product2 = min1*min2*max1

    if product1 >= product2:
        return {product1}
    else:
        return {product2}
    
    
        
arr = [int(x) for x in input('Please enter a list of numeric values divided by empty space:    ').split()]
n = len(arr)

q = pr(arr, n)
print('The highest product of the list:',q)
print('Thank you for your time!')