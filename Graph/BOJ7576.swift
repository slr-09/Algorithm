import Foundation

let mn = readLine()!.split(separator: " ").map{Int($0)!}
var graph: [[Int]] = []
var queue: [(Int, Int)] = []
var (answer, count) = (0,queue.count)
for j in 0..<mn[1] {
    let input = readLine()!.split(separator: " ").map{Int($0)!}
    graph.append(input)
    for i in 0..<input.count {
        if input[i] == 1 {
            queue.append((j,i))
            count += 1
        } else if input[i] == -1 {
            count += 1
        }
    }
}

func bfs() {
    var index = 0
    while index < queue.count {
        // removeFirst() 대신 index를 사용하는 것이 시간 절약의 핵심! 
        let (x,y) = queue[index]
        index += 1
        
        for (nx, ny) in [(x-1, y), (x, y-1), (x+1, y), (x, y+1)] {
            if !(0..<mn[1] ~= nx) || !(0..<mn[0] ~= ny) { continue }
            if graph[nx][ny] != 0 { continue }
            
            graph[nx][ny] = graph[x][y] + 1
            answer = max(answer, graph[x][y])
            queue.append((nx,ny))
            count += 1
            
        }
    }
}

bfs()

print(count == mn[0]*mn[1] ? answer : -1)
