#! python3
print("What is your name?")
myName = input()
print("It is good to meet you, " + myName, '\n')
print("The length of your name is:", len(myName), '\n')

print("What is your age?")
myAge = input()
print("You will be " + str(int(myAge) + 1) + " in a year.") # Concatenates the int value of myAge + 1 as string