print('Enter a name')
name = input()
if name.lower() == 'william' or name.lower() == 'will':
    print('How old are you - ' + name + '?')
    age = int(input())
    if age > 4 and age < 100:
        print('You are not ' + name )
    elif age > 100:
        print('Man ' + name.upper() + ' you must be immortal or a Vampire! You cannot be the ' + name.upper + ' that I know...')
    else:
        print('Hello ' + name + ' my son!')
else:
    print('Hello ' + name)