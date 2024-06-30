def solution(arr, n):
    answer = 0
    
    if (len(arr) % 2 != 0): #arr 길이가 홀수라면
        for i in range(len(arr)):
            if i % 2 == 0:
                arr[i] = arr[i] + n
    else: #arr 길이가 짝수라면
        for i in range(len(arr)):
            if i % 2 != 0:
                arr[i] = arr[i] + n

    answer = arr
    return answer