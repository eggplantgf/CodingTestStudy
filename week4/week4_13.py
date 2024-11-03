# 치킨 쿠폰

def solution(chicken):
    total_chicken = chicken
    coupons = chicken

    while coupons >= 10:
        new_chicken = coupons // 10
        total_chicken += new_chicken
        coupons = coupons % 10 + new_chicken

    return total_chicken //10