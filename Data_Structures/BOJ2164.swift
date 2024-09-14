import Foundation

let n = Int(readLine()!)!
var array: [Int] = Array(1...n)

var index = 1
while array.count > index {
    array.append(array[index])
    index += 2
}

print(array[array.count-1])
