def solution(s):
    answer = []
    s = list(s.split(' '))

    for i in s: #i에 try, hello, world 이렇게 들어옴
        new_word = ''
        for index, char in enumerate(i): # i의 인덱스값과 문자를 각각 index와 char에 넣음
            if index % 2 == 0: # 인덱스가 짝수일 경우
                new_word += char.upper() # 대문자로 변환해 new_word에 넣어줌
            else: # 홀수일 경우
                new_word += char.lower() # 소문자로 변환해 new_word에 넣어줌
        answer.append(new_word) # TrY, HeLlo, WoRlD이렇게 각각 answer에 추가함
    
    return ' '.join(answer) # 리스트를 문자열로 변환