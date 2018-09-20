import random

class bcolors:
	HEADER = '\033[95m'
	OKBLUE = '\033[94m'
	OKGREEN = '\033[92m'
	WARNING = '\033[93m'
	FAIL = '\033[91m'

	ENDC = '\033[0m'
	BOLD = '\033[1m'
	GREY = '\033[2m'
	ITALIC = '\033[3m'
	UNDERLINE = '\033[4m'
	INVERSE = '\033[7m'
	INVISIBLE = '\033[8m'
	CROSSED = '\033[9m'

	D_BLACK = '\033[30m'
	D_RED = '\033[31m'
	D_GREEN = '\033[32m'
	D_YELLOW = '\033[33m'
	D_BLUE = '\033[34m'
	D_PURPLE = '\033[35m'
	D_CYAN = '\033[36m'
	D_WHITE = '\033[37m'

	DI_BLACK = '\033[40m'
	DI_RED = '\033[41m'
	DI_GREEN = '\033[42m'
	DI_YELLOW = '\033[43m'
	DI_BLUE = '\033[44m'
	DI_PURPLE = '\033[45m'
	DI_CYAN = '\033[46m'
	DI_WHITE = '\033[47m'

	BLACK = '\033[90m'
	RED = '\033[91m'
	GREEN = '\033[92m'
	YELLOW = '\033[93m'
	BLUE = '\033[94m'
	PURPLE = '\033[95m'
	CYAN = '\033[96m'
	WHITE = '\033[97m'

	I_BLACK = '\033[100m'
	I_RED = '\033[101m'
	I_GREEN = '\033[102m'
	I_YELLOW = '\033[103m'
	I_BLUE = '\033[104m'
	I_PURPLE = '\033[105m'
	I_CYAN = '\033[106m'
	I_WHITE = '\033[107m'

field = [[0, 0, 0, 0],
[0, 0, 0, 0],
[0, 0, 0, 0],
[0, 0, 0, 0]]

def printField():
    print('-' * 18)
    for i in range(4):
        print('|', end='')
        for j in range(4):
            if field[i][j] == 0:
                print(bcolors.BLACK, end='')
            elif field[i][j] == 2:
                print(bcolors.DI_WHITE, end='')
                print(bcolors.D_BLACK, end='')
            elif field[i][j] == 4:
                print(bcolors.DI_YELLOW, end='')
                print(bcolors.D_BLACK, end='')
            elif field[i][j] == 8:
                print(bcolors.DI_RED, end='')
                print(bcolors.WHITE, end='')
            elif field[i][j] == 16:
                print(bcolors.DI_PURPLE, end='')
                print(bcolors.WHITE, end='')
            elif field[i][j] == 32:
                print(bcolors.DI_BLUE, end='')
                print(bcolors.WHITE, end='')
            elif field[i][j] == 64:
                print(bcolors.DI_CYAN, end='')
                print(bcolors.WHITE, end='')
            elif field[i][j] == 128:
                print(bcolors.DI_GREEN, end='')
                print(bcolors.WHITE, end='')
            elif field[i][j] == 256:
                print(bcolors.I_WHITE, end='')
                print(bcolors.D_BLACK, end='')
            elif field[i][j] == 512:
                print(bcolors.I_YELLOW, end='')
                print(bcolors.D_BLACK, end='')
            elif field[i][j] == 1024:
                print(bcolors.I_RED, end='')
                print(bcolors.WHITE, end='')
            elif field[i][j] == 2048:
                print(bcolors.I_PURPLE, end='')
                print(bcolors.WHITE, end='')
            if field[i][j] != 0:
                print(str(field[i][j]).rjust(4, ' '), end='')
            else:
                print('    ', end='')
            print(bcolors.ENDC, end='')
        print('|')
    print('-' * 18)

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
