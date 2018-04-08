print('Enter a name')
name = input()
if name.lower() == 'rob':
    print('Hello Rob!')
print('Please enter password - ' + name)
password = input()
if password == 'swordfish':
    print('Access Granted...')
else:
    print('Access Denied...')
    