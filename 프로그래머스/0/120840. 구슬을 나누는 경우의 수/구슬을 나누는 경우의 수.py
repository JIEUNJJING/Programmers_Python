from math import factorial as fac
def solution(balls, share):
    answer = 0

    d = fac(balls)
    n1 = fac(balls - share)
    n2 = fac(share)

    answer = d //(n1 * n2)
    return answer