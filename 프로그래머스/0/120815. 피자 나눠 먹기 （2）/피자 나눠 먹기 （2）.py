def solution(n):
    answer = 0
    p = 0 # 피자 조각수 카운트
    r = 1 # 사람수 * 피자조각수를 피자 한판갯수로 나눈 나머지
    while r != 0: # r이 0이 되면 반복문 종료
        p += 1
        r = (n * p) % 6

    answer = (n * p) // 6
    return answer