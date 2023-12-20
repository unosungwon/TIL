# 02_function_I
>
> - 정의
> - output
> - input 
>   - 위치 인자
>   - 고정 인자
>   - 키워드 인자 
>   - *args
>   - **kwargs
>

## 1. 정의
```py
 def <함수이름>(parameter1, parameter2):
    코드블럭    
    return value
```

- `parameter` : 변수
- return 값 없으면 : `none`
  
```py
# # 아래의 코드의 결과는 무엇일까요? 실행하기 전에 예측해봅시다!

num1 = 0
num2 = 1

def func1(a, b):
    return a + b

def func2(a, b):
    return a - b

def func3(a, b):
    return func1(a, 5) + func2(5, 6)

result = func3(num1, num2)
print(result)

```

## 2. output = return

- `오직 한 개의 객체만 반환`
- return이 없으면 끝까지 실행하고, None을 반환.
- return이 있으면, 그자리에서 바로 종료.
- return 뒤에 아무것도 안쓰면, none 이 나옴.
  
``` py
def inf():
    while True:
        print('무한')
        return

print(inf())

# -> 무한
# -> None
```

## 3. input
-` parameter (매개변수)`

-` argument (전달인자)`

## 1. parameter
``` py
def func(x):
  return x + 2

# -> x 가 parameter(변수)
```


## 2. argument

```py
func(2) 

# -> 2가 argument (인자)

# -> 암호를 호출하는 역할
```


## 3. positional arguments (위치인자)

- 인자는 위치에 따라 함수 내에 전달.

```py
def cylinder (r, h):
    return 3.14 * r**2 * h

# -> func(2, 3) =! func(3, 2)
# -> 인자 위치에 따라 함수 값이 달라진다.
```

## 4. default argument values (기본 인자 값) -> 함수 정의시!!!! 

- `함수 정의할 떄,` `기본값을 지정`하여 함수를 호출할 때 인자의 값을 설정하지 않도록 하여, 정의된 것 보다 더 적은 개수의 인자들로 호출 될 수 있다. 

```py
def greeting(name='john', age) :
            # 기본인자    #기본값이없는 인자

# positional argument
def greeting(name):
    return f'{name}, hi'

# default argument
def greeting(name='익명'):
    return f'{name}, hi'

# default argument는 무시도 가능
def my_sum(a, b=0):
    return(a + b)
my_sum(2, 3)   # -> b = 0
               #    a = 2
               #    b = 3
               #    5

# 호출 시 인자가 없으면 defalut argument가 활용
my_sum(2)     # -> b = 0
              #    a = 2
              #    2
```

`'=' 이 있는 기본 인자값은 앞에 위치 할 수 없음. `

```py
# X
def greeting(name='kim', age):
    return f'{name}, age'

# O
def greeting(age, name='kim'):
    return f'{name}, age'

greeting(3)  #->'kim, 3'
greeting(2, 'json') #-> 'json, 2'

```

## 5. keyword arguments (키워드 인자) -> 함수 호출 시!!

- 기본 인자값은 `함수 정의할 떄`
- 키워드 인자값은 `함수를 호출할 때`

```py
# default argument
 def greeting(name='kim', age)

# keyword argument
 greeting(name='kim', age=20)
```

- 키워드 인자도 마찬가지로, 위치 인자 보다 앞에 있을 수 없음.

```py
def greeting(name, age):
    return f'{name} is {age}'

greeting(name='kim', 8 ) # X

greeting(8, name='kim')  # O

greeting('kim', 8)  # O

```

## 6. 정해지지 않은 여러개의 인자처리
- print() 함수 안에 있는 인자
- print(`sep=''`)
- print(`end=''`)

```py
# 첫번째 문장
# 두번째 문장_세번째 문장 네번째 문장
# 다섯번째 문장/마지막 문장끝!

print('첫번쨰 문장')
print('두번째 문장', end='_')
print('세번째 문장', '네번째 문장')
print('다섯번째 문장', '마지막 문장', sep='/', end='문장 끝!')
```


## 7. arbitrary argument lists 가변(임의) 인자
- `print()`는 안에 갯수가 정해지지 않은 인수를 받을 수 있다. -> print(1, 2, 3)
- print 함수와 같이 `정해지지않은 임의의 인수들을 받기 위해서` `함수 정의시` 가변 인자 리스트 `*args` 활용.
- 가변 인자 리스트는 `tuple` 처리. 
- `*매개변수`


```py
# (1, 2, 'a', [1, 2, 3])
# <class 'tuple'>

def my_funcs(*args):
    return args

type(print(my_funcs(1, 2, 'a', [1, 2, 3])))


# 1, 2, 3
# (4, 5, 6, 7, 8, 9, 10)
# <class 'None type'>

def funcs(a, b, c, *d):
     print(a, b, c)
     print(d)

type(funcs(1, 2, 3, 4, 5, 6, 7, 8, 9, 10))
    
```

## 8. arbitrary keyword argumrnts 가변 (임의) 키워드 인자
- 정해지지 않은 `키워드 인자들`을 `함수를 정의할 때` 가변 키워드 인자 `**kwargs` 활용.
- 가변 키워드 인자는 `dict 형태`로 처리.
- `**매개변수`

```py
def func(**kwargs):
    return kwargs

func(한국어='안녕', 중국어='니하오', 일본어='곤니찌와')

# -> {'한국어':'안녕', '중국어':'니하오', '일본어':'곤니찌와'}
```