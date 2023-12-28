# PYTHON BASIC 00

>
>   1. 기초문법
> 
>   1. 변수 (Variable)
> 
>   1. 데이터 타입
>       - 숫자 타입 
>           - int
>           - float
>       - 문자열 타입 String
>           - input() / 따옴표 / '+' 가능
>           - 이스케이프 시퀀스 
>           - String Interpolation
>       - Boolean 타입 (참/거짓)
>       - None 타입
> 
>   1. 형 변환 (Type conversion)
>       -  암시적 형변환 (Implicit)
>       -  명시적 형변환 (Explicit)
>           - v type
>               - int(), flaot(), str()
>
>   1. 연산자 (Operator)
>       - 산술 연산자
>       - 비교 연산자 : is, is not
>       - 논리 연산자 : and, or, short circuit evaluation
>       - 복합 연산자 : += 1
>       - 기타 연산자 : concatenation , containment test, identify, indexing/ slicing
>       - 연산자 우선순위
>


# 1. 기초문법

## 1. 2. 코드라인
- 파이썬 코드 = `1줄에 1문장`
```PYTHON
print(1)
print(2)
# -> 1
     2

print(1) , print(2)
# -> 1 
     2
```

# 2. 변수 (Variable)

## 2.1. 할당연산자 (operator)
- 변수는 `'우항에 있는 값을 좌항 이름(=변수)에 넣는다.'` 라고 생각.
- `type()` : 변수의 데이터 값 확인.
- `id()` : 변수의 메모리 주소 확인.
- 같은 값, 다른 값 `동시 할당` 가능.
- 값 `SWAP` 가능

```PYTHON
# 같은 값을 x와 y에 동시에 할당해봅시다
x = y = 1    # x, y = 1 (X) // x, y = 1, 2, 3 (X)
print(x , y)
# -> 1 1


# 두 개의 변수 x, y 에 1, 2 값을 동시에 할당해봅시다.
x, y = 1, 2
print(x)
print(y)


# 변수 x와 y의 값을 바꿔봅시다.
x = 1
y = 2
x, y = y, x
print(x)
print(y)
```

## 2.2 식별자 (identifiers = name)
- 이름에 `영문알파벳, _ , 숫자` 가능
- 첫 글자에 숫자 (X)
- 모듈 키워드로 이름 (X)


# 3. 데이터 타입

## 3.1. 숫자 타입

### 3.1.1. int

- `int = 정수`
  
    |2진수|0b|
    |---|--|
    |8진수|0o|
    |16진수|0x|

```PYTHON
# 2진수는 binary_number에 0b10을 할당
# 8진수는 octal_number에 0o10을 할당
# 10진수는 decimal_number에 10을 할당
# 16진수는 hexadecimal_number에 0x10을 할당
bn = 0b10
on = 0o10
dn = 10
hn = 0x10

print(bn)
print(on)
print(dn)
print(hn)
```


### 3.1.2. float
- float = 실수

```PYTHON
# 변수 a에 실수 3.5를 넣고 해당 변수의 type을 알아봅시다.

a = 3.5
print(type(3.5))
```

- 실수의 연산
```PYTHON
3.5 - 3.12  # -> 0.3799999999999
#부동소수점 떄문에 답이 저렇게 나옴. = 근삿값으로 나온다. 


# round(값, 소수점자릿수)
# 3.5 - 3.12 의 값을 반올림하는데 소수점 2자리까지 나타나게 해봅시다.

round(3.5 - 3.12, 2)  # -> 0.38
```

```PYTHON
# 주의해야할 점
3.5 - 3.12 == 0.38   #-> False


# math.isclose() 를 이용해서 a와 b의 값이 같은지 확인할수 있습니다.

import math
math.isclose(3.5 - 3.12, 0.38)  #-> True
```


## 3.1. 문자열 타입

### 3.1.1. 문자열 기본 활용법
- `input()` 은 무조건 `문자열`

```PYTHON
a = input()
print(a)
type(a)   # -> str


b = [input()]
print(b)   # -> ['']
type(b)  # -> list

# 생각해볼 점
c = [input()] , [1, 2, 3]
print(c)                 # -> ([''], [1, 2, 3])
type(c)                  # -> tuple

d = [input()] + [1, 2, 3]
print(d)                # -> [' ' , 1, 2, 3]
type(d)                 # -> list
```

### 3.1.2. 따옴표 사용

