from Day0 import day_data


def get_dots_folds(day_data):
    dots, folds = day_data.split('\n\n')

    dots = [
        tuple(int(c) for c in dot.split(','))
        for dot in dots.split('\n')
    ]

    folds = [
        tuple(fold.split(' ')[-1].split('='))
        for fold in folds.strip().split('\n')
    ]

    return dots, folds


def fold_sheet(dots, dir):
    xx, yy = max(dots, key=lambda x: x[0])[0], max(dots, key=lambda x: x[1])[1]

    xy_fold, val_fold = dir[0], int(dir[1])

    new_dots = []

    if xy_fold == 'x':
        # for x in range(val_fold):
        #     for y in range(yy+1):
        #         if (x, y) in dots or (xx - x, y) in dots:
        #             new_dots.append((x, y))
        for dot in dots:
            if dot[0] < val_fold:
                new_dots.append(dot)
            else:
                new_dots.append((xx - dot[0], dot[1]))
    else:
        # for x in range(xx+1):
        #     for y in range(val_fold):
        #         if (x, y) in dots or (x, yy - y) in dots:
        #             new_dots.append((x, y))
        for dot in dots:
            if dot[1] < val_fold:
                new_dots.append(dot)
            else:
                new_dots.append((dot[0], yy - dot[1]))

    return list(set(new_dots))


def print_sheet(dots):
    xx, yy = max(dots, key=lambda x: x[0])[0], max(dots, key=lambda x: x[1])[1]

    for i in range(yy+1):
        for j in range(xx+1):
            if (j, i) in dots:
                print('#', end='')
            else:
                print(' ', end='')
        print()


dots, folds = get_dots_folds(day_data(13))

part1 = True

for fold in folds:
    dots = fold_sheet(dots, fold)
    if part1:
        print('Part1:', len(dots), '\n')
        part1 = False

print_sheet(dots)
