def read_input(file):
    with open(file) as f:
        dots = []
        folds = []
        parse_dots = True
        for line in f.read().splitlines():
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

def count_visible(dots):
    return len(set(dots))

def fold(folds, dots):
    folded = dots
    for fold in folds:
        new_folded = []
        for dot in folded:
            value = fold["value"]
            if fold["direction"] == "y":
                new_folded.append(fold_y(value, dot))
            else:
                new_folded.append(fold_x(value, dot))

        folded = new_folded

    return folded

def visualize(dots):
    unique_dots = list(set(dots))
    max_x = 0
    max_y = 0
    for dot in unique_dots:
        x, y = dot
        if x > max_x:
            max_x = x

        if y > max_y:
            max_y = y

    visual = ""
    for y in range(0, max_y + 1):
        row = ""
        for x in range(0, max_x + 1):
            if (x, y) in unique_dots:
                row += "#"
            else:
                row += " "

        visual += row + "\n"

    return visual

if __name__ == '__main__':
    dots, folds = read_input("inputs/day13.txt")
    after_first = fold([folds[0]], dots)
    print(f"Day 13, part 1: {count_visible(after_first)}")
    folded = fold(folds, dots)
    print(f"Day 13, part 2:")
    print(visualize(folded))
