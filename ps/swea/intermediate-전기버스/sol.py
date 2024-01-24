
T = int(input())
for tc in range(1,T+1):
    K, N, M = list(map(int, input().split(' ')))
    station_N = list(range(N+1))
    charger_M = list(map(int, input().split(' ')))
    charge_cnt = 0
    n = 0

    while n < 100:

        if station_N[n] + K >= station_N[-1]:
            print(f'#{tc} {charge_cnt}')
            break

        elif station_N[n] + K not in charger_M:
            for i in range(1, K):
                if station_N[n] + K - i in charger_M:
                    charge_cnt += 1
                    n = n + K - i
                    break
            else:
                n = 100
                print(f'#{tc} 0')
        elif station_N[n] + K in charger_M:
            charge_cnt += 1
            n = n + K