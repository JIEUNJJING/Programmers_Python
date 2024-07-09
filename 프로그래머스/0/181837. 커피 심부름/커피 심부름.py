def solution(order):
    answer = 0
    price = 0
    
    for i in order:
        if ('americano' in i) or (i == 'anything'):
            price += 4500
        elif 'latte' in i:
            price += 5000
    answer = price
    return answer