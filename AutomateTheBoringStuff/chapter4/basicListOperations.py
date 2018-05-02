#The comma at the end is on purpose and it works fine.
aList3 = [1,2,3,4,5,6,7,8,80,90,100,9,10,20,30,40,50,60,70,]

def printOut(x, y):
    if y is not None:
        print(str(y))
    for a in x:
        print('****' + str(a) + '****')
    print('========== END ==========')

   
printOut(aList3, 'printing out the list as is\n')    
printOut(aList3, None)  
##Preferring to use sorted over the sort operation on the list. sort() mutates the list in place.
aListSorted3 = sorted(aList3, reverse=True)  
print(aListSorted3, 'Printing Sorted in order')
    
