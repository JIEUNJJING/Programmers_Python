def solution(arr, k):
    answer = 0
    
    if (k % 2 != 0):
        for i in range(len(arr)):
            arr[i] = arr[i] * k
    else:
        for i in range(len(arr)):
            arr[i] = arr[i] + k
    answer = arr

    return answer