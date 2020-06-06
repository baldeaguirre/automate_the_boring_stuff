for i in range(4):
    print(i, '\n')

print(list(range(4)), '\n')

spam = list(range(0, 100, 2))
print(spam, '\n')

supplies = ['pens', 'staplers', 'flame-throwers', 'binders']
print(supplies, '\n')

for i in range(len(supplies)):
    print('Index ' + str(i) + ' in supplies is: ' + supplies[i], '\n')

# Multiple assignment
cat = ['fat', 'orange', 'loud']
size, color, disposition = cat
print(size)
print(color)
print(disposition, '\n')
size, color, disposition = 'skinny', 'black', 'quiet'

# Swapping values
a = 'AAA'
b = 'BBB'
a, b = b, a
print('a = ', a)
print('b = ', b, '\n')

# Augmented operators
spam = 10
spam += 1
print(spam)