aCollection = [1,2,3,]

def printIt(coll):
    print(str(coll))
    
def printType(t):
    print(str(type(t)))        

def printLineBreaker():
    print('------------------------')

## Original list
printType(aCollection)
printIt(aCollection)
printLineBreaker()

##After converting the list to a tuple
aCollection = tuple(aCollection)
printType(aCollection)
printIt(aCollection)
printLineBreaker()

##After converting the tuple back to a list
aCollection = list(aCollection)
printType(aCollection)
printIt(aCollection)
printLineBreaker()

print('************ Done ************\t')


    