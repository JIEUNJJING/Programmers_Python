def solution(n):
    answer = 0
    b = 0 # 나머지
    c = [] # 순서대로 나머지 담는 배열 변수

    while(n > 0):
        b = n % 3 # 나머지 값을 b에 저장
        n = n // 3 # 3으로 나눈 몫을 다시 n에 저장
        c.append(b) # 배열에 나머지 값 넣어줌

    l = len(c) - 1 # 지수
    for i in c: # 3진법을 10진법으로 표현하는 반복문
        if l == 0: # 지수가 1일 경우 1을 더해준다(2의 1승 = 2)
            answer += (i * 1)
        else:
            answer += (i * (3 ** l))
            l -= 1 # 지수 1 감소
    return answer