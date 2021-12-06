namespace Day03
  open Utils

  module Day03 =
    let takePos (bits: list<list<char>>) (pos: int): list<char> =
      bits |> List.map (List.item pos)

    let groupBitsByPos(bits: list<list<char>>) =
      let bitLenght = List.item 0 bits |> List.length
      let listIndexes = [0 .. 1 .. bitLenght - 1]

      listIndexes |> List.map (takePos bits)

    let findMostCommonBit (posBits: list<char>): char =
      let countBits (acc: int * int) (bit: char): int * int =
        let (zeroes, ones) = acc
        if bit.Equals('0') then
          (zeroes + 1, ones)
        else
          (zeroes, ones + 1)

      let initialState = (0, 0)
      let (zeroes, ones) = posBits |> List.fold countBits initialState

      if zeroes > ones then
        '0'
      else
        '1'

    let flipBits(bits: list<char>): list<char> =
      bits |> List.map (fun b -> if b.Equals('0') then '1' else '0')

    let gammaAndEpsilon (mostCommonBits: list<char>): int * int =
      (mostCommonBits |> charListToString |> binaryStringToInt32, mostCommonBits |> flipBits |> charListToString |> binaryStringToInt32)

    let part1() =
      let input = readLines "inputs/day03.txt" |> Seq.map Seq.toList |> Seq.toList
      let powerConsumption = input |>
                                    groupBitsByPos |>
                                    List.map findMostCommonBit |>
                                    gammaAndEpsilon |>
                                    (fun (gamma, epsilon) -> gamma * epsilon)

      printfn "Day 3, part 1: %A" powerConsumption