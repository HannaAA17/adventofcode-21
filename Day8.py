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

'''
1,4,7,8 - each have a unique segment count
0,6,9 - 6 segments - distinguish by whether they contain 4 and/or contain 1
2,3,5 - 5 segments - 6 contains 5, 3 contains 1, and 2 is not contained in 9
'''

'''
count how many times each letter appears in the first 10 digits.

Segments B, E, and F all appear a unique number of times, 
C and A both appear 7 times 
D and G both appear 8 times.

using this you can directly substitute a capital B, E, and F into 
the latter half signals and arbitrary letters representing C or A, and D or G. 
I chose Q and X. 

Then sort the strings alphabetically 
and now each string directly corresponds to a real digit, 

so you can just find and replace with a dictionary with the integer digit for each string.
'''

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