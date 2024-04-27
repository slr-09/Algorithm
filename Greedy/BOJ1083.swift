let n = Int(readLine()!)!
var arr: [Int] = readLine()!.split(separator: " ").map { Int($0)! }
var s = Int(readLine()!)!

var idx = 0
while s > 0 && idx < n-1 {
    let maxIdx = arr.firstIndex(of: arr[idx ... min(n-1,idx+s)].max()!)!
    let removedValue = arr.remove(at: maxIdx)
    arr.insert(removedValue, at: idx)
    s -= maxIdx - idx
    idx += 1
}

print(arr.map { String($0) }.joined(separator: " "))
