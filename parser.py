expression = str(input())

expression = expression.split(' ')

i = 0

while i < len(expression):
    expression[i] = int(expression[i])
    i += 2

startNum = int(expression[0])

startOp = expression[1]

pos = 2

while pos + 2 < len(expression):
    op = expression[pos + 1]
    lhs = expression[pos]
    rhs = expression[pos + 2]
    if op == '+' or op == '-':
        if startOp == '+':
            startNum += lhs
        elif startOp == '-':
            startNum -= lhs
        elif startOp == '*':
            startNum *= lhs
        elif startOp == '/':
            startNum /= lhs
        startOp = op
    else:
        if op == '*':
            expression[pos + 2] = lhs * rhs
        elif op == '/':
            expression[pos + 2] = lhs / rhs
    pos += 2

last = expression[pos]
if startOp == '+':
    startNum += last
elif startOp == '-':
    startNum -= last
elif startOp == '*':
    startNum *= last
elif startOp == '/':
    startNum /= last

print(startNum)
