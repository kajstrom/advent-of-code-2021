def read_input(file):
    with open(file) as f:
        lines = f.read().splitlines()
        algorithm = lines.pop(0)
        lines.pop(0) #empty line

        image = list(map(list, lines))

        return algorithm, image


def take_comparison_area(middle, image, default):
    area = ""
    max_y = len(image) - 1
    max_x = len(image[0]) - 1
    mx, my = middle
    for y in range(my - 1, my + 2):
        for x in range(mx - 1, mx + 2):
            if y < 0 or x < 0 or y > max_y or x > max_x:
                area += default
            else:
                area += image[y][x]

    return area


def get_enhancement_pixel(algorithm, area: str):
    idx_str = ""
    for c in area:
        if c == ".":
            idx_str += "0"
        else:
            idx_str += "1"

    idx = int(idx_str, 2)

    if idx > 511:
        print(idx, idx_str)

    return algorithm[idx]

def visualize(image):
    for row in image:
        print("".join(row))

def enhance(image, algorithm, default):
    enhanced = []
    row_len = len(image[0])

    for y in range(-2, len(image) + 2):
        new_row = []
        for x in range(-2, row_len + 2):
            area = take_comparison_area((x, y), image, default)
            new_row.append(get_enhancement_pixel(algorithm, area))

        enhanced.append(new_row)

    return enhanced

def count_lit(image):
    lit = 0
    for row in image:
        for p in row:
            if p == "#":
                lit += 1

    return lit

def enhance_times(image, algorithm, times):
    enhanced = image

    default = "."
    for _ in range(0, times):
        enhanced = enhance(enhanced, algorithm, default)

        # Hack
        if default == ".":
            default = "#"
        else:
            default = "."

    return enhanced

if __name__ == '__main__':
    algorithm, image = read_input("inputs/day20.txt")
    enhanced = enhance_times(image, algorithm, 2)
    print(f"Day 20, part 1: {count_lit(enhanced)}")
    enhanced = enhance_times(image, algorithm, 50)
    print(f"Day 20, part 2: {count_lit(enhanced)}")