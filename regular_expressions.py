import re

message = 'Call me at 415-555-1011 tomorrow, or at 415-555-9999 phone office.'

phoneNumRegex = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')
mo = phoneNumRegex.search(message) # match object
print(mo.group(), '\n')
mo = phoneNumRegex.findall(message)
print(mo, '\n')

message = 'My number is 415-555-4242'

# Regex groups
phoneNumRegex = re.compile(r'(\d\d\d)-(\d\d\d-\d\d\d\d)')
mo = phoneNumRegex.search(message)
print(mo.group(1))
print(mo.group(2), '\n')

message = 'My number is (415) 555-4242'

phoneNumRegex = re.compile(r'\(\d\d\d\) \d\d\d-\d\d\d\d')
mo = phoneNumRegex.search(message)
print(mo.group(), '\n')

# Pipe character
string = 'Batmobile lost a wheel'

batRegex = re.compile(r'Bat(man|mobile|copter|bat)')
mo = batRegex.search(string)
print(mo.group())
print(mo.group(1))