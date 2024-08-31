def solution(n):
    answer = 0
        
    for i in range(2, n + 1): # 1은 소수가 아니므로 2부터 시작
        flag = True # 현재 숫자가 소수인지 판별하는 플래그 변수
        for j in range(2, int(i ** 0.5) + 1): # 제곱근까지만 반복
            if i % j == 0: # 나누어 떨어진다면 (약수가 존재한다면)
                flag = False
                break # 반복문 종료
        
        if flag == True: # 소수인 경우
            answer += 1
    
    return answer