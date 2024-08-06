def solution(A, B):
    answer = 0

    if A == B:
        return 0

    for i in range(len(A)): # A길이만큼 반복 
        if A == B:# A와 B가 같다면
            answer = i # 1 반환
            break
        A = A[-1] + A[0:len(A) - 1] # A와 B가 다르면, 맨 뒤 문자를 제일 앞으로 옮겨 다시 비교
    if A != B:
        answer = -1
    return answer