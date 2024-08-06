def solution(A, B):
    answer = -1
    a_len = len(A)

    for i in range(a_len): # A길이만큼 반복 
        if(A == B): # A와 B가 같다면
            answer = i # 첫번째 비교라 i에 0이 들어가 있음(0 반환)
            break
        A = A[-1] + A[0:a_len-1] # 젤 뒤에 문자를 젤 앞으로 보내줌

    return answer