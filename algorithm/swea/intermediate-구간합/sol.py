# swea 풀때는, 폴더 안에 input 파일을 넣어서 run 할 수 있음.
import sys
# 이 파일의 입력(input()) 을 파일로 대체
sys.stdin = open('input.txt')


T = int(input())

for tc in range(1, T +1):
    N, M = map(int, input().split(' '))
    ai = input().split(' ')

    # 혹시 모를 공백들 제거
    if '' in ai:
        ai.remove('')

    # ai 리스트 요소들을 int 로 형변형
    ai_int = list(map(int, ai))

    max = 0
    min = 0

    for i in range(N-M+1):
        # max 에 일단 비교 가능한 수 넣어놓기
        if max == 0:
            max = sum(ai_int[i:i+M])
        elif max != 0:
            if max < sum(ai_int[i:i+M]):
                max = sum(ai_int[i:i+M])

    for i in range(N - M + 1):
        # max 에 일단 비교 가능한 수 넣어놓기
        if min == 0:
            min = sum(ai_int[i:i+M])
        elif min != 0:
            if min > sum(ai_int[i:i+M]):
                min = sum(ai_int[i:i+M])

    print(f'#{tc} {max-min}')