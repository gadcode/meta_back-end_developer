# Control Flow and Conditionals
# Math and Logical Operators

from math import factorial


num_factorial = factorial(5)
print(num_factorial)
print('\n')


# The order in which namespaces are scanned 
# when looking for a name:
#   local, enclosing, global, built-in (LEGB)
n = 3
address = '221b Baker Street, NW1 6XE, London'
employee = {
    'age': 45,
    'role': 'CTO',
    'SSN': 'AB1234567',
}

print(n)
print(address)
print(employee)


# Scopes
# Local versus Global scopes
def local():
    m = 7
    print(m)
    
m = 5
print(m)    #=> 5
local()     #=> 7

# Example Two
def local_two():
    print(m, 'printing from the local scope')

m = 6
print(m, 'printing from the global scope')

local_two()
print('\n')


# Local, Enclosing, and Global
def enclosing_func():
    m = 13
    def local():
        print(m, 'printing from the local scope')
        
    local()

m = 5
print(m, 'printing from the global scope')

enclosing_func()
print('\n')


# The Zen of Python
import this


print(this)
# --------------------------------------------------
# The Zen of Python, by Tim Peters

# Beautiful is better than ugly.
# Explicit is better than implicit.
# Simple is better than complex.
# Complex is better than complicated.
# Flat is better than nested.
# Sparse is better than dense.
# Readability counts.
# Special cases aren't special enough to break the rules.
# Although practicality beats purity.
# Errors should never pass silently.
# Unless explicitly silenced.
# In the face of ambiguity, refuse the temptation to guess.
# There should be one-- and preferably only one --obvious way to do it.
# Although that way may not be obvious at first unless you're Dutch.
# Now is better than never.
# Although never is often better than *right* now.
# If the implementation is hard to explain, it's a bad idea.
# If the implementation is easy to explain, it may be a good idea.
# Namespaces are one honking great idea -- let's do more of those!
# X------------------X---------------------X----------------------X
