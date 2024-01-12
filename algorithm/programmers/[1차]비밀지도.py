# https://school.programmers.co.kr/learn/courses/30/lessons/17681

# 노가다 내 1번 답
def solution(n, arr1, arr2):

    binaries1 = []
    for num in arr1:
        binary1 = []
        while num >= 0 :
            if num == 0:
                break
            elif num > 0:
                binary1.append(num % 2)
                num = num // 2
        binary1 = binary1[::-1]
        # n 길이 맞추기
        if len(binary1) != n:
            lack = n - len(binary1)
            for i in range(lack):
                binary1.insert(0,0)
        binaries1.append(binary1)

    binaries2 = []
    for num in arr2:
        binary2 = []
        while num >= 0:
            if num == 0:
                break
            elif num > 0:
                binary2.append(num % 2)
                num = num // 2
        binary2 = binary2[::-1]
        # n 길이 맞추기
        if len(binary2) != n:
            lack = n - len(binary2)
            for i in range(lack):
                binary2.insert(0, 0)
        binaries2.append(binary2)

    secret_maps = []
    for r in range(n):
        secret_map = ''
        for c in range(n):
            if binaries1[r][c] or binaries2[r][c]:
                secret_map += '#'
            else:
                secret_map += ' '
        secret_maps.append(secret_map)

    print(secret_maps)




solution(5,[9,20,28,18,11],[30,1, 21, 17, 28])