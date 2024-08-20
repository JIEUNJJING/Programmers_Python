def solution(array):
    answer = 0
    arr = {}
    
    for i in array: # value값이 0으로 초기화 된 dictionary(arr) 생성
        arr[i] = 0

    # 최빈값 구하기
    for i in array: # array 반복
        if i in arr: # arr에 array의 key값이 있다면
            arr[i] += 1 # 1 증가(카운트)

    arr = sorted(arr.items(), key=lambda x:x[1], reverse=True)

    # 정렬된 arr 은 list 자료형으로 되어 있어서 2차원 배열 형태로 사용하면 된다.
    if len(arr) != 1 and arr[0][1] == arr[1][1]: # 길이가 1이 아니거나 큰값이 2개 이상인 경우
        answer = -1
    else: # 최빈값의 key값을 반환합니다. (arr[0][0]->key값, arr[0][1]->value값)
        answer = arr[0][0]
    return answer