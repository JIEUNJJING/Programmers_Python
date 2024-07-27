from math import gcd
def solution(a, b):
    b = b/gcd(a, b) # 분모(b)를 a와 b의 최대 공약수로 나누어 기약분수 형태로 만듬
    while b%2==0: # 분모를 2로 나누어 나머지가 0이 될 때까지 나눔
        b//=2 # 2로 나눈 몫을 b에 할당
    while b%5==0: # 분모를 5로 나누어 나머지가 0이 될 때까지 나눔
        b//=5 # 5로 나눈 몫을 b에 할당
    if b == 1: # 재할당된 분모가 1이면 1반환
        return 1
    else: # 아니면 2 반환
        return 2