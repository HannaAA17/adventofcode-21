from Day_0 import day_data

data_in = day_data(2)

directs = {
    # x, y, aim, depth
    'forward': (1, 0, 0, 1),
    'down': (0, 1, 1, 0),
    'up': (0, -1, -1, 0),
}

def move1(x, y, command):
    
    direction, value = command.split()
    
    x += directs[direction][0] * int(value)
    y += directs[direction][1] * int(value)
    
    return x, y

def move2(x, y, aim, command):
    
    direction, value = command.split()
    
    x += directs[direction][0] * int(value)
    y += directs[direction][3]*aim * int(value)
    aim += directs[direction][2] * int(value)
    
    return x, y, aim

def part1(data_in):
    x, y = 0, 0
    
    for command in data_in.splitlines():
        x, y = move1(x, y, command)
    
    print('Part 1:', x * y)
    return

def part2(data_in):
    x, y, aim = 0, 0, 0
    
    for command in data_in.splitlines():
        x, y, aim = move2(x, y, aim, command)
    
    print('Part 2:', x * y)
    return

part1(data_in)
part2(data_in)
