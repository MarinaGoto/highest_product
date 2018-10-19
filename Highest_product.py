# This program creates a method that, given a list of integers, returns the highest product between 3 of those numbers.

def pr(arr, n, s):
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
        
        
arr = [1, -2, -3, 4, 7]
n = len(arr)

q = pr(arr, n, s)
print(q)