from Day0 import day_data

data_in = day_data(11).splitlines()


def create_matrix(data_in: list) -> dict:
    ii = len(data_in)
    jj = len(data_in[0])

    matrix = {
        (i, j): int(data_in[i][j])
        for i in range(ii)
        for j in range(jj)
    }
    
    return matrix


def step(matrix: dict) -> dict:
    for k, v in matrix.items():
        matrix[k] = v + 1
    return matrix


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


def print_matrix(matrix: dict, ii: int, jj: int) -> None:
    for i in range(ii):
        for j in range(jj):
            print(matrix[(i, j)], end='')
        print()

# print_matrix(step(matrix), ii, jj)
# print(get_neighbors((0, 0), matrix))
