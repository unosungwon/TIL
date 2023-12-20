# https://school.programmers.co.kr/learn/courses/30/lessons/12930

def solution(s):
    ss= s.split(' ')
    word_box = []
    for word in ss:
        word_part = []
        for idx in range(len(word)):
            if idx % 2 == 0:
                word_part.append(word[idx].upper())
            else:
                word_part.append(word[idx].lower())

        word_box.append(''.join(word_part))

    result = ' '.join(word_box)
    return result

print(solution("try hello   world"))
print(solution('y  dkjsfa fbgearbgs   znzh d  '))