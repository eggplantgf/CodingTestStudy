# 각도기

def solution(angle):
    if angle < 90:
        answer = 1
    elif angle == 90:
        answer = 2
    elif angle > 90 and angle < 180 :
        answer = 3
    elif angle == 180:
        answer = 4
    else:
        return 0
    return answer