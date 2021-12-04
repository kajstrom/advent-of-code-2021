namespace Day01
  open Utils

  module Day01 = 

    let countIncreases (acc: int * int) (measurement: int) = 
      let (increases, previous) = acc

      if measurement > previous then
        (increases + 1, measurement)
      else
        (increases, measurement)

    let part1() =
      let measurements = Utils.readLines "inputs/day01.txt" |> Seq.map(fun r -> r |> int) |> Seq.toList

      let state = (0, measurements.Head)
      let finalState = measurements.Tail |> List.fold countIncreases state
      let (increases, lastMeasurement) = finalState

      let increasesStr = string increases
      printfn "Day 1, part 1 %s" increasesStr