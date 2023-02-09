def solution(arr):
    arr.sort()
    num=1
    while True:
        answer = num*arr[-1]
        check = True
        for i in range(len(arr)):
            if answer%arr[i] != 0:
                num += 1
                check = False
                break
        if check:   break
    return answer