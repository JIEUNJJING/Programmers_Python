def solution(arr, idx):
    answer = 0

    for i in range(idx, len(arr)):
        if arr[i] == 1:
            answer = i
            return answer
        elif arr[i] == 0:
            answer = -1

    return answer