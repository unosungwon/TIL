# https://www.acmicpc.net/problem/1000
# 입력값 1 2 / 결과값 3

x = input()\
x = list(map(int,x.split()))  #['1', '2']  # map은 우리 눈에 안보일 뿐. list 굳이 안해도 됨.
A, B = x[0], x[1]
print(A + B)


# 더짧게 가능
# # A, B = map(int,input().split())
# # print(A + B)

# A = int(input())
# B = int(input())
# -> 입력받으면
# 1
# 2
#
# 이렇게 받지만, 문제에서는
# 1 2
# 이렇게 받고 싶어함.
#
# X = input() 으로 받아야 됨.


