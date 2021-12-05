module Utils
  open System.IO
  open System.Diagnostics

  let readLines (filePath:string) = seq {
    use sr = new StreamReader (filePath)
    while not sr.EndOfStream do
        yield sr.ReadLine ()
  }

  let timeOperation func: unit =
    let timer = new Stopwatch()
    timer.Start()
    func()
    timer.Stop()
    let duration = string timer.ElapsedMilliseconds
    printfn "Duration %sms" duration