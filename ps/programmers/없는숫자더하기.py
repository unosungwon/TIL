# https://school.programmers.co.kr/learn/courses/30/lessons/86051

# 만약 주석처리 하고 싶으면
# ctrl + / 하면
# 한번에 주석 처리 가능.


def solution(numbers):
    number_box = range(10)
    total = 0
    for n in number_box:
        if n not in numbers:
            total += n
    return total

def solutions(numbers):
    number_box = range(10)
    for n in number_box:
        if n in numbers:
            numbers.remove(n)
    return sum(numbers)


print(solution([1,2,3,4,6,7,8,0]))   # 14
print(solution([5,8,4,0,6,7,9]))   # 6