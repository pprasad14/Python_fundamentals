import re

string = "Prem 14 Prasad"
reg = r'\d+'
reg_start = r'^\w+'
reg_end = r'\w+$'

re.search(reg,string)


# .match()

list = ["prem99 prasad", "prem99 prem", "prem prakash"]
for element in list:
    z = re.match("(p\w+)\W(p\w+)", element)
    if z:
        print((z.groups()))
    

# .search()
        
patterns = ['Prem', 'Prasad']
text = 'Prem is fun?'
for pattern in patterns:
    print('Looking for "%s" in "%s" ->' % (pattern, text), end=' ')
    if re.search(pattern, text):
        print('found a match!')
else:
    print('no match')

abc = 'guru99@google.com, careerguru99@hotmail.com, users@yahoomail.com'
emails = re.findall(r'[\w\.]+@[\w\.]+', abc)
for email in emails:
    print(email)
  
print(re.findall(reg,string))
print(re.findall(reg_start,string))
print(re.findall(reg_end,string))

xx = "guru99,education is fun"
r1 = re.findall(r"^\w+", xx)
#print((re.split(r'\s','we are splitting the words')))


regex = r"([a-zA-Z]+) (\d+)"

if re.search(regex, "June 24"):
    match = re.search(regex, "2June 243")
    
    print("Match at index %s, %s" % (match.start(), match.end()))
    print("Full match: %s" % (match.group(0)))
    print("Month: %s" % (match.group(1)))
    print("Day: %s" % (match.group(2)))
else:
    # If re.search() does not match, then None is returned
    print("The regex pattern does not match. :(")
    
# using findall()
# Lets use a regular expression to match a few date strings.

regex = r"[a-zA-Z]+ \d+"
matches = re.findall(regex, "June 24, August 9, Dec 12")
for match in matches:
    # This will print:
    #   June 24
    #   August 9
    #   Dec 12
    print("Full match: %s" % (match))
    
# To capture the specific months of each date we can use the following pattern
regex = r"([a-zA-Z]+) \d+"
matches = re.findall(regex, "June 24, August 9, Dec 12")
for match in matches:
    # This will now print:
    #   June
    #   August
    #   Dec
    print("Match month: %s" % (match))
    
# If we need the exact positions of each match
regex = r"([a-zA-Z]+) \d+"
matches = re.finditer(regex, "June 24, August 9, Dec 12")
for match in matches:
    # This will now print:
    #   0 7
    #   9 17
    #   19 25
    # which corresponds with the start and end of each match in the input string
    print("Match at index: %s, %s" % (match.start(), match.end()))
    
#finding an replacing strings
    
regex = r"([a-zA-Z]+) (\d+)"
print(re.sub(regex,r'\2 of \1','June 24, August 9, Dec 12')) #changes all matches

#to change 'count' no of matches

print(re.sub(regex,r'\2 of \1','June 24, August 9, Dec 12',count = 2))


#compiling a regular expression for performance
regex = re.compile(r"(\w+) World")
result = regex.search("Hello World is the easiest")

if result:
    print(result.start(), result.end())
    
for result in regex.findall("Hello World, Bonjour World"):
    print(result)
    
# This will substitute "World" with "Earth" and print:
print(regex.sub(r"\1 Earth", "Hello World"))

    
# Python Flags

xx = """prem 
prasad	
kumar"""
k1 = re.findall(r"^\w", xx)
k2 = re.findall(r"^\w", xx, re.MULTILINE)
print(k1)
print(k2)