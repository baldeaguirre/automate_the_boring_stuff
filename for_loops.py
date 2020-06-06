# While loop
i = 0
while i < 5:
    print("Hello: " + str(i))
    i = i + 1

print('\n')

# For loops
for i in range(5):
    print("Hello: " + str(i))

print('\n')

# Adding values from 0 to 100
total = 0
for num in range(101):
    total = total + num # 0 + 1 + 2...100 = 5050

print(total, '\n')

for i in range(0, 11, 2):
    print(i)

print('\n')

for i in range(5, -1, -1):
    print(i)