number = int(input())

divisor = 2

print(str(number) + '=', end='')

firstDivisor = True

while number > 1:
    if number % divisor == 0:
        if not firstDivisor:
            print('*', end='')
        else:
            firstDivisor = False
        print(divisor, end='')
        number //= divisor
    else:
        divisor += 1
print()
