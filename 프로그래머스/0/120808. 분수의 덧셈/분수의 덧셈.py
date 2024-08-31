import math

def solution(numer1, denom1, numer2, denom2):
    answer = []
    d = denom1 * denom2 # 분모끼리 곱해줌 (공통분모)
    n = numer1 * denom2 + numer2 * denom1 # 각 분자와 다른 분수의 분모와 곱셈 계산한 두 분자를 더해줌

    g = math.gcd(n, d) # 최대공약수 찾음

    answer = [n // g, d // g] # 약분

    return answer