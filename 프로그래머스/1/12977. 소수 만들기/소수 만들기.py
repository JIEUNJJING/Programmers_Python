from itertools import combinations

def solution(nums):
    answer = 0

    # nums 리스트에서 3개의 요소를 선택하는 모든 조합 만들어줌
    for i in combinations(nums, 3): # 튜플 i = (1, 2, 3), (1, 2, 4) ...
        s = sum(i) # 현재 조합 i의 합 계산
        chk = True # s가 소수인지 아닌지 체크하는 플래그 변수
        for j in range(2, int(s ** 0.5) + 1): # 2부터 s의 제곱근 까지만 반복
            if s % j == 0: # 소수가 아닌 경우
                chk = False
                break
        if chk is True: # 소수인 경우
            answer += 1
    return answer