# %%
"""
- By convention, we generally use tuple for  different datatypes 
and list for similar datatypes
- Since tuple are immutable,  then iteration througth tuple
is faster than with list!!!
- Tuple that contain immutables elements can be used as key for a 
dictionary. With list, this is  NOT possible.
- If you have  data that doesn't change, implementing  
it as tuple will GUARANTEE that is remains write-protected
"""

# Empty tuple
tuple = ()
print(tuple)


# Tuple containing integers
tuple1 = (1, 2, 3)
print(tuple1)


# Tuple with mixed datatypes
tuple1 = (1, 'hello', 3.4)
print(tuple1)

# Nested tuple
tuple1 = ('mouse', [8, 4, 6], (1, 2, 3))
print(tuple1)

# %%
# How to check 'type' in python
print(type(tuple))


# Create a tuple is not necessary to use '( )'
tuple2 = 1, 2, 3
print(type(tuple2))


#Creating a tuple with one element
tuple3 = 1,
print(type(tuple3))