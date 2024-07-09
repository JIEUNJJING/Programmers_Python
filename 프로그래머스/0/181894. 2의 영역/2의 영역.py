def solution(arr):
    answer = []
    
    if 2 in arr:
        if arr.count(2) > 1:
            start = arr[:].index(2)
            # 전체 길이에서 마지막 인덱스 값을 빼주는 이유:
            # 역순으로 순서를 바꿔 마지막 원소 인덱스가 0이기 때문에 전체 길이에서 빼줘야 찾는 문자의 마지막 인덱스 값이 됨
            end = len(arr) - arr[::-1].index(2)
        else:
            answer = [arr[arr.index(2)]]
            return answer
    else:
        return [-1]

    print(start, end)

    answer = arr[start:end]
    return answer