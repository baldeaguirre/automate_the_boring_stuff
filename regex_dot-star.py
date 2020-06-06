import re

beginsWithHelloRegex = re.compile(r'^Hello') # ^ sign at the beginning of the string
mo = beginsWithHelloRegex.search('Hello there!')
print(mo.group())
mo = beginsWithHelloRegex.search('He said: "Hello!"')
print(mo, '\n')

endsWithWorldRegex = re.compile(r'world!$') # $ sign at the end of the string
mo = endsWithWorldRegex.search('Hello world!')
print(mo.group())
mo = endsWithWorldRegex.search('Hello world!, how are you?')
print(mo, '\n')

allDigitsRegex = re.compile(r'^\d+$')
mo = allDigitsRegex.search('7813647834')
print(mo.group())
mo = allDigitsRegex.search('78136x47834')
print(mo)
allDigitsRegex =  re.compile(r'^\d+\w+$')
mo = allDigitsRegex.search('78136x47834')
print(mo.group(), '\n')

atRegex = re.compile(r'.at')
print(atRegex.findall('The cat in the hat sat on the flat mat.'))
atRegex = re.compile(r'.{1,2}at')
print(atRegex.findall('The cat in the hat sat on the flat mat.'), '\n')

info = '''First Name: Baldemar Last Name: Aguirre Fraire
          First Name: Baldemar Last Name: Aguirre Fraire
          First Name: Baldemar Last Name: Aguirre Fraire'''
nameRegex = re.compile(r'First Name: (.*) Last Name: (.*)')
print(nameRegex.findall(info), '\n')

serve = '<To serve humans> for dinner.>'
nongreedy = re.compile(r'<.*?>')
print(nongreedy.findall(serve))
greedy = re.compile(r'<.*>')
print(greedy.findall(serve), '\n')

prime = 'Serve the public trust. \nProtect the innocent. \nUphold the law'
dotStar = re.compile(r'.*')
mo = dotStar.search(prime)
print(mo.group(), '\n')
dotStar = re.compile(r'.*', re.DOTALL)
mo = dotStar.search(prime)
print(mo.group(), '\n')

string = 'Al, why does your programming book talk about RoboCop so much?'
vowelRegex = re.compile(r'[aeiou]')
print(vowelRegex.findall(string))
vowelRegex = re.compile(r'[aeiou]', re.I)
print(vowelRegex.findall(string))