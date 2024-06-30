def solution(arr):
    answer = 0
    X=[]
    
    for i in range(len(arr)):
        for j in range(arr[i]):
            X.append(arr[i])

    answer = X
    
    return answer