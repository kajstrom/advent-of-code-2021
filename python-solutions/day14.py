def read_input(file: str):
    with open(file) as f:
        lines = f.read().splitlines()

        pair_rules = dict()
        for rule in lines[2:]:
            match, insertion = rule.split(" -> ")
            pair_rules[match] = insertion


        return lines[0], pair_rules


def part1():
    template, pair_rules = read_input("inputs/day14.txt")

    current_template = template
    for step in range(0, 10):
        new_template = ""

        for idx in range(0, len(current_template)):
            pair = current_template[idx:idx+2]
            if pair in pair_rules:
                insert = pair_rules[pair]
                new_template += pair[0] + insert
            else:
                new_template += pair

        current_template = new_template

    template_as_list = list(current_template)
    most_common = max(set(template_as_list), key=template_as_list.count)
    least_common = min(set(template_as_list), key=template_as_list.count)

    most_common_cnt = template_as_list.count(most_common)
    least_common_cnt = template_as_list.count(least_common)

    print(f"Day 14, part 1: {most_common_cnt - least_common_cnt}")

def part2():
    template, pair_rules = read_input("inputs/day14.txt")

    results = {}
    queue = {}
    for idx in range(0, len(template)):
        pair = template[idx:idx + 2]
        if len(pair) == 2:
            queue[pair] = queue.get(pair, 0) + 1

    for k, v in queue.items():
        results[k[0]] = results.get(k[0], 0) + 1
        results[k[1]] = results.get(k[1], 0) + 1

    for step in range(0, 40):
        next_queue = {}
        for pair, count in queue.items():
            insert = pair_rules[pair]

            results[insert] = results.get(insert, 0) + count

            pair1 = pair[0] + insert
            pair2 = insert + pair[1]

            next_queue[pair1] = next_queue.get(pair1, 0) + count
            next_queue[pair2] = next_queue.get(pair2, 0) + count

        queue = next_queue

    most_common = max(results.values())
    least_common = min(results.values())

    # Off by one :)
    print(f"Day 14, part 2: {(most_common - least_common) + 1}")


if __name__ == '__main__':
    part1()
    part2()