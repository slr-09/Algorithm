import Foundation

let input = readLine()!.split(separator: " ").map{Int($0)!}
var visitors = readLine()!.split(separator: " ").map{Int($0)!}

for i in 1..<input[0] {
    visitors[i] += visitors[i-1]
}

var compareDict: Dictionary<Int, Int> = [visitors[input[1]-1]:1]
for i in input[1]..<input[0] {
    let sub = visitors[i]-visitors[i-input[1]]
    compareDict[sub, default: 0] += 1
}

let dict = compareDict.sorted { $0 > $1 }
let answer = dict.first!
print(answer.key==0 ? "SAD" : "\(answer.key)\n\(answer.value)")
