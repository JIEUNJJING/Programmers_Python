def solution(strings, n):
    answer = []
    j = 0

    new_s = sorted(strings) # sorted() 함수는 정렬된 새로운 리스트를 반환

    #삽입정렬(Insertion Sort)
    for i in range(1, len(new_s)):
        j = i
        while new_s[j-1][n] > new_s[j][n] and j > 0:
            new_s[j], new_s[j-1] = new_s[j-1], new_s[j] # 앞자리와 swap 
            j = j - 1

    answer = new_s
    return answer