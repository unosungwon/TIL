# https://school.programmers.co.kr/learn/courses/30/lessons/42889


def solution(N, stages):
    failure = []

    for s in range(1, N+1):
        in_or_pass_stage = []
        for n in stages:
            if n >= s:
                in_or_pass_stage.append(n)
        if in_or_pass_stage != []:
            failure.append(stages.count(s) / len(in_or_pass_stage))
        else:
            failure.append(0)


    failure_dict = {}
    for idx, f in enumerate(failure,1):
        failure_dict[idx] = f
    failure_dict = sorted(failure_dict.items(), key=lambda x:x[1], reverse=True)
    result = []
    for d in failure_dict:
        result.append(d[0])

    print(result)


# 참고 예시답안 https://1ets-just-do-it.tistory.com/45

def solution(N, stages):
    n_stage = {}

    challenger = len(stages)

    for i in range(1, N+1):
        if challenger != 0:
            fail_num = stages.count(i)
            n_stage[i] = fail_num/challenger
            challenger -= fail_num

        else:
            n_stage[i] = 0

    result = sorted(n_stage, key=lambda x:n_stage[x], reverse=True)
    print(result)

solution(10, [1,11,3,3,5,6,8,8,8,9,2,3,5,5,11,11,6,8,9])