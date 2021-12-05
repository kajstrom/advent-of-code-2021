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

    let countSlidingIncreses (acc: int * List<int>) (measurement: int) =
      let (increases, window) = acc
      let newWindow =  List.append window.Tail [measurement]
      
      if List.sum(newWindow) > List.sum(window) then
        (increases + 1, newWindow)
      else
        (increases, newWindow)

    let part2() =
      let measurements = Utils.readLines "inputs/day01.txt" |> Seq.map(fun r -> r |> int) |> Seq.toList

      let firstThree = measurements |> List.take 3
      let state = (0, firstThree)
      let finalState = measurements |> List.removeManyAt 0 3 |> List.fold countSlidingIncreses state
      let (increases, lastWindow) = finalState

      printfn "Day 1, part 2 %A" increases
