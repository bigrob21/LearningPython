commonDivisor = 40
def divideMe(num):
    try:
        return commonDivisor / num
    except ZeroDivisionError:
        print('Error: ' + 'cannot devide by zero!')

print(divideMe(3))
print(divideMe(100))
print(divideMe(0))
print(divideMe(1))