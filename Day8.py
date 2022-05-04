from collections import Counter
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
keys = {
    'BEFXYY': '0',
    'FY': '1',
    'EXXYY': '2',
    'FXXYY': '3',
    'BFXY': '4',
    'BFXXY': '5',
    'BEFXXY': '6',
    'FYY': '7',
    'BEFXXYY': '8',
    'BFXXYY': '9'
}

counts = {
    4: 'E',
    6: 'B',
    7: 'X',
    8: 'Y',
    9: 'F',
}


def get_line_decoder(line_in: str) -> dict:
    decoder = {}
    for k, v in Counter(line_in.replace(' ', '')).items():
        decoder[k] = counts[v]
    return decoder


def line_decode(line_out: str, decoder: dict) -> int:
    for k, v in decoder.items():
        line_out = line_out.replace(k, v)

    return int(''.join(keys[''.join(sorted(key))] for key in line_out.split(' ')))


print(
    'Part 2: ',
    sum(
        line_decode(line_out.strip(), get_line_decoder(line_in.strip()))
        for line in data_in.splitlines()
        for line_in, line_out in [line.split(' | ')]
    )
)

'''other method
1,4,7,8 - each have a unique segment count
0,6,9 - 6 segments - distinguish by whether they contain 4 and/or contain 1
2,3,5 - 5 segments - 6 contains 5, 3 contains 1, and 2 is not contained in 9
'''