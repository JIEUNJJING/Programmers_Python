def solution(n, m):
    answer = []
    a = 0
    b = 0
    
    for i in range(1, n+1):
        if n % i == 0 and m % i == 0:
            a = i
    b = (n * m) / a # 최소 공배수 구하는 공식 : n * m하고 최대 공약수로 나누기

    return [a, int(b)]