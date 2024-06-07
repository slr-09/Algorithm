import Foundation

let n = Int(readLine()!)!
var arr = readLine()!.split(separator: " ").map{Int($0)!}
let sortedArr = Array(Set(arr)).sorted()    // 중복 제거 후 정렬

var indexMap = [Int:Int]()
for (index, value) in sortedArr.enumerated() {
    indexMap[value] = index
}

for i in 0..<arr.count {
    arr[i] = indexMap[arr[i]]!
}

print(arr.map{String($0)}.joined(separator: " "))
