import Foundation

// 정규식 사용
// 메모리: 79660KB, 시간: 28ms
let n = Int(readLine()!)!
let regex = "^(100+1+|01)+$"
for _ in 0..<n {
    let input = readLine()!
    if input.range(of: regex, options: .regularExpression) != nil {
        print("YES")
    } else {
        print("NO")
    }
}

// 직접 구현 
// 메모리: 79660KB, 시간: 8ms
import Foundation

let n = Int(readLine()!)!
for _ in 0..<n {
    let input = readLine()!
    print(isCorrect(str: input))
}

func isCorrect(str: String) -> String {
    var s = str
    while !s.isEmpty {
        if s.hasPrefix("01") {
            s.removeFirst(2)
        } else if s.hasPrefix("100") {
            s.removeFirst(3)
            s = remove(str: s, ch: "0")
            if !s.hasPrefix("1") { return "NO" }
            s = remove(str: s, ch: "1")
        } else {
            return "NO"
        }
    }
    return "YES"
}

func remove(str: String, ch: String) -> String {
    var s = str
    var count = 0
    while true {
        if s.isEmpty { return s }
        if s.hasPrefix("100") && (ch != "1" || count > 0) {
            return s
        }
        if s.hasPrefix(ch) {
            s.removeFirst()
            count += 1
        } else {
            return s
        }
    }
}
