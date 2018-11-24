# %%
# Empty list
list1 = []

list1 = ['mouse', [2, 4, 6], ['a']]
print(list1)
print(list1[1][1])

# %%
# How to access elements in list
list2 = ['p', 'r', 'o', 'b', 'l', 'e', 'm']
print(list2[4])


# Slicing in a list
print(list2[:-5])

# %%
# List  is muaable
odd = [2, 4, 6, 8]
odd[0] = 1
print(odd)
odd[1:4] = [3, 5, 7]
print(odd)

# Append and extend can be also done in list
odd.append(9)
print(odd)
odd.extend([11, 13])
print(odd)

# Insert an element into a list
odd = [1, 9]
odd.insert(1, 3)
print(odd)

odd[2:2] = [5, 7]
print(odd)


# %%
# How to delete or remove elements from a list?
del odd[0]
print(odd)

# %%
# Clear
odd.clear()
print(odd)

# %%
# Sort a list
numbers = [1, 5, 2, 4]
numbers.sort()
print(numbers)


# %%
# An element way to create a list
pow2 = [2**x for x in range(10)]
print(pow2)


pow2 = [2 ** x for x in range(10) if x > 5]
print(pow2)

#%%
#Membership in list 
print(2 in pow2)
print(2 not in pow2)

#%%
# Iterate through in a list 
for fruit in ['apple', 'banana', 'orange' ]:
    print('I like', fruit)