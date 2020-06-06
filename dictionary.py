myCat = {'size': 'fat',
         'color': 'gray',
         'disposition': 'loud'}

print(myCat['size'], '\n')
print('My cat has ' + myCat['color'] + ' fur.', '\n')

print('size' in myCat)
print('size' not in myCat, '\n')

print(list(myCat.keys()))
print(list(myCat.values()))
print(list(myCat.items()), '\n')

for k in myCat.keys():
    print(k)
print('\n')

for v in myCat.values():
    print(v)
print('\n')

for k, v in myCat.items():
    print(k, v)
print('\n')

print('fat' in myCat.values(), '\n')

print(myCat.get('size'))
print(myCat.get('age'), '\n')

myCat.setdefault('age', 3)
# myCat['age'] = 3
print(myCat, '\n')