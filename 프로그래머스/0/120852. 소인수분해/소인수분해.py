def solution(n):
    answer = []
    i = 2
    while (i <= n): # 소인수라 n보다 작거나 같음
        if n % i == 0: # 나머지가 0이라면 
            answer.append(i) # i값 추가
            n = n // i # n // i해서 나온 값으로 n을 바꿔줌
        else: # 나머지가 0이 아니라면 
            i += 1 # 소인수를 찾기위해 2부터 시작해 1씩 증가하며 찾아주기위해
    answer = list(sorted(set(answer))) # 중복된값 삭제 : set()
    return answer 