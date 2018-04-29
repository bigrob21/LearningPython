aList2 = [1,2,3,4,5,6,7,8,9,10,20,30,40,50,60,70,80,90,100]

print('Showing you the list - ' + str(aList2))
print('Showing the list via slicing from the 5th element to the end of it --> ' + str(aList2[4:len(aList2)]))
print('First element in the list is = ' + str(aList2[0]) + ' .Now changing it to 1000')
aList2[0] = 1000
print('Now the first element is == ' + str(aList2[0]))