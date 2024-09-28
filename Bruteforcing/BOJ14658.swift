import Foundation

let input = readLine()!.split(separator: " ").map{Int($0)!}
let (n,m,l,k) = (input[0],input[1],input[2],input[3])
var star: [(Int,Int)] = []
for _ in 0..<k {
    let xy = readLine()!.split(separator: " ").map{Int($0)!}
    star.append((xy[0],xy[1]))
}

var answer = 101
for (nx, _) in star {
    for (_, ny) in star {
        var count = k
        for (x,y) in star {
            if nx...nx+l ~= x && ny...ny+l ~= y {
                count -= 1
            }
        }
        answer = min(answer, count)
    }
}

print(answer)
