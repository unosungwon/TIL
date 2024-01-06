def solution(n):
    numbers = []

    for i in range(1, n + 1):
        # 나누어 떨어지지 않는 경우 무시
        if n % i != 0:
            continue

        # 나누어 떨어지는 경우
        elif n % i == 0:
            if i == n // i:
                numbers.append(i)
            elif i and n // i not in numbers:
                numbers.append(i)
                numbers.append(n // i)

    answer = sum(numbers)
    print(answer)

solution(12)
