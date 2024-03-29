﻿module Entry

open Day01
open Day02
open Day03
open Utils

[<EntryPoint>]
let main args =
    let arguments = args |> Array.toList
    match arguments.Head with
      |"day01" -> 
              Utils.timeOperation Day01.part1
              Utils.timeOperation Day01.part2
      |"day02" ->
              Utils.timeOperation Day02.part1
              Utils.timeOperation Day02.part2
      |"day03" ->
              Utils.timeOperation Day03.part1
      |_ -> printfn "Unknown command"

    0