def solution(arr):
    answer = []
    stk = []
    i = 0

    while(i < len(arr)):
        if not stk: # 빈 배열인지 확인 
            stk.append(arr[i])
            i += 1
        else:
            if stk[-1] == arr[i]:
                stk.pop()
                i += 1
            else:
                stk.append(arr[i])
                i += 1

    if not stk:
        return  [-1]
    answer = stk
    return answer