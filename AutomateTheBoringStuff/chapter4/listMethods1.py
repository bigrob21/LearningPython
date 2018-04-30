aList4 = ['Dog', 'Cat', 'Fish', 'Shark', 'Sugar Glider', 'Three Toed Sloth']
print(aList4)
print(aList4.index('Cat'))
aList4.append('Ferret')
print(aList4)
idx = aList4.index('Ferret')
if idx is None:
    print('No match found')