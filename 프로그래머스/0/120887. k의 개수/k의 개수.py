def solution(i, j, k):
    answer = 0
    for num in range(i, j + 1):
        for i in str(num): # 숫자를 문자열로 변환 후 각 자리의 숫자 순회
            if i == str(k): # 현재 자리 숫자와 k가 같다면
                answer += 1 # 1 증가
    return answer