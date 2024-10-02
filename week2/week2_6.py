# 외계행성의 나이

def solution(age):
    answer = ''
    age_list = list(map(int,str(age)))
    for i in age_list:
        answer += chr(i+97)
    return answer