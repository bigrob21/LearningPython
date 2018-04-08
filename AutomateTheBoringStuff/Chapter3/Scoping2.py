
def spam():
    ## Note the keyword global can be defined within a method to set a global variable. 
    global eggs
    eggs = 'spam'
##Setting global variable since it is not defined in a function
eggs = 'global'
spam()
#eggs = 'global'
print(eggs)

