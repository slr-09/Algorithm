import Foundation

let nk = readLine()!.split(separator: " ").map{Int($0)!}
let arr = readLine()!.split(separator: " ").map{Int($0)!}

var (st, ed, maxlength) = (0, 1, 0)
var number: Dictionary<Int,Int> = [arr[st]:1]

// ed가 arr의 마지막 인덱스에 닿을 때까지
while ed < nk[0] {
    number[arr[ed], default: 0] += 1
    
    // 현재 나온 숫자의 개수가 k보다 클 때
    if number[arr[ed]]! > nk[1] {
        // maxlength를 업데이트
        maxlength = max(maxlength, ed-st)
        
        // st 위치를 하나씩 뒤로 이동하며 같은 정수가 k개 이하가 되는 지점을 찾는다.
        while true {
            number[arr[st]]! -= 1
            st += 1
            
            if number[arr[ed]]! <= nk[1] {
                break
            }
        }
    }
    
    maxlength = max(maxlength, ed-st+1)
    ed += 1
}
print(maxlength)
