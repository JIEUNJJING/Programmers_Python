def solution(array, commands):
    answer = []
    a = 0

    for i, j , k in commands: # 각각 i, j, k로 세개의 숫자를 받아옴
        a = array[i - 1:j] # a변수를 지정해주어 i번째부터 j번째 숫자까지 자름
        a.sort() # 숫자를 정렬해줌
        answer.append(a[k - 1]) # 정렬된 숫자의 k번째 수를 answer에 넣어줌
    
    return answer