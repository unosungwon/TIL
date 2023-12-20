def solution(d, budget):
    for i in range(1, len(d)):
        sort_d = sorted(d)
        if sum(sort_d[0:i]) > budget:
            break

    return i - 1

print(solution([1, 3, 2, 5, 4], 9))