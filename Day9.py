from pprint import pprint
from Day0 import day_data
data_in = day_data(9)

hight_map = [[int(num) for num in line] for line in data_in.splitlines()]
mark_map = [[int(num) for num in line] for line in data_in.splitlines()]

def low_points(hight_map: list[list], mark_map):
    risk = 0

    for i, row in enumerate(hight_map):
        for j, num in enumerate(row):
            if all([
                True if i == 0 else hight_map[i-1][j] > num,  # ^
                True if i == len(hight_map)-1 else hight_map[i+1][j] > num,  # down
                True if j == 0 else hight_map[i][j-1] > num,  # <
                True if j == len(row)-1 else hight_map[i][j+1] > num,  # >
            ]):
                risk += num+1
                mark_map[i][j] = 'X'
    
    return risk, mark_map

risk, mark_map = low_points(hight_map, mark_map)
print('Part 1:', risk)
# pprint(mark_map)

