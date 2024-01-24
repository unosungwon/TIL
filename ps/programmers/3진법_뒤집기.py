# https://school.programmers.co.kr/learn/courses/30/lessons/68935

def solution(num):
    i = 1
    i_list = []
    while i > 0:
        if num > 0:
            if 3 ** i == num:
                num -= 3 ** i
                i_list.append(i)
                i = 1
                continue
            elif 3 ** i > num:
                num -= 3 ** (i-1)
                i_list.append(i-1)
                i = 1
                continue
            elif 3 ** i < num:
                i += 1
        elif num <= 0:
            break

    power_3 = {}
    for n in range(i_list[0] + 1):
        for i in i_list:
            if n == i :
                if str(n) not in power_3:
                    power_3[str(n)] = 1
                elif power_3[str(n)] == 0:
                    power_3[str(n)] = 1
                elif power_3[str(n)] >= 1:
                    power_3[str(n)] += 1
            elif n != i :
                if str(n) not in power_3:
                    power_3[str(n)] = 0
                elif power_3[str(n)] >= 1:
                    continue

    power_10 = []
    for k, v in power_3.items():
        power_10.append(v)

    total = 0
    for idx,p in enumerate(power_10):
        if p >= 1 :
            total += 3 ** (len(power_10)-1 -idx) * p

    return total

solution(45)




