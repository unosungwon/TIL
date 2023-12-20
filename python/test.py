
## break 사용
# 조건을 돌리는데, 뭔가 만족한 조건이 나오면 멈추고 빠져나오고 싶을 떄 = break

numbers = [26, 39, 51, 53, 57, 79, 85]

# n % range(2, n) == True -> 소수입니다.
for num in numbers:
    for yaksoo in range(2, num):
        if num % yaksoo == 0:
            print(f'{num}는 소수가 아닙니다. {yaksoo}는 {num}의 인수입니다.')
            break  
            # -> 처음나오는 yaksoo는 2, 그 이후는 13도 나오지만, break를 걸었기에,
            # -> 최초로 true 나오는 값만 갖고 다음 num 으로 순회.
    else:
        print(f'{num}은 소수입니다.')
    # => break 보다 전 포지션에 else 적어야함.
    # -> 위에 조건을 만족 못시키면, break 자동으로 무시한 후 여기서 슨회.


## 
