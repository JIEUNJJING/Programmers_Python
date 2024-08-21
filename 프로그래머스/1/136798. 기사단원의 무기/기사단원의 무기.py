def solution(number, limit, power):
    answer = 0
    numlist = [0] * (number) # [0, 0, 0, 0, 0]
    
    for i in range(1, number + 1): # 1부터 number까지 (1 - 5)
        for j in range(1, int(i ** 0.5) + 1): # 1부터 자기자신의 제곱수까지 반복하며 약수 구하기
            if i % j == 0: # 나누어 떨어지면 (약수)
                numlist[i - 1] += 1
                if j ** 2 != i: # 제곱이 되는 수는 count 1 하여 중복 방지
                    numlist[i - 1] += 1
        if numlist[i - 1] > limit: # 약수의 갯수가 limit을 초과하면
            answer += power # power 더해주기
        else: # limit 이하인 경우
            answer += numlist[i - 1] # 약수의 갯수 그대로 더해주기

    return answer