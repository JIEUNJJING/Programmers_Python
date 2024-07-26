def solution(rank, attendance):
    answer = 0
    pick = []
    a = 0
    b = 0
    c = 0

    for i in range(len(rank)): 
        if attendance[i] == True:
            pick.append(rank[i])

    pick.sort() 

    a = rank.index(pick[0]) * 10000 
    b = rank.index(pick[1]) * 100 
    c = rank.index(pick[2]) 
    answer = a + b + c 
        
    return answer