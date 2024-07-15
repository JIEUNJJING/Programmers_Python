def solution(sides):
    answer = 0
    max_num = max(sides)
    min_num = min(sides)
    sum_num = max_num + min_num

    for i in range(1, max_num + 1): # 가장 긴 변이 sides의 max값일 경우
        if i + min_num > max_num:
            answer += 1
        
    for j in range(max_num + 1, sum_num): # 가장 긴 변이 새로 들어오는 수일 경우
        answer += 1
    return answer