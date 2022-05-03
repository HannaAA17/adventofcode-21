import re
from Day0 import day_data

data_in = day_data(4)
data_list = data_in.split('\n\n', 1)

call_nums = data_list[0]
mark_txt = data_list[1]

# boards = data_in[1:]
patterns = [
    r"^(?:XX\s){5}",
    r"^((?:.{2}\s){0}(XX\s)(?:.{2}\s){4}){5}",
    r"^((?:.{2}\s){1}(XX\s)(?:.{2}\s){3}){5}",
    r"^((?:.{2}\s){2}(XX\s)(?:.{2}\s){2}){5}",
    r"^((?:.{2}\s){3}(XX\s)(?:.{2}\s){1}){5}",
    r"^((?:.{2}\s){4}(XX\s)(?:.{2}\s){0}){5}",
]

def remove_num(num, mark_txt):
    mark_txt = re.sub(
        r"(?<=\s)(" + str(num).rjust(2) + r")(?=\s)",
        'XX',
        mark_txt,
        0,
        re.MULTILINE
    )
    return mark_txt

def check_won(num, mark_txt, won_boards):
    won_board_nums = [board_num for board_num, _ in won_boards]
    
    for board_num, board in enumerate(mark_txt.split('\n\n'), start=1):
        if board_num in won_board_nums:
            continue
        
        for pattern in patterns:
            if re.search(pattern, board+'\n', re.MULTILINE):
                score = sum(
                    int(col)
                    for row in board.replace('  ', ' ').split('\n')
                    for col in row.split()
                    if col != 'XX'
                )*int(num)
                
                won_boards.append((board_num, score))
                break
    
    return won_boards

won_boards = []

for num in call_nums.split(','):
    mark_txt = remove_num(num, mark_txt)
    won_boards = check_won(num, mark_txt, won_boards)

print(won_boards[0])
print(won_boards[-1])