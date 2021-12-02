def read_input():
    file = open("inputs/day02.txt", "r")
    lines = file.read().splitlines()
    file.close()

    inputs = []
    for line in lines:
        command, value = line.split(" ")
        inputs.append((command, int(value)))

    return inputs

commands = read_input()

def part1():
    depth = 0
    position = 0

    for command, value in commands:
        if command == "forward":
            position += value
        elif command == "up":
            depth -= value
        elif command == "down":
            depth += value

    print(f"Day 02, part 1: {depth * position}")

def part2():
    aim = 0
    depth = 0
    position = 0

    for command, value in commands:
        if command == "forward":
            position += value
            depth += aim * value
        elif command == "up":
            aim -= value
        elif command == "down":
            aim += value

    print(f"Day 02, part 2: {depth * position}")


part1()
part2()