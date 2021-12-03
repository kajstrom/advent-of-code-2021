def read_input():
    with open("inputs/day03.txt", "r") as f:
        return f.read().splitlines()


bits = read_input()

def part1():
    bits_per_pos = []

    for bit_idx in range(0, len(bits[0])):
        position_bits = ""
        for bit in bits:
            position_bits += bit[bit_idx]

        bits_per_pos.append(position_bits)

    gamma_rate_bits = ""
    epsilon_rate_bits = ""
    #print(bits_per_pos)

    for pos_bits in bits_per_pos:
        zeroes = pos_bits.count("0")
        ones = pos_bits.count("1")

        if zeroes > ones:
            gamma_rate_bits += "0"
            epsilon_rate_bits += "1"
        else:
            gamma_rate_bits += "1"
            epsilon_rate_bits += "0"

    print(f"Day 3, part 1: {int(gamma_rate_bits, 2) * int(epsilon_rate_bits, 2)}")

def collect_pos_bits(bits, pos):
    bits_in_pos = ""

    for bit in bits:
        bits_in_pos += bit[pos]

    return bits_in_pos

def filter_bits(bits, pos, bit_to_keep):
    filtered_bits = []

    for bit in bits:
        if bit[pos] == bit_to_keep:
            filtered_bits.append(bit)

    return filtered_bits


def oxygen_rating(bits, pos, bit_len):
    if pos == bit_len or len(bits) == 1:
        return bits[0]

    bits_in_pos = collect_pos_bits(bits, pos)

    zeroes = bits_in_pos.count("0")
    ones = bits_in_pos.count("1")

    if zeroes > ones:
        # keep only zeroes
        return oxygen_rating(
            filter_bits(bits, pos, "0"),
            pos + 1,
            bit_len
        )
    else:
        # keep only ones
        return oxygen_rating(
            filter_bits(bits, pos, "1"),
            pos + 1,
            bit_len
        )


def co2_scrubber_rating(bits, pos, bit_len):
    if pos == bit_len or len(bits) == 1:
        return bits[0]

    bits_in_pos = collect_pos_bits(bits, pos)

    zeroes = bits_in_pos.count("0")
    ones = bits_in_pos.count("1")

    if zeroes > ones:
        # keep only ones
        return co2_scrubber_rating(
            filter_bits(bits, pos, "1"),
            pos + 1,
            bit_len
        )
    else:
        # keep only zeroes
        return co2_scrubber_rating(
            filter_bits(bits, pos, "0"),
            pos + 1,
            bit_len
        )



def part2():
    bit_len = len(bits[0])

    o_rating = oxygen_rating(bits, 0, bit_len)
    co2_rating = co2_scrubber_rating(bits, 0, bit_len)

    print(f"Day 3, part 2: {int(o_rating, 2) * int(co2_rating, 2)}")


part1()
part2()
