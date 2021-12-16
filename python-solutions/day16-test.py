import unittest
from day16 import *


class Day16TestCase(unittest.TestCase):
    def test_hex_to_bin(self):
        self.assertEqual("110100101111111000101000", hex_to_bin("D2FE28"))
        self.assertEqual("00111000000000000110111101000101001010010001001000000000", hex_to_bin("38006F45291200"))

    def test_decode_packets_with_literal_packet(self):
        packets = decode_packets("110100101111111000101000110100101111111000101000")
        first_packet = packets[0]
        self.assertEqual(6, first_packet["version"])
        self.assertEqual(4, first_packet["type"])
        self.assertEqual(2021, first_packet["value"])

    def test_decode_packets_with_operator_type_0(self):
        packets = decode_packets("00111000000000000110111101000101001010010001001000000000")
        first_packet = packets[0]

        self.assertEqual(2, len(first_packet["subpackets"]))
        self.assertEqual(10, first_packet["subpackets"][0]["value"])
        self.assertEqual(20, first_packet["subpackets"][1]["value"])

    def test_decode_packets_with_operator_type_1(self):
        packets = decode_packets("11101110000000001101010000001100100000100011000001100000")
        first_packet = packets[0]

        self.assertEqual(3, len(first_packet["subpackets"]))
        self.assertEqual(1, first_packet["subpackets"][0]["value"])
        self.assertEqual(2, first_packet["subpackets"][1]["value"])
        self.assertEqual(3, first_packet["subpackets"][2]["value"])

    def test_sum_version_numbers(self):
        packets = decode_packets(hex_to_bin("8A004A801A8002F478"))
        self.assertEqual(16, sum_version_numbers(packets))

        packets = decode_packets(hex_to_bin("620080001611562C8802118E34"))
        self.assertEqual(12, sum_version_numbers(packets))

        packets = decode_packets(hex_to_bin("C0015000016115A2E0802F182340"))
        self.assertEqual(23, sum_version_numbers(packets))

        packets = decode_packets(hex_to_bin("A0016C880162017C3686B18A3D4780"))
        self.assertEqual(31, sum_version_numbers(packets))

    def test_part1_input(self):
        packets = decode_packets(hex_to_bin(read_input("inputs/day16.txt")))
        summed = sum_version_numbers(packets)

        self.assertEqual(986, summed)


if __name__ == '__main__':
    unittest.main()
