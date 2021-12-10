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
        #print(chunk)
        open = []
        for symbol in chunk:
            #print(symbol)
            if symbol in start_symbols:
                open.append(symbol)
            elif symbol in end_symbols:
                previous_open = open.pop()
                #print(f"Previous open {previous_open}")

                if not is_matching_end(previous_open, symbol):
                    illegals.append(symbol)
                    #print(f"Illegal: {symbol}")
                    break

    syntax_score = sum(map(score_symbol, illegals))
    print(f"Day 10, part 1: {syntax_score}")

part1()