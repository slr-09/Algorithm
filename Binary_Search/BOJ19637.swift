import Foundation

let nm = readLine()!.split(separator: " ").map{Int($0)!}
var type: [(String, Int)] = []

var maxNum = 0
for _ in 0..<nm[0] {
    let input = readLine()!.split(separator: " ").map{String($0)}
    type.append((input[0],Int(input[1])!))
    maxNum = max(maxNum, Int(input[1])!)
}

var answer = ""
for _ in 0..<nm[1] {
    let power = Int(readLine()!)!
    
    var (stIdx,edIdx) = (0,nm[0]-1)
    while stIdx <= edIdx {
        let midIdx = (stIdx+edIdx)/2
        if power <= type[midIdx].1 {
            edIdx = midIdx - 1
        } else if power > type[midIdx].1 {
            stIdx = midIdx + 1
        }
    }
    
    answer += "\(type[stIdx].0)\n"
}
print(answer)
