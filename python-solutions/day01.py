def read_input():
    file = open("inputs/day01.txt", "r")
    lines = file.read().splitlines()
    file.close()

    inputs = []
    for line in lines:
        inputs.append(int(line))

    return inputs


measurements = read_input()

def part1():
    previous = measurements[0]
    increases = 0
    for measurement in measurements[1:]:
        if measurement > previous:
            increases += 1

        previous = measurement

    print(f"Day 01, part 1: {increases}")


part1()