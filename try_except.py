# def div42by(divideBy):
#     try:
#         return 42 / divideBy
#     except ZeroDivisionError:
#         print('Error: You tried to divide by zero.')
#
# print(div42by(2), '\n')
# print(div42by(12), '\n')
# print(div42by(0), '\n')
# print(div42by(1))

print('How many cats you have?')
numCats = input()
try:
    if int(numCats) >= 4:
        print('That is a lot of cats!')
    elif int(numCats) <= -1:
        print('You wrote a negative number.')
    else:
        print('That is not that many cats.')
except ValueError:
    print('You did not enter a number, try again.')