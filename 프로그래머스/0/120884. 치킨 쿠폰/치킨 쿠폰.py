def solution(chicken):
    answer = -1
    service = chicken // 10 
    coupon = service + (chicken % 10) 
    while(coupon >= 10): 
        service += coupon // 10
        coupon = (coupon // 10) + (coupon % 10) 
    
    answer = service
    return answer