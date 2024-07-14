def solution(numbers, k):
    answer = 0
    idx = 1 # 계산 쉽게하기위해 1로 초기화
    
    while k > 1: # k가 1보다 작아지면 종료
        if idx + 2 <= len(numbers): # 현재 인덱스 값에 2를 더했을 때 numbers길이 안에 값이라면
            idx += 2 # 2를 더해주고
            k -= 1 # k는 1 감소
        elif idx + 2 >= len(numbers): # 현재 인덱스 값에 2를 더했을 때 numbers길이를 넘어선 값이라면 
            idx = (idx + 2) % len(numbers) # 2를 더한 값을 numbers 길이로 나눠주면 다음 친구 번호가 나옴
            k -= 1
    answer = idx # 현재 번호를 넘겨줌
    return answer