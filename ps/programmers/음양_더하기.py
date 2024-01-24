# https://school.programmers.co.kr/learn/courses/30/lessons/76501

# 1. 답안
def solution(absolutes, signs):
    int_list = []
    for i in range(len(absolutes)):
        if signs[i] == False:
            int_list.append(absolutes[i] * (-1))
        else:
            int_list.append(absolutes[i])
    return sum(int_list)

