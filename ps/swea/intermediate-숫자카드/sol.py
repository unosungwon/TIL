T = int(input())

for tc in range(1, T+1):
    N = int(input())
    ai = list(map(int, list(input())))
    cnt = {}

    for i in ai:
        # 숫자 cnt에 최초 등록
        if i not in cnt:
            cnt[i] = 1
        # 숫자 cnt에 있으면 1씩 카운트
        elif i in cnt:
            cnt[i] += 1

    max = []
    max_dict = {}
    for k, v in cnt.items():
        # 크기 비교를 위해 첫번째 요소를 max에 등록
        if max == []:
            max.append(v)
            max_dict[k]=v
        elif max != []:
            if v > max[0]:
                max = []
                max_dict = {}
                max.append(v)
                max_dict[k] = v
            elif v == max[0]:
                max.append(v)
                max_dict[k] = v
    # 만약 max_dict 에 key 가 2개인 경우 sorted()해서 오름차순 정리
    sorted_tuple = sorted(max_dict.items())
    # 딕셔너리를 items() 메소드 사용해서 정렬하면, tuple로 나온다.
    # 가장 높은 숫자가 맨 뒤에 있을 테니, indexing -1 사용

    print(f'#{tc} {sorted_tuple[-1][0]} {sorted_tuple[-1][1]}')

