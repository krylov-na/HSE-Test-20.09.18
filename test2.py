a = int(input())
b = int(input())

diff = a ^ b

numOfBits = 0

while diff > 0:
    numOfBits += diff % 2
    diff //= 2

print(numOfBits)
