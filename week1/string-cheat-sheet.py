# %%
# how to create a string in python?
my_string = 'hello'
print(my_string)

my_string = "hello"
print(my_string)

my_string = '''hello'''
print(my_string)

my_string = """hello"""
print(my_string)

# %%
# format string in python
print("Hello {name}".format(name=my_string))


# %%
# How to access caracters in a string
string1 = 'programming'

# %%
# first character
print('string1[0]', string1[0])
# last character
print('string1[-1]', string1[-1])

# slicing 2nd to 5th character
print('string1[1:5]', string1[1:5])

# slicing 6th to 2nd character
print('string1[5:2] ', string1[5:-2])

#String is immutable
my_string = 'hello'
# my_string[0] = 'a'  <- this is not correct

# Delete the entire string
del my_string
print(my_string)


# %%
# How to concatenate two strings
string1 = 'hello'
string2 = 'world'
print('string1 +string2', string1+string2)

count = 0
for idx, letter in enumerate('hello world'):
    if letter == 'l':
        count += 1

print(count, 'letters founds')

# %%
# check char in member
print('a' in 'programming')

# %%
print('pr' not in 'programming')

# %%
# built-in functions of python
print('len(string1) = ', len(string1))

# enumerate a string
print('list(enumerate(string1)))', list(enumerate(string1)))
print('[enumerate(string1)]', [e for e in string1])

# %%
# Escape special symbols
# He said, "what's there?"
print('what\'s there ?')

# formatting integers 
print("Binary representation of {0} is {0:b}".format(12))
