import random

field = [[0, 0, 0, 0],
[0, 0, 0, 0],
[0, 0, 0, 0],
[0, 0, 0, 0]]

def printField():
    print('-' * 21)
    for i in range(4):
        print('|', end='')
        for j in range(4):
            print(str(field[i][j]).rjust(4, ' '), end='')
            print('|', end='')
        print()
        print('-' * 21)

def genNewNumber():
    placed = False
    while not placed:
        cell = random.randrange(0, 16)
        x = cell // 4
        y = cell % 4
        if field[x][y] == 0:
            if random.random() > 10 / 11:
                field[x][y] = 4
            else:
                field[x][y] = 2
            placed = True

def checkIfLost():
    for row in field:
        for cell in row:
            if cell == 0:
                return False
    return True

def getField(row, cell, direction):
    if direction == 'j':
        return field[row][cell]
    elif direction == 'l':
        return field[row][3 - cell]
    elif direction == 'i':
        return field[cell][row]
    elif direction == 'k':
        return field[3 - cell][row]

def setField(row, cell, direction, value):
    if direction == 'j':
        field[row][cell] = value
    elif direction == 'l':
        field[row][3 - cell] = value
    elif direction == 'i':
        field[cell][row] = value
    elif direction == 'k':
        field[3 - cell][row] = value

def move(_dir):
    for row in range(4):
        for cell in range(3):
            steps = 0
            while getField(row, cell, _dir) == 0:
                for nextCell in range(cell, 3):
                    value = getField(row, nextCell + 1, _dir)
                    setField(row, nextCell, _dir, value)
                setField(row, 3, _dir, 0)
                if steps == 4:
                    break
                steps += 1
            if getField(row, cell, _dir) == getField(row, cell + 1, _dir):
                if getField(row, cell, _dir) != 0:
                    newValue = int(getField(row, cell + 1, _dir) * 2)
                    setField(row, cell, _dir, newValue)
                    for nextCell in range(cell + 1, 3):
                        value = getField(row, nextCell + 1, _dir)
                        setField(row, nextCell, _dir, value)
                    setField(row, 3, _dir, 0)

def validateInput(_dir):
    if _dir == 'j' or _dir == 'k' or _dir == 'i' or _dir == 'l':
        return True
    return False

firstMove = True

while not checkIfLost():
    if not firstMove:
        _dir = input()
        while not validateInput(_dir):
            _dir = input()
        move(_dir)
    else:
        firstMove = False
    genNewNumber()
    printField()
