from Day_0 import day_data

data_in = day_data(6)
counts = [data_in.strip().count(str(i)) for i in range(10)]

def step(counts):
    result = [0] * 9
    result[6] = result[8] = counts[0]
    for i in range(8):
        result[i] += counts[i + 1]
    return result

def run(counts, n):
    for _ in range(n):
        counts = step(counts)
    return sum(counts)

print(run(counts, 80))
print(run(counts, 256))
