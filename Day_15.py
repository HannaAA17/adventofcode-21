import heapq
from Day0 import day_data
from collections import namedtuple

Point = namedtuple('Point', ['x', 'y'])

def Dijkstra(start, end, risk_map):
    '''Dijkstra's algorithm'''
    
    def calc_risk(point):
        R = (risk_map[(point.x % X, point.y % Y)] + (point.x // X) + (point.y // Y))
        return (R - 1) % 9 + 1
    
    # visit 1 time
    visited = {start}

    # Priority Queue
    queue = []
    heapq.heappush(queue, (0, start))
    
    # right, up, left, down
    moves = [(1, 0), (0, 1), (-1, 0), (0, -1)]

    while True:
        risk, point = heapq.heappop(queue)
        for dx, dy in moves:
            new_p = Point(point.x+dx, point.y+dy)
            
            if new_p == end:
                return risk + calc_risk(new_p)
            
            elif all([0 <= new_p.x <= end.x, 0 <= new_p.y <= end.y, new_p not in visited]):
                visited.add(new_p)
                heapq.heappush(queue, (risk + calc_risk(new_p), new_p))
            # end if
        # end for
    # end while

risk_map = dict(
    (Point(x, y), int(risk)) 
    for y, row in enumerate(day_data(15).splitlines())
    for x, risk in enumerate(row.strip())
)

start = Point(0, 0)
end = max(risk_map)

X, Y = end.x+1, end.y+1

print(Dijkstra(start, end, risk_map))
print(Dijkstra(start, Point(X*5-1, Y*5-1), risk_map))
