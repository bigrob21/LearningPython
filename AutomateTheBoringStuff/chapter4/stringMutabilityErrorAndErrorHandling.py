import random

aString = 'Rob the developer'
print('the size of the string is ' + str(len(aString)))
randomIndex = random.randint(0, len(aString))
print(str(randomIndex))
#This is a no no
try:
    aString[randomIndex] = 'foobar'
    print(aString)
except TypeError as te:
    print('Opps Python does not like this: ' + str(te))
    
