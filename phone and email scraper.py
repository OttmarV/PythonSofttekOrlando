import re, pyperclip
from warnings import resetwarnings
from typing import Text

#TODO: Create a regx for phone numbers
phoneRegex = re.compile('''
(
    ((\d\d\d)|(\(\d\d\d\)))?    #area code (optional)
(\s|-)   #first separator
\d\d\d   #first 3 digits
-        #separator
\d\d\d\d   #last 4 digits
((ext(\.)?\s|x)    #extension word-part (optional)
(\d{2,5}))?    #extension number-part (optional)
)
''', re.VERBOSE)

#TODO: Create a regex for email addresses
emailRegex = re.compile('''
[a-zA-Z0-9.+]+ #name part
@               # @ symbol
[a-zA-Z0-9.+]+ #domain name part
''', re.VERBOSE)

#TODO: Get the text off the clipboard
text = pyperclip.paste()

#TODO Extract the email/phonee from this text
extractedPhone = phoneRegex.findall(text)
extractedEmail = emailRegex.findall(text)

#print(extractedPhone)
print(extractedEmail)

allPhoneNumbers = []
for phoneNummber in extractedPhone:
    allPhoneNumbers.append(phoneNummber[0])

print(allPhoneNumbers)

results = '\n'.join(allPhoneNumbers) + '\n' + '\n'.join(extractedEmail)
pyperclip.copy(results)