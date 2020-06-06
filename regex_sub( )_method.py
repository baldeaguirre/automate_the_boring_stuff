import re

string = 'Agent Alice gave the secret documents to Agent Bob.'

namesRegex = re.compile(r'Agent \w+')
print(namesRegex.findall(string))
print(namesRegex.sub('REDACTED', string), '\n')

namesRegex = re.compile(r'Agent (\w)\w*')
print(namesRegex.findall(string))
print(namesRegex.sub(r'Agent \1****', string), '\n')

# Verbose Mode
phoneNumber = '(123)456-7890 x1234, (123)456-7890...'

phoneRegex = re.compile(r'''
(
(\d\d\d-) |         # area code (without parenthesis and dash)
(\(\d\d\d\))        # -or- area code (with parenthesis and no dash)
\d\d\d              # first 3 digits
-                   # second dash
\d\d\d\d            # last 4 digits
(\sx\d{2,4})?       # extension, like x1234
)
''', re.IGNORECASE | re.DOTALL | re.VERBOSE)

extractedPhone = phoneRegex.findall(phoneNumber)

allPhoneNumbers = []
for phoneNumber in extractedPhone:
    allPhoneNumbers.append(phoneNumber[0])

print(allPhoneNumbers)