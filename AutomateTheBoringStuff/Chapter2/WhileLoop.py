print('Enter your name')
while True:
    name = input()
    if name.lower() != 'rob':
        continue
    print('Hello ' + name + ', please enter your password')
    password = input()
    if password == 'password':
       break
    else:
        print('Access Denied!')
print('Access Granted, program exiting....') 