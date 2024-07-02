def solution(num_list):
    answer = 0
    a = len(num_list)
    
    if (a >= 11):
        answer = sum(num_list)
    else:
        answer = 1
        for i in num_list:
            answer = answer * i
    return answer