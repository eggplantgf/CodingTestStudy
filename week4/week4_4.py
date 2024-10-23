# 머쓱이보다 키 큰 사람

def solution(array, height):
    cnt = 0
    for i in array:
        if i > height :
            cnt += 1
        else:
            pass
    return cnt