eggs = [1,2,3]
eggs = [4,5,6]
print(str(eggs) + '... Note the overriding of the list with the second invocation.')

del eggs[2]
del eggs[1]
del eggs[0]
print(str(eggs) + '  note that eggs is now empty, cause I did so.')

eggs.append(7)
eggs.append(8)
eggs.append('foo')
print(str(eggs) + '   New Eggs Values.')