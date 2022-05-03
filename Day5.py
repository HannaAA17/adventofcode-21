from itertools import cycle
from collections import Counter
from Day0 import day_data

data_in = day_data(5)

points = []

for line in data_in.splitlines():
    x1,y1,x2,y2 = [int(cor) for point in line.split(' -> ') for cor in point.split(',')]
    
    ## uncomment for part 1
    # if x1 != x2 and y1 != y2:
    #     continue
    
    points.extend(
        [(x1,y1)]
        if (x1==x2 and y1==y2)
        else [
            (x, y)
            
            for x,y in zip(
                range(x1, x2 + [-1, 1][x2>x1], [-1, 1][x2>x1])
                if x2 != x1 else cycle([x1]),
                
                range(y1, y2 + [-1, 1][y2>y1], [-1, 1][y2>y1])
                if y2 != y1 else cycle([y1]),
            )
        ]
    )

print(
    len(
        [1 for _,intersections in Counter(points).items() if intersections >= 2]
    )
)

# x1, y1, x2, y2 = zip(*[
#     point1.split(',') + point2.split(',')
#     for line in data_in.splitlines()
#     for point1, point2 in [line.split(' -> ')]
# ])

# matrix = [[0 for _ in range(10)] for _ in range(10)]
# 
# for x, y in points:
#     matrix[y][x] += 1
# 
# from pprint import pprint
# pprint(matrix)