def solution(arr):
    answer = 0
    x = 0

    while True:
        next = []
        for i in arr:
            if (i >= 50) and (i % 2 == 0):
                next.append(i // 2)
            elif (i < 50) and (i % 2 != 0):
                next.append((i * 2) + 1)
            else:
                next.append(i)

        if arr == next: # arr(x) = arr(x + 1) 두 배열이 같으면
            return x # 전 배열 값인 x 반환
        else: # 두 배열이 다르면
            x += 1 # 반복횟수 1 증가
            arr = next # 바뀐 배열 값으로 현재 배열 값 바꿔주기
        
    return answer