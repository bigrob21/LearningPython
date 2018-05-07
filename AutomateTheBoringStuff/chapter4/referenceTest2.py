import copy
import sys

eggs = ['Rob', 'Da', 'PYTHON', 'dEv3lop3R']

## Defining a custom exception class in Python
class UncheckedExceptionError(Exception):pass

def printColl(c):
    print(str(c))

print(printColl(eggs))

eggs2 = copy.copy(eggs)
eggs2.append('And')
eggs2.append("Don't")
eggs2.append('forget')
eggs2.append('Java!!')

printColl(eggs)
printColl(eggs2)

## This should not be true if it is we have a problem!!!
if eggs == eggs2:
    raise UncheckedExceptionError('Oh Oh, eggs and eggs2 should not be the same reference. Exiting now!!!')





