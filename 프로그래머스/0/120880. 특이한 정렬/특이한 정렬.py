def solution(numlist, n):
    answer = []
    num_len = len(numlist)
    min_idx = 0 # 작은 값의 인덱스 담는 변수
    n1 = 0  
    n2 = 0
    
    for i in range(num_len): # 이중 for문 사용해 비교
        min_idx = i
        for j in range(i+1, num_len):
            n1 = abs(n - numlist[min_idx]) 
            n2 = abs(n - numlist[j]) 
            if n1 > n2: # 앞에 숫자가 뒤에 숫자보다 n과 거리가 크다면
                min_idx = j # min_idx 를 j로 바꿔줌 
            elif n1 == n2 and numlist[min_idx] < numlist[j]: # 두 수의 거리가 같은데 j번째 숫자가 더 크다면
                min_idx = j # min_idx 를 j로 바꿔줌 (거리가 같을 경우 더 큰 수를 앞에 오도록 배치하기 때문)
        numlist[i], numlist[min_idx] = numlist[min_idx], numlist[i] # 인덱스 값 바꿔준 후 숫자 자리 swap

    answer = numlist
    return answer