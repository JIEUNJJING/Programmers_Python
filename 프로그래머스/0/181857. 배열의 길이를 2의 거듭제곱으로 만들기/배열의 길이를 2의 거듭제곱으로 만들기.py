def solution(arr):
    while(True) :
        if len(arr) & len(arr)-1 == 0 : #2의 거듭제곱수인지 확인
            return arr
        else : #2의 거듭제곱이 아니라면
            arr.append(0)
            
    return answer