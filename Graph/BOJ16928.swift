import Foundation

let nm = readLine()!.split(separator: " ").map{Int($0)!}
var graph = (0...100).map { i in Array(stride(from: min(i+6, 100), through: i+1, by: -1))}
var price: [Int] = Array(repeating: 0, count: 101)
for _ in 0..<nm[0]+nm[1] {
    let input = readLine()!.split(separator: " ").map{Int($0)!}
    graph[input[0]] = [input[1]]
}

func bfs() {
    var queue = [1]
    var index = 0
    
    while index < queue.count {
        let q = queue[index]
        index += 1
        
        var check: Int = 1
        // 뱀 or 사다리
        if graph[q].count == 1 && q != 99 {
            check = 0
        }
        
        for i in graph[q] {
            // 1. 다음 목적지에 방문한 적이 없거나
            // 2. 다음 목적지의 최소 이동 횟수가 현재보다 클 때 (업데이트 필요할 때)
            if price[i] == 0 || price[i] > price[q]+check {
                price[i] = price[q]+check
                queue.append(i)
            }
        }
    }
}

bfs()

print(price[100])
