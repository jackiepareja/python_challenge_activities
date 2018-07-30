#Write a for loop to print each contact in contact_emails.

contact_emails = {
    'Sue Reyn' : 's.reyn@email.com',
    'Mike Filt': 'mike.filt@bmail.com',
    'Nate Arty': 'narty042@nmail.com'
}

for names in contact_emails:
    print(contact_emails[names], 'is', names)
