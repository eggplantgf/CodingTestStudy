# 구슬을 나누는 경우의 수

def solution(balls, share):
    a = 1
    b = 1
    for i in range(share):
        a = a * (balls-i)
        b = b * (share-i)
    return int(a/b)