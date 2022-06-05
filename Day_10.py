from statistics import median
from Day0 import day_data
data_in = day_data(10)


def bracket_matcher(data, fix=False):
    stack=[""]
    brackets={"(":")","[":"]","{":"}","<":">"}
    for c in data:
        if c in brackets:
            stack.append(brackets[c])

        elif c in brackets.values() and c!=stack.pop(): # corrupted
            return [c, ''][fix]
        
    return ['', ''.join(stack[-1::-1])][fix] # need fix


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

def calc_fix(fixes):
    score = {     
        ')': 1,
        ']': 2,
        '}': 3,
        '>': 4,
    }
    fix_scores = []
    
    for fix in fixes:
        if not fix: continue
        
        fix_score = 0
        for l in fix:
            fix_score = (fix_score*5) + score[l]
        
        fix_scores.append(fix_score)
    
    return median(fix_scores)

errs = ''

for line in data_in.splitlines():
    errs += bracket_matcher(line)
    
print('part 1:', calc_err(errs))

fixes = []

for line in data_in.splitlines():
    fixes += [bracket_matcher(line, True)]
    
print('part 2:', calc_fix(fixes))
