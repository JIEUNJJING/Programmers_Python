def solution(arr):
    answer = []
    a = [arr[0]]
    
    for i in range(1, len(arr)):
        if arr[i] != a[-1]:
            a.append(arr[i])
    answer = a

    return answer