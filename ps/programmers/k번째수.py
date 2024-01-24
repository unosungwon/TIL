def solution(array, commands):
    result = []
    for i, j, k in commands:
        new = sorted(array[i-1:j])
        result.append(new[k-1])

    return result

print(solution([1, 5, 2, 6, 3, 7, 4],
               [[2, 5, 3], [4, 4, 1], [1, 7, 3]]))
# [5, 6, 3]