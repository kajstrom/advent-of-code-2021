import re

def read_input(file):
    with open(file) as f:
        return f.read()

conversion_rules = {
    "0": "0000",
    "1": "0001",
    "2": "0010",
    "3": "0011",
    "4": "0100",
    "5": "0101",
    "6": "0110",
    "7": "0111",
    "8": "1000",
    "9": "1001",
    "A": "1010",
    "B": "1011",
    "C": "1100",
    "D": "1101",
    "E": "1110",
    "F": "1111"
}


def hex_to_bin(hex_str):
    bin_str = ""
    for c in hex_str:
        bin_str += conversion_rules[c]

    return bin_str


def decode_header(bin_str, pointer):
    version = bin_str[pointer:pointer + 3]
    type = bin_str[pointer + 3:pointer + 6]
    pointer += 6

    version = int(version, 2)
    type = int(type, 2)

    return version, type, pointer


def decode_literal_subpacket(bin_str, pointer):
    version, type, pointer = decode_header(bin_str, pointer)

    last_group_reached = False
    value = ""
    while not last_group_reached:
        group = bin_str[pointer:pointer + 5]
        if group[0] == "0":
            last_group_reached = True

        value += group[1:]
        pointer += 5

    subpacket = {
        "version": version,
        "type": type,
        "value": int(value, 2)
    }

    return subpacket, pointer


def decode_operation_subpacket(bin_str, pointer):
    version, type, pointer = decode_header(bin_str, pointer)

    length_type_id = bin_str[pointer]
    pointer += 1

    packet = None
    if length_type_id == "0":
        length = int(bin_str[pointer:pointer + 15], 2)
        pointer += 15
        packet = {
            "version": version,
            "type": type,
            "subpackets": []
        }

        pointer_at_start = pointer
        while pointer - pointer_at_start != length:
            s_version, s_type, ignore = decode_header(bin_str, pointer)
            if s_type == 4:
                subpacket, pointer = decode_literal_subpacket(bin_str, pointer)
            else:
                subpacket, pointer = decode_operation_subpacket(bin_str, pointer)

            packet["subpackets"].append(subpacket)
    elif length_type_id == "1":
        length = bin_str[pointer:pointer + 11]
        pointer += 11
        length = int(length, 2)
        packet = {
            "version": version,
            "type": type,
            "subpackets": []
        }

        for _ in range(0, length):
            s_version, s_type, ignore = decode_header(bin_str, pointer)
            if s_type == 4:
                subpacket, pointer = decode_literal_subpacket(bin_str, pointer)
            else:
                subpacket, pointer = decode_operation_subpacket(bin_str, pointer)

            packet["subpackets"].append(subpacket)

    return packet, pointer


def decode_packets(bin_str):
    pointer = 0
    packets = []

    while pointer < len(bin_str):
        version, type, pointer = decode_header(bin_str, pointer)

        if type == 4:
            last_group_reached = False
            value = ""
            while not last_group_reached:
                group = bin_str[pointer:pointer+5]
                if group[0] == "0":
                    last_group_reached = True

                value += group[1:]

                pointer += 5

            packets.append({
                "version": version,
                "type": type,
                "value": int(value, 2)
            })

            pointer += 4 - (pointer % 4)
        else:
            length_type_id = bin_str[pointer]
            pointer += 1

            if length_type_id == "0":
                length = int(bin_str[pointer:pointer+15], 2)
                pointer += 15

                packet = {
                    "version": version,
                    "type": type,
                    "subpackets": []
                }

                pointer_at_start = pointer
                while pointer - pointer_at_start != length:
                    s_version, s_type, ignore = decode_header(bin_str, pointer)
                    if s_type == 4:
                        subpacket, pointer = decode_literal_subpacket(bin_str, pointer)
                    else:
                        subpacket, pointer = decode_operation_subpacket(bin_str, pointer)

                    packet["subpackets"].append(subpacket)

                packets.append(packet)
            elif length_type_id == "1":
                length = bin_str[pointer:pointer+11]
                pointer += 11
                length = int(length, 2)
                packet = {
                    "version": version,
                    "type": type,
                    "subpackets": []
                }

                for _ in range(0, length):
                    s_version, s_type, ignore = decode_header(bin_str, pointer)
                    if s_type == 4:
                        subpacket, pointer = decode_literal_subpacket(bin_str, pointer)
                    else:
                        subpacket, pointer = decode_operation_subpacket(bin_str, pointer)

                    packet["subpackets"].append(subpacket)

                packets.append(packet)

        if re.match("0+", bin_str[pointer:]):
            #Terminate if there are only zeroes in the remaining bin_str
            pointer = len(bin_str)


    return packets


def sum_version_numbers(packets):
    version_sum = 0
    for packet in packets:
        version_sum += packet["version"]
        if packet["type"] != 4:
            for sub in packet["subpackets"]:
                version_sum += sub["version"]
                if sub["type"] != 4:
                    version_sum += sum_version_numbers(sub["subpackets"])

    return version_sum


def part1():
    packets = decode_packets(hex_to_bin(read_input("inputs/day16.txt")))
    summed = sum_version_numbers(packets)

    print(f"Day 16, part 1: {summed}")


if __name__ == '__main__':
    part1()