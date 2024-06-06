import Foundation

let nm = readLine()!.split(separator: " ").map{Int($0)!}
var arr = readLine()!.split(separator: " ").map{Int($0)!}

for i in 1..<nm[0] {
    arr[i] += arr[i-1]
}
for _ in 0..<nm[1] {
    let ij = readLine()!.split(separator: " ").map{Int($0)!}
    let (i,j) = (ij[0]-1, ij[1]-1)
    if i==0 {
        print(arr[j])
    } else {
        print(arr[j]-arr[i-1])
    }
}
