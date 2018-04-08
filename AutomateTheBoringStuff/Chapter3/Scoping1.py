def func1():
    value = 1
    return value

## Ok so this gets the point across but always avoid using variables with the same name!!!

value = 100
print('Local variable of func1 is ' + str(func1()))
print('Global scoped variable ' + str(value))