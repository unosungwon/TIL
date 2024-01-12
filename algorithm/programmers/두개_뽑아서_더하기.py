# https://school.programmers.co.kr/learn/courses/30/lessons/68644


def solution(numbers):
    result = []

    for idx in range(len(numbers)):
        for i in range(idx+1, len(numbers)):
            result.append(numbers[idx] + numbers[i])

    result = set(result)
    result = list(result)
    print(result)

