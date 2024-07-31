def solution(s):
    answer = []
    a = ''
    old = 0
    
    for i in range(len(s)): 
        if s[i] not in a: # a라는 문자열로 선언된 변수에 현재값인 s[i]가 없다면
           a += s[i] # a를 넣어줌
           answer += [-1] # 처음 나온 문자이므로 answer에는 -1을 넣어줘야함
        else: # s[i]가 a에 있다면
            old = a.rfind(s[i]) # 현재 자신과 가장 가까운 곳에 있는 글자의 인덱스 값을 알아야하므로 rfind()함수 사용
            a +=(s[i]) # 가까운 곳에 있는 글자의 인덱스 값을 찾은 후, a에 문자 넣어줌
            answer += [i - old] # answer에는 현재 인덱스값에서 자신과 같으면서 가까이 있는 글자의 인덱스값(old)를 빼준 값을 넣어줌
    return answer