def solution(str_list, ex):
    answer = ''
    a = []
    
    for i in str_list:
        if ex not in i:
            a.append(i)
    answer = "".join(a)
        
    return answer
# 같은 코드를 실행 하였는데, 처음에는 실행 실패를 하였고,
# 다른 코드로 작성해 실행 후 통과 되었지만 다시 실행했을 때 실ㅍ
# 다시 처음 코드로 실행하니 성공함
# 왜 이런지 모르겟엄