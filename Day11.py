from Day0 import day_data

def create_matrix(data_in: list) -> tuple[dict, int, int]:
    ii = len(data_in)
    jj = len(data_in[0])

    matrix = {
        (i, j): int(data_in[i][j])
        for i in range(ii)
        for j in range(jj)
    }
    
    return matrix, ii, jj


def step(matrix: dict) -> tuple[dict, list]:
    flashed = []
    for k, v in matrix.items():
        if v == 9:
            matrix[k] = 0
            flashed.append(k)
        else:
            matrix[k] = v + 1
    return matrix, flashed


def get_neighbors(point: tuple[int, int], matrix: dict) -> list[tuple[int, int]]:
    ii, jj = point
    
    neighbors = [
        (i, j)
        for i in range(ii-1, ii+2)
        for j in range(jj-1, jj+2)
        if (i, j) in matrix.keys()
        and (i, j) != point
    ]
    
    return neighbors

def double_step(matrix:dict, flashed:list):
    c_f = len(flashed)
    
    while flashed:
        p = flashed.pop()
        for n_p in get_neighbors(p, matrix):
            if matrix[n_p] == 0:
                continue
            
            elif matrix[n_p] == 9:
                matrix[n_p] = 0
                flashed.append(n_p)
                c_f += 1
            
            else:
                matrix[n_p] += 1
    
    return matrix, c_f

def triple_step(matrix, n=1):
    t_f = 0
    for _ in range(n):
        matrix, flashed = step(matrix)
        matrix, c_f = double_step(matrix, flashed)
        t_f += c_f
    return matrix, t_f

def print_matrix(matrix: dict, ii, jj) -> None:
    for i in range(ii):
        for j in range(jj):
            print(matrix[(i, j)], end='')
        print()

# print_matrix(step(matrix), ii, jj)

data_in = day_data(11).splitlines()
matrix, ii, jj = create_matrix(data_in)
# print(get_neighbors((0, 0), matrix))

matrix, t_f = triple_step(matrix, 100)

print('\nNumber of Flashed:', t_f, '\n')
print_matrix(matrix, ii, jj)