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



print(part1())