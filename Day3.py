from Day0 import day_data

# data_in = ['00100', '11110', '10110', '10111', '10101', '01111', '00111', '11100', '10000', '11001', '00010', '01010']
data_in = day_data(3).splitlines()

def part1(data_in):
    print(
        int(''.join(min(col, key=col.count) for col in zip(*data_in)), base=2) *
        int(''.join(max(col, key=col.count) for col in zip(*data_in)), base=2)
    )
    return

def part2(data_in, func):
    mc = ''
    for i in range(len(data_in[0])):
        col = [row[i] for row in data_in]
        mc += func(col, key=lambda x: (col.count(x), x))
        data_in = [row for row in data_in if row.startswith(mc)]
        # print(mc, len(data_in))
    print(mc)
    return int(mc, base=2)

# def part2(data_in, func):
#     mc = ''
#     i= 0
#     while len(data_in)!=1:
#         col = [row[i] for row in data_in]
#         mc += func(col, key=lambda x: (col.count(x), x))
#         data_in = [row for row in data_in if row.startswith(mc)]
#         i+=1
#         # print(mc, len(data_in))
#     
#     print(mc)
#     return int(mc, base=2)


print(part2(data_in, max) * part2(data_in, min))