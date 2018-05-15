pets = {"Fido":"Dog", "Marvy":"Cat","Goldy":"Fish"}

def getValues(p):
    x = []
    for v in p.values():
        x.append(v)
    return x

def getKeys(p):
    y = []
    for x in p.keys():
        y.append(x)
    return y

'''
Note that getItems deals with tuples of key/value pairs. In this function I start with a list
then append tuples to the list. Finally when returning return a tuple of k/v pairs. 
'''
def getItems(p):
    z = []
    for k,v in p.items():
        z.append((k,v))
    return tuple(z)

print('Printing the keys of pets ' + str(getKeys(pets)))
print('Printing the values of pets ' + str(getValues(pets)))
print('Printing the items of pets ' + str(getItems(pets)))


