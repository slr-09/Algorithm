import Foundation

let input = readLine()!.split(separator: " ").map{Int($0)!}
let (n, L, R) = (input[0],input[1],input[2])
var graph: [[Int]] = []
for _ in 0..<n {
    graph.append(readLine()!.split(separator: " ").map{Int($0)!})
}

var visited: [[Bool]] = Array(repeating: Array(repeating: false, count: n), count: n)

var answer = 0

var idxList: [(Int, Int)] = []
var sum: Int = 0
func bfs(_ x: Int, _ y: Int) {
    var queue = [(x,y)]
    var index = 0
    
    // 시작점 초기화
    visited[x][y] = true
    idxList = [(x,y)]
    sum = graph[x][y]
    
    while index < queue.count {
        let (x,y) = queue[index]
        index += 1
        
        for (nx,ny) in [(x+1,y), (x,y+1), (x-1,y), (x,y-1)] {
            if !(0..<n ~= nx) || !(0..<n ~= ny) { continue }
            if visited[nx][ny] { continue }
            
            // 차이가 L 이상 R 이하
            if L...R ~= abs(graph[x][y] - graph[nx][ny]) {
                // 방문 기록
                visited[nx][ny] = true
                
                sum += graph[nx][ny]
                idxList.append((nx,ny))
                
                queue.append((nx,ny))
            }
        }
    }
}

// 인구 업데이트
func update() {
    for (x,y) in idxList {
        graph[x][y] = sum / idxList.count
    }
}

while true {
    var count = 0
    visited = Array(repeating: Array(repeating: false, count: n), count: n)
    
    for i in 0..<n {
        for j in 0..<n {
            if !visited[i][j] {
                bfs(i,j)
                update()
                count += 1
            }
        }
    }
    
    // count가 n*n이면 모든 나라가 인구 이동을 안하는 것
    if count == n*n { break }
    
    answer += 1
}

print(answer)
