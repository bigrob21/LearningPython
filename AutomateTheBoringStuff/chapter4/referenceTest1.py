eggs = ['Mr.', 'Roboto']
spam = eggs

if eggs == spam:
    print('SPAM and EGGS are equal referring to the same reference!!!')

spam.append('Arigato')

print(str(eggs))
print(str(spam))

eggs = tuple(eggs)
spam = eggs

