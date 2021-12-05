module Entry

open Day01
open Utils

[<EntryPoint>]
let main args =
    let arguments = args |> Array.toList
    match arguments.Head with
      |"day01" -> 
              Utils.timeOperation Day01.part1
              Utils.timeOperation Day01.part2
      |_ -> printfn "Unknown command"

    0