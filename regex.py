'''
The ? says the group matches zero or one times.
The * says the group matches zero or more times.
The + says the group matches one or more times.
The curly braces can match a specific number of times.
The curly braces with two numbers matches a minimum and maximum number of times.
Leaving out the first or second number in the curly braces says there is no minimum or maximum.
"Greedy matching" matches the longest string possible, "nongreedy matching" (or "lazy matching") matches the shortest string possible.
Putting a question mark after the curly braces makes it do a nongreedy/lazy match.

Groups are created in regex strings with parentheses.
The first set of parentheses is group 1, the second is 2, and so on.
Calling group() or group(0) returns the full matching string, group(1) returns group 1's matching string, and so on.
Use \( and \) to match literal parentheses in the regex string.
The | pipe can match one of many possible groups.

The regex method findall() is passed a string, and returns all matches in it, not just the first match.
If the regex has 0 or 1 group, findall() returns a list of strings.
If the regex has 2 or more groups, findall() returns a list of tuples of strings.
\d is a shorthand character class that matches digits. \w matches "word characters" (letters, numbers, and the underscore). \s matches whitespace characters (space, tab, newline).
The uppercase shorthand character classes \D, \W, and \S match charaters that are not digits, word characters, and whitespace.
You can make your own character classes with square brackets: [aeiou]
A ^ caret makes it a negative character class, matching anything not in the brackets: [^aeiou]

^ means the string must start with pattern, $ means the string must end with the pattern. Both means the entire string must match the entire pattern.
The . dot is a wildcard; it matches any character except newlines.
Pass re.DOTALL as the second argument to re.compile() to make the . dot match newlines as well.
Pass re.I as the second argument to re.compile() to make the matching case-insensitive.


The sub() regex method will substitute matches with some other text.
Using \1, \2 and so will substitute group 1, 2, etc in the regex pattern.
Passing re.VERBOSE lets you add whitespace and comments to the regex string passed to re.compile().
If you want to pass multiple arguments (re.DOTALL , re.IGNORECASE, re.VERBOSE), combine them with the | bitwise operator.

'''


# Search for lines that contain 'From'
import re
hand = open('mbox-short.txt')
count = 0
for line in hand:
    line = line.rstrip()
    if re.search('^From:.+@', line):
        print(line)
        count += 1

print(count)


s = 'A message from csev@umich.edu to cwen@iupui.edu about meeting @2PM'
lst = re.findall('\S+@\S+', s)
print(lst)

# Search for lines that start 'X' followed by any non whitespace
# characters and ':' then output the first group of non whitespace
# characters that follows
hand = open('mbox-short.txt')
count = 0
for line in hand:
    line = line.rstrip()
    
    x = re.findall('^X\S*: (\S+)', line)
    if not x: continue
    print(x)
    count += 1
print(count)

  
# Search for lines that start with 'X' followed by any non
# whitespace characters and ':'
# followed by a space and any number.
# The number can include a decimal.
hand = open('mbox-short.txt')
for line in hand:
    line = line.rstrip()
    if re.search('^X\S*: [0-9.]+', line):
        print(line)



# Search for lines that start with 'Details: rev='
# followed by numbers and '.'
# Then print the number if it is greater than zero
hand = open('mbox-short.txt')
for line in hand:
    line = line.rstrip()
    x = re.findall('^Details:.*rev=([0-9.]+)', line)
    if len(x) > 0:
        print(x)


# Search for lines that start with From and a character
# followed by a two digit number between 00 and 99 followed by ':'
# Then print the number if it is greater than zero
hand = open('mbox-short.txt')
for line in hand:
    line = line.rstrip()
    x = re.findall('^From .* ([0-9][0-9]):', line)
    if len(x) > 0: print(x)



# Search for lines that contain 'Author:' followed by any characters,
# an at sign, and any non whitespace character
# Then print the character group that follows the at sign
hand = open('mbox-short.txt')
for line in hand:
    line = line.rstrip()
    x = re.findall('Author:.*@(\S+)', line)
    if not x: continue
    print(x)


# Search for lines that contain 'New Revision: ' followed by a number
# Then turn the number into a float and append it to nums
# Finally print the length and the average of nums
'''
fname = input('Enter file:')
hand = open(fname)
nums = list()
for line in hand:
    line = line.rstrip()
    x = re.findall('New Revision: ([0-9]+)', line)
    if len(x) == 1:
        val = float(x[0])
        nums.append(val)
print(len(nums))
print(int(sum(nums)/len(nums)))
'''
count = 0
hand = open('mbox-short.txt')
for line in hand:
    line = line.rstrip()
    x = re.findall('^Date:.*(10|11):(\d\d):(\d\d)', line)
    if not x: continue
    print(x)
    count += 1
print(count)


phoneNumRegex = re.compile(r"(\d\d\d)-(\d\d\d-\d\d\d\d)")
mo = phoneNumRegex.search("My number is 415-555-4242")
print(phoneNumRegex)
print(type(phoneNumRegex))
print(mo.group())
print(mo.group(1))
print(mo.group(2))