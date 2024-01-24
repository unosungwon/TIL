def solution(d, budget):
    answer = 0

    d.sort()
    answer = 0

    for n in d:
        budget -= n    # => for 돌릴때 budget 이 9 가 아니라 n 만큼 뺀 budget이 된다.
        if budget >= 0:
            answer += 1
        else:
            break


    return answer








print(solution([1, 3, 2, 5, 4], 9))  # 3
print(solution([2, 2, 3, 3], 10))  # 4