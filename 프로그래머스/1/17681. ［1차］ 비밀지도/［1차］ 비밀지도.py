def solution(n, arr1, arr2):
    answer = []
    new_map = ''
    for i in range(n):
        # or연산 후 2진수로 바꿔주고, zfill()함수를 사용해 앞자리를 0으로 채워준다.
        # 변환해준 후, replace()함수를 사용해 1은 #으로 0은 공백으로 교체해준다. 
        new_map = format(arr1[i] | arr2[i], 'b').zfill(n).replace('1', '#' ).replace('0', ' ') 
        answer.append(new_map)
    
    return answer