def solution(num_list):
    answer = 0
    
    for i in range(len(num_list)):
        if num_list[i] < 0:
            answer = i
            return answer
    answer = -1
    return answer