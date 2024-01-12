# https://school.programmers.co.kr/learn/courses/30/lessons/12977

def solution(nums):
    s = []
    for a in range(len(nums)-2):
        for b in range(a+1, len(nums)-1):
            for c in range(b+1, len(nums)):
                s.append(nums[a] + nums[b] + nums[c])
    result = 0
    for n in s:
        for number in range(2,n):
            if n % number == False:
                break
        else:
            result += 1
    print(result)

solution([1,2,7,6,4])
