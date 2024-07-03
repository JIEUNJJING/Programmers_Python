def solution(myString):
    answer = ''
    a = list(myString)

    for i in range(len(a)):
        if a[i] == "a":
            a[i] = "A"
        elif(66 <= ord(a[i]) <=90):
            a[i] = a[i].lower()
        else:
            a[i] = a[i]
    
    answer = "".join(a)

    return answer