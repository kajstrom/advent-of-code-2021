module Entry

open Day01

[<EntryPoint>]
let main args =
    let arguments = args |> Array.toList
    match arguments.Head with
      |"day01" -> Day01.part1()
      |_ -> printfn "Unknown command"

    0