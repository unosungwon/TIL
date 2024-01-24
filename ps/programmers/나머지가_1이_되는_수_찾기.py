# https://school.programmers.co.kr/learn/courses/30/lessons/87389

# 1. 답안
def solution(n):
    for i in range(1, n+1):
        if n % i == 1:
            return(i)
            break


# 2. list comprehension 사용.
def solution(n):
    return [i for i in range(1,n+1) if n % 1 == 1][0]