#Note tuples are declared with the open and close parenthesis. Not the square brackets for Python lists. 
## Another major difference between TUPLES and LISTS are TUPLES are immutable once created.
fooTuple = ('Rob', 21, 2014)
print(str(fooTuple))

print('First element in the tuple: ' + fooTuple[0])
print(fooTuple[0:len(fooTuple)])

## This is not going to go well due to the mutability restriction of a tuple!!
try:
    fooTuple[0] = 'FoobBared'
except TypeError as e:
    print('See I told you so you cannot mutate a tuple!!! Python Error => ' + str(e))