import Foundation

let n = Int(readLine()!)!
var meeting: [(Int, Int)] = []
for _ in 0..<n {
    let input = readLine()!.split(separator: " ").map{Int($0)!}
    meeting.append((input[0], input[1]))
}

meeting.sort { a, b in
    if a.1 == b.1 {
        return a.0 < b.0
    }
    return a.1 < b.1
}

var count = 0
var endTime = 0
for (st, ed) in meeting {
    if st >= endTime {
        endTime = ed
        count += 1
    }
}
print(count)
