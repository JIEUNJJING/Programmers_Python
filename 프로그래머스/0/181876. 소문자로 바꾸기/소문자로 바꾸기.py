def solution(myString):
    answer = ''

    for i in myString:
        if (97 <= ord(i) <= 122):
            answer += (i)
        else:
            answer += chr(ord(i) + 32)
    return answer