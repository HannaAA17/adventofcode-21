from Day0 import day_data
data_in = day_data(8)


print(
    'Part 1: ',
    len([
        word 
        for line in data_in.splitlines() 
        for word in line.split(' | ')[-1].strip().split(' ')
        if len(word.strip()) in [2, 3, 4, 7]
    ])
)

# nums = [
#     'abcdeg', 'ab', 'acdfg', 'abcdf', 'abef',
#     'bcdef', 'bcdefg', 'abd', 'abcdefg', 'abcdef' #, 'abcefg'
# ]
# nums_sets = [set(num) for num in nums]
# nums_lens = {2:1, 3:7, 4:4, 7:8}
# 
# print(
#     'Part 2: ',
#     sum([
#         int(''.join(
#             str(nums_lens[len(word)])
#             if not set(word) in nums_sets
#             else
#             str(nums_sets.index(set(word)))
#             
#             for word in line.split(' | ')[-1].strip().split(' ')
#         ))
#         
#         for line in data_in.splitlines()
#     ])
# )