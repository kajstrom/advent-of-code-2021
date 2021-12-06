def read_input():
    with open("inputs/day06.txt") as f:
        input = f.read().splitlines()[0].split(",")
        return list(map(lambda i: int(i), input))

def lanternfish_after(lanternfishes, days):
    fishes = {8: 0, 7: 0, 6: 0, 5: 0, 4: 0, 3: 0, 2: 0, 1: 0, 0: 0}

    for fish in lanternfishes:
        if fish in lanternfishes:
            fishes[fish] += 1

    for _ in range(0, days):
        next_fishes = {8: 0, 7: 0, 6: 0, 5: 0, 4: 0, 3: 0, 2: 0, 1: 0, 0: 0}
        for fish_number in range(8, -1, -1):
            fish_count = fishes[fish_number]
            if fish_count == 0:
                continue

            if fish_number == 0:
                next_fishes[8] = fish_count
                next_fishes[6] = next_fishes[6] + fish_count
            else:
                next_fishes[fish_number-1] = fish_count

        fishes = next_fishes

    return sum(fishes.values())


lanternfishes = read_input()
print(f"Day 06, part 1: {lanternfish_after(lanternfishes, 80)}")
print(f"Day 06, part 2: {lanternfish_after(lanternfishes, 256)}")