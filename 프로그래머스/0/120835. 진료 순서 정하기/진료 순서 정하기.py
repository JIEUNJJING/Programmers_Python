def solution(emergency):
    answer = []
    
    for i in emergency:
        seq = 1 # 1로 초기화
        for j in emergency:
            if i < j:
                seq += 1
        answer.append(seq)
    return answer