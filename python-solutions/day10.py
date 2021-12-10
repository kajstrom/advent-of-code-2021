def read_input():
    with open("inputs/day10.txt") as f:
        return list(map(list, f.read().splitlines()))


chunks = read_input()

start_symbols = ['(', '[', '{', '<']
end_symbols = [')', ']', '}', '>']

def score_symbol(symbol):
    if symbol == ')':
        return 3
    elif symbol == ']':
        return 57
    elif symbol == '}':
        return 1197
    elif symbol == '>':
        return 25137


def is_matching_end(start, end):
    if start == '(':
        return end == ')'
    elif start == '[':
        return end == ']'
    elif start == '{':
        return end == '}'
    elif start == '<':
        return end == '>'


def part1():
    illegals = []
    for chunk in chunks:
        open = []
        for symbol in chunk:
            if symbol in start_symbols:
                open.append(symbol)
            elif symbol in end_symbols:
                previous_open = open.pop()

                if not is_matching_end(previous_open, symbol):
                    illegals.append(symbol)
                    break

    syntax_score = sum(map(score_symbol, illegals))
    print(f"Day 10, part 1: {syntax_score}")


def score_incomplete(open_symbols):
    total_score = 0
    while len(open_symbols) > 0:
        total_score *= 5

        symbol = open_symbols.pop()
        if symbol == '(':
            total_score += 1
        elif symbol == '[':
            total_score += 2
        elif symbol == '{':
            total_score += 3
        elif symbol == '<':
            total_score += 4

    return total_score



def part2():

    valid_open = []
    for chunk in chunks:
        open = []
        is_valid = True
        for symbol in chunk:
            if symbol in start_symbols:
                open.append(symbol)
            elif symbol in end_symbols:
                previous_open = open.pop()

                if not is_matching_end(previous_open, symbol):
                    is_valid = False
                    break

        if is_valid:
            valid_open.append(open)

    scored = list(map(score_incomplete, valid_open))
    scored_sorted = sorted(scored)
    middle_idx = int((len(scored_sorted) / 2))

    print(f"Day 10, part 2: {scored_sorted[middle_idx]}")


part1()
part2()