import Foundation

let n = readLine()!.split(separator: " ").map{Int($0)!}
var graph: [[Int]] = Array(repeating: [], count: n[0]+1)
var visited: [Int] = Array(repeating: 0, count: n[0]+1)
for _ in 0..<n[1] {
    let u = readLine()!.split(separator: " ").map{Int($0)!}
    graph[u[0]].append(u[1])
    graph[u[1]].append(u[0])
}
var index = 1
var idx = 0
func bfs(_ v: Int) {
    visited[v] = index
    var queue = [v]
    while idx < queue.count {
        let q = queue[idx]      // removeFirst() 대신 idx로
        for i in graph[q].sorted() {
            if visited[i] == 0 {
                index += 1
                visited[i] = index
                queue.append(i)
            }
        }
        idx += 1
    }
}

bfs(n[2])
print(visited[1...].map{String($0)}.joined(separator: "\n"))