### 3.1.3. 이스케이프 시퀀스

|예약문자|내용(의미)|
|---|----|
|\n|줄 바꿈|
|\t|탭|
|\r|캐리지리턴|
|\0|널(Null)|
|\\\\ |`\`|
|\\'|단일인용부호(`'`)|
|\\"|이중인용부호(`"`)|


### 3.1.4. string interpolation
- str.format()
- f - strings

```PYTHON
# str.format()을 활용해봅시다.

name = '김성원'
score = 100
'제 이름은 {}, 점수는 {}점 입니다.'.format(name, score)


# f-string을 활용해봅시다.
f'제 이름은 {name}, 점수는 {score}점 입니다.'


lotto = [input()]
f'오늘의 로또번호는 {lotto} 입니다.'
# -> '오늘의 로또번호는 [' '] 입니다.


lotto_1 = [input()]
lotto_2 = [input()]
f.'오늘의 로또번호는 {lotto_1 + lotto_2} 입니다.
# -> ' 오늘의 로또번호는 ['', ''] 입니다.
```


### 3.1.5. 참/ 거짓 (boolean)
- 파이썬에는 True와 False로 이뤄진 bool 타입이 있습니다.
- `false`에 가까운 것 = `'비어있다, 없다'`의 뉘앙스를 갖고 있는 아이들 ex> `0, '', [], none`
- `true` 에 가까운 것 = `그 외의 것들`

```PYTHON
bool(0)     # -> false
bool(None)
bool('')
bool([])

bool(' ')    # -> true
bool('hi')
bool(['hi']) 

```

### 3.1.6. None


# 4. 형 변환 (Type conversion)
- 암시적 형변환 -> 조용히 적당히 혼자서 바뀌는 애들
- 명시적 형변환 -> 확실히 명확하게 말해줘야 바뀌는 애들

## 4.1. 암시적 형변환 Implicit Type Conversion
- `bool`
- Numbers `(int, float, complex)`

 -> `이 상황에서만 파이썬이 내부적으로 자동으로 형변환` 시키는 경우

```PYTHON
i = 3
f = 3.14

i + f 
type(i + f)  
# -> int + float 이지만, 파이썬 내부적으로 float type 으로 결과를 내놓음

```

## 4.2. 암시적 형변환 Explicit Type Conversion
- str + int -> 당연히 안됨
- int를 str로 형변환 해야 함
- `str('int') -> type : str`
- `str('flaot') -> X`
- `int('str') -> X`

# 5. 연산자 (Operator)

## 5.1. 산술 연산자

|연산자|내용|
|----|---|
|+|덧셈|
|-|뺄셈|
|\*|곱셈|
|/|나눗셈|
|//|몫|
|%|나머지(modulo)|
|\*\*|거듭제곱|

## 5.2. 비교 연산자

|연산자|내용|
|----|---|
|`<`|미만|
|`<=`|이하|
|`>`|초과|
|`>=`|이상|
|`==`|같음|
|`!=`|같지않음|
|`is`|객체 아이덴티티|
|`is not`|부정된 객체 아이덴티티|

## 5.3. 논리 연산자

|연산자|내용|
|---|---|
|a and b|a와 b 모두 True시만 True|
|a or b|a 와 b 모두 False시만 False|
|not a|True -> False, False -> True|

## 5.3.1. short circuit evaluation

```py
'a' and 10 and True and 0 and 4 and 3.14 and 'asdf'

# -> 0

0 or '' or False or '0' or None or [] or () or {}

# -> '0'
```

## 5.4. 복합 연산자

- `반복문`을 통해 갯수 셀 떄 자주 쓰임

|연산자|내용|
|----|---|
|a += b|a = a + b|
|a -= b|a = a - b|
|a \*= b|a = a \* b|
|a /= b|a = a / b|
|a //= b|a = a // b|
|a %= b|a = a % b|
|a \*\*= b|a = a ** b|

```py
# 복합연산자는 이럴 때 사용
# 0으로 할당된 변수 cnt 를
# 반복문 while 을 이용하여 5회 반복하는데
# 반복하는 동안 cnt를 print로 출력하고 cnt에 1씩 더해봅시다.
# 단, cnt 를 더할때는 복합연산자를 사용해봅시다.

cnt = 0

while cnt <= 5:
    print(cnt)
    cnt += 1
```

## 5.5. concatenation (연결하다)

- `숫자가 아닌 자료형 +`로 연결 가능

