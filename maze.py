import random

class Maze:
    def __init__(self, rowsNumber, columnsNumber):
        self.rowsNumber = rowsNumber
        self.columnsNumber = columnsNumber
        self.maze = []
    
    def isEven(self, number):
        return number % 2 == 0

    def getRandomFrom(self, array):
        return random.choice(array)

    def setField(self, x, y, value):
        if x < 0 or x >= self.columnsNumber or y < 0 or y >= self.rowsNumber:
            return False

        self.maze[y][x] = value

    def getField(self, x, y):
        if x < 0 or x >= self.columnsNumber or y < 0 or y >= self.rowsNumber:
            return False

        return self.maze[y][x]

    def isMaze(self):
        for x in range(self.columnsNumber):
            for y in range(self.rowsNumber):
                if self.isEven(x) and self.isEven(y) and self.getField(x, y) == '⬛️':
                    return False

        return True

    def moveTractor(self, tractor):
        directs = []
        if tractor['x'] > 0:
            directs.append('left')

        n = self.columnsNumber - 2

        if tractor['x'] < n:
            directs.append('right')

        if tractor['y'] > 0:
            directs.append('up')

        n = self.rowsNumber - 2

        if tractor['y'] < n:
            directs.append('down')

        direct = self.getRandomFrom(directs)

        if direct == 'left':
            if self.getField(tractor['x'] - 2, tractor['y']) == '⬛️':
                self.setField(tractor['x'] - 1, tractor['y'], '⬜️')
                self.setField(tractor['x'] - 2, tractor['y'], '⬜️')
            tractor['x'] -= 2
        if direct == 'right':
            if self.getField(tractor['x'] + 2, tractor['y']) == '⬛️':
                self.setField(tractor['x'] + 1, tractor['y'], '⬜️')
                self.setField(tractor['x'] + 2, tractor['y'], '⬜️')
            tractor['x'] += 2
        if direct == 'up':
            if self.getField(tractor['x'], tractor['y'] - 2) == '⬛️':
                self.setField(tractor['x'], tractor['y'] - 1, '⬜️')
                self.setField(tractor['x'], tractor['y'] - 2, '⬜️')
            tractor['y'] -= 2
        if direct == 'down':
            if self.getField(tractor['x'], tractor['y'] + 2) == '⬛️':
                self.setField(tractor['x'], tractor['y'] + 1, '⬜️')
                self.setField(tractor['x'], tractor['y'] + 2, '⬜️')
            tractor['y'] += 2

    def generate_map(self):
        for i in range(self.rowsNumber):
            row = []
            for j in range(self.columnsNumber):
                row.append('⬛️')
            self.maze.append(row)

        evenColums = []
        for column in range(self.columnsNumber):
            if self.isEven(column):
                evenColums.append(column)

        evenRows = []
        for row in range(self.rowsNumber):
            if self.isEven(column):
                evenRows.append(row)

        startX = 2
        startY = 2


        tractor = {'x': startX, 'y': startY}

        self.setField(startX, startY, '⬜️')

        while not self.isMaze():
            self.moveTractor(tractor)

        return self.maze

generate = Maze(31, 31)
maze = generate.generate_map()

player = {'x': 0, 'y': 0}
maze[player['y']][player['x']] = '🟦'
maze[30][30] = '🟩'

#print(maze)
for column in maze:
    for row in column:
        for i in row:
            print(i, end='')
    print('\n', end='')