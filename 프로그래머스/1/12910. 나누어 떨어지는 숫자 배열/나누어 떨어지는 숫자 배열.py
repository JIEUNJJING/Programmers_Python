def solution(arr, divisor):
    answer = []

    for i in arr:
        if i % divisor == 0:
            answer.append(i)

    if len(answer) == 0: # divisor로 나누어 떨어지는 element가 하나도 없는경우
        return [-1]
    
    answer.sort()
    return answer