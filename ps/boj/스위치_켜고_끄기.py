# https://www.acmicpc.net/problem/1244

N = int(input())

switch = list(map(int, input().split()))

for student_cnt in range(int(input())):
    gender, no = map(int, input().split(' '))
    index = no -1

    if gender == 1 :
        while index < N:
            switch[index] = 0 if switch[index] else 1
            index += no

    else:
        switch[index] = 0 if switch[index] else 1

        for i in range(1, (len(switch)-1) // 2 + 1):
            if 0 <= index - i and index + i <= len(switch) - 1 :

                if switch[index - i] == switch[index + i]:
                    if switch[index - i] == 1:
                        switch[index - i], switch[index + i] = 0, 0
                    else:
                        switch[index - i], switch[index + i] = 1, 1
                else:
                    break
            else:
                break

for n in range( N//20 + 1):
    print(' '.join(map(str, switch[(n*20) : (n*20) +20])))
