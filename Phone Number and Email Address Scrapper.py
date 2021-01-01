import re, pyperclip

#TODO: Create Regex for phone number

#415-555-0000, (415) 555-0000, ext 12345, ext. 12345, x12345

phoneRegex = re.compile(r'''
(((\d\d\d)|(\(\d\d\d\)))?       #Area code
(\s|-)                         #First separator
\d\d\d                         #First 3 digits
-                              #Separator
\d\d\d\d                       #Last 4 digits
(((ext(\.)?\s)|x)              #extension word part
 (\d{2,5}))?                   #extension number part
)''', re.VERBOSE)

#TODO: Create Regex for email

#some.+_thing@some.+_thing.com

emailRegex = re.compile(r'''
[a-zA-Z0-9.+_]+                #name part
@                              #symbol part
[a-zA-Z0-9.+_]+                #domain name part
''', re.VERBOSE)


#TODO: Get text off the clipboard
text = pyperclip.paste()

#TODO: Extract Phone and email address
extractedPhone = phoneRegex.findall(text)
extractedEmail = emailRegex.findall(text)

allphone = []
for phone in extractedPhone:
    allphone.append(phone[0])

#TODO: Copy extracted email and phone to clipboard
results = '\n'.join(allphone) + '\n' + '\n'.join(extractedEmail)
pyperclip.copy(results)
print("All Phone numbers and Email Addresses copied to clipboard successfully...\nOpen any word document and paste phone numbers and Email Addresses there...!!!")
