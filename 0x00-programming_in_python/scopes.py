# Local, Enclosed, Global, Built-in

# Local scope
def get_total(a, b):
    # local variable declared inside a function
    total = a + b
    return total

print(get_total(5, 2))      # 7

# To access variable outside of the function
# print(total)
# NameError: name 'total' is not defined


# Enclosed scope
def get_total(a, b):
    # enclosed variable declared inside a function
    total = a + b
    
    def double_it():
        # local variable
        double = total * 2
        print(double)
    
    double_it()
    # double variable is not accessible from here
    # print(double)
    
    return total

get_total(4, 5)
# 18
# NameError: name 'double' is not defined. Did you mean: 'double_it'?


# Global scope
special = 5

def get_total(a, b):
    # enclosed scope variable inside a function
    total = a + b
    print(special)
    
    def double_it():
        # local variable
        double = total * 2
        print(special)
    
    double_it()
    
    return total

get_total(10, 15)   # 5 5
get_total(6, 6)     # 5 5


# Built-in scope
# def
# print
# for
# in
