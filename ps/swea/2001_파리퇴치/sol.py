# swea 풀때는, 폴더 안에 input 파일을 넣어서 run 할 수 있음.
import sys
# 이 파일의 입력(input()) 을 파일로 대체
sys.stdin = open('input.txt')

### 위 두 줄은 제출할때 빼야함!!!


T = int(input())
for test_case in range(1, T + 1):

    N, M = map(int,input().split(' '))
    board = []
    for _ in range(N):
        board.append(list(map(int, input().split(' '))))

    maximum = 0
    for r_start in range(N - M + 1):
        for c_start in range(N - M + 1):
            total = 0
            for r in range(M):
                for c in range(M):
                    row, col = r_start + r, c_start + c
                    total += board[row][col]
            if total > maximum:
                maximum = total

    print(f'#{test_case} {maximum}')