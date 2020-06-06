import re

data = '''State	Office Name/Address	Manager	Phone/Fax	
Region/Regional Office
AK	Anchorage Field Office
3000 C Street
Suite 401
Anchorage, AK 99503	COLLEEN K. BICKFORD
Field Office Director	
(907) 677-9800
Email 
Fax
(907) 677-9803

Region X
Seattle WA
AL	Birmingham Field Office
950 22nd Street North
Suite 900
Birmingham, AL 35203-5302	KENNETH E. FREE
Field Office Director	(205) 731-2617
Email
Fax
(205) 731-2593	
Region IV
Atlanta GA
AR	Little Rock Field Office
425 West Capitol Avenue
Suite 1000
Little Rock, AR 72201-3488	WANDA C. MERRITT
Field Office Director	(501) 918-5700
Email
Fax
(501) 324-6142	
Region VI
Ft. Worth TX'''

phoneRegex = re.compile(r'\(\d\d\d\) \d\d\d-\d\d\d\d')
print(phoneRegex.findall(data), '\n')

phoneRegex = re.compile(r'(\(\d\d\d\)) (\d\d\d-\d\d\d\d)')
print(phoneRegex.findall(data), '\n')

phoneRegex = re.compile(r'((\(\d\d\d\)) (\d\d\d-\d\d\d\d))')
print(phoneRegex.findall(data), '\n')

lyrics = '''12 drummers drumming, 11 pipers piping, 10 lords a-leaping, 9 ladies dancing, 8 maids a-milking, 
7swans a-swimming, 6 geese a-laying, 5 golden rings, 4 calling birds, 3 french hens, 2 turtle doves, and
1 partridge in a pear tree'''

xmasRegex =  re.compile(r'\d+\s\w+')
print(xmasRegex.findall(lyrics), '\n')

vowelRegex = re.compile(r'[aeiouAEIOU]') # Equal to r'(a|e|i|o|u)'
print(vowelRegex.findall('Robocop eats baby food.'), '\n')

vowelRegex = re.compile(r'[aeiouAEIOU]{2}')
print(vowelRegex.findall('Robocop eats baby food.'), '\n')

# Negative Character Classes
consonantRegex = re.compile(r'[^aeiouAEIOU]')
print(consonantRegex.findall('Robocop eats baby food.'))