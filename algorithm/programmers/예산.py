# https://school.programmers.co.kr/learn/courses/30/lessons/12982

def solution(d, budget):
    d.sort(reverse=True)
    total = sum(d)
    if total == budget:
        result = d
    else:
        for n in d:
            if total >= budget:
                total -= n
                d.remove(n)
            else:
                result = d
    return len(d)

print(solution([1,3,2,5,4], 9))   # 3
print(solution([2,2,3,3], 10))   # 4