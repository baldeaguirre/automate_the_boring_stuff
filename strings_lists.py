# String concatenetion
name = 'Zophie a cat'
newName = name[0:7] + 'the' + name[8:12]
#print(newName, '\n')

def eggs(cheese):
    cheese.append(4)
    return cheese

import copy
spam = [1, 2, 3]
# print(spam)
print(eggs(spam))
print(spam, '\n')

import copy
cheese = copy.deepcopy(spam)
# print(id(spam))
# print(id(cheese))
cheese[0] =  4
print(cheese)
print(spam)