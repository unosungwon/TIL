# swea 풀때는, 폴더 안에 input 파일을 넣어서 run 할 수 있음.
import sys
# 이 파일의 입력(input()) 을 파일로 대체
sys.stdin = open('sample_input.txt')

for test_case in range(1, (int(input()) + 1)):
    N = int(input())
    num_list = list(map(int, input().split(' ')))
    minimun = min(num_list)
    maximun = max(num_list)
    print(f'#{test_case} {maximun - minimun}')
