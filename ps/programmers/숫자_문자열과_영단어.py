# https://school.programmers.co.kr/learn/courses/30/lessons/81301

def solution(s):
    num_int = list(map(str, range(10)))
    num_str = ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
    result = []
    alphabet = ''

    for char in s:
        if char in num_int:
            result.append(char)

        elif char not in num_int:
            alphabet += char
            if alphabet in num_str:
                for i, n in enumerate(num_str):
                    if n == alphabet:
                        result.append(str(i))
                        alphabet = ''
                        break
            else:
                continue

    return int(''.join(result))







