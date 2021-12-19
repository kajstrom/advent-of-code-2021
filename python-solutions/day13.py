def read_input(file):
    with open(file) as f:
        dots = []
        folds = []
        parse_dots = True
        for line in f.read().splitlines():
            print(line)
            if len(line) < 3:
                parse_dots = False
                continue

            if parse_dots:
                x, y = line.split(",")
                x = int(x)
                y = int(y)

                dots.append((x, y))
            else:
                line = line.replace("fold along ", "")
                direction, value = line.split("=")
                value = int(value)
                folds.append({
                    "direction": direction,
                    "value": value
                })

    return dots, folds

#print(read_input("inputs/day13-example.txt"))

def fold_y(along, dot):
    if dot[1] < along:
        #Not affected by fold
        return dot

    diff_to_fold = dot[1] - along

    return dot[0], along - diff_to_fold

def fold_x(along, dot):
    if dot[0] < along:
        #Not affected by fold
        return dot

    diff_to_fold = dot[0] - along

    return along - diff_to_fold, dot[1]

def first_fold_only(folds, dots):
    first_fold = folds[0]
    folded_dots = []
    for dot in dots:
        value = first_fold["value"]
        if first_fold["direction"] == "y":
            folded_dots.append(fold_y(value, dot))
        else:
            folded_dots.append(fold_x(value, dot))

    return folded_dots

def count_visible(dots):
    return len(set(dots))

if __name__ == '__main__':
    dots, folds = read_input("inputs/day13.txt")
    folded = first_fold_only(folds, dots)
    print(f"Day 13, part 1: {count_visible(folded)}")