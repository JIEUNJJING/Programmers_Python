from math import sqrt
def solution(n):
    answer = 0
    sqrt_n = sqrt(n)
    
    if sqrt_n == int(sqrt_n):
        answer = (sqrt_n + 1) * (sqrt_n + 1)
    else:
        answer = -1

    return int(answer)