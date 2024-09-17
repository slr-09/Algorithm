import Foundation

let input = readLine()!.split(separator: " ").map{Int($0)!}
var dict: Dictionary<String, Int> = [:]
for _ in 0..<input[0] {
    let word = readLine()!
    if word.count < input[1] { continue }
    dict[word, default: 1] += 1
}

let sortedDict = dict.sorted {
    if $0.value == $1.value {
        if $0.key.count == $1.key.count {
            return $0.key < $1.key
        } else {
            return $0.key.count > $1.key.count
        }
    } else {
        return $0.value > $1.value
    }
}

var answer = ""
for (key, _) in sortedDict {
    answer += "\(key)\n"
}
print(answer)
