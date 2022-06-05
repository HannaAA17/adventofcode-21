from Day0 import day_data

data_in = day_data(1)

input_list = [int(x) for x in data_in.splitlines()]

def part1(input_list):
    print(
        sum(
            # check if the current element larger than the pervious one
            input_list[ndx] > input_list[ndx-1]

            for ndx
            # start from 1 to avoid input_list[0-1]
            in range(1, len(input_list))
        )
    )
    return

def part2(input_list):
    part1([
        sum(a)
        #  iteration 1 => a = (1st, 2nd, 3rd)
        #  iteration 2 => a = (2nd, 3rd, 4rth)
        for a
        # start from the 1st elem, start from the 2nd elem, start from the 3rd elem
        in zip(input_list, input_list[1:], input_list[2:])
    ])
    return

print('\npart 1:')
part1(input_list)

print('\npart 2:')
part2(input_list)

# print(
#     sum(
#         val > input_list[ndx-1]
#         for ndx, val in enumerate(input_list)
#         if ndx > 0
#     )
# )
# 
# print(
#     sum(
#         1 for idx, val 
#         in enumerate(input_list) 
#         if sum(input_list[idx + 1 : idx + 4]) > sum(input_list[idx : idx + 3])
#     )
# )
