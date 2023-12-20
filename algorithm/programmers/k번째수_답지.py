# https://school.programmers.co.kr/learn/courses/30/lessons/42748
# from itertools import permutations, combinations => 순열 만드는 코드
# nPr, nCr

def solution(array, commands):
    answer = []
    for start, end, k in commands:
        part = array[start-1:end]
        part.sort()
        answer.append(part[k-1])
    return answer

print(solution([1, 5, 2, 6, 3, 7, 4],[[2, 5, 3], [4, 4, 1], [1, 7, 3]]))
# [5, 6, 3]
