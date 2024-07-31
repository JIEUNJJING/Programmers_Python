def solution(s, n):
    answer = ''

    for i in s:
        if i == ' ': # 공백일 경우
            answer += ' ' # 그대로 공백 넣어줌
        else:
            if 'a' <= i <= 'z':
                if ord(i) + n <= ord('z'): # n을 더해줬을 때, z보다 작거나 같으면 
                    answer += chr(ord(i) + n) # n을 더해주고
                else: # z보다 커서 범위를 넘어간다면 
                    answer += chr(ord(i) - 26 + n) # 현재 ord(i)에 26을 빼준 후, n을 더해준다
            elif 'A' <= i <= 'Z':
                if ord(i) + n <= ord('Z'):
                    answer += chr(ord(i) + n)
                else:
                    answer += chr(ord(i) - 26 + n)
    return answer