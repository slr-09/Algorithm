import Foundation

var num = 1
while true {
    let n = Int(readLine()!)!
    if n == 0 { break }
    
    var graph: [[Int]] = []
    for _ in 0..<n {
        graph.append(readLine()!.split(separator: " ").map{Int($0)!})
    }
    
    bfs(n, graph)
}

func bfs(_ n: Int, _ graph: [[Int]]) {
    var visited: [[Int]] = Array(repeating: Array(repeating: Int.max, count: n), count: n)
    var queue = [(0,0)]
    var index = 0
    visited[0][0] = graph[0][0]
   
    while index < queue.count {
        let (x,y) = queue[index]
        index += 1
        
        for (nx,ny) in [(x+1,y),(x-1,y),(x,y-1),(x,y+1)] {
            if !(0..<n ~= nx && 0..<n ~= ny) { continue }
            
            let cost = visited[x][y]+graph[nx][ny]
            if visited[nx][ny] > cost {
                visited[nx][ny] = cost
                queue.append((nx,ny))
            }
        }
    }
    
    print("Problem \(num):", visited[n-1][n-1])
    num += 1
}
