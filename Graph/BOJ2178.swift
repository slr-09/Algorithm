import Foundation

let nm = readLine()!.split(separator: " ").map{ Int($0)! }
var graph: [[Int]] = []
for _ in 0..<nm[0] {
    graph.append(readLine()!.compactMap{Int(String($0))})
}

let dx = [-1,1,0,0], dy = [0,0,1,-1]
func bfs() {
    var queue = [(0,0)]
    
    while !queue.isEmpty {
        let (x,y) = queue.removeFirst()
        for i in 0..<4 {
            let nx = dx[i] + x
            let ny = dy[i] + y
            if nx<0 || nx>=nm[0] || ny<0 || ny>=nm[1] {
                continue
            }
            if graph[nx][ny] == 1 {
                graph[nx][ny] = graph[x][y]+1
                queue.append((nx,ny))
            }
        }
    }
}
bfs()
print(graph[nm[0]-1][nm[1]-1])
