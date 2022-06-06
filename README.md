# Maze Generator in python

## Generate

```bash
python3 maze.py
```

Play in console:

```python
player = {'x': 0, 'y': 0}
move = {'x': 0, 'y': 0}
maze[player['y']][player['x']] = '🟦'
maze[30][30] = '🟩'
# play
while True:
    # rendering the map to the console
    for column in maze:
        for row in column:
            for i in row:
                print(i, end='')
        print('\n', end='')
       
    move = {'x': player['x'], 'y': player['y']}
    press = input('Press w, a, s or d to move: ')

    if press == 'w':
        move['y'] = move['y'] - 1
    if press == 'a':
        move['x'] = move['x'] - 1
    if press == 's':
        move['y'] = move['y'] + 1
    if press == 'd':
        move['x'] = move['x'] + 1

    if maze[move['y']][move['x']] == '⬛️':
        print('Not allowed')
    elif maze[move['y']][move['x']] == '⬜️':
        maze[player['y']][player['x']] = '⬜'
        player = move
    elif maze[move['y']][move['x']] == '🟩':
        print('You win!')
        break

    maze[player['y']][player['x']] = '🟦'
```

## Screen

![50x50](https://raw.githubusercontent.com/vsecoder/maze-generater/main/maze.png)
