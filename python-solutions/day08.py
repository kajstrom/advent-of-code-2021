from typing import Set

def split_signals(number_str):
    return list(map(set, number_str))

def read_input():
    with open("inputs/day08.txt") as f:
        lines = f.read().splitlines()

        signals = []
        for line in lines:
            input, output = line.split(" | ")

            input = split_signals(input.split(" "))
            output = split_signals(output.split(" "))

            signals.append((input, output))

        return signals

def map_digit(signal: Set[str]):
    if len(signal) == 2:
        return 1
    elif len(signal) == 4:
        return 4
    elif len(signal) == 3:
        return 7
    elif len(signal) == 7:
        return 8
    else:
        return None


signals = read_input()
def part1():
    numbers = []
    for input, output in signals:
        for signal in output:
            numbers.append(map_digit(signal))

    count = 0
    for number in numbers:
        if number is not None:
            count += 1

    print(f"Day 8, part 1: {count}")


part1()
