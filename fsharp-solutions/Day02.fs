namespace Day02
  open Utils

  module Day02 =
    let mapInput (line: string): string * int =
      let lineParts = line.Split " "
      let value = lineParts[1] |> int

      (lineParts[0], value)

    let followDirection (acc: int * int) (direction: string * int): int * int =
      let (name, value) = direction
      let (x, y) = acc

      if name.Equals "forward" then
        (x + value, y)
      else if name.Equals "down" then
        (x, y + value)
      else
        (x, y - value)

    let part1() =
      let directions = Utils.readLines "inputs/day02.txt" |> Seq.map mapInput |> Seq.toList
      let initialState = (0, 0)
      let (x, y) = directions |> List.fold followDirection initialState

      let result = x * y
      printfn "Day 02, part 1: %A" result

    let followAimDirection (acc: int * int * int) (direction: string * int): int * int * int =
      let (name, value) = direction
      let (aim, x, y) = acc

      if name.Equals "up" then
        (aim - value, x, y)
      else if name.Equals "down" then
        (aim + value, x, y)
      else
        (aim, x + value, y + aim * value)

    let part2() =
      let directions = Utils.readLines "inputs/day02.txt" |> Seq.map mapInput |> Seq.toList
      let initialState = (0, 0, 0)
      let (aim, x, y) = directions |> List.fold followAimDirection initialState

      let result = x * y
      printfn "Day 02, part 2: %A" result