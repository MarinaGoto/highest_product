
# coding: utf-8

# In[1]:


def pr(arr, n):
    n = len(arr)
    arr.sort()
    a = {}

    r = arr[n-1]
    s = arr[n-2]
    d = arr[n-3]
    product = r*s*d
    return {product}


# In[2]:


arr = [1, 10, 2, 6, 5, 3]
q = pr(arr, 6)
print(q)


# In[3]:


arr = [10, 9, 2, 1, 0, 3]
q = pr(arr, 6)
print(q)


# In[4]:


arr = [-1, -10, 2, 6, 5, 3]
q = pr(arr, 6)
print(q)


# In[5]:


arr = [1, -10, 2, -6, 5, 3]
q = pr(arr, 6)
print(q)


# In[6]:


arr = [1, -10, -2, -6, -5, 3]
q = pr(arr, 6)
print(q)


# In[7]:


arr = [-1, -10, -2, -6, -5, -3]
q = pr(arr, 6)
print(q)


# In[8]:


arr = [1, -10, 10, -6, 5, 6]
q = pr(arr, 6)
print(q)


# In[9]:


def pr(arr, n):
    n = len(arr)
    arr.sort()
    a = {}

    max1 = arr[n-1]
    max2 = arr[n-2]
    max3 = arr[n-3]
    min1 = arr[n-6]
    min2 = arr[n-5]
    
    product1 = max1*max2*max3
    product2 = min1*min2*max1

    if product1 >= product2:
        return {product1}
    else:
        return {product2}
    


# In[10]:


arr = [1, 10, 2, 6, 5, 3]
q = pr(arr, 6)
print(q)


# In[11]:


arr = [10, 9, 2, 1, 0, 3]
q = pr(arr, 6)
print(q)


# In[12]:


arr = [-1, -10, 2, 6, 5, 3]
q = pr(arr, 6)
print(q)


# In[13]:


arr = [1, -10, 2, -6, 5, 3]
q = pr(arr, 6)
print(q)


# In[14]:


arr = [1, -10, -2, -6, -5, 3]
q = pr(arr, 6)
print(q)


# In[15]:


arr = [-1, -10, -2, -6, -5, -3]
q = pr(arr, 6)
print(q)


# In[16]:


arr = [1, -10, 10, -6, 5, 6]
q = pr(arr, 6)
print(q)


# In[17]:


arr = [0, -10, -10, -6, -5, -6]
q = pr(arr, 6)
print(q)


# In[23]:


def pr(arr, n, s):
    arr.sort()
    a = {}

    max1 = arr[n-1]
    max2 = arr[n-2]
    max3 = arr[n-3]
    min1 = min(arr)
    min2 = s
    
    product1 = max1*max2*max3
    product2 = min1*min2*max1

    if product1 >= product2:
        return {product1}
    else:
        return {product2}
    


# In[24]:


arr =  [-1, -100, -2, -6, -5, 100]
n = len(arr)
s = sorted(arr)[1] #find the second smallest integer 

q = pr(arr, n, s)

print(q)


# In[25]:


arr =  [-10, -12, -2, -6, -5, 100]
n = len(arr)
s = sorted(arr)[1] #find the second smallest integer 

q = pr(arr, n, s)

print(q)


# In[26]:


arr =  [-1, -30, -2, 6, -1, 10]
n = len(arr)
s = sorted(arr)[1] #find the second smallest integer 

q = pr(arr, n, s)

print(q)


# In[27]:


arr =  [11, -3, -2, -6, -5, 70]
n = len(arr)
s = sorted(arr)[1] #find the second smallest integer 

q = pr(arr, n, s)

print(q)


# In[30]:


#    V2

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
    
    


# In[31]:



arr = [1, -2, -3, 4]
n = len(arr)

q = pr(arr, n, s)
print(q)

