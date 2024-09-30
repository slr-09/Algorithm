import Foundation

let n = Int(readLine()!)!
let p = readLine()!.split(separator: " ").map { Int($0)! }
let m = Int(readLine()!)!
var family: [[Int]] = Array(repeating: [], count: n+1)
var visited: [Int] = Array(repeating: -1, count: n+1)
for _ in 0 ..< m {
    let input = readLine()!.split(separator: " ").map { Int($0)! }
    family[input[0]].append(input[1])
    family[input[1]].append(input[0])
}


visited[p[0]] = 0
func bfs(_ v: Int) {
    var queue = [v]
    
    while !queue.isEmpty {
        let v = queue.removeFirst()
        if v == p[1] { break }
        
        for i in family[v] {
            if visited[i] == -1 {
                visited[i] = visited[v] + 1
                queue.append(i)
            }
        }
    }
}

bfs(p[0])
print(visited[p[1]])
