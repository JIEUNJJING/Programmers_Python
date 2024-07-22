def solution(hp):
    answer = 0
    a = 5
    b = 3
    c = 1
    while (hp != 0):
        if hp >= a:
            answer += hp // a
            hp = hp % a
        elif hp >= b:
            answer += hp // b
            hp = hp % b
        else:
            answer += hp // c
            hp = hp % c
    
    return answer
