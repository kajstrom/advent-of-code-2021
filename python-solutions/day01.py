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

def part2():

    window = measurements[:3]
    increases = 0
    for measurement in measurements[3:]:
        new_window = window[1:]
        new_window.append(measurement)

        if sum(new_window) > sum(window):
            increases += 1

        window = new_window

    print(f"Day 01, part 2: {increases}")


part1()
part2()