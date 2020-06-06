# spam = 42 # Global variable
#
# def eggs():
#     spam = 42 # Local variable

# def spam():
#     eggs = 99
#     print(eggs)
#     print(bacon(), '\n')
#
# def bacon():
#     ham = 101
#     eggs = 0
#     return eggs
#
# spam()
#print(bacon())

eggs = 42 # Global variable

def spam():
    #global eggs # Defining the variable as global
    eggs = 99 # Local variable
    print(eggs, '\n')

spam()
print(eggs)