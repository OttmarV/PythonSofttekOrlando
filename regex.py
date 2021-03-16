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
