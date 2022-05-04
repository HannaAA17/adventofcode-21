from Day0 import day_data
data_in = day_data(10)


def bracket_matcher(data):
    stack=[""]
    brackets={"(":")","[":"]","{":"}","<":">"}
    for c in data:
        if c in brackets:
            stack.append(brackets[c])

        elif c in brackets.values() and c!=stack.pop(): # corrupted
            return c
        
    return '' if stack==[""] else stack[0] # need fix


def calc_err(errs):
    score = {     
        ')': 3,
        ']': 57,
        '}': 1197,
        '>': 25137,
    }
    err_score = 0
    for er in errs:
        err_score += score[er]
    
    return err_score

# print(bracket_matcher("(((1+(1+1))]))"))
errs = ''

for line in data_in.splitlines():
    errs += bracket_matcher(line)
    
print(calc_err(errs))