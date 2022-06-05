from Day0 import day_data
data_in = day_data(9)

hight_map = [[int(num) for num in line] for line in data_in.splitlines()]
mark_map = [[int(num) for num in line] for line in data_in.splitlines()]

def low_points(hight_map: list[list], mark_map):
    risk = 0
    points = []
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
                points.append((i, j))
    
    return risk, mark_map, points

risk, mark_map, points = low_points(hight_map, mark_map)
print('Part 1:', risk)

# from pprint import pprint
# pprint(mark_map)


def basin(point):
    global mark_map
    visited_points = [point]
    
    def get_adjs(point):
        adjs = []
        
        i, j = point
        
        if not (i == 0 or mark_map[i-1][j] in ['X', 9]):  # ^
            adjs.append((i-1, j))
            mark_map[i-1][j] = 'X'
        
        if not (i == len(mark_map)-1 or mark_map[i+1][j] in ['X', 9]):  # down
            adjs.append((i+1, j))
            mark_map[i+1][j] = 'X'
        
        if not (j == 0 or mark_map[i][j-1] in ['X', 9]):  # <
            adjs.append((i, j-1))
            mark_map[i][j-1] = 'X'
        
        if not (j == len(mark_map[0])-1 or mark_map[i][j+1] in ['X', 9]):  # >
            adjs.append((i, j+1))
            mark_map[i][j+1] = 'X'
        
        return [point for point in adjs if point not in visited_points]
    
    visited_points.extend(get_adjs(point))
    
    for point in visited_points:
        visited_points.extend(get_adjs(point))

    return len(visited_points)


# print(len(points))
sizes = []

for point in points:
    size = basin(point)
    sizes += [size]
    # print(size)

sizes.sort(reverse=True)
s1,s2,s3 = sizes[:3]

print('Part 2:', s1*s2*s3)

# print('\n'.join(''.join(str(i) for i in row) for row in mark_map))
