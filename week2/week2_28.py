# 삼각형의 완성조건 (1)

def solution(sides):
    sides.sort()
    if sides.pop() < sum(sides):
        return 1
    else:
        return 2