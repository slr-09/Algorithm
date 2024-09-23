import Foundation

let input = readLine()!
let n = Int(readLine()!)!

// 커서의 좌,우에 있는 문자를 스택에 따로 저장
var left: [String] = Array(input.map{String($0)})
var right: [String] = []

for _ in 0..<n {
    let command = readLine()!
    
    switch(command) {
    case "L":
        if !left.isEmpty {
            right.append(left.removeLast())
        }
    case "D":
        if !right.isEmpty {
            left.append(right.removeLast())
        }
    case "B":
        if !left.isEmpty {
            left.removeLast()
        }
    default:
        left.append(String(command.last!))
    }
}

print((left+right.reversed()).joined())
