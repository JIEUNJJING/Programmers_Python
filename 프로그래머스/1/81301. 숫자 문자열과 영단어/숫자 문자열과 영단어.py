def solution(s):
    answer = ''
    dic = {0:'zero', 1 : 'one', 2:'two', 3:'three', 4:'four', 5:'five', 6:'six', 7:'seven', 8:'eight', 9:'nine'}
    
    for k, v in dic.items(): # for문을 반복하며 k,v로 각각 key,value값을 받아옴
        s = s.replace(v, str(k)) # s문자열에서 v를 찾아 k로 대체해줌
    answer = int(s)
    
    return answer