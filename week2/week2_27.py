# 중복된 문자 제거

def solution(my_string):
    new_list = list(dict.fromkeys(my_string))
    return (''.join(new_list))