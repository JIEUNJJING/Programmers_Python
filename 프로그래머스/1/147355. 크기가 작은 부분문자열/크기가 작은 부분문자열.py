def solution(t, p):
    answer = 0

    for i in range(len(t)): # t문자열을 돌며
        # i번째부터 i + len(p)인덱스까지 슬라이싱하여 p보다 작거나 같고, 둘의 길이가 같을경우 
        if (t[i : i + len(p)]) <= p and len(t[i : i + len(p)]) == len(p):
            answer += 1 # 1 더해줌
    return answer